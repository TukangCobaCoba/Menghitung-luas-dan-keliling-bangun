import math
def calculator():
    while True:
        print(f"""
Selamat datang di program kalkulator bangun datar.
Disini kamu dapat memilih 8 bangun datar untuk dihitung
    1. Persegi
    2. Persegi Panjang
    3. Segitiga
    4. Jajargenjang
    5. Belah Ketupat
    6. Layang - Layang
    7. Trapesium
    8. Lingkaran
    9. Keluar
        """)
        pilih=int(input("Silahkan masukkan angka (1-8) atau 9 untuk keluar: "))

        if pilih==1:
            bangun='Persegi'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi1=int(input('Masukkan sisi : '))
            Keliling=4*sisi1
            Luas=sisi1**2
        elif pilih==2:
            bangun='Persegi Panjang'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            panjang=int(input('Masukkan panjang : '))
            lebar=int(input('Masukkan lebar : '))
            Keliling=2*(panjang+lebar)
            Luas=panjang*lebar
        elif pilih==3:
            bangun='Segitiga'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi1=int(input('Masukkan sisi pertama : '))
            sisi2=int(input('Masukkan sisi kedua : '))
            sisi3=int(input('Masukkan sisi ketiga : '))
            alas=int(input('Masukkan alas : '))
            tinggi=int(input('Masukkan tinggi : '))
            Keliling=sisi1+sisi2+sisi3
            Luas=alas*tinggi/2
        elif pilih==4:
            bangun='Jajargenjang'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi1=int(input('Masukkan sisi alas/sisi pertama : '))
            sisi2=int(input('Masukkan sisi kedua : '))
            tinggi=int(input('Masukkan tinggi : '))
            Keliling=2*(sisi1+sisi2)
            Luas=sisi1*tinggi
        elif pilih==5:
            bangun='Belah Ketupat'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi=int(input('Masukkan sisi : '))
            diagonal1=int(input('Masukkan diagonal pertama : '))
            diagonal2=int(input('Masukkan diagonal kedua : '))
            Keliling=4*sisi
            Luas=diagonal1*diagonal2/2
        elif pilih==6:
            bangun='Layang - Layang'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi1=int(input('Masukkan sisi pertama : '))
            sisi2=int(input('Masukkan sisi kedua : '))
            diagonal1=int(input('Masukkan diagonal pertama : '))
            diagonal2=int(input('Masukkan diagonal kedua : '))
            Keliling=2*(sisi1+sisi2)
            Luas=diagonal1*diagonal2/2
        elif pilih==7:
            bangun='Trapesium'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            sisi1=int(input('Masukkan sisi pertama/a : '))
            sisi2=int(input('Masukkan sisi kedua/b : '))
            sisi3=int(input('Masukkan sisi ketiga/c : '))
            sisi4=int(input('Masukkan sisi keempat/d : '))
            tinggi=int(input('Masukkan tinggi : '))
            Keliling=sisi1+sisi2+sisi3+sisi4
            Luas=(sisi1+sisi2)*tinggi/2
        elif pilih==8:
            bangun='Lingkaran'
            print(f'=====Program menghitung Keliling dan Luas {bangun}=====')
            jari=int(input('Masukkan jari- jari : '))
            Keliling=2*math.pi*jari
            Luas=math.pi*jari**2
        elif pilih==9:
            print('Terima kasih dan sampai jumpa')
            break
        print(f"""
Jadi,
Keliling {bangun} adalah {Keliling}
Luas {bangun} adalah {Luas}
        """)
calculator()