import tkinter as tk
import random

def kapanma():
    global pencere  # pencere değişkenini global olarak tanımla
    pencere.destroy()
def durma():
     global a
     a=False
a=True
while a:
    # Ana pencereyi oluştur
    pencere = tk.Tk()
    pencere.title("DİKKAT")
    
    #label yazı efek verildi
    def yazı_efekt():
       if la.cget("foreground") == "red":
           la.config(foreground="blue")
       else:
          la.config(foreground="red")
    
       pencere.after(100, yazı_efekt)

    # label oluşturuldu
    la=tk.Label(
       pencere,
       text="DİKKAT HACKLENDİNİZ",
       width=50,
       height=10 ,
       bg="black",
       foreground="red",
       font="ariel 36",
       wraplength=400
    )
    # label eklendi
    la.pack()

    # buton oluşturuldu
    buton=tk.Button(
       pencere,
       width=80,
       height=5,
       text="PES ETTİM",
       activebackground="black",  
       activeforeground="green", 
       bg="black",
       foreground="yellow",
       font="ariel 24",
       command=durma
    )
    # buton eklendi
    buton.pack()

    yazı_efekt()
    
    # Pencere boyutunu ayarla
    pencere_genislik = 600
    pencere_yukseklik = 600

    # Ekranın genişlik ve yüksekliğini al
    ekran_genislik = pencere.winfo_screenwidth()
    ekran_yukseklik = pencere.winfo_screenheight()

    # Pencereyi rastgele konuma yerleştir
    x = random.randint(0, ekran_genislik - pencere_genislik)
    y = random.randint(0, ekran_yukseklik - pencere_yukseklik)
    pencere.geometry(f"{pencere_genislik}x{pencere_yukseklik}+{x}+{y}")

    # 2 saniye sonra pencereyi kapat
    pencere.after(2000, kapanma)

    # Pencereyi göster
    pencere.mainloop()