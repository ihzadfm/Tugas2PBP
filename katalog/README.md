Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/katalog/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

https://drive.google.com/file/d/1YWppt325fTGqCI-MLWnx2nuLjMN8LxqW/view?usp=sharing

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Saat kita menginstal modul/library menggunakan pip, modulnya akan terinstal secara global di /usr/lib/python2.7/site-packages. Semua aplikasi web django bisa dibuat tanpa menggunakan virtual environment . Akan tetapi mempunyai kekurangan jika saat kita mendapatkan suatu perubahan versi modul pada Django akan menjadi masalah yang berbarengan dengan pembuatan suatu proyek aplikasi. Walaupun setelah itu, kita sudah update modul, tetap saja akan menjadikan aplikasi yang sudah kita buat tidak bisa berjalan akibat perubahan versi modul yang terbaru karena update fungsi, dll. Sedangkan modul versi lama masih masih dibutuhkan proyek aplikasi lain, oleh karena itulah gunanya virtual environment supaya masing-masing aplikasi mempunyai modul sendiri. Di samping itu virtual environment, dependencies dan packages yang diperlukan oleh kerangka kerja Django secara otomatis diinstal padahal di local tidak terinstall secara global. Jika kita tidak memakai env, hanya akan dapat mengaksesnya dari direktori tempat yang sudah dinstall saja. Tujuan lain untuk membuat ruang kerja Python yang terisolasi, sehingga kita tidak akan mengganggu saat punya banyak proyek. 

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pertama-tama saya mulai dengan membuat fungsi show_catalog() pada views.py yang bertujuan untuk return dengan render kedalam katalog.html dan juga taken object dari CatalogItem.objects.all(). Selanjutnya ada dictionary context yang isinya container, dengan tambahan daftar catalog, nama, NPM. Semua yang telah ditambahkan tersebut akan dirender ke HTML nya.

Langkah kedua saya mengisi urls.py yang ada pada project_django untuk mendaftarkan aplikasi katalog supaya terlihat tampilannya dengan cara menambahkan path yang include katalog.urls. Selain itu urls.py pada folder katalog juga di routing dengan memanggil fungsi show_catalog() yang didapat dari impor fungsi pada file views.py, lalu menambahkan path fungsi diatas supaya render bisa dilakukan ke katalog.html di urlpatterns. Tidak lupa kita harus mengubah fill me menjadi {{name}} pada file katalog.html supaya nama yang sudah kita buat pada views.py bisa muncul dan terender di aplikasi web, semua itu dilaukan karena saya melakukan pemetaan data yang mau di render yang berada pada views.py. Selanjutnya ada pemanggilan list_catalog berdasarkan pengiterasian data_catalog_item yang berasal dari fungsi show_catalog().

Tahap akhir mengatur deploy Heroku dengan cara membuat file Procfile, saya melakukan deployment dengan cara membuat aplikasi dengan namanya di HEROKU, jangan lupa untuk implementasi penilaian diharuskan impor repo tugas2pbp dari Github Ke Heroku. Selanjutnya mendapatkan API KEY setelah pembuatan aplikasi di Heroku dengan merevealnya dan, saya menambahkan action secret pada Github yaitu HEROKU_API_KEY dan HEROKU_APP_NAME. Selesai sudah akhirnya dengan membuka aplikasi yang kita buat di https://<nama-aplikasi-heroku>.herokuapp.com