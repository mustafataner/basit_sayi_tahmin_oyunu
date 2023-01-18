import random

sayi = random.randint(1, 100)

hak = 10

while hak > 0:
    tahmin = int(input("lütfen 1-100 arası bir tam sayı giriniz: "))
    if tahmin < 0 or tahmin > 100:
        print("girdiğiniz sayı 1-100 aralığında değildir!")
        continue
    hak = hak - 1

    if sayi == tahmin:
        print("tebrikler sayıyı doğru tahmin ettiniz")
        break

    elif sayi > tahmin:
        print("sayınızı yükseltin, kalan hakkınız {}".format(hak))

    elif sayi < tahmin:
        print("sayınızı küçültün, kalan hakkınız {}".format(hak))

    if hak == 0:
        print("hakkınız bitti doğru sayı {}'idi.".format(sayi))






