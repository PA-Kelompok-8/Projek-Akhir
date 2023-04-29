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

