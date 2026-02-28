from random  import randint
onay_durumu=True
while onay_durumu:
    rastegele_sayi=randint(1,50)
    hak=5
    while True:
        if hak>0:
            tahmin=int(input("sayi giriniz lütfen:"))
        else:
            print("sayıyı bilemdiniz:) sayı: {}".format(rastegele_sayi))
            break
        if tahmin != rastegele_sayi:
            hak-=1
            if tahmin>rastegele_sayi:
                print("sayı aşağıda! kalan hakk:{}".format(hak))
            else:
                print("sayı yukarıda! kalan hak:{}".format(hak))
        else:
            print("tebrikler. sayıyı buldunuz")
            break

    kontrol=input("devam etmek istiyor musunuz?(E/H)")
    if kontrol=="E":
        oyun_durumu=True
    else:
        oyun_durumu=False






