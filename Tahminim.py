def tahmin():
    ilk = 0
    son = 100
    orta = 50
    sayac=1
    sorgu = input("Aklındaki sayı " + str(orta) + "mı? (Tahminim doğru ise; 1, tahminim daha küçükse 2, tahminim daha büyükse 3 yazın)")
    while int(sorgu) != 1:
        sayac+=1
        if int(sorgu) == 2:
            ilk = orta + 1
        elif int(sorgu) == 3:
            son = orta - 1
        orta = (ilk + son) / 2
        tahminim= round(orta)
        sorgu = input("Aklındaki sayı " + str(tahminim) + "mı? (Tahminim doğru ise; 1, tahminim daha küçükse 2, tahminim daha büyükse 3 yazın)")
        if int(sorgu)==1:
          print(sayac, "kere tahminde bulundum ve sonunda doğru bildim!!!")
tahmin()
