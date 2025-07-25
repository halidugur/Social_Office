# -*- coding: utf-8 -*-
"""halidugurproje.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DCAQc6S1Q_xzqEvo96x5od8yCRDoa-IB
"""

def dosya_oku():
    try:
        with open("gorevler.txt", "r", encoding="utf-8") as f:
            return [i.strip() for i in f.readlines()]
    except:
        return []
def dosya_yaz(gorevler):
    try:
        with open("gorevler.txt", "w", encoding="utf-8") as f:
            for g in gorevler:
                f.write(g + "\n")
    except:
        print("dosyaya yazılamadı.")
def gorev_ekle(liste):
    g = input("Görev Giriniz: ").strip()
    if g == "":
        print("Boş Görev Girilmez.")
    else:
        liste.append(g)
        dosya_yaz(liste)
        print("Görev Listenize Eklendi.")
def gorev_listele(liste):
    if not liste:
        print("Görev Mevcut değil.")
    else:
        for i in range(len(liste)):
            print(f"{i+1}. {liste[i]}")
def gorev_sil(liste):
    gorev_listele(liste)
    try:
        no = int(input("Silinecek görev numarasını girin: "))
        if 1 <= no <= len(liste):
            silinen = liste.pop(no-1)
            dosya_yaz(liste)
            print(f"{silinen} görev imha edildi :) ")
        else:
            print("Geçersiz görev numarası.")
    except:
        print("Sayı gir!")
def gorev_duzenle(liste):
    gorev_listele(liste)
    try:
        no = int(input("Düzenlenecek görev numarasını girin: "))
        if 1 <= no <= len(liste):
            yeni = input("Yeni görev yazın: ").strip()
            if yeni == "":
                print("Boş görev olmaz! ")
            else:
                liste[no-1] = yeni
                dosya_yaz(liste)
                print("Yeni Görevle Güncellendi.")
        else:
            print("Geçersiz Görev Numarası. ")
    except:
        print("Hatalı giriş yaptınız.")
def menu():
    veri = dosya_oku()
    while True:
        print("\n1-Görevleri Listele\n2-Görev Ekle\n3-Görev Düzenle\n4-Görev Sil\n5-Çıkış")
        secim = input("Seçim yapmak için geçerli numara gir: ")

        if secim == "1":
            gorev_listele(veri)
        elif secim == "2":
            gorev_ekle(veri)
        elif secim == "3":
            gorev_duzenle(veri)
        elif secim == "4":
            gorev_sil(veri)
        elif secim == "5":
            print("Çıkış yapıldı.")
            break
        else:
            print("1-5 arası numara gir.")
menu()