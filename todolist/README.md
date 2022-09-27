Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/todolist/

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

{% csrf_token %} sebagai Cross Site Request Forgery sebagai sebuah attack terhadap sebuah aplikasi website yang sedang digunakan dimana menjadikan user internet tanpa sengaja mengajukan suatu request sehingga pada aplikasinya terjadi eksesusi suatu tindakan yang tidak diinginkan oleh user internet, CSRF merupakan token unik yang dibuat untuk alasan keamanan. Token CSRF biasanya selalu ada ketika pengiriman sebuah data dimana dalam situasi pembuatan aplikasi website yang terdapat elemen form dari klien sama seperti mengintegrate POST berupa sebagai data. Hal tersebut berguna untuk pengamanan dan pencegahan data yang bukan berasal dari sumber yang berbahaya atau tidak dikenal saat server menerima datanya memang berdasarkan aplikasi website yang memang kredibel dan sesuai keinginan user. Karena bisa saja individu atau komunitas tidak bertanggung jawab mengirim data ke server yang digunakan tanpa melalui aplikasinya, seperti serangan replay, untuk itu hal tersebut dicegah agak tidak terjadi hal yang diinginkan. CSRF juga disebut sebagai One-Click Attack dimana dalam suatu attack hanya membutuhkan satu kali klik dari user internet. Apabila kode {% csrf_token %} tidak ikut disertakan pada elemen <form> akan terjadi error token CSRF missing dengan penolakan search engine atau portal karena data yang dikirim ke server merupakan data yang tidak kredibel sumbernya.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{form.as_table}})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Sebuah form dalam HTML harus berada di dalam tag form, yang diawali dengan <form> dan diakhiri dengan </form>. Tag form akan membutuhkan beberapa atribut untuk dapat berfungsi dengan seharusnya. Ya, kita dapat membuat elemen <form> secara manual dengan ketentuan sama pada login.html yang menggunakan tag <input> dimana tag-tag tersebut didapat dan ada disiapkan oleh HTML. Salah satu contohnya pada file views.py dapat diakses form yang menerima data dengan atribut method get() yang menghasilkan isiam form pada url browser dengan parameter nama tag input sebagai berikut : password = request.POST.get('password').

<td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pertama-tama user melakukan pengajuan data yang disimpan pada file views.py disuatu variabel dan dilakukan oleh request. 
if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

Langkah kedua simpanlah data yang telah kita ajukan ke database pada form dengan mengggunakan method save().
if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

Ketiga, database kita pergunakan untuk taken data berdasarkan request dari views.py kepada models.py terhadap datanya. Setelah itu semua dilakukan kita kirimkan ke folder templates yang berisi file .html untuk user interface pada browser. 
from todolist.models import Task

def show_todolist(request):
    data_todolist = Task.objects.all()
    return render(request, 'todolist.html', {'data_todolist':data_todolist})


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

a) Membuat sebuah aplikasi django beserta konfigurasi modelnya bernama todolist dengan perintah python manage.py startapp todolist, kita buat di repo tugas 2 PBP yang sudah dibuat sebelumnya.
b) Kita sebagai user wajib menambahkan path todolist agar dapat membuka localhost dengan cara pada file urls.py kita tambahkan path('todolist/', include('todolist.urls')), pada bagian urlpatterns. Jika kita telah menambahkan path, dapat dipastikan ketika kita mengakses `http://localhost:8000/todolist` akan muncul aplikasi yang kita buat. 
c) Pada file models.py yang ada pada folder todolist saya menambahkan beberapa atribut yang dibutuhkan seperti `user` menghubungkan task dengan pengguna yang membuat task tersebut dengan menggunakan tipe model models.ForeignKey dan parameternya user, lalu ada atribut `title` untuk memetakan judul pada task, selanjutnya ada atribut `date` yang berguna mendeskripsikan tanggal pembuatan task, setelah itu atribut `description` berguna mendeskripsikan deskripsi task. 
d) Tidak lupa melakukan makemigrations dan migrate dengan python manage.py pada cmd ke dalam local database, lalu implementasikan form registrasi registrasi, login, dan logout dengan membuat HTML pada template yang isinya file register.html dan login.html . Disamping itu untuk dapat menjalankan request user, kita perlu membuat fungsi pada file views.py
e) Saya membuat page utama pada file todolist.html berbarengan dengan kedua file HTML sebelumnya di folder templates dengan menambahkan potongan kode berikut "{% url 'todolist:create_task' %}" yang dijadikan button.
f) Page form perlu dibuat untuk konfigurasi model dan fields yang dijadikan tampilan interface dengan hanya perlu memasukkan judul task dan deskripsi task oleh user, semua itu menjadi proses pembuatan task dengan menambahkan file forms.py dan mengisi create_task.html pada folder templates. Setelah semua dilakukan buat juga fungsi pada file views.py yang bertujuan mengalirkan data yang dibutuhkan untuk ditampilkan pada page create_task
g)  Terakhir kita buat routing agar beberapa fungsi dapat kita buka melalui localhost seperti path-path login, register, logout, create task, dan halaman utama todolist pada file urls.py di bagian urlpatternsnya pada folder todolist. Terakhir saya melakukan`deployment` yang sudah otomatis terdeploy ke `herokuapp` karena menggunakan repo tugas sebelumnya yang pasti sudah terdeploy pekan lalu.