from prettytable import PrettyTable
from queue import Queue
import mysql.connector
import sys, math
    
class Queue_teller:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def jumpSearch(self):
        x = (input("Masukkan nama yang ingin dicari: "))
        # Inisialisasi variabel untuk menyimpan indeks awal dan akhir blok
        start = 0
        end = int(math.sqrt(len(self.items)))

        # Iterasi pada setiap blok data
        while start < len(self.items):
            # Jika data ditemukan di blok saat ini, kembalikan indeks data tersebut
            for i in range(start, min(end, len(self.items))):
                if self.items[i] == x:
                    print("Nasabah berada pada antrian: ", i+1)
                    break
            
            # Jika data belum ditemukan di blok saat ini, pindah ke blok berikutnya
            else:
                start = end
                end += end
                continue
    
    # Jika data sudah ditemukan, keluar dari loop
            break
    
# Jika data tidak ditemukan, kembalikan pesan bahwa data tidak ditemukan
        else:
            print("Data tidak ditemukan")


def print_queue(queue):
    print("Antrian:")
    for i, item in enumerate(queue.items):
        print(f"[{i+1}] {item}")

class Queue_cs:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def jumpSearch(self):
        x = (input("Masukkan nama yang ingin dicari: "))
        # Inisialisasi variabel untuk menyimpan indeks awal dan akhir blok
        start = 0
        end = int(math.sqrt(len(self.items)))

        # Iterasi pada setiap blok data
        while start < len(self.items):
            # Jika data ditemukan di blok saat ini, kembalikan indeks data tersebut
            for i in range(start, min(end, len(self.items))):
                if self.items[i] == x:
                    print("Nasabah berada pada antrian: ", i+1)
                    break
            
            # Jika data belum ditemukan di blok saat ini, pindah ke blok berikutnya
            else:
                start = end
                end += end
                continue
    
    # Jika data sudah ditemukan, keluar dari loop
            break
    
# Jika data tidak ditemukan, kembalikan pesan bahwa data tidak ditemukan
        else:
            print("Data tidak ditemukan")
            
def print_queue(queue):
    print("Antrian:")
    for i, item in enumerate(queue.items):
        print(f"[{i+1}] {item}")

teller_queue = Queue_teller()
cs_queue = Queue_cs()

def teller_menu():
    while True:
        print("Menu Teller:")
        print("1. Tambah Antrian")
        print("2. Lihat antrian")
        print("3. Memanggil Antrian")
        print("4. Mencari Nasabah")
        print("5. Tambah Saldo")
        print("6. Tarik Saldo")
        print("7. keluar dari teller")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            name = input("Masukkan nama nasabah: ")
            teller_queue.enqueue(name)
            print(f"{name} telah ditambahkan ke antrian.")
        elif choice == "2":
            print_queue(teller_queue)
        elif choice == "3":
            if not teller_queue.is_empty():
                name = teller_queue.dequeue()
                print(f"Saudara {name} harap mendatangi meja teller.")
            else:
                print("Antrian Teller Kosong.")
        elif choice == "4":
            teller_queue.jumpSearch()
        elif choice == "5":
            datanasabah()
            tambahsaldo()
        elif choice == "6":
            datanasabah()
            kurangsaldo()
        elif choice == "7":
            return menu_login()
        else:
            print("Pilihan tidak tersedia")

def cs_menu():
    while True:
        print("Menu CS:")
        print("1. Tambah Antrian")
        print("2. Lihat antrian")
        print("3. Memanggil Antrian")
        print("4. Urutkan Data Nasabah Berdasarkan Saldo")
        print("5. Lihat data Nasabah")
        print("6. Mencari Nasabah")
        print("7. Buat Akun")
        print("8. keluar dari cs")
        choice = input("Masukkan pilihan: ")
        if choice == "1":
            name = input("Masukkan nama nasabah: ")
            cs_queue.enqueue(name)
            print(f"{name} telah ditambahkan ke antrian.")
        elif choice == "2":
            print_queue(cs_queue)
        elif choice == "3":
            if not cs_queue.is_empty():
                name = cs_queue.dequeue()
                print(f"Saudara {name} harap mendatangi meja CS.")
            else:
                print("Antrian CS Kosong.")
        elif choice == "4":
            ngurut()
        elif choice == "5":
            datanasabah()
        elif choice == "6":
            cs_queue.jumpSearch()
        elif choice == "7":
            buatnasabah()
        elif choice == "8":
            return menu_login()
        else:
            print("Pilihan tidak tersedia.")


def shellSort(arr, col):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and temp[col] > arr[j - gap][col]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
        
def ngurut(): 
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customer")
    result = mycursor.fetchall()
# sort data by saldo using shell sort
# sort data by saldo using shell sort
    shellSort(result, 3)  

# Ngeprint data yang ter sorting
    table = PrettyTable()
    table.field_names = ["ID","Nama","No. Rekening", "Saldo","PIN"]
    
    # add rows to the table
    for row in result:
        table.add_row(row)
    
    # print the table
    print(table)

