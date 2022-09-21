Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/katalog/

Membuat sebuah README.md yang berisi tautan menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
 1. Jelaskan perbedaan antara JSON, XML, dan HTML!


 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

 Dikarenakan saat mendevelopment sebuah platform akan diperlukan bagian  mengirim data dari satu tumpukan (stack) ke tumpukan lainnya. Format data umum yang dikirim bisa bermacam-macam bentuknya seperti HTML, XML, dan JSON. 

 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 
 Pertama-tama saya mulai dengan membuaT sebuah aplikasi baru dengan menggunakan folder penyimpanan tugas2pbp dengan menggunakan startapp kode 'python manage.py startapp wishlist', tahap kedua agar kita sebagai user dapat membuka localhost dengan cara pada file urls.py kita tambahkan path 'mywatchlist', sehingga ketika kita membuka

 Pertama saya membuat app baru pada folde tugas 2 pekan kemarin dengan perintah `python manage.py startapp mywatchlist`. Kemudian saya menambahkan path *mywatchlist* di `urls.py`agar pengguna dapat mengakses di `http://localhost:8000/mywatchlist`. Selanjutnya saya membuat sebuah model `MyWatchlist` pada *models.py* yang memiliki atribut `watched` untuk mendeskripsikan film tersebut sudah ditonton atau belum, `title` untuk mendeskripsikan judul film, `rating` untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5, `release_date` untuk mendeskripsikan kapan film dirilis, `review` untuk mendeskripsikan review untuk film tersebut. Lalu saya membuat file `initial_mywatchlist_data.json` yang isinya 10 data untuk objek `MyWatchList`. untuk menyajikan data dalam bentuk `HTML`, `XML`, dan `JSON` saya menambahkan `urlspatterns` di `urls.py` dengan cara 
1. `path('html', show_MyWatchList name='show_MyWatchlist'),`
2. `path('xml/', show_xml, name='show_xml'),`
3. `path('json/', show_json, name='show_json'),`

Saya juga membuat fungsi pada file `views.py` 
1. `def show_xml(request):`
    `data = MyWatchList.objects.all()`
    `return HttpResponse(serializers.serialize("xml" data), content_type="application/xml")`

2. `def show_json (request):`
    `data = MyWatchList.objects.all()`
    `return HttpResponse(serializers.serialize("json",` `data), content_type="application/json")`

3. `def show_json_by_id (request,id):`
    `data = MyWatchList.objects.filter(pk=id)`
    `return HttpResponse(serializers.serialize("json",` `data), content_type="application/json")`

4. `def show_xml_by_id (request,id):`
    `data = MyWatchList.objects.filter(pk=id)`
    `return HttpResponse(serializers.serialize("xml",` `data), content_type="application/xml")`

untuk membuat routing saya menambahkan path pada `urls.py` agar data dapat diakses berupa `HTML`, `XML`, dan `JSON`. Untuk `deployment` sudah otomatis terdeploy ke `herokuapp` karena memakai repo github yang sama yang sudah terdeploy juga. 

Pada `tests.py` saya membuat 3 fungsi yang isi parameternya `self` dan variabel response isinya `client().get` dengan paramaternya masing - masing jenis data.

html.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/html.png width = "1920" height = "1080">

json.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/json.png width = "1920" height = "1080">

xml.png
<img src= https://github.com/ihzadfm/Tugas2PBP/blob/main/mywatchlist/SS%20Postman/xml.png width = "1920" height = "1080">