import customtkinter as ctk
from tkinter import filedialog, messagebox
import ctypes
import threading

# Ayırdığımız motor sınıfını içeri alıyoruz
from backend import OCREngine


class VocabGrabberGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VocabGrabber - Görüntüden Çeviri Aracı")
        self.geometry("750x650")

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")

        self.islem_aktif = False
        self.nokta_sayaci = 0

        # Çeviri motorunu başlat
        self.motor = OCREngine()

        self.arayuzu_insaa_et()
        self.baslik_cubugu_rengi_guncelle()

    def arayuzu_insaa_et(self):
        self.tema_secici = ctk.CTkSegmentedButton(self, values=["☀️ Açık", "🌙 Koyu"], command=self.tema_degistir,
                                                  font=("Segoe UI", 12, "bold"), height=32, corner_radius=16)
        self.tema_secici.pack(anchor="ne", padx=25, pady=(15, 0))
        self.tema_secici.set("☀️ Açık")

        self.ust_cerceve = ctk.CTkFrame(self, fg_color=("gray85", "gray25"), corner_radius=10)
        self.ust_cerceve.pack(fill="x", padx=25, pady=(5, 10))

        self.ust_bilgi = ctk.CTkLabel(self.ust_cerceve, text="İngilizce Metin İçeren Bir Resim Seçin",
                                      font=("Segoe UI", 18, "bold"))
        self.ust_bilgi.pack(pady=(18, 2))

        self.alt_bilgi = ctk.CTkLabel(self.ust_cerceve, text="Sistem metni okuyup kelimeleri otomatik çevirecektir",
                                      font=("Segoe UI", 13), text_color=("gray40", "gray60"))
        self.alt_bilgi.pack(pady=(0, 15))

        self.secim_butonu = ctk.CTkButton(self.ust_cerceve, text="📸 Resim Seç", font=("Segoe UI", 14, "bold"),
                                          height=36, corner_radius=6, command=self.resim_sec_ve_isle,
                                          fg_color="#1DB954", hover_color="#1AA34A")
        self.secim_butonu.pack(pady=(0, 18))

        self.metin_kutusu = ctk.CTkTextbox(self, wrap="word", font=("Consolas", 14), corner_radius=10, border_width=2,
                                           border_color="#1DB954")
        self.metin_kutusu.pack(expand=True, fill='both', padx=25, pady=(5, 25))

    def resim_sec_ve_isle(self):
        dosya_yolu = filedialog.askopenfilename(title="Okutulacak Resmi Seçin",
                                                filetypes=[("Resim Dosyaları", "*.png;*.jpg;*.jpeg")])
        if not dosya_yolu:
            return

        self.islem_aktif = True
        self.nokta_sayaci = 0
        self.secim_butonu.configure(state="disabled")
        self.animasyonu_oynat()

        threading.Thread(target=self.arkaplanda_calistir, args=(dosya_yolu,), daemon=True).start()

    def arkaplanda_calistir(self, dosya_yolu):
        try:
            # İşlemi backend'deki OCREngine'e devrediyoruz
            sonuc_metni = self.motor.resmi_isle_ve_cevir(dosya_yolu)
            self.after(0, self.islemi_bitir, sonuc_metni)
        except Exception as e:
            self.after(0, self.hata_goster, str(e))

    def animasyonu_oynat(self):
        if self.islem_aktif:
            noktalar = "." * (self.nokta_sayaci % 4)
            self.metin_kutusu.delete("0.0", "end")
            self.metin_kutusu.insert("end", f"\n\n    Resim işleniyor, çeviri yapılıyor. Lütfen bekleyin{noktalar}\n")
            self.nokta_sayaci += 1
            self.after(400, self.animasyonu_oynat)

    def islemi_bitir(self, sonuc_metni):
        self.islem_aktif = False
        self.metin_kutusu.delete("0.0", "end")
        self.metin_kutusu.insert("end", sonuc_metni)
        self.secim_butonu.configure(state="normal")

    def hata_goster(self, hata_mesaji):
        self.islem_aktif = False
        messagebox.showerror("Hata", f"Bir sorun oluştu: {hata_mesaji}")
        self.metin_kutusu.delete("0.0", "end")
        self.secim_butonu.configure(state="normal")

    def baslik_cubugu_rengi_guncelle(self):
        try:
            self.update()
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(ctypes.c_int(0x00FFFFFF)),
                                                       ctypes.sizeof(ctypes.c_int))
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(ctypes.c_int(0)),
                                                       ctypes.sizeof(ctypes.c_int))
        except Exception:
            pass

    def tema_degistir(self, secim):
        yeni_tema = "Dark" if "Koyu" in secim else "Light"
        ctk.set_appearance_mode(yeni_tema)
        self.baslik_cubugu_rengi_guncelle()