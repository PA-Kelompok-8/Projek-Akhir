
Kelompok 8 ASD

Deskripsi Program :
Program ini adalah program untuk karyawan bank untuk mengatur antrian bank yang menggunakan struktur data queue (antrian). Queue program ini menggunakan prinsip FIFO (First in First Out) yaitu nasabah yang pertama kali masuk antrian akan dilayani terlebih dahulu. Program ini menggunakan Jump search untuk mencari nama nasabah dalam antrian. Lalu program ini juga menggunakan shell sort untuk mengurutkan saldo nasabah dari yang tertinggi ke terendah (Descending). Program ini menggunakan Database online untuk Login dan Menyimpan data nasabah.


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



Fitur dan Fungsionalitas : 

Fitur : 

Menu Utama :
1.	Login Teller
2.	Login CS
3.	Exit

Menu Teller :
1.	Menambah antrian
2.	Melihat antrian
3.	Memanggil antrian
4.	Mencari antrian
5.	Menambah saldo nasabah
6.	Setor Tunai 
7.	Keluar dari Teller

Menu Customer Service :
1.	Menambah antrian
2.	Melihat antrian
3.	Memanggil antrian
4.	Mencari antrian
5.	Melihat data nasabah
6.	Mengurutkan data nasabah 
7.	Buat Akun/ Rekening baru
8.	Keluar dari CS

Fungsionalitas :

Program ini merupakan program untuk pegawai bank (Teller dan Customer Service) yang bertugas mengatur antrian nasabah. Pada menu teller, bisa melayani nasabah yang ingin melakukan setor tunai dan menarik saldo. Selain itu, Teller juga dapat menambahkan nama nasabah ke dalam antrian serta bisa melihat dan memanggil nasabah dari antrian. Lalu, pada menu customer service, kurang lebih sama dengan teller yaitu bisa menambah dan melihat, nama nasabah dari antrian. Bedanya, Customer service bisa melihat data nasabah, mencari data nasabah, mengurutkan data nasabah berdasarkan saldo dari yang terbesar ke terkecil, serta membuat rekening atau akun nasabah. 


 Cara Penggunaan :
1.	Pertama, user diminta memilih menu yang diinginkan antara Login sebagai Teller atau Login sebagai Customer service.

2.	Semisal user memilih Login sebagai teller maka selanjutnya user diminta memasukkan username dan password yang sudah tersedia khusus Login Teller.

3.	Setelah berhasil masuk, ada 7 hal yang bisa dilakukan Teller terhadap antrian. Teller  menambahkan nama nasabah terlebih dahulu ke dalam antrian sebelum melihat, memanggil, dan mencari data nasabah.
•	Menu melihat antrian : pada menu ini user memasukkan nama nasabah terlebih dahulu agar dapat melihat antrian yang ada
•	menu memanggil antrian : pada menu ini nasabah yang terpanggil otomatis akan terhapus dari antrian
•	Menu mencari nasabah : pada menu ini user dapat mencari nama nasabah

Jika nama nasabah sudah ada didalam antrian, maka nasabah bisa menarik saldo ataupun setor tunai.

•	Menu Menarik saldo : pada menu ini nasabah bisa menarik uang sesuai saldo yang tersedia
•	Menu Setor tunai : pada menu ini nasabah bisa menyetor uang agar bisa disimpan didalam rekening 
•	Keluar dari Menu Teller : pada menu ini user dapat keluar dari Menu Teller
 
4.	Selanjutnya, jika user memilih login sebagai CS maka User diminta memasukkan username dan password yang sudah tersedia khusus login CS.

5.	Setelah berhasil masuk, ada 7 hal juga yang dapat dilakukan CS terhadap antrian. CS wajib menambahkan nama nasabah terlebih dahulu ke dalam antrian sebelum melihat dan menghapus nama nasabah dari antrian.

•	Menu melihat data nasabah : Pada menu ini user dapat melihat data nasabah yaitu Nama, No rekening, dan saldo.
•	Menu mencari nasabah : Pada menu ini user dapat mencari nama nasabah
•	Menu membuat akun/rekening : Pada menu ini user dapat membuat rekening baru untuk nasabah yang belum memilki rekening
•	Keluar dari Menu CS : Pada menu ini user dapat keluar dari Menu CS
