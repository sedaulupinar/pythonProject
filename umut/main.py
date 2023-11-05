import datetime
def print_conversation(name,number):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, my name is {name} and my number is {number}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_versiyon():
    if False:
        crt=datetime.datetime.now()
    crt='2023-10-19 00:37:50.801773'
    print(f'{crt}')

def carpim(number1,number2):
    sonuc=number1*number2
    return sonuc

def print_pyramid():
    taban_uzunlugu = int(input("Piramidin taban uzunluğunu girin: "))

    for i in range(1, taban_uzunlugu + 1):
        bosluk_sayisi = taban_uzunlugu - i
        yildiz_sayisi = 2 * i - 1
        bosluklar = " " * bosluk_sayisi
        yildizlar = "*" * yildiz_sayisi
        print(bosluklar + yildizlar)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_versiyon()
    print_conversation('umut','009')
    carpimSonucu=carpim(4,5)
    print(carpimSonucu)
    print_pyramid()
