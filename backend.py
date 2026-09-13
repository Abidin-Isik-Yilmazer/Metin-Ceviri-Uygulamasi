import cv2
import pytesseract
import re
import numpy as np
from deep_translator import MyMemoryTranslator

# Tesseract motorunun yolu
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCREngine:
    def __init__(self):
        self.cevirmen = MyMemoryTranslator(source='english', target='turkish')

    def resmi_isle_ve_cevir(self, dosya_yolu):
        with open(dosya_yolu, "rb") as f:
            resim_dizisi = np.frombuffer(f.read(), np.uint8)
            resim = cv2.imdecode(resim_dizisi, cv2.IMREAD_COLOR)

        gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
        _, temiz_resim = cv2.threshold(gri, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        ingilizce_metin = pytesseract.image_to_string(temiz_resim, lang='eng').strip()
        turkce_metin = self.cevirmen.translate(ingilizce_metin)

        kelimeler = re.findall(r'\b[A-Za-z]+\b', ingilizce_metin)
        benzersiz_kelimeler = set(kelimeler)
        sozluk_ciktisi = ""

        for kelime in benzersiz_kelimeler:
            if len(kelime) > 2:
                kucuk_harf = kelime.lower()
                try:
                    anlam = self.cevirmen.translate(kucuk_harf)
                    sozluk_ciktisi += f"{kucuk_harf} -> {anlam}\n"
                except:
                    pass

        sonuc_metni = "=== İNGİLİZCE METİN ===\n" + ingilizce_metin + "\n\n"
        sonuc_metni += "=== TÜRKÇE ÇEVİRİ ===\n" + turkce_metin + "\n\n"
        sonuc_metni += "=== KELİME SÖZLÜĞÜ ===\n" + sozluk_ciktisi + "\n"

        with open("ocr_sonuclari.txt", "w", encoding="utf-8") as dosya:
            dosya.write(sonuc_metni)

        return sonuc_metni