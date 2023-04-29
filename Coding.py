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
