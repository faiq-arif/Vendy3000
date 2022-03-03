# Program Vending Machine
# Program ini mensimulasikan cara kerja sebuah vending machine dengan perantara
# command line.

# KAMUS
# prod, money_denom : list
# df_products, df_denom : pd.DataFrame
# run, run_opt, run_vend, run_money, run_prod,. finish : boolean
# opt_menu, opt_opt, stok, j_awal, m, p, denom, n_prod : integer
# opt_vend = string
# total, sisa: float

# Import Modules
import os
import pandas as pd
import time

# ALGORITMA
# Definisi Prosedur dan Fungsi
def wait():
    # Prosedur Animasi Loading
    # Prosedur ini menampilkan animasi berupa titik titik.
    
    # KAMUS
    # i : integer
    
    # ALGORITMA
    for i in range(10):
        print('.', end='')
        time.sleep(0.3)
    print(' ')

def MainDisplay():
    # Prosedur Tampilan Utama Vending Machine Untuk Pembeli
    # Prosedur ini menampilkan tampilan utama Vending Machine beserta data produk
    # dan nominal uang yang diterima oleh mesin.
    
    # ALGORITMA
    print('-------------------------------------------------------------------------------')
    print('     0       0  0000  0   0  000    0   0       000    000    000    000       ')
    print('      0     0   0     00  0  0  0    0 0           0  0   0  0   0  0   0      ')
    print('       0   0    0000  0 0 0  0   0    0   0000   00   0   0  0   0  0   0      ')
    print('        0 0     0     0  00  0  0     0            0  0   0  0   0  0   0      ')
    print('         0      0000  0   0  000      0         000    000    000    000       ')
    print('-------------------------------------------------------------------------------')
    print('                            By Group 6 - Class 43                              ')
    print('-------------------------------------------------------------------------------')
    DisplayProducts()
    print('  ')
    DisplayDenom()
    print('  ')
    print('  ')
    print('Press Any Key to Continue...')

def StartMenu():
    # Prosedur Tampilan Menu Utama Untuk Penjual
    # Prosedur ini menampilkan menu untuk menyalakan, mematikan, dan mengubah
    # pengaturan mesin.
    
    # ALGORITMA
    print('                                 MENU UTAMA                                    ')
    print('-------------------------------------------------------------------------------')
    print('1 - START Vending Machine')
    print('2 - Pengaturan')
    print('3 - STOP Vending Machine')
    print('-------------------------------------------------------------------------------')

def MainSettings():
    # Prosedur Tampilan Pengaturan Untuk Penjual
    # Prosedur ini menampilkan data lengkap uang dan produk, juga memberikan opsi
    # untuk mengubah data itu.
    
    # KAMUS
    # df_products, df_denom : pd. DataFrame
    
    # ALGORITMA
    print('                                 PENGATURAN                                    ')
    print('-------------------------------------------------------------------------------')
    print('Data Produk')
    print(df_products)
    print(' ')
    print('Data Uang')
    print(df_denom.to_string(index=False))
    print('-------------------------------------------------------------------------------')
    print('1 - Ubah Produk dan Stok')
    print('2 - Reset Stok')
    print('3 - Ubah Nominal yang Diterima')
    print('4 - Reset Jumlah Uang')
    print(' ')
    print('0 - Kembali ke MENU UTAMA')
    print(' ')
  
def DisplayProducts():
    # Prosedur Tampilan Data Produk Untuk Pembeli dan Penjual
    # Prosedur ini menampilkan tabel data produk.
    
    # KAMUS
    # df_products : pd.DataFrame
    
    # ALGORITMA
    print('                                   PRODUK                                      ')
    print('-------------------------------------------------------------------------------')
    print(df_products)
    print('-------------------------------------------------------------------------------')
  
def DisplayDenom():
    # Prosedur Menampilkan Nominal Yang Diterima Oleh Mesin
    # Prosedur ini menampilkan nominal uang berapa saja yang diterima oleh mesin.
    
    # KAMUS
    # i : integer
    # money_denom : list
    
    # ALGORITMA
    print('Mesin ini menerima', end=' ')
    for i in range(denom):
        print(money_denom[i][2],money_denom[i][0], end=' ')
    
def inputProducts():
    # Fungsi Pengulangan Input Data Produk - Untuk Penjual
    # Fungsi ini melakukan pengulangan input produk lalu menyusunnya menjadi
    # bentuk list dua dimensi.
    
    # KAMUS
    # n_prod, i : integer
    # prod : list
    
    # ALGORITMA
    print('                               INPUT PRODUK                                    ')
    print('-------------------------------------------------------------------------------')
    n_prod = int(input('Jumlah produk : '))
    prod = [[0 for i in range(3)]for j in range(n_prod)]
    for i in range(n_prod):
            prod[i][0] = input('Nama Produk ' + str(i+1) + ' : ')
            prod[i][1] = int(input('Stok Produk ' + str(i+1) + ' : '))
            prod[i][2] = float(input('Harga Produk ' + str(i+1) + ' : ' + money_denom[0][2] + ' '))
    return prod

