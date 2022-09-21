Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/katalog/

Membuat sebuah README.md yang berisi tautan menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
 1. Jelaskan perbedaan antara JSON, XML, dan HTML!

Perbedaan JSON XML HTML Tugas 3.jpg
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/Perbedaan%20JSON%20XML%20HTML%20Tugas%203.jpg width = "1920" height = "1080">

 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

 Dikarenakan saat mendevelopment sebuah platform akan diperlukan bagian  mengirim data dari satu tumpukan (stack) ke tumpukan lainnya. Format data umum yang dikirim bisa bermacam-macam bentuknya seperti HTML, XML, dan JSON. 

 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 
 Pertama-tama saya mulai dengan membuat sebuah aplikasi baru dengan menggunakan folder penyimpanan tugas2pbp dengan menggunakan startapp kode `python manage.py startapp mywatchlist`, tahap kedua agar kita sebagai user dapat membuka localhost dengan cara pada file urls.py kita tambahkan path 'mywatchlist', sehingga ketika kita membuka `http://localhost:8000/mywatchlist` akan muncul yang kita buat. Pada file models.py yang ada pada folder mywatchlist saya menambahkan beberapa atribut yang dibutuhkan seperti `watched` untuk menyatakan apakah sudah ditonton apa belum sebuah film pada html, lalu ada atribut `title` untuk memetakan judul pada film, selanjutnya ada atribut `rating` yang berguna mendeskripsikan rating film dalam rentang 1 sampai dengan 5, setelah itu atribut `release_date` berguna mendeskripsikan kapan sebuah film dirilis, dan yang terakhir atribut `review` untuk menjelaskan review kepada sebuah film dengan kata-kata. Tidak lupa melakukan makemigrations dan migrate dengan python manage.py pada cmd ke dalam local database
 
 Langkah ketiga saya mengisi file `initial_mywatchlist_data.json` pada folder fictures didalam mywatchlist dengan potongan kode 10 data object mywatchlist dengan atribut yang sudah dibuat diatas. Setelah itu, saya mengimplementasikan fitur untuk penyajian data kedalam format `HTML`, `XML`, dan `JSON`, jika sudah tambahkan path url pada urls.py ke dalam `urlspatterns` untuk mengakses fungsi yang sudah diimpor tadi (saya juga menghandle path kosong selain ketiga format diatas). Pada file views.py karena telah diimporshow_xml dan show_json pada urls.py, maka saya tambahkan fungsi `def show_xml(request):` dan `def show_json (request):`.

Tahap akhir saya membuat routing agar data yang kita buat diatas dapat diakses melalui `http://localhost:8000/`baik dengan pengaksesan berupa `HTML`, `XML`, dan `JSON`, semua itu dilakukan oleh path pada urls.py. Terakhir saya melakukan`deployment` yang sudah otomatis terdeploy ke `herokuapp` karena menggunakan repo tugas sebelumnya yang pasti sudah terdeploy pekan lalu. Jangan lupa untuk menggunakan postman yang mengembalikan respon HTTP 200 OK kita tambahkan 3 fungsi pada tests.py. Pada tests.py saya membuat 3 fungsi `def testmywatchlisturl_html_exists`, `def testmywatchlisturl_xml_exists`, dan `def testmywatchlisturl_json_exists` dengan parameter `self` yang masing-masing jenis data dan variabel response `client().get`.

html.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/html.png width = "1920" height = "1080">

json.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/json.png width = "1920" height = "1080">

xml.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/xml.png width = "1920" height = "1080">