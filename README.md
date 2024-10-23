
# Flask Tabanlı Veri Görselleştirme Uygulaması

Bu proje, bir CSV dosyasını yükleyip veri ön işleme adımlarını gerçekleştiren ve çeşitli veri görselleştirme yöntemleriyle veriyi analiz eden bir Flask web uygulamasıdır. Uygulama, bir dashboard üzerinde korelasyon matrisi, histogram, kutu grafiği ve dağılım grafiği gibi görseller sunar.

---

## İçindekiler

1. [Genel Bilgi](#genel-bilgi)
2. [Özellikler](#özellikler)
3. [Kurulum](#kurulum)
4. [Kullanım](#kullanım)
5. [Dosya Yapısı](#dosya-yapısı)
6. [Teknolojiler](#teknolojiler)
7. [Ekran Görüntüleri](#ekran-görüntüleri)
8. [İletişim](#iletişim)

---

### 1. Genel Bilgi

Bu proje, kullanıcının kendi yüklediği CSV dosyaları üzerinde veri analizi yapmasını sağlayan bir web uygulamasıdır. Uygulama, kullanıcıya dört farklı veri görselleştirme yöntemi sunar ve verinin detaylı analizi için bir dashboard oluşturur. Ayrıca, veri temizleme ve aykırı değerleri ortadan kaldırma gibi ön işleme adımları da içerir.

---

### 2. Özellikler

- **CSV Dosyası Yükleme**: Kullanıcılar CSV dosyalarını yükleyebilir.
- **Veri Ön İşleme**: Eksik ve hatalı veriler temizlenir, aykırı değerler kaldırılır.
- **Veri Görselleştirme**: Korelasyon matrisi, histogram, kutu grafiği (boxplot) ve dağılım grafikleri.
- **Dinamik Dashboard**: Her veri seti için otomatik olarak güncellenen bir veri dashboard’u.
- **API Entegrasyonu (Opsiyonel)**: Copilot API ile veri analizi.

---

### 3. Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

#### Gerekli Bağımlılıklar

Aşağıdaki teknolojiler ve kütüphanelerin kurulu olması gerekmektedir:

- Python 3.8+
- Flask
- Pandas
- Matplotlib
- Seaborn
- NumPy
- SciPy

#### Kurulum Adımları

1. **Proje Deposu**nu indirin veya klonlayın:
   ```bash
   git clone https://github.com/erenistein/flask-veri-gorsellestirme.git
   cd flask-veri-gorsellestirme
   ```

2. **Gerekli Python paketlerini** kurun:
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı başlatın**:
   ```bash
   python app.py
   ```

4. Web tarayıcınızı açın ve **http://127.0.0.1:5000/** adresine gidin.

---

### 4. Kullanım

1. Ana sayfada **CSV dosyanızı yükleyin**.
2. Dosyanız yüklendikten sonra veri temizleme işlemi otomatik olarak yapılır.
3. Görselleştirme sayfasına yönlendirilirsiniz. Bu sayfada verinizin çeşitli grafiklerle analiz edildiğini göreceksiniz:
   - Korelasyon Matrisi
   - Histogram
   - Boxplot
   - Dağılım Grafiği
4. Dashboard üzerinde yer alan görseller üzerinden veriyi analiz edebilirsiniz.

---

### 5. Dosya Yapısı

```
flask-veri-gorsellestirme/
│
├── static/
│   └── images/
│       └── dashboard.png      # Oluşturulan dashboard görseli
├── templates/
│   ├── index.html             # Ana sayfa şablonu
│   ├── visualize.html         # Görselleştirme sayfası şablonu
├── app.py                     # Ana uygulama dosyası
├── requirements.txt           # Gerekli bağımlılıklar
└── README.txt                 # Proje açıklamaları
```

---

### 6. Teknolojiler

- **Flask**: Web framework
- **Pandas**: Veri işleme ve analiz
- **Matplotlib**: Veri görselleştirme
- **Seaborn**: İleri düzey veri görselleştirme
- **NumPy**: Sayısal hesaplamalar
- **SciPy**: İstatistiksel analiz
- **HTML/CSS**: Web sayfası tasarımı

---

### 7. Ekran Görüntüleri

**Ana Sayfa**  
Kullanıcıların CSV dosyasını yükleyebileceği giriş ekranı.

![Ana Sayfa](static/images/homepage_screenshot.png)

**Dashboard Sayfası**  
Korelasyon matrisi, histogram, boxplot ve scatter plot'u gösteren dashboard ekranı.

![Dashboard](static/images/dashboard_screenshot.png)

---

### 8. İletişim

Eğer herhangi bir sorunuz varsa ya da projeye katkıda bulunmak istiyorsanız, bana ulaşabilirsiniz:

- **Eren Takeş**
- **E-posta**: erentakes3@gmail.com
- **GitHub**: [https://github.com/erenistein](https://github.com/erenistein)

---

Bu dosya, projeyi kullanacak veya projeye katkıda bulunacak kişilere net bir yönlendirme sağlamak amacıyla detaylı şekilde hazırlanmıştır.
