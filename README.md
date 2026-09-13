<div align="center">

# 🚀 VocabGrabber 
### Görüntüden Çeviri ve Akıllı Sözlük Aracı

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-brightgreen.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![OpenCV](https://img.shields.io/badge/CV-OpenCV-red.svg)](https://opencv.org/)

*İngilizce metin içeren görselleri anında okuyan, Türkçeye çeviren ve kelime kelime detaylı analiz sunan modern masaüstü uygulaması.*

</div>

<br>

**VocabGrabber**, özellikle İngilizce dil öğrenimini ve metin analizini hızlandırmak için geliştirilmiş OOP (Nesne Yönelimli) mimariye sahip bir Python projesidir. Sistem, Tesseract OCR ve OpenCV kullanarak resimlerden metin çeker, Deep Translator ile tam metin çevirisi yapar ve metindeki her bir kelimenin Türkçe anlamını tek tek çıkararak bir sözlük oluşturur.

## ✨ Öne Çıkan Özellikler

* **Gelişmiş Metin Tanıma:** OpenCV ile görüntü ön işleme (gri tonlama, otsu thresholding) ve PyTesseract ile yüksek doğruluklu OCR okuması.
* **Kelime Bazlı Analiz:** Metni sadece bütün olarak çevirmekle kalmaz, benzersiz kelimeleri ayrıştırarak kelime kelime Türkçe sözlük dökümü verir.
* **Modern ve Akıcı Arayüz:** CustomTkinter ile tasarlanmış, Windows DWM API entegreli başlık çubuğuna sahip, koyu/açık (Dark/Light) tema destekli minimalist GUI.
* **Asenkron İşlem (Threading):** Ağır OCR ve çeviri süreçlerinde arayüz donmaz, kullanıcıya animasyonlu durum bilgisi verilir.
* **Modüler Mimari:** Arayüz (`gui.py`) ve arka plan işlemleri (`backend.py`) tamamen ayrıştırılarak temiz kod (Clean Code) prensipleri uygulanmıştır.

## 🛠️ Kullanılan Teknolojiler

* **Programlama Dili:** Python
* **Arayüz Tasarımı:** CustomTkinter, Tkinter
* **Görüntü İşleme:** OpenCV (`cv2`), NumPy
* **Optik Karakter Tanıma (OCR):** PyTesseract
* **Çeviri Motoru:** Deep Translator (`MyMemoryTranslator`)
* **Sistem Çağrıları:** Ctypes, Threading

## ⚙️ Kurulum ve Çalıştırma

**1. Tesseract OCR Kurulumu:** 
Bilgisayarınızda Tesseract OCR programının kurulu olması gerekmektedir (Varsayılan Windows yolu: `C:\Program Files\Tesseract-OCR\tesseract.exe`).

**2. Projeyi Klonlayın:**

    git clone https://github.com/Abidin-Isik-Yilmazer/Metin-Ceviri-Uygulamasi.git

**3. Proje Klasörüne Girin:**

    cd Metin-Ceviri-Uygulamasi

**4. Gerekli Kütüphaneleri Yükleyin:**

    pip install customtkinter opencv-python pytesseract deep-translator numpy

**5. Uygulamayı Başlatın:**

    python main.py

