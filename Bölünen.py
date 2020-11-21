def bölünen(başlangıç,bitiş,bölen):
    bölünen=[sayı for sayı in range(başlangıç,bitiş) if sayı%bölen==0]
    return(bölünen)
