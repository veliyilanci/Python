from random import randint
 
rassal=randint(1, 100)
tahminhakki=5
while True:
    tahmin=(input("Aklımda tuttuğum sayı 1 ile 100 arasındadır. 5 hakkınız var. (Oyundan çıkmak için: q ):"))
    if(tahmin=="q"):
        print("Oyundan çıktınız.")
        break
    elif int(tahmin) < rassal:
        tahminhakki -= 1
        print("Lütfen daha büyük bir sayı giriniz.")
        print("Kalan tahmin hakkınız : ", tahminhakki)
    elif int(tahmin) > rassal:
        tahminhakki -= 1
        print("Lütfen daha küçük bir sayı giriniz.")
        print("Kalan tahmin hakkınız : ", tahminhakki)
    else:
        print("\n***Tebrikler, aklımda tuttuğum sayıyı doğru tahmin ettiniz:***\n".format(rassal))
        print("Toplam deneme sayınız:".format(tahminhakki))
        break
    if (tahminhakki == 0 ):
        print("Tahmin hakkınız dolmuştur!")
        print("Aklımdan tuttuğum sayı:",rassal)
        break
