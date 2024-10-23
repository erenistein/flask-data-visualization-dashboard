from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests

app = Flask(__name__)

# API anahtarı ve URL'si
API_KEY = 'YOUR API KEY'  # Copilot API anahtarı
API_URL = 'https://api.copilot.com/v1/<resource>'  # API uç noktası (API URL'si)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# CSV dosyası yükleme ve ön işleme
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Dosyayı Pandas ile yükleme
            data = pd.read_csv(file)

            # Ön işlem yapılacak fonksiyonu çağır
            cleaned_data = preprocess_data(data)

            # Ön işlenmiş veriyi kaydet
            cleaned_data.to_csv('processed_data.csv', index=False)

            # Dashboard oluştur ve kaydet
            image_url = create_dashboard(cleaned_data)

            # API'ye veriyi gönder (opsiyonel)
            send_to_copilot_api(cleaned_data)

            # Görselleştirme sayfasına yönlendir
            return redirect(url_for('visualize', image_url=image_url))

# API'ye veri gönderme fonksiyonu
def send_to_copilot_api(data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # Veriyi JSON formatına dönüştür
    json_data = data.to_json(orient='split')  # Pandas DataFrame'i JSON formatına dönüştür

    # API'ye istek gönder
    response = requests.post(API_URL, headers=headers, json={'data': json_data})

    # API'den başarılı sonuç dönerse
    if response.status_code == 200:
        return response.json()  # API'den dönen JSON verisini işle
    else:
        print(f"API isteğinde hata oluştu: {response.status_code}, {response.text}")
        return None

# Veriyi ön işleme fonksiyonu
def preprocess_data(data):
    # 1. Eksik Değerlerin İşlenmesi
    data = data.dropna()
    data = data.select_dtypes(include=['float64', 'int64'])

    # 2. Aykırı Değerlerin İşlenmesi (IQR Yöntemi)
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]

    # 3. Gürültülü Verilerin İşlenmesi
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = data[col].apply(lambda x: np.nan if isinstance(x, str) and x.strip() == '' else x)

    # 4. Tutarsız Verilerin Düzeltilmesi
    for col in data.columns:
        if data[col].dtype == 'object':
            try:
                data[col] = pd.to_numeric(data[col])
            except ValueError:
                data = data.drop(columns=[col])

    return data

# Dashboard oluşturma ve görselleri kaydetme
def create_dashboard(df):
    # Grafik boyutunu ayarla
    plt.figure(figsize=(15, 10))

    # Subplotlar: Farklı görseller için 2x2 grid oluşturuyoruz
    plt.subplot(2, 2, 1)
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")  # Korelasyon matrisi
    plt.title('Korelasyon Matrisi')

    plt.subplot(2, 2, 2)
    sns.histplot(df)  # Histogram
    plt.title('Histogram Grafigi')
    plt.subplot(2, 2, 3)
    sns.boxplot(data=df)  # Kutu grafiği (Boxplot) aykırı değerleri görmek için
    plt.title('Kutu Grafigi')

    plt.subplot(2, 2, 4)
    sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1])  # İlk iki değişken arasında dağılım
    plt.title('Scatter Grafigi')
    # Dashboard'u PNG olarak kaydet
    plt.tight_layout()  # Grafikler arası boşluğu düzenler
    image_path = os.path.join('static', 'images', 'dashboard.png')
    plt.savefig(image_path)  # Görseli static/images altında kaydet
    plt.close()  # Grafiği kapat

    # Görselin URL'ini döndür
    return url_for('static', filename='images/dashboard.png')

# Görselleştirme sayfası
@app.route('/visualize')
def visualize():
    # İşlenmiş veriyi yükle
    processed_data = pd.read_csv('processed_data.csv')

    # Görselin URL'ini al
    image_url = request.args.get('image_url')

    # Görselleştirme sayfasını render et
    return render_template('visualize.html', image_url=image_url)

if __name__ == '__main__':
    # Uygulama çalıştır
    app.run(debug=True)
