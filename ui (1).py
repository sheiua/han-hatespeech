"""Tampilan halaman Deteksi: CSS dan potongan HTML.

Semua potongan HTML dibuat tanpa baris kosong dan tanpa indentasi di awal baris
supaya tidak dibaca sebagai kode oleh parser markdown Streamlit.
"""
import html

# urutan kartu pada tampilan; nama tampilan, nama kapital kartu, dan kalimat keterangan
LABEL_ORDER = ["HS_Religion", "HS_Physical", "HS_Individual", "HS_Group", "HS_Race", "HS_Gender"]
NAMA = {
    "HS_Religion": ("AGAMA", "Agama", "yang berkaitan dengan agama"),
    "HS_Physical": ("FISIK", "Fisik", "yang berkaitan dengan fisik"),
    "HS_Individual": ("INDIVIDU", "Individu", "yang menyerang individu secara personal"),
    "HS_Group": ("KELOMPOK", "Kelompok", "yang menargetkan kelompok tertentu"),
    "HS_Race": ("RAS", "Ras", "yang berkaitan dengan ras"),
    "HS_Gender": ("GENDER", "Gender", "yang berkaitan dengan gender"),
}

# urutan penyebutan kategori pada banner
BANNER_ORDER = ["HS_Individual", "HS_Group", "HS_Physical", "HS_Religion", "HS_Race", "HS_Gender"]

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700;800&display=swap');
.stApp{background:#F4F5FB;color:#1B1B4B;font-family:'Public Sans',system-ui,sans-serif}
.stApp textarea,.stApp button{font-family:'Public Sans',system-ui,sans-serif}
header[data-testid="stHeader"],#MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"]{display:none !important}
.block-container{max-width:1280px;padding:0 48px 48px !important}
@media (max-width:700px){.block-container{padding:0 16px 32px !important}}

.han-hero{display:flex;flex-direction:column;align-items:center;gap:8px;padding:24px 0 18px;text-align:center}
.han-hero h1{margin:0;padding:0;font-size:clamp(30px,4.2vw,46px);line-height:1.1;font-weight:800;letter-spacing:-0.02em;color:#1B1B4B}
.han-hero h1 span{color:#4338CA}
.han-hero p{margin:0;font-size:clamp(14px,1.6vw,17px);font-weight:500;color:#4338CA}
.han-hero i{display:block;width:48px;height:4px;border-radius:2px;background:#4338CA}

.st-key-input_card{background:#fff;border:1px solid #E3E5F2;border-radius:16px;padding:18px 24px;margin-bottom:14px}
.han-input-title{font-size:18px;font-weight:700;color:#1B1B4B;margin:0 0 2px}
.st-key-boxteks{border:1px solid #B9BDD8;border-radius:12px;background:#fff;padding:6px 12px 10px}
.st-key-boxteks:focus-within{border-color:#4338CA}
.st-key-boxteks [data-baseweb="textarea"],.st-key-boxteks [data-baseweb="base-input"],.st-key-boxteks [data-testid="stTextAreaRootElement"]{border:0 !important;box-shadow:none !important;outline:0 !important;background:transparent !important}
.st-key-boxteks textarea{font-size:16px;line-height:1.5;color:#1B1B4B;background:transparent !important}
.st-key-deteksi button{width:100%;max-width:180px;height:56px;border:0;border-radius:14px;background:#4338CA;color:#fff}
.st-key-deteksi button:hover{background:#3730A3;color:#fff}
.st-key-deteksi button p{font-size:20px;font-weight:700;letter-spacing:0.01em}
.st-key-bersihkan{display:flex;justify-content:flex-end}
.st-key-bersihkan button{min-height:36px;padding:6px 16px;border:1px solid #B9BDD8;border-radius:8px;background:#fff;color:#1B1B4B}
.st-key-bersihkan button:hover{border-color:#4338CA;color:#4338CA}
.st-key-bersihkan button p{font-size:14px;font-weight:600}
.han-err{margin-top:6px;font-size:15px;font-weight:600;color:#B91C1C}

.han-res{background:#fff;border:1px solid #E3E5F2;border-radius:16px;padding:28px;display:flex;flex-direction:column;gap:22px;margin-bottom:28px}
.han-res-head{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center}
.han-res-title{font-size:20px;font-weight:700;color:#1B1B4B}
.han-status{padding:8px 14px;border-radius:8px;font-size:14px;font-weight:600;background:#E9F7EF;border:1px solid #B7E1C8;color:#14532D}
.han-status-warn{background:#FFF4DB;border-color:#E8C873;color:#6B4700}
.han-banner{border-radius:12px;padding:20px 24px;display:flex;flex-direction:column;gap:4px;background:#FFF1F1;border:1px solid #F5BDBD}
.han-banner b{font-size:20px;color:#B91C1C}
.han-banner span{font-size:16px;line-height:1.6;color:#1B1B4B}
.han-banner-ok{background:#E9F7EF;border-color:#B7E1C8}
.han-banner-ok b{color:#14532D}
.han-banner-warn{background:#FFF4DB;border-color:#E8C873}
.han-banner-warn b{color:#6B4700}
.han-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
@media (max-width:900px){.han-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.han-grid{grid-template-columns:minmax(0,1fr)}}
.han-c{background:#fff;border:1px solid #E3E5F2;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:12px}
.han-c-on{background:#FFF8F8;border:1.5px solid #E58B8B;padding:19.5px}
.han-c-top{display:flex;justify-content:space-between;align-items:center;gap:8px}
.han-c-name{font-size:16px;font-weight:700;letter-spacing:0.04em;color:#1B1B4B}
.han-c-on .han-c-name{color:#B91C1C}
.han-chip{padding:5px 10px;border-radius:6px;background:#4B5563;color:#fff;font-size:12px;font-weight:600;white-space:nowrap}
.han-chip-on{background:#C81E1E}
.han-c-pct{font-size:32px;font-weight:700;line-height:1.1;color:#4B5563}
.han-c-on .han-c-pct{color:#B91C1C}
.han-c-sub{font-size:14px;color:#4A4D75}
.han-track{height:10px;background:#ECEDF5;border-radius:5px}
.han-c-on .han-track{background:#F8DADA}
.han-fill{height:10px;min-width:4px;background:#6B7280;border-radius:5px}
.han-c-on .han-fill{background:#C81E1E}
.han-c-desc{font-size:13px;line-height:1.6;color:#4A4D75}

.han-att{border:1px solid #E3E5F2;border-radius:14px;padding:24px;display:flex;flex-direction:column;gap:18px}
.han-att-title{font-size:18px;font-weight:700;color:#1B1B4B}
.han-att-sub,.han-att-note{font-size:14px;color:#4A4D75}
.han-words{display:flex;flex-wrap:wrap;gap:8px}
.han-w{padding:8px 14px;border-radius:8px;font-size:16px}
.han-legend{display:flex;align-items:center;gap:12px;font-size:14px;font-weight:600;color:#1B1B4B}
.han-legend i{display:block;width:260px;max-width:50%;height:12px;border-radius:6px;background:linear-gradient(90deg,#B91C1C,#FDECEC)}
.han-note{font-size:13px;color:#4A4D75}

.han-wise{background:#EEF8F1;border:1px solid #BFE3CB;border-radius:14px;padding:14px 24px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center;margin-bottom:16px}
.han-wise b{font-size:16px;color:#14532D}
.han-wise span{max-width:760px;font-size:14px;line-height:1.5;color:#1B1B4B}
.han-disc{background:#EEF0FB;border:1px solid #D4D8F2;border-radius:14px;padding:18px 24px;display:flex;flex-direction:column;gap:2px;font-size:15px;line-height:1.6;color:#312E81}
</style>"""

CSS_ERROR = """<style>
.st-key-boxteks{border:2px solid #C81E1E !important}
</style>"""


def hero_html():
    return ('<div class="han-hero"><h1>Deteksi <span>Ujaran Kebencian</span></h1>'
            '<p>Kenali Ujaran Kebencian, Bangun Ruang Digital yang Lebih Aman.</p><i></i></div>')


def input_title_html():
    return '<div class="han-input-title">Masukkan Cuitan</div>'


def error_html():
    return '<div class="han-err">Masukkan cuitan terlebih dahulu.</div>'


def wise_html():
    return ('<div class="han-wise"><b>Bijak Berkomunikasi di Ruang Digital</b>'
            '<span>Perbedaan pendapat adalah hal yang wajar. Mari gunakan kata-kata yang sopan dan menghargai '
            'agar media sosial menjadi tempat yang aman dan nyaman untuk semua.</span></div>')


def disclaimer_html():
    return ('<div class="han-disc"><span>Hasil ini merupakan prediksi model AI dan bukan keputusan mutlak.</span>'
            '<span>Penilaian manusia tetap diperlukan.</span></div>')


def _pct(p):
    return ("%.1f" % (100.0 * float(p))).replace(".", ",") + "%"


def _daftar(nama):
    if len(nama) == 1:
        return nama[0]
    if len(nama) == 2:
        return nama[0] + " dan " + nama[1]
    return ", ".join(nama[:-1]) + ", dan " + nama[-1]


def _card(label, p, det):
    kap, _, desc = NAMA[label]
    chip = ('<span class="han-chip han-chip-on">Terdeteksi</span>' if det
            else '<span class="han-chip">Tidak terdeteksi</span>')
    ket = ("Terdeteksi indikasi ujaran kebencian " if det else "Tidak ditemukan indikasi ujaran kebencian ") + desc + "."
    return ('<div class="han-c%s"><div class="han-c-top"><span class="han-c-name">%s</span>%s</div>'
            '<div class="han-c-pct">%s</div><div class="han-c-sub">Skor Analisis</div>'
            '<div class="han-track"><div class="han-fill" style="width:%.2f%%"></div></div>'
            '<div class="han-c-desc">%s</div></div>') % (" han-c-on" if det else "", kap, chip, _pct(p),
                                                          100.0 * float(p), ket)


def _mix(t):
    a, b = (253, 236, 236), (185, 28, 28)
    return "rgb(%d,%d,%d)" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def attention_html(exp):
    """Sorotan kata (opsi B): warna dari bobot kata x bobot kalimat, dinormalisasi ke kata terbesar."""
    if not exp:
        return ""
    skor = [w * s["sent_w"] for s in exp for w in s["word_w"]]
    mx = max(skor) + 1e-12
    chips = []
    for s in exp:
        for tok, w in zip(s["tokens"], s["word_w"]):
            t = min(1.0, (w * s["sent_w"]) / mx)
            gelap = t > 0.75
            chips.append('<span class="han-w" style="background:%s;color:%s;font-weight:%d">%s</span>'
                         % (_mix(t), "#FFFFFF" if gelap else "#1A0303", 600 if t > 0.5 else 500, html.escape(tok)))
    return ('<div class="han-att"><div><div class="han-att-title">Kata yang mendapat perhatian model (Attention)</div>'
            '<div class="han-att-sub">Kata dengan warna lebih gelap memiliki bobot perhatian lebih tinggi terhadap '
            'hasil prediksi.</div></div><div class="han-words">%s</div>'
            '<div class="han-legend"><span>Tinggi</span><i></i><span>Rendah</span></div>'
            '<div class="han-att-note">Visualisasi ini menunjukkan fokus model, bukan bukti bahwa kata tersebut '
            'merupakan penyebab ujaran kebencian.</div></div>') % "".join(chips)


def result_html(h, labels, max_sent, max_words):
    """Kartu Hasil Analisis untuk satu hasil (dict dari app.py)."""
    if h["empty"]:
        return ('<div class="han-res"><div class="han-res-head"><span class="han-res-title">Hasil Analisis</span>'
                '<span class="han-status han-status-warn">Tidak dapat dianalisis</span></div>'
                '<div class="han-banner han-banner-warn"><b>Teks Tidak Dapat Dianalisis</b>'
                '<span>Setelah pembersihan, tidak ada kata yang tersisa karena teks hanya berisi emoji, tautan, '
                'mention, atau tanda baca. Silakan masukkan cuitan yang berisi teks.</span></div></div>')
    idx = {l: i for i, l in enumerate(labels)}
    urut = [l for l in LABEL_ORDER if l in idx]
    det = [l for l in urut if bool(h["flags"][idx[l]])]
    if det:
        det.sort(key=lambda l: BANNER_ORDER.index(l))
        banner = ('<div class="han-banner"><b>Terindikasi Ujaran Kebencian</b><span>Menemukan indikasi pada %d '
                  'kategori: %s.</span></div>') % (len(det), _daftar([NAMA[l][1] for l in det]))
    else:
        banner = ('<div class="han-banner han-banner-ok"><b>Tidak Ditemukan Indikasi Ujaran Kebencian</b>'
                  '<span>Tidak menemukan indikasi pada keenam kategori.</span></div>')
    kartu = "".join(_card(l, h["P"][idx[l]], l in det) for l in urut)
    pot = ""
    if h["truncated"]:
        pot = ('<div class="han-note">Cuitan panjang dipotong: maksimal %d kalimat dan %d kata per kalimat yang '
               'dianalisis.</div>') % (max_sent, max_words)
    att = attention_html(h["exp"]) if det else ""
    return ('<div class="han-res"><div class="han-res-head"><span class="han-res-title">Hasil Analisis</span>'
            '<span class="han-status">Analisis selesai</span></div>%s<div class="han-grid">%s</div>%s%s</div>'
            % (banner, kartu, att, pot))
