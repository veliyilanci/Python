s = input()
kalinsesli_harf = ‘aıou’
incesesli_harf = ‘eiöü’
sayi = 0
sayi1=0
for i in s:
if i in kalinsesli_harf:
sayi += 1
sayac1 = 0
for j in s:
if j in incesesli_harf:
sayi1 += 1

print(“%s metnindeki kalın sesli harf sayisi:%d” % (s,sayi))
print(“%s metnindeki ince sesli harf sayisi:%d” % (s,sayi1))
