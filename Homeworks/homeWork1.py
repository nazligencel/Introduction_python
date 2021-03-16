listTek=[1,3,4,5,7,9]
listCift=[0,2,4,6,8]

listTek.extend(listCift)
print("Yeni Liste=",listTek)

yeniList=listTek

for listType in yeniList:
    print(type(listType))

toplam=sum(yeniList)
print(toplam)