# Koneksi ke database
def konek():
    try:
        mydb = None
        mydb = mysql.connector.connect(
        host="db4free.net",
        user="yusril",
        password="yusril1234",
        database="kelompok8"
        )
        print("Database Connected")
    except mysql.connector.Error as z:
        print(f"Erorr: {z}")
    return mydb

# fungsi untuk login teller
def loginteller():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    query = "SELECT * FROM teller WHERE username = %s AND password = %s"
    value = (username, password)
    cursor = mydb.cursor()
    cursor.execute(query, value)
    result = cursor.fetchall()

    if result:
        print("Login berhasil")
        teller_menu()
    else:
        print("Login gagal")
        
# fungsi untuk login cs
def logincs():
    username = input("Masukkan username CS: ")
    password = input("Masukkan password CS: ")

    # query untuk mencari data admin di tabel cs
    query = "SELECT * FROM cs WHERE username = %s AND password = %s"
    value = (username, password)

    # eksekusi query
    cursor = mydb.cursor()
    cursor.execute(query, value)
    result = cursor.fetchall()

    if result:
        print("Login berhasil")
        cs_menu()
    else:
        print("Login gagal")

# Unruk melihat data nasabah
def datanasabah():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchall()

    if result:
        table = PrettyTable()
        table.field_names = ["ID","Nama","No. Rekening", "Saldo","PIN"]
        for row in result:
            table.add_row(row)
        print(table)
    else:
        print("Tidak ada data nasabah")

# Untuk membuat akun / buka rekening
def buatnasabah():
    try:
        id = input("Masukkan ID Nasabah: ")
        nama = input("Masukkan nama: ")
        rek = input("Masukkan nomor rekening: ")
        saldo = input("Masukkan saldo awal: ")
        pin = input("Masukkan PIN: ")

        # Menginput data ke dalam tabel MySQL
        mycursor = mydb.cursor()
        sql = "INSERT INTO customer (ID, nama, norek, saldo, PIN) VALUES (%s, %s, %s, %s,%s)"
        val = (id,nama, rek, saldo,  pin)
        mycursor.execute(sql, val)

        # Commit perubahan dan menutup koneksi ke database
        mydb.commit()
    except:
        print("Data Error")

#Untuk menarik saldo nasabah
def kurangsaldo():
    try:
        id = input("Masukkan ID nasabah yang ingin menarik saldo:")
        saldo = int(input("Masukkan jumlah saldo: "))

        # Query SQL untuk mengambil data saldo
        mycursor = mydb.cursor()
        sql = "SELECT saldo FROM customer WHERE id = %s"
        val = (id,)

        # Eksekusi query
        mycursor.execute(sql, val)

        # Ambil data saldo dari hasil query
        result = mycursor.fetchone()
        saldo_db = result[0]

        # Kurangi saldo di database dengan inputan saldo
        saldo2 = saldo_db - int(saldo)

        # Query SQL untuk mengupdate data
        if saldo2 > 0:
            sql = "UPDATE customer SET saldo = %s WHERE id = %s"
            val = (saldo2, id)

            # Eksekusi query
            mycursor.execute(sql, val)

            # Commit perubahan
            mydb.commit()

            # Cetak jumlah baris yang diupdate
            print(mycursor.rowcount, "Saldo Telah ditarik")
        else:
            print("Inputan harus benar")
    except:
        print("Error")
    
#Untuk menambah saldo
def tambahsaldo():
    try:
        id = input("Masukkan ID nasabah yang ingin memasukkan saldo:")
        saldo = int(input("Masukkan jumlah saldo: "))

        # Query SQL untuk mengambil data saldo
        mycursor = mydb.cursor()
        sql = "SELECT saldo FROM customer WHERE id = %s"
        val = (id,)

        # Eksekusi query
        mycursor.execute(sql, val)

        # Ambil data saldo dari hasil query
        result = mycursor.fetchone()
        saldo_db = result[0]

        # Kurangi saldo di database dengan inputan saldo
        saldo2 = saldo_db + int(saldo)

        # Query SQL untuk mengupdate data
        if saldo2 > 0:
            sql = "UPDATE customer SET saldo = %s WHERE id = %s"
            val = (saldo2, id)

            # Eksekusi query
            mycursor.execute(sql, val)

            # Commit perubahan
            mydb.commit()

            # Cetak jumlah baris yang diupdate
            print(mycursor.rowcount, "Saldo telah ditambah")
        else:
            print("Inputan Harus benar")
    except:
            print("Error")

# Untuk memanggil fungsi untuk menyambung database          
mydb = konek()

# Menu awal
def menu_login():
    while True:
        print("Menu Bank:")
        print("1. Login Teller")
        print("2. Login CS")
        print("3. Exit")
        menu = input("Pilih menu: ")

        if menu == "1":
                loginteller()
        elif menu == "2":
                logincs()
        elif menu == "3":
            print("Program telah berakhir")
            break
        else:
                print("Menu tidak tersedia")
menu_login()

