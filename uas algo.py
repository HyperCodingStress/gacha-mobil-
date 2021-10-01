data = []
status = []
print("="*25)
print ("Temukan Keberuntugan Anda")
print("="*25)
def cek():
    print("="*100)
    for i in range(len(data)):
        print(i+1,"Nama Pengundi ~>", data[i], "\t\tStatus Pengundi ~>", status[i])
    print("="*100)
def gacha():
        a = input(str("Masukan Nama Anda : "))
        data.append(a)
        b = len(data)
        if b < 10:
            print("="*20)
            print('Belum Beruntung')
            print("="*20)
            status.append('Belum Beruntung')
        elif b == 10:
            print("="*30)
            print('Anda Mendapatkan Mobil Fortuner 2020 ')
            print("="*30)
            status.append('Anda Mendapatkan Mobil Fortuner 2020 ')
        else:
            print("="*20)
            print('Belum Beruntung')
            print("="*20)
            status.append('Belum Beruntung')
while True:
    print("1.Gacha Mobil")
    print("2.Cek Pemenang")
    print("3.Exit")
    pilih = input("Masukan Pilihan: ")
    if pilih == "1":
        gacha()
    elif pilih == "2":
        cek()
    elif pilih == "3":
        print("Terimakasih Sudah Mencoba Keberuntungan")
        break
    else:
        print("Pilihan Hanya 1-3")