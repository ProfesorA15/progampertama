# -*- coding: utf-8 -*-
"""Membuat fungsi python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P7vxLr8hNuw73t-v1ATssXd0yw_wc61I
"""

#membuat fungsi
def salam():
    print ("Hello, Konichiwa")

## Pemanggilan Fungsi
salam()

salam()
salam()

def salam(ucapan):
    print(ucapan)
salam("konichiwa")

#membuat fungsi dengan parameter
def luas_segitiga(alas,tinggi):
    luas = (alas * tinggi) / 2
    print ("luas segitiga: %f" % luas)

#Pemanggilan fungsi
luas_segitiga(7,8)

#fungsu return
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

#pemanggilan fungsi
print ("luas persegi: %d" % luas_persegi(9))

# Membuat variabel global
nama = "Belajar Kode"
versi = "1.0.1"

def help():
    # ini vsriabel lokal
    nama = "My Program"
    versi = "1.0.1"
    # mengakses variabel lokal
    print ("Nama: %s" % nama)
    print ("Versi: %s" % versi)


# mengakses variabel gloabal
print ("nama: %s" % nama)
print ("versi: %s" % versi)

#memanggil fungsi help
help()

# Membuat variabel global
nama = "Muhammad Qodrat Hanif Fadhila"
tgl_lhr = "14-07-2002"

def biodata():
    # ini vsriabel lokal
    hobi = "Yang Enak Enak"
    jurusan = "Computer Science"
    tmpt_tinggal = "Belitung Timur"
    # mengakses variabel lokal
    print ("hobi: %s" % hobi)
    print ("jurusan: %s" % jurusan)
    print ("tmpt_tinggal: %s" % tmpt_tinggal)


# mengakses variabel gloabal
print ("nama: %s" % nama)
print ("tgl_lhr: %s" % tgl_lhr)

#memanggil fungsi help
biodata()

Buku = []

# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("Nothing File")
    else:
        for indeks in range(len(buku)):
            print("[{}]] {}".format(indeks, buku[indeks]))

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku: " )
    buku.append(buku_baru)

#fungsi untuk edit data
def edit_data():
    show_data
    indeks = int(input("Inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

#fungsi untuk edit data
def delete_data():
    show_data
    indeks = int(input("Inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

# funsi untuk menampilkan menu
def show_menu():
    print("\in")
    print("------------ MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU")
    print("\n")

if int(menu) == 1:
    show_data()
 elif int(menu) == 2:
    insert_data()
 elif int(menu) == 3:
    edit_data()
 elif int(menu) == 4:
    delete_data()
 elif int(menu) == 5:
    exit()
 else:
    print("Salah pilih")


if __name__ == "__main__":

    while True:
        show_menu()

buku = []

def show_data():
    if len(buku) <= 0:
        print("Nothing File")
    else:
        for indeks in range(len(buku)):
            print("[{}]] {}".format(indeks, buku[indeks]))
def insert_data():
    buku_baru = input("Judul Buku: " )
    buku.append(buku_baru)
def edit_data():
    show_data
    indeks = int(input("Inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
def delete_data():
    show_data
    indeks = int(input("Inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])
def show_menu():
    print("\in")
    print("------------ MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU")
    print("\n")
    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        exit()
    else:
        print("Salah pilih")

if __name__ == "__main__":

         while True:
             show_menu()

\