from random import shuffle
def karıştır(listem):
  shuffle(listem)
  return listem
def tahmini():
  tahmin=""
  while tahmin not in ["1","2","3"]:
    tahmin=input("Bul karayı al parayı")
  return int(tahmin)
def karar(listem,tahmin):
  if listem[tahmin-1]=="Kara":
    print("Eyvah, gene kazandın!")
    print(listem)
  else:
    print("Tüh be, gördün mü kırmızı çıktı, bu sefer kör talih bana güldü!")
    print(listem)
kart_listesi=["Kırmızı","Kara","Kırmızı"]
listem=karıştır(kart_listesi)
tahmin=tahmini()
karar(listem,tahmin)
