def Durbin_watson(anlamlilik, bagimsizd, gozlem):
    if anlamlilik == 5 and bagimsizd ==1 and gozlems > 0:
        altbeta1=-3.26916
        altbeta2=-2.21789
        altbeta3=2.931711
        altbeta4=4.263415
        ustbeta1=-3.27441
        ustbeta2=1.917299
        ustbeta3=1.830633
        ustbeta4=10.64619
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 5 and bagimsizd ==2 and gozlems > 0:
        altbeta1=-3.3121
        altbeta2=-3.33254
        altbeta3=-3.63217
        altbeta4=19.31135
        ustbeta1=-3.27354
        ustbeta2=4.017121
        ustbeta3=-0.17134
        ustbeta4=28.01835   
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 5 and bagimsizd ==3 and gozlems > 0:
        altbeta1=-3.37284
        altbeta2=-3.98877
        altbeta3=-14.2457
        altbeta4=44.18308
        ustbeta1=-3.21224
        ustbeta2=5.005001
        ustbeta3=4.19282
        ustbeta4=39.3574
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 5 and bagimsizd ==4 and gozlems > 0:
        altbeta1=-3.3121
        altbeta2=-3.33254
        altbeta3=-3.63217
        altbeta4=19.31135
        ustbeta1=-3.27354
        ustbeta2=4.017121
        ustbeta3=-0.17134
        ustbeta4=28.01835
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 5 and bagimsizd ==5 and gozlems > 0:
        altbeta1=-3.53533
        altbeta2=-4.08519
        altbeta3=-47.6365
        altbeta4=127.7127
        ustbeta1=-2.88907
        ustbeta2=2.831871
        ustbeta3=40.52079
        ustbeta4=17.67699
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 1 and bagimsizd ==1 and gozlems > 0:
        altbeta1=-4.65899
        altbeta2=-1.91795
        altbeta3=6.992628
        altbeta4=4.799035
        ustbeta1=-4.87574
        ustbeta2=5.814534
        ustbeta3=-13.5426
        ustbeta4=38.75486
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 1 and bagimsizd ==2 and gozlems > 0:
        altbeta1=-4.64292
        altbeta2=-4.05298
        altbeta3=5.966592
        altbeta4=14.91894
        ustbeta1=-4.98518
        ustbeta2=10.07143
        ustbeta3=-29.2779
        ustbeta4=82.95705
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))   
    elif anlamlilik == 1 and bagimsizd ==3 and gozlems > 0:
        altbeta1=-4.64318
        altbeta2=-5.82505
        altbeta3=1.825873
        altbeta4=33.13285
        ustbeta1=-4.99832
        ustbeta2=12.71578
        ustbeta3=-37.0259
        ustbeta4=122.0812
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 1 and bagimsizd ==4 and gozlems > 0:
        altbeta1=-4.65507
        altbeta2=-7.29607
        altbeta3=-5.30044
        altbeta4=60.1113
        ustbeta1=-4.91493
        ustbeta2=13.54419
        ustbeta3=-34.1517
        ustbeta4=147.8301
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    elif anlamlilik == 1 and bagimsizd ==5 and gozlems > 0:
        altbeta1=-4.67504
        altbeta2=-8.51891
        altbeta3=-15.2571
        altbeta4=96.32291
        ustbeta1=-4.74351
        ustbeta2=12.55718
        ustbeta3=-19.3902
        ustbeta4=154.4401
        dw1 = float(2 + (altbeta1/(gozlems**0.5)) + (altbeta2/gozlems) + (altbeta3/(gozlems**1.5)) +(altbeta4/(gozlems**2)))
        dw2 = float(2 + (ustbeta1/(gozlems**0.5)) + (ustbeta2/gozlems) + (ustbeta3/(gozlems**1.5)) +(ustbeta4/(gozlems**2)))
    else:
        print("Hatalı değer girilmiştir, program sonlandırılıyor...")
    
    print("Alt kritik değer:",dw1, "\nÜst kritik değer:", dw2)        
    
print("Durbin-Watson otokorelasyon testinin kritik değerlerini elde etmek için istenen değerleri giriniz:")
anlamlilik = int(input("Anlamlılık Düzeyi (1 ya da 5): "))
bagimsiz = int(input("Bağımsız Değişken Sayısı (1 - 5 arası): "))
gozlems = int(input("Gözlem Sayısı: "))

Durbin_watson(anlamlilik, bagimsiz, gozlems)
