def faktöriyel(sayı):
    faktöriyel = 1
    if sayı == 0 or sayı == 1:
        return(faktöriyel)
    elif sayı <0:
        print("Lütfen pozitif bir doğal sayı giriniz!")
    else:
        while sayı >= 1:
            faktöriyel = faktöriyel*sayı
            sayı =sayı- 1
        return(faktöriyel)
