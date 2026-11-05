"""Pemuat model bersama."""
from pathlib import Path

import streamlit as st

from han_inference import HANPredictor

BASE = Path(__file__).resolve().parent
MODEL_PATH = BASE / "models" / "han_model.pt"


@st.cache_resource(show_spinner="Memuat model...")
def get_predictor():
    return HANPredictor(MODEL_PATH)


def model_missing_error():
    st.error("File model `models/han_model.pt` tidak ditemukan. Letakkan `han_model.pt` di folder `models/`.")
