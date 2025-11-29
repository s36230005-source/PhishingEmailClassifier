# Phishing Email Classifier
Sistem deteksi phishing berbasis Machine Learning untuk mengklasifikasikan email menjadi phishing atau legitimate berdasarkan konten teks email.

# 🔗 Demo Website (Streamlit App):
https://phishingemailclassifier-y5gtn4yzvrnzzn8xmh6zfg.streamlit.app/

# 📌 Deskripsi Proyek
Proyek ini membangun model klasifikasi berbasis TF-IDF untuk memproses teks email, kemudian melakukan prediksi menggunakan algoritma Machine Learning yaitu Random Forest Classifier

# 📂 Dataset
Dataset yang digunakan berasal dari Kaggle:
Cara download dataset
Buka link Kaggle dataset (contoh dataset phishing email):
(https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=phishing_email.csv)
Login menggunakan akun Kaggle.
Klik tombol Download.

# 🛠 Persyaratan Library & Environment
Rekomendasi Python version:
Python 3.10+

Install dependencies utama:
pip install -r requirements.txt

Isi file requirements.txt
streamlit
scikit-learn
pandas
numpy
joblib

phishing_email_classifier/
│
├── models/
│   └── random_forest_tfidf_model.pkl     # model hasil training & save
│
├── src/
│   ├── preprocessing.py                  # fungsi text preprocessing
│   ├── predict.py                        # fungsi load model & prediksi
│
├── app/
│   └── app.py                            # aplikasi Streamlit
│
├── requirements.txt                      # dependencies
├── README.md                             # dokumentasi


