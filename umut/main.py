import datetime
def print_conversation(name,number):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, my name is {name} and my number is {number}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_versiyon():
    if False:
        crt=datetime.datetime.now()
    crt='2023-10-19 00:37:50.801773'
    print(f'{crt}')

def carpim():
    number1=int(input("1. sayiyi giriniz: "))
    number2=int(input("2. sayiyi giriniz: "))
    sonuc=number1*number2
    print(sonuc)

def print_pyramid():
    taban_uzunlugu = int(input("Piramidin taban uzunluğunu girin: "))

    for i in range(1, taban_uzunlugu + 1):
        bosluk_sayisi = taban_uzunlugu - i
        yildiz_sayisi = 2 * i - 1
        bosluklar = " " * bosluk_sayisi
        yildizlar = "*" * yildiz_sayisi
        print(bosluklar + yildizlar)

def print_square():
    kenar_uzunlugu = int(input("karenin bir kenar uzunlugunu giriniz: "))

    for i in range(1,kenar_uzunlugu+1):
        yildizlar = "*  " * kenar_uzunlugu
        print(yildizlar)

def menu():
    return int(input("hangi islemi yaptirmak istiyorsunuz:\n1)ad-numara yazdirma\n2)carpim islemi\n3)piramit cizdirme\n4)kare cizdirme\n"))

def islem(secenek):
    if secenek == 1:
        print_conversation("umut", 6)
    elif secenek == 2:
        carpim()
    elif secenek == 3:
        print_pyramid()
    elif secenek == 4:
        print_square()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secenek=menu()
    islem(secenek)
