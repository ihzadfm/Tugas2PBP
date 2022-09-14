Membuat sebuah README.md yang berisi link menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;



2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Saat kita menginstal modul/library menggunakan pip, modulnya akan terinstal secara global di /usr/lib/python2.7/site-packages. Semua aplikasi bisa mengakses dan menggunakannya. Akan tetapi mempunyai kekurangan jika saat kita mendapatkan suatu perubahan versi modul pada Django akan menjadi masalah yang berbarengan dengan pembuatan suatu proyek aplikasi. Walaupun setelah itu, kita sudah update modul, tetap saja akan menjadikan aplikasi yang sudah kita buat tidak bisa berjalan akibat perubahan versi modul yang terbaru karena update fungsi, dll. Sedangkan modul versi lama masih masih dibutuhkan proyek aplikasi lain, oleh karena itulah gunanya virtual environment supaya masing-masing aplikasi mempunyai modul sendiri


3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.



Link aplikasi Heroku : https://tugas2pbpihza.herokuapp.com/katalog/