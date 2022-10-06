## Tugas 5
Link :  [Todolist](https://rikzapbp2.herokuapp.com/todolist)
- 



## Tugas 4
Link :  [Todolist](https://rikzapbp2.herokuapp.com/todolist)
- `{% csrf_token %}` berfungsi untuk mencegah terjadinya serangan Cross Site Request Forgery (CSRF), yaitu serangan berupa request palsu yang tidak diinginkan oleh user.  Cara kerja csrf token yaitu dengan membuat suatu token dari server-side yang akan selalu dicek ketika user melakukan request. Jika suatu request tidak memiliki token tadi maka request tersebut tidak akan dieksekusi. Jika kita tidak menggunakan `{% csrf_token %}` maka CSRF attack bisa terjadi dan keamanan user dan web itu sendiri tidak terjamin.

- Form dapat dibuat tanpa menggunakan `{{ form.as_table }}`. Untuk membuat form secara manual, kita perlu mendefinisikan terlebih dahulu url untuk mengirim data dan method yang akan digunakan yaitu GET atau POST dalam tag `<form>`. Selanjutnya kita bisa membuat elemen-elemen lainnya untuk menerima input atau memberi label/nama.


- Alur datanya berawal dari request user. Setelah menerima request server akan menampilkan file html yang memiliki form di dalamnya. User dapat mengisi form tersebut dan mengirimkan request lagi ke server. Request yang dikirim akan dijalankan sesuai URL untuk mengirim data dan method yg digunakan(GET/POST). Setelah itu data yang dikirimkan akan diproses untuk disimpan ke database dan/atau untuk menampilkan halaman baru. Jika terjadi perubahan data pada database maka html akan menampilkan halaman yang telah diperbarui ke user.

Hal yang pertama saya lakukan adalah menjalankan fungsi `startapp` untuk membuat folder baru yaitu "todolist". Selanjutnya mengatur routing pada urls di project_django dan todolist. Lalu membuat models yaitu Task dengan attribute pengguna, tanggal, judul dan deskripsi serta melakukan makemigrations dan migrate. Selanjutnya saya mengimplementasikan form untuk login, registrasi dan logout sesuai dengan yang telah dipelajari pada tutorial sebelumnya. Lalu saya membuat file todolist.html dan mengatur tampilan web dengan menambahkan tabel serta beberapa label dan tombol. Membuat file create_task.html untuk menerima input berupa judul dan deskripsi serta menambahkan fungsi create_task pada views.py untuk menjalankan dan menyimpan data. Lalu saya menambahkan kolom sebagai status mengerjakan dan tombol untuk ubah status tersebut pada file html. 

---
## Tugas 3
Link :  [HTML](https://rikzapbp2.herokuapp.com/mywatchlist/html) -- [XML](https://rikzapbp2.herokuapp.com/mywatchlist/xml) -- [JSON](https://rikzapbp2.herokuapp.com/mywatchlist/json)

- Html digunakan untuk menyajikan data yang telah terstruktur ke halaman web. Sementara xml dan json digunakan untuk menyimpan dan mengirim data dari dan ke database. Perbedaan yang paling terlihat adalah cara menulis kode yang berbeda seperti untuk merepresentasukan suatu object. Json menggunakan data structure berupa map yang memiliki key dan value sedangkan xml menggunakan structrure tree dengan menggunakan tag sama seperti html. Kelebihan json yaitu lebih mudah dibaca dan lebih cepat dijalankan dibanding xml. Sementara kelebihan xml yaitu bisa menggunakan array dan lebih secured.

- Data delivery diperlukan agar data yang ada di database kita dapat ditampilkan ke web(platform) sehingga bisa dilihat oleh orang yang kita tuju(pengguna). Data yang ingin kita tampilkan pasti akan berubah sesuai perubahan kondisi dan permintaan pengguna. Dengan adanya data delivery, data yang akan ditampilkan dapat disesuaikan dengan permintaan sehingga tidak semua data yang ada di database perlu ditampilkan dan bisa menghemat waktu. 

Dalam mengerjakan tugas 3 ini, hal yang pertama saya lakukan adalah menjalankan command 
`python manage.py startapp mywatchlist` Tujuannya adalah untuk membuat folder untuk app mywatchlist secara otomatis. Selanjutanya saya mengatur urls pada folder project_django untuk routing ke app yg baru dibuat. Lalu dilanjutkan dengan mengatur MVT, yaitu pada models.py saya menambahkan MovieWatchList dengan judul, status_watched, rating, release_date, dan review sebagi attribute. Lalu saya melakukan migration untuk memasukan models tersebut. Pada views.py saya membuat fungsi show_watchlist untuk mengirim data ke template. Selanjutnya saya membuat file watchlist.html untuk menampilkan data. Data yang akan ditampilkan yaitu berupa film-film yang mau atau sudag saya tonton. Untuk menambahkannya saya membuat file initial_watchlist_data.json dan memasukan nama dan atribut lainnya secara manual. Setelahnya saya menjalankan command `python manage.py loaddata initial_wishlist_data.json` untuk memasukkan data. Langkah selanjutnya sama seperti pada tutorial saya menambahkan fungsi show_xml dan show_json dan mengatur routingnya. Lalu saya menambahkan fungsi test. Untuk melengkapi bagian bonus, saya menambahkan variabel untuk menghitung jumlah film yang ditonton dan mengatur if else statement pada views.py dan watchlist.html untuk menghandle kondisi yang benar. Pada file html juga saya mengubah linknya menjadi bentuk hyperlinkagar lebih mudah digunakan.

Postman:
![tug3pbp1](https://user-images.githubusercontent.com/112408954/191659509-235ac930-8b0e-4a7e-b4dd-da54c43117d0.PNG)


![tug3pbp2](https://user-images.githubusercontent.com/112408954/191659527-35f88c08-95d4-4eb3-be93-4048c0931627.PNG)


![tug3pbp3](https://user-images.githubusercontent.com/112408954/191659540-5b156310-d850-4e91-861c-b06cbdb1da4c.PNG)

---

## Tugas 2

Link app yang telah di deploy:
[KATALOG](https://rikzapbp2.herokuapp.com/katalog/)

Penjelasan:
![Mind map](https://user-images.githubusercontent.com/112408954/190227677-a70cc712-dad4-4eff-a6e0-1ed17b4c35c1.png)

Virtual environment adalah lingkungan virtual yang terpisah dari host OS. Setiap project sebaiknya dibuat dengan menerapkan virtual environment, karena tiap project mungkin saja memiliki keperluan package atau dependency yang berbeda. Jika kita tidak menggunakan virtual environment, maka ketika kita menginstall atau menghapus suatu dependency yang diperlukan oleh salah satu project terhapus sehingga project tersebut tidak bisa di-run.  Oleh sebab itu virtual environment digunakan agar package dan dependency dari project yang berbeda tidak akan bertabrakan dan mengganggu satu sama lain. 

Untuk mengerjakan tugas ini saya banyak mengambil referensi dari tutorial 1, yang pertama saya lakukan adalah membuat fungsi yang bernama show_katalog yang mengambil data dari models.py dan menyimpan data berupa nama, npm dan barang katalog dari object CatalogItem di file models.py dalam suatu dictionary bernama context. Lalu fungsi tersebut akan memanggil fungsi render() dengan parameter berupa request, nama template html dan dictionary "context". Fungsi render tadi akan mengirimkan data-data tersebut ke template untuk digabungkan menjadi file html. Selanjutnya pada file urls.py, saya menambahkan path baru sebagai mapping ke app katalog. Setelah selesai saya melanjutkan untuk deploy ke heroku. Hal yang pertama saya lakukan adalah memastikan file Procfile telah ada. Selanjutnya saya menambahkan dua repository secret yaitu HEROKU_APP_KEY dan HEROKU_APP_NAME agar proses deploy bisa dijalankan. Setelahnya proses deploy akan berlangsung secara otomatis. 
