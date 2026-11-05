import streamlit as st

import ui
from common import MODEL_PATH, get_predictor, model_missing_error

MAX_CHARS = 500

st.set_page_config(page_title="Deteksi Ujaran Kebencian", layout="wide", initial_sidebar_state="collapsed")
st.markdown(ui.CSS, unsafe_allow_html=True)
st.markdown(ui.hero_html(), unsafe_allow_html=True)

if not MODEL_PATH.exists():
    model_missing_error()
    st.stop()
predictor = get_predictor()


def _detect():
    """Dijalankan saat tombol Deteksi ditekan, sebelum halaman digambar ulang."""
    text = st.session_state.get("input_text", "")
    if not text.strip():
        st.session_state["hasil"] = None
        st.session_state["salah_kosong"] = True
        return
    st.session_state["salah_kosong"] = False
    out = predictor.predict([text])
    kosong = bool(out["empty"][0])
    st.session_state["hasil"] = {
        "empty": kosong,
        "P": out["P"][0],
        "flags": out["flags"][0],
        "truncated": bool(out["truncated"][0]),
        "exp": None if kosong else predictor.explain(text),
    }


def _clear():
    st.session_state["input_text"] = ""
    st.session_state["hasil"] = None
    st.session_state["salah_kosong"] = False


# ---------------------------------------------------------------- input
with st.container(key="input_card"):
    st.markdown(ui.input_title_html(), unsafe_allow_html=True)
    kol_teks, kol_tombol = st.columns([4.6, 1.2], vertical_alignment="center")
    with kol_teks:
        st.text_area("Teks", key="input_text", height=130, max_chars=MAX_CHARS, label_visibility="collapsed",
                     placeholder="Ketik atau tempel cuitan di sini")
        st.button("Bersihkan", key="bersihkan", on_click=_clear)
    with kol_tombol:
        st.button("Deteksi", type="primary", key="deteksi", on_click=_detect)
    if st.session_state.get("salah_kosong"):
        st.markdown(ui.CSS_ERROR + ui.error_html(), unsafe_allow_html=True)

# ---------------------------------------------------------------- hasil
h = st.session_state.get("hasil")
if h is not None:
    st.markdown(ui.result_html(h, predictor.labels, predictor.max_sent, predictor.max_words),
                unsafe_allow_html=True)

st.markdown(ui.wise_html(), unsafe_allow_html=True)
if h is not None:
    st.markdown(ui.disclaimer_html(), unsafe_allow_html=True)
