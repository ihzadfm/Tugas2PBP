Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/todolist/

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

-Inline Style Sheet adalah metode penulisan CSS langsung pada tag-tag HTML yang ingin kita stylekan CSSnya. Metode ini biasanya digunakan ketika kita tidak ingin mengatur semua elemen dalam dokumen web yang mempunyai kelebihan dimana bisa membuat style yang berlaku pada semua tag html. Metode ini tidak disarankan karena mengisi tag HTML dengan atribut HTML dan membuat file HTML menjadi lebih besar.
-Internal Style Sheet adalah cara untuk menulis CSS secara langsung dalam file HTML dan bisa membuat styel yang berlaku pada semua tag html, tepat sebelum kita memulai menulis kode CSS, tepat di antara tag head dan tag style. Kerugian internal css adalah peningkatan waktu kunjungan situs web karena perubahan terjadi pada 1 halaman dan tidak valid jika digunakan pada banyak file dengan css yang sama.
-Eksternal Style Sheet adalah cara untuk menulis CSS secara terpisah dengan memberi nama file ekstensi .css. dan kita taro pada css filenya buka html file. Metode ini sangat disarankan untuk menulis kode CSS, karena kita dapat dengan mudah memodifikasi kode yang dikumpulkan dalam satu file. Keuntungan dari css eksternal adalah kita dapat membuat styling yang berlaku untuk semua tag html dan kita dapat mengubah styling yang sudah dibuat tanpa mengubah file html. Kekurangannya Css eksternal hilang Jika css yang dimuat tidak selesai atau panggilan gagal, halaman akan berantakan.


2. Jelaskan tag HTML5 yang kamu ketahui.
Tag HTML5 yang saya ketahui adalah tag <header> yang	mendefinisikan sebuah header untuk bagian atau dokumen suatu halaman, lalu ada <div> yang mendefinisikan bagian dalam suatu dokumen dengan block, setelah itu ada <title> yang berguna mendefinisikan judul dokumen seperti HTML, ,<footer> yang mendeklarasikan bagian footernya, <form> untuk membuat formulir HTML untuk input user, <button> menambahkan sebuah tombol yang dapat ditekan, <table> yang dipergunakan untuk mendefinisikan sebuah tabel, dan lain sebagainya.


3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
a) ID selector, Selector jenis Id menggunakan atribut id pada html untuk menetapkan target tag yang ingin dimanipulasi. Penggunaan id pada kode CSS menggunakan tanda pagar(#).
b) Class selector, Selector jenis Class menggunakan atribut class pada html untuk menetapkan target tag yang ingin dimanipulasi. Penggunaan class pada kode CSS menggunakan titik(.)
c) Element selector, Element type selector merupakan selector yang langsung disisipkan di dalam tag HTML nya.Dalam praktiknya, setiap tag HTML bisa digunakan sebagai selector CSS.Contoh : h1 { color: red;}
p { text-decoration: italic;font-size: 20px; }

d) Universal selector,mSelector jenis Universal berfungsi untuk memengaruhi semua tag sehingga hanya ada 1 kode CSS di dalam HTML.Universal Selector ditulis dengan menggunakan tanda "*" yang bertujuan untuk memengaruhi semua tag yang ada dalam kode HTML.Contohnya untuk membuat agar seluruh tag HTML berwarna merah dan warna latar belakang berwarna biru : * { color:red; background-color: blue; }


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya melakukan perubahan class tabel pada todolist menjadikannya sebagi komponen cards yang tiap cards berisi satu task yang responsivenya di class cards saya mengambil referensi dari ristek.link/cardsmd. Ohiya saya menggunakan CSS selector yakni inline dan internal CSS sebagai styling pada file htmlnya. Untuk kreativitas styling dan cards saya menggunakan bootstrap karena lebih mudah bagi saya dan akan bootstrap akan merespon, lalu tag div dipergunakan karena tidak menggunakan tabel.

Langkah kedua kita tinggal mengatur komponen sesuai kreativitas kita seperti penempatan width, display, margin, dan text-align yang lebih ketengah dengan penambahan background sesuai keinginan. Pada semua file htmlnya kita menggunakan kerangka dengan tabel yang berisi button dan informasi untuk sebuah operasi yang diinginkan, agar lebih responsive saya tambahkan pseudo-class hover.

Langkah ketiga saya iseng membuat bonus dengan menambahkan beberapa hal di dalam cards dan page untuk styling supaya dapat dihover dan lebih responsive. Selain itu, saya melakukan beberapa editan styling dengan melihat perbandingannya pada http://localhost:8000/todolist/. Terakhir saya melakukan deployment yang sudah otomatis terdeploy ke herokuapp karena menggunakan repo tugas sebelumnya yang pasti sudah terdeploy pekan lalu (add, commit, push) dan mengecheck kembali aplikasi heroku berjalan sesuai keinginan.