def inputDenom():
    # Fungsi Pengulangan Input Data Uang - Untuk Penjual
    # Fungsi ini melakukan pengulangan input data uang dan lalu menyusunnya
    # menjadi bentuk list dua dimensi.
    
    # KAMUS
    # denom : integer
    # cur : string
    # money_denom : list
    
    # ALGORITMA
    print('                              INPUT NOMINAL                                    ')
    print('-------------------------------------------------------------------------------')
    denom = int(input('Jumlah nominal yang dapat diterima : '))
    cur = input('Simbol Mata Uang : ')
    money_denom = [[0 for i in range(3)]for j in range(denom)]
    for i in range(denom):
        money_denom[i][0] = round(float(input('Nominal ' + str(i+1) + ' : ')), 2)
        money_denom[i][1] = int(input('Jumlah Awal ' + str(i+1) + ' : '))
        money_denom[i][2] = cur
    return money_denom

def CalcChange(a):
    # Fungsi Menghitung Uang Kembalian
    # Fungsi ini menerima masukan sisa uang pembeli dan mengembalikan nominal
    # berapa saja yang akan dikembalikan mesin.    
    
    # KAMUS
    # a, sisa : float
    # i : integer
    # money_denom : list
    
    # ALGORITMA
    sisa = a
    for i in range(len(money_denom)-1, -1, -1):
        while (sisa - money_denom[i][0] >= 0 and money_denom[i][1] > 0):
            print(money_denom[i][2],money_denom[i][0])
            money_denom[i][1] -= 1
            sisa -= money_denom[i][0]
    return sisa

# Memeriksa apakah program dijalankan pertama kali dengan memeriksa keberadaaan file .csv
# Memeriksa adanya file 'money.csv' (Data Uang di dalam mesin)
if (os.path.isfile('money.csv') == False):
    # initial setup
    print('                             PENGATURAN AWAL                                   ')
    print('-------------------------------------------------------------------------------')
    money_denom = inputDenom()
    denom = len(money_denom)
    df_denom = pd.DataFrame.from_records(money_denom, columns=['Nominal','Jumlah','Simbol'])
    df_denom.to_csv(r'money.csv', index = False)
else:
    df_denom = pd.read_csv('money.csv')
    money_denom = df_denom.values.tolist()
    denom = len(money_denom)

# Memeriksa adanya file 'products.csv' (Data produk di dalam mesin)        
if (os.path.isfile('products.csv') == False):
    prod = inputProducts()
    n_prod = len(prod)
    df_products = pd.DataFrame.from_records(prod, columns=['Nama', 'Stok', 'Harga'])
    df_products.index = df_products.index + 1
    df_products.to_csv(r'products.csv', index = False)
else:
    df_products = pd.read_csv('products.csv')
    df_products.index = df_products.index + 1
    prod = df_products.values.tolist()
    n_prod = len(prod)

