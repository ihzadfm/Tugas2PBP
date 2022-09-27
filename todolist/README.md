Nama : Ihza Dafa Maulidan
NPM : 21066652726
Link deploy Heroku : https://tugas2pbpihza.herokuapp.com/katalog/

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