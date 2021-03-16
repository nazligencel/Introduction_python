ogrVize1=input('Vize Notunuz:')
ogrFinal1=input('Final Notunuz:')
ogrProje1=input('Proje Notunuz:')

ogrVize2=input('Vize Notunuz:')
ogrFinal2=input('Final Notunuz:')
ogrProje2=input('Proje Notunuz:')

ogrVize3=input('Vize Notunuz:')
ogrFinal3=input('Final Notunuz:')
ogrProje3=input('Proje Notunuz:')

ogrVize4=input('Vize Notunuz:')
ogrFinal4=input('Final Notunuz:')
ogrProje4=input('Proje Notunuz:')

ogrVize5=input('Vize Notunuz:')
ogrFinal5=input('Final Notunuz:')
ogrProje5=input('Proje Notunuz:')

gecmeNotu1=(float(ogrVize1)*0.3)+(float(ogrFinal1)*0.3)+(float(ogrProje1)*0.4)
gecmeNotu2=(float(ogrVize2)*0.3)+(float(ogrFinal2)*0.3)+(float(ogrProje2)*0.4)
gecmeNotu3=(float(ogrVize3)*0.3)+(float(ogrFinal3)*0.3)+(float(ogrProje3)*0.4)
gecmeNotu4=(float(ogrVize4)*0.3)+(float(ogrFinal4)*0.3)+(float(ogrProje4)*0.4)
gecmeNotu5=(float(ogrVize5)*0.3)+(float(ogrFinal5)*0.3)+(float(ogrProje5)*0.4)

print("Geçme Notunuz1: {0}" .format(gecmeNotu1))
print("Geçme Notunuz2: {0}" .format(gecmeNotu2))
print("Geçme Notunuz3: {0}" .format(gecmeNotu3))
print("Geçme Notunuz4: {0}" .format(gecmeNotu4))
print("Geçme Notunuz5: {0}" .format(gecmeNotu5))

liste=[gecmeNotu1,gecmeNotu2,gecmeNotu3,gecmeNotu4,gecmeNotu5]
print(liste)
listeSirala=liste
listeSirala.sort()
listeSirala.reverse()
print(listeSirala)

