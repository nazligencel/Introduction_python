sorular = ['Hangisi Kaymağı İle Ünlü Olan İlimizdir ?','Hangisi Dondurması İle Ünlü Olan İlimizdir ?',

'Hangisi Pidesi İle Ünlü Olan İlimizdir ?''Almanyanın Başkenti Neresidir?','Haberleşmenin eski dildeki adı nedir?',
'Telli çalgılarda sazların en kalın teli nedir?','Japonların geleneksel güreşine ne ad verilir?',
'Yeni bir işe girerken, iş yerlerine verdiğimiz kısa öz geçmişin kısa adı nedir?',
'Deniz yolculuğunda toplu insan taşımacılığında kullanılan araçların ortak adı?',
'İp üstünde gösteri yapanlar hangi mesleği icra eder?']

soru_1_cevaplar = ['A) Afyon','B) Mersin','C) Yozgat','D) Bursa']
soru_2_cevaplar = ['A) Denizli','B) Konya','C) KahramanMaraş','D) Eskişehir']
soru_3_cevaplar = ['A) Bursa','B) Konya','C) İstanbul','D) Ankara']
soru_4_cevaplar = ['A) Berlin','B) Saksonya','C) Bremen','D) Hessen']
soru_5_cevaplar = ['A) Müzakere','B) Muhabere','C) İcazet','D) Mezbaha']
soru_6_cevaplar = ['A) Vurgu','B) Tokmak','C) Tel','D) Bam Teli']
soru_7_cevaplar = ['A) Tekvando','B) Summo','C) Güreş','D) Kick Boks']
soru_8_cevaplar = ['A) Dosya','B) CV','C) Biyografi','D) Otobiyografi']
soru_9_cevaplar = ['A) Sandal','B) Gemi','C) Tekne','D) Vapur']
soru_10_cevaplar = ['A) Cambaz','B) Hokkabaz','C) Sihirbaz','D) Şakacı']

dogru_cevaplar = ['a','c','b','a','b','d','b','b','d','a']



def sor():

    puan = 0

    print('Soru 1:',sorular[0])

    for x in soru_1_cevaplar:

        print(x)

    cevap_1 = input('Cevabınız Nedir: ')

    if (cevap_1.lower() == dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)

    

    print('Soru 2:',sorular[1])

    for x in soru_2_cevaplar:

        print(x)

    cevap_2 = input('Cevabınız Nedir: ')

    if (cevap_2.lower() == dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap C Şıkkı.')

    print('-'*50)



    print('Soru 3:',sorular[2])

    for x in soru_3_cevaplar:

        print(x)

    cevap_3 = input('Cevabınız Nedir: ')

    if (cevap_3.lower() == dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru 4:',sorular[3])

    for x in soru_4_cevaplar:

        print(x)

    cevap_4 = input('Cevabınız Nedir: ')

    if (cevap_4.lower() == dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)

    print('Soru 5:',sorular[4])

    for x in soru_5_cevaplar:

        print(x)

    cevap_5 = input('Cevabınız Nedir: ')

    if (cevap_5.lower() == dogru_cevaplar[4]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru 6:',sorular[5])

    for x in soru_6_cevaplar:

        print(x)

    cevap_6 = input('Cevabınız Nedir: ')

    if (cevap_6.lower() == dogru_cevaplar[5]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap D Şıkkı.')

    print('-'*50)

    print('Soru 7:',sorular[6])

    for x in soru_7_cevaplar:

        print(x)

    cevap_7 = input('Cevabınız Nedir: ')

    if (cevap_7.lower() == dogru_cevaplar[6]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru 8:',sorular[7])

    for x in soru_8_cevaplar:

        print(x)

    cevap_8 = input('Cevabınız Nedir: ')

    if (cevap_8.lower() == dogru_cevaplar[7]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru 9:',sorular[8])

    for x in soru_9_cevaplar:

        print(x)

    cevap_9 = input('Cevabınız Nedir: ')

    if (cevap_9.lower() == dogru_cevaplar[8]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap D Şıkkı.')

    print('-'*50)

    print('Soru 10:',sorular[9])

    for x in soru_10_cevaplar:

        print(x)

    cevap_10 = input('Cevabınız Nedir: ')

    if (cevap_10.lower() == dogru_cevaplar[9]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)



    print('Soru Oyunumuz Bitmiştir. Toplamda {} Soruya Doğru Cevap Verdiniz.'.format(puan))


    if puan > 50 :
        print("Tebrikler Başarılı")
    else:
        print("Üzgünüm Başarısız oldunuz")



sor()