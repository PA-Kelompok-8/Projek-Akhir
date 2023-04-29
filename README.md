
Struktur Projek : 
-	Import Library : 
berfungsi untuk mengimport suatu fungsi agar bisa dijalankan di dalam suatu program.
Library yang digunakan dalam program antrian bank ini yaitu :
1.	Library Pretty Table : untuk membuat table pada output program yang berisi data nasabah
2.	Library Math : digunakan untuk algoritma shell sort
3.	Library Sys : untuk exit program
4.	Library Mysql.connector : untuk menghubungkan database online yang dipakai dalam program.
5.	Library Queue : untuk penggunaan struktur data queue dalam program

-	Class : 
Didalam Program ini ada 2 class yaitu Class queue_teller dan Class queue_cs. Di Queue teller dan CS terdapat 6 fungsi/method, yaitu :
1.	Def init : untuk membuat list yang akan digunakan pada antrian
2.	Def is empty : untuk mengetahui apakah antrian tersebut kosong atau tidak
3.	Def enqueue : untuk menambah nasabah ke dalam antrian
4.	Def Dequeue : untuk memanggil nasabah (menghapus nasabah dari antrian)
5.	Def Size : untuk mengetahui Panjang list antrian
6.	Def Jump Search : untuk menjalankan algoritma jump search untuk mencari nasabah pada antrian

-	Algoritma Searching:
Program ini menggunakan algoritma Jump search yang dikombinasikan dengan linier search. Data daftar antrian dibagi menjadi beberapa bagian dengan ukuran yang ditentukan berdasarkan kuadrat dari Panjang list. Program kemudian mencari data di blok ini menggunakan linier search. Jika data yang di cari tidak ada di blok saat ini, program akan pindah ke blok berikutnya dengan menambahkan nilai awal dan akhir blok ke ukuran blok.Jika data ditemukan, program mengembalikan indeks data. Namun, jika tidak ada data yang ditemukan di semua blok, program akan mengeluarkan pesan bahwa tidak ada data yang ditemukan.
-	Algoritma Sorting :
Program ini menggunakan algoritma Shell Sort yang digunakan untuk mengurutkan data nasabah berdasarkan saldo dari yang terbesar ke terkecil. Algoritma ini bekerja dengan cara membagi list data menjadi beberapa bagian kemudian melakukan Insertion Sort pada setiap bagian secara terpisah. Setelah itu, nilai gap yang digunakan untuk membagi data dikurangi setengah dan proses Insertion Sort diulang pada setiap bagian hingga gap mencapai nilai 1.
