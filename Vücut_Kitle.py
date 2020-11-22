def vki(boy,kilo):
  boy=float(boy/100)
  kilo=int(kilo)
  endeks=kilo/(boy**2)
  if endeks <= 18.49:
    print("İdeal kilonun altındasınız. Vücut kitle indeksiniz:", endeks)
  elif endeks => 18.5 and endeks <=24.99 :
    print("İdeal kiloya sahipsiniz. Vücut kitle indeksiniz:", endeks)
  elif endeks => 25 and endeks <=29.99:
    print("İdeal kilonun üstündesiniz. Vücut kitle indeksiniz:", endeks)
  elif endeks => 30:
    print("Boyunuza göre vücut ağırlığınız fazladır. Obez sınıfına giriyorsunuz. Vücut kitle indeksiniz:", endeks)
