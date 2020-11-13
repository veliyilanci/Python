girdi = int(input("İlgilendiğiniz sayıyı giriniz:"))
toplam=0
for i in range(1,girdi):
    if(girdi%i == 0):
        toplam +=i     
if(girdi == toplam):
    print("İlgilendiğiniz sayı mükemmel sayıdır.")
else:
    print("İlgilendiğiniz sayı mükemmel sayı değildir.")
