
## Tugas 3
Link :  [HTML](https://rikzapbp2.herokuapp.com/mywatchlist/html) -- [XML](https://rikzapbp2.herokuapp.com/mywatchlist/xml) -- [JSON](https://rikzapbp2.herokuapp.com/mywatchlist/json)

- Html digunakan untuk menyajikan data yang telah terstruktur ke halaman web. Sementara xml dan json digunakan untuk menyimpan dan mengirim data dari dan ke database. Perbedaan yang paling terlihat adalah cara menulis kode yang berbeda seperti untuk merepresentasukan suatu object. Json menggunakan data structure berupa map yang memiliki key dan value sedangkan xml menggunakan structrure tree dengan menggunakan tag sama seperti html. Kelebihan json yaitu lebih mudah dibaca dan lebih cepat dijalankan dibanding xml. Sementara kelebihan xml yaitu bisa menggunakan array dan lebih secured.

- Data delivery diperlukan agar data yang ada di database kita dapat ditampilkan ke web(platform) sehingga bisa dilihat oleh orang yang kita tuju(pengguna). Data yang ingin kita tampilkan pasti akan berubah sesuai perubahan kondisi dan permintaan pengguna. Dengan adanya data delivery, data yang akan ditampilkan dapat disesuaikan dengan permintaan sehingga tidak semua data yang ada di database perlu ditampilkan dan bisa menghemat waktu. 

Dalam mengerjakan tugas 3 ini, hal yang pertama saya lakukan adalah menjalankan command 
`python manage.py startapp mywatchlist` Tujuannya adalah untuk membuat folder untuk app mywatchlist secara otomatis. Selanjutanya saya mengatur urls pada folder project_django untuk routing ke app yg baru dibuat. Lalu dilanjutkan dengan mengatur MVT, yaitu pada models.py saya menambahkan MovieWatchList dengan judul, status_watched, rating, release_date, dan review sebagi attribute. Lalu saya melakukan migration untuk memasukan models tersebut. Pada views.py saya membuat fungsi show_watchlist untuk mengirim data ke template. Selanjutnya saya membuat file watchlist.html untuk menampilkan data. Data yang akan ditampilkan yaitu berupa film-film yang mau atau sudag saya tonton. Untuk menambahkannya saya membuat file initial_watchlist_data.json dan memasukan nama dan atribut lainnya secara manual. Setelahnya saya menjalankan command `python manage.py loaddata initial_wishlist_data.json` untuk memasukkan data. Langkah selanjutnya sama seperti pada tutorial saya menambahkan fungsi show_xml dan show_json dan mengatur routingnya. Lalu saya menambahkan fungsi test. Untuk melengkapi bagian bonus, saya menambahkan variabel untuk menghitung jumlah film yang ditonton dan mengatur if else statement pada views.py dan watchlist.html untuk menghandle kondisi yang benar. Pada file html juga saya mengubah linknya menjadi bentuk hyperlinkagar lebih mudah digunakan.

Postman:




---

## Tugas 2

Link app yang telah di deploy:
[KATALOG](https://rikzapbp2.herokuapp.com/katalog/)

Penjelasan:
![Mind map](https://user-images.githubusercontent.com/112408954/190227677-a70cc712-dad4-4eff-a6e0-1ed17b4c35c1.png)

Virtual environment adalah lingkungan virtual yang terpisah dari host OS. Setiap project sebaiknya dibuat dengan menerapkan virtual environment, karena tiap project mungkin saja memiliki keperluan package atau dependency yang berbeda. Jika kita tidak menggunakan virtual environment, maka ketika kita menginstall atau menghapus suatu dependency yang diperlukan oleh salah satu project terhapus sehingga project tersebut tidak bisa di-run.  Oleh sebab itu virtual environment digunakan agar package dan dependency dari project yang berbeda tidak akan bertabrakan dan mengganggu satu sama lain. 

Untuk mengerjakan tugas ini saya banyak mengambil referensi dari tutorial 1, yang pertama saya lakukan adalah membuat fungsi yang bernama show_katalog yang mengambil data dari models.py dan menyimpan data berupa nama, npm dan barang katalog dari object CatalogItem di file models.py dalam suatu dictionary bernama context. Lalu fungsi tersebut akan memanggil fungsi render() dengan parameter berupa request, nama template html dan dictionary "context". Fungsi render tadi akan mengirimkan data-data tersebut ke template untuk digabungkan menjadi file html. Selanjutnya pada file urls.py, saya menambahkan path baru sebagai mapping ke app katalog. Setelah selesai saya melanjutkan untuk deploy ke heroku. Hal yang pertama saya lakukan adalah memastikan file Procfile telah ada. Selanjutnya saya menambahkan dua repository secret yaitu HEROKU_APP_KEY dan HEROKU_APP_NAME agar proses deploy bisa dijalankan. Setelahnya proses deploy akan berlangsung secara otomatis. 
