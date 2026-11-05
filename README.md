# Deteksi Ujaran Kebencian (Hierarchical BiLSTM + Attention, kata → kalimat)

Aplikasi Streamlit satu halaman untuk model multi-label enam kategori:
Agama, Fisik, Individu, Kelompok, Ras, dan Gender.

## Isi folder
| File | Fungsi |
|---|---|
| `app.py` | halaman Deteksi (input cuitan, enam kartu hasil, sorotan kata attention) |
| `ui.py` | CSS dan potongan HTML tampilan |
| `common.py` | pemuat model (di-cache) |
| `han_inference.py` | preprocessing + model + prediksi, identik dengan notebook (sudah lulus uji kesesuaian 304/304) |
| `.streamlit/config.toml` | tema |
| `models/han_model.pt` | **dari Anda**: hasil notebook final 6 label, bagian 14 (`MyDrive/skripsi_hs6/han_model.pt`) |

## Langkah
1. Salin `han_model.pt` dari Drive ke folder `models/`.
2. Uji lokal (opsional): `pip install -r requirements.txt` lalu `streamlit run app.py`.
3. Unggah seluruh isi folder ke GitHub. Jika `han_model.pt` lebih dari 25 MB, jangan lewat unggah web;
   pakai `git push` (batas 100 MB per file) atau Git LFS.
4. share.streamlit.io → Create app → pilih repo dan branch → Main file path `app.py` →
   Advanced settings → **Python 3.12** → Deploy.

## Catatan
- Status "Terdeteksi" memakai ambang tiap label yang tersimpan di dalam `han_model.pt` (dipilih dari data validasi).
  Ambang tidak ditampilkan di antarmuka.
- Skor persen adalah rata-rata probabilitas lima model (ensemble). Warna kata pada bagian attention memakai bobot
  kata × bobot kalimat dari model pertama ensemble, diskalakan agar kata paling berpengaruh paling merah.
- Aplikasi tidak menyimpan teks masukan; kode tidak menulis ke disk.
- Model dimuat dengan `torch.load(weights_only=False)` karena berkas memuat kamus dan vocabulary. Muat hanya berkas buatan Anda sendiri.
