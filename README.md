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
https://www.kaggle.com/datasets/monkeysnatch/large-email-phishing-dataset
Login menggunakan akun Kaggle.
Klik tombol Download.
Ekstrak dataset ke folder:
./dataset/
sehingga struktur folder menjadi:

phishing_email_classifier/
├── dataset/
│   ├── phishing.csv
│   ├── legitimate.csv

🛠 Persyaratan Library & Environment

Rekomendasi Python version:

Python 3.10+


Install dependencies utama:

pip install -r requirements.txt

Isi file requirements.txt (contoh minimal)
pandas
numpy
scikit-learn
nltk
matplotlib
seaborn
imbalanced-learn
xgboost
streamlit