# Pengulangan Utama
run = True # Variabel indikator pengulangan utama
while (run): # Pengulangan utama dimulai
    StartMenu() # Tampilan menu utama untuk penjual
    opt_menu = int(input('Pilihan : ')) # Input pilihan menu item
    
    # Jika pengguna memilih 1 - START Vending Machine
    if (opt_menu == 1):
        run_vend = True
        
        # Loop Tampilan Utama Vending Machine
        while (run_vend):
            total = 0
            MainDisplay()
            opt_vend = input()
            if (opt_vend == 'EXIT'):
                run_vend = False
            else:
                run_money = True
                finish = True
                
                # Loop Input Uang (Pembayaran)
                while (run_money):
                    print('Berapa uang yang anda masukkan?')
                    for i in range(denom):
                        m = int(input(money_denom[i][2] + ' ' + str(money_denom[i][0]) + ' : '))
                        money_denom[i][1] += m
                        total += m*money_denom[i][0]
                    df_denom = pd.DataFrame.from_records(money_denom, columns=['Nominal','Jumlah','Simbol'])
                    df_denom.to_csv(r'money.csv', index = False)
                    wait()
                    run_prod = True
                    
                    # Loop Pemilihan Produk
                    while (run_prod):
                        DisplayProducts()
                        print('Total uang anda : '+ money_denom[0][2] + ' ' + str(total))
                        p = int(input("Beli Produk No. Berapa (Tekan 0 untuk SELESAI): "))
                        # Kondisional cek stok produk
                        if (p < 0 or p > len(prod)):
                            print('Pilihan tidak ada')
                        elif (p == 0):
                            run_prod = False
                            finish = True
                        else:
                            # Kondisional cek harga produk
                            if (prod[p-1][1] > 0):
                                if (total >= prod[p-1][2]):
                                    prod[p-1][1] -= 1
                                    total -= prod[p-1][2]
                                    print('Mengeluarkan ' + prod[p-1][0])
                                    df_products = pd.DataFrame.from_records(prod, columns=['Nama', 'Stok', 'Harga'])
                                    df_products.index = df_products.index + 1
                                    df_products.to_csv(r'products.csv', index = False)
                                    wait()
                                else:
                                    print('Uang tidak cukup')
                                    cont = input('Apakah anda ingin memasukkan uang lagi (y/n) : ')
                                    if (cont == 'y'):
                                        run_prod = False
                                        finish = False
                            elif (prod[p-1][1] == 0):
                                print('Produk habis')
                        print(' ')
                    
                    # Proses penghitungan kembalian
                    if (finish == True):
                        if (total > 0):
                            print('Mengeluarkan kembalian '+ money_denom[0][2]+ ' ' + str(total))
                            sisa = CalcChange(total)
                            if (sisa > 0):
                                print('Maaf uang anda tidak bisa dikembalikan')
                                opt_sisa = input('Apakah anda ingin membeli produk lagi? (y/n) : ')
                                if (opt_sisa == 'n'):
                                    run_money = False
                            elif (sisa == 0):
                                run_money = False
                        elif (total == 0):
                            run_money = False
                    
                    # Menyimpan File CSV
                    df_denom = pd.DataFrame.from_records(money_denom, columns=['Nominal','Jumlah','Simbol'])
                    df_denom.to_csv(r'money.csv', index = False)
                
                # Ucapan di akhir transaksi
                wait()
                print(' ')
                print('-------------------------------------------------------------------------------')
                print('                                TERIMA KASIH                                   ')
                print('-------------------------------------------------------------------------------')
                print(' ')
                wait()
    
    # Jika pengguna memilih 2 - Pengaturan
    elif (opt_menu == 2):
        
        # Loop Pengaturan
        run_opt = True
        while (run_opt):
            MainSettings()
            opt_opt = int(input('Pilihan : '))
            # 1 - Ubah Produk dan Stok
            if (opt_opt == 1):
                # Mengubah semua data produk dan stok
                prod = inputProducts() # dengan fungsi inputProducts()
                n_prod = len(prod)
                df_products = pd.DataFrame.from_records(prod, columns=['Nama', 'Stok', 'Harga'])
                df_products.index = df_products.index + 1
                df_products.to_csv(r'products.csv', index = False)
            
            # 2 - Reset Stok
            elif (opt_opt == 2):
                # Mengembalikan stok semua produk ke stok awal
                stok = int(input('Stok Awal : '))
                for i in range(len(prod)):
                    prod[i][1] = stok
                df_products = pd.DataFrame.from_records(prod, columns=['Nama', 'Stok', 'Harga'])
                df_products.index = df_products.index + 1
                df_products.to_csv(r'products.csv', index = False)
                
            # 3 - Ubah Nominal Yang Diterima
            elif (opt_opt == 3):
                # Mengubah semua data inventaris uang
                money_denom = inputDenom() # dengan fungsi inputDenom()
                denom = len(money_denom)
                df_denom = pd.DataFrame.from_records(money_denom, columns=['Nominal','Jumlah','Simbol'])
                df_denom.to_csv(r'money.csv', index = False)
            
            # 4 - Reset Jumlah Uang
            elif (opt_opt == 4):
                # Mengembalikan jumlah semua nominal ke jumlah awal yang sama
                j_awal = int(input('Jumlah Awal : '))
                for i in range(len(money_denom)):
                    money_denom[i][1] = j_awal
                df_denom = pd.DataFrame.from_records(money_denom, columns=['Nominal','Jumlah','Simbol'])
                df_denom.to_csv(r'money.csv', index = False)
            
            # 0 - Kembali ke MENU UTAMA
            elif (opt_opt == 0):
                # Memberhentikan loop pengaturan
                run_opt = False
    
    # Jika pengguna memilih 3 - STOP Vending Machine
    elif(opt_menu == 3):
        # Memberhentikan pengulangan utama
        run = False

# File CSV disimpan sebelum sekuens program berakhir
df_products.to_csv(r'products.csv', index = False)
df_denom.to_csv(r'money.csv', index = False)