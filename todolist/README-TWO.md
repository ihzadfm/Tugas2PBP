Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/todolist/

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent. Sedangkan, synchronous programming memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.
Synchronous melakukan eksekusi secara berurutan dan umumnya function 1 harus benar-benar selesai baru melakukan eksekusi function 2 dan seterusnya. Sedangkan, Asynchronous bersifat menunda function yang berarti function 1 yang dijalankan dan belum selesai, dapat menjalankan function 2 dan seterusnya secara bersamaan dalam satu waktu.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming adalah paradigma pemrogrman yang jalannya program ini  ditentukan oleh event / peristiwa  yaitu sensor keloaran atau tindakan pengguna ( mouse klik, tombol ) atau pesan dari program lain. Event-driven programming juga dapat didefinisikan sebagai aplikasi teknik arsitektur yang memiliki aplikasi utama loop yang jelas ke bawah dibagi dua bagian: yang pertama adalah kegiatan seleksi (atau aktivitas deteksi), dan yang kedua adalah penanganan event.
Konsep event-driven yaitu suatu program yang pengeksekusiannya didasarkan atas kejadian (event) tertentu. Kejadian-kejadian itu sendiri, mempunyai kode program sendiri yang disimpan dalam sebuah fungsi (yang dirancang untuk melaksanakan tugas khusus).
Contoh penerapan yang ada pada tugas ini seperti saat event klik pada sebuah atribut tombol "Create a new task" / "Delete" / "Change Progression", yang bertujuan untuk menunggu aksi pengguna seperti klik (menekan tombol) sebelum melakukan fungsi yang bersesuaian.

3. Jelaskan penerapan asynchronous programming pada AJAX.
AJAX dapat digunakan untuk mengirim pesan ke server lalu mengambil hasil data dari server ke browser. Prinsip yang dikerjakan pun adalah asynchronous. Jadi, selama proses mengirim pesan terjadi, browser bisa tetap terus digunakan sambil menunggu respon dari server. AJAX JavaScript dan XML ini bekerja secara asynchronous untuk berkomunikasi dengan server. Proses pertukaran informasi ini dilakukan di background. Artinya, saat AJAX JavaScript dan XML bekerja, halaman dapat tetap diakses oleh pengunjung website. 
a)Browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server. 
b)XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron.
c)Server menerima, memproses, dan mengirimkan data kembali ke browser.  
d)Browser menerima data tersebut dan langsung ditampilkan di halaman website, tanpa perlu reload atau membuat halaman baru. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

a) Membuat sebuah implementasi views.py dan urls.py beserta konfigurasinya yang diperlukan yakni fungsi def show_todolist_json beserta urlsnya pada folder todolist, setelah itu menambahkan script calling AJAX untuk pengambilan task dengan AJAX yakni post dan get sesuai operasinya tepatnya fungsi get seperti function deleteTask(id), toggleTaskStatus(id), dan getTaskList(id) pada file todolist.html. Ketiga function tersebut berguna pengambilan data berdasarkan url yang telah di map dari json nya.
b) Kita sebagai user wajib menambahkan juga pada file todolist.html fungsi Post createTask() dan putTaskList() yang akan mengiterasi data for each berisikan card dengan  TaskItem dan dimasukkan ke dalam tag didalamnya. Selain itu tambahkan path /todolist/json agar dapat menghubungkan ke view yang baru dibuat sebelumnya pada bagian urlpatterns. 
c) Tidak lupa melakukan pengubahan pada form menjadi didalam tag form sehingga dapat mengirim sebuah request dengan javascript, yang sebelumnya sebagai template (UserCreationForm() untuk form createTask()) bertujuan memudahkan memasukannya ke dalam modal untuk ditampilkan
d) Saya mengubah bagian yang relevan dan berkaitan satu sama lain dengan data yang terdapat di todolisnya, yang nantinya kita sesuai dengan perintah soal yakni program yang menggunakan AJAX dan kita bandingkan dengan menggunakan templates Django.
e)  Terakhir kita buat routing agar beberapa fungsi dapat kita buka melalui localhost dan juga saya melakukan`deployment` yang sudah otomatis terdeploy ke `herokuapp` karena menggunakan repo tugas sebelumnya yang pasti sudah terdeploy pekan lalu.