# **PBP Tugas 4**

## **Nama**     : Muhammad Hadziq Razin
## **NPM**      : 2106707076
## **Kelas**    : D

#

## Link deploy:
## 🔗 **[Tugas 4](http://pbp-tugas2-hadziq.herokuapp.com/todolist)**

<br>

# 💻 **Kegunaan `{% csrf_token %}` pada elemen `<form>`**

CSRF (Cross Site Request Forgery) dengan kode `{% csrf_token %}` adalah sebuah token unik yang diciptakan dengan alasan keamanan. Saat kita membuat web yang dapat menerima POST berupa data seperti `form` dari client, **data** yang dikirim harus bersamaan dengan token unik ini. Tujuannya adalah memastikan bahwa **data** yang dikirim ke server memang berasal dari website atau aplikasi kita, bukan yang dari lain. Hal ini mencegah adanya orang lain yang mengirim data ke server kita tanpa melewati aplikasi kita seperti _replay attack_.<br>

Jika kita tidak menambahkan `{% csrf_token %}` pada elemen `<form>`, browser akan me-_reject_ request kita dengan error `CSRF token missing` karena browser tidak dapat memastikan asal data yang dikirim ke server.

```
<form method="POST" action="{% url 'todolist:create_task' %}">
        {% csrf_token %}
        <table>
            {{ form }}
            <tr>
                <td></td>
                <td><input type="submit" value="Create"></td>
            </tr>
        </table>
    </form>
```
<br>

# 💻 **Membuat elemen `<form>` secara manual tanpa {{ form }}**
Tentu ktia dapat membuatnya secara manual menggunakan tag-tag yang disediakan oleh HTML. Salah satunya dengan menggunakan tag `<input>` seperti yang ada pada `login.html`. Nantinya, data yang diterima oleh form akan disimpan dan kita dapat mengaksesnya di dalam `views.py` dengan method `get()` dengan parameter nama tag input.

```
<input type="text" name="username" placeholder="Username" class="form-control">
```
```
username = request.POST.get('username')
```

<br>

# 💻 **Alur data**
1. Pengguna melakukan submisi data yang nantinya dibawa oleh request dan dapat disimpan ke suatu variabel di dalam file `views.py`.
    ```
    if request.method == "POST":
            form = UserCreationForm(request.POST)
    ```
<br>

2. Kemudian kita dapat menggunakan method `save()` pada form untuk menyimpan data kita ke databse _back-end_.
    ```
    form.save()
    ```
<br>

3. File `views.py` dapat meminta data ke `models.py` untuk diambil dari database yang kemudian dikirimkan ke templates .html untuk ditampilkan.
    ```
    from todolist.models import Task

    def show_todolist(request):
        data_todolist = Task.objects.all()
        return render(request, 'todolist.html', {'data_todolist':data_todolist})
    ```
    ```
    {% for task in data_todolist %}
        <tr>
            <td style="text-align: center;">{{task.date}}</td>
            <td style="text-align: center;">{{task.title}}</td>
            <td style="text-align: center;">{{task.description}}</td>
        </tr>
    {% endfor %}
    ```
<br>

# 💻 **Cara Mengimplementasikan Langkah-Langkah Pengerjaan Tugas 4**

**✅ Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.**

Aplikasi baru dapat dibuat dengan menjalankan command pada direktori Tugas 2 PBP
```
python manage.py startapp todolist
```
<br>

**✅ Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.**

Menambahkan path todolist ke dalam  `urlpatterns` yang di  `urls.py` pada folder `django_project`.
```
urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
]
```
<br>

**✅ Membuat sebuah model Task yang memiliki atribut user, date, title, dan description**

Membuat sebuah class pada file `models.py` yang berisi atribut di atas dengan parameter `models.Model`.
```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
```
<br>

**✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**

Mengimplementasikannya dengan membuat fungsi-fungsi pada `views.py` yang dapat memproses request-request di atas. Kemudian membuat templates `register.html` dan `login.html` untuk form registrasi dan login.
```
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        ...


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ...


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    ...
```
<br>

**✅ Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.**

Membuat halaman dengan membuat dan mengisi templates pada file `todolist.html`. Contoh tombol:
```
<button><a href="{% url 'todolist:create_task' %}">Create a New Task</a></button>

<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
```
<br>

**✅ Membuat halaman form untuk pembuatan task.**

Membuat halaman dengan membuat dan mengisi templates pada file `create_task.html`. Membuat input field yang ingin ditampilkan pada form yakni `title` dan `description`. Tidak lupa membuat fungsi pada `views.py` yang memproses data-data yang dibutuhkan untuk ditampilkan pada halaman form create task.
```
def create_task(request):
    if request.method == 'POST':
        task_title = request.POST['task_title']
        description = request.POST['description']
        ...
```
```
<div class="form_create">
        <table>
            <form method="POST" action="/todolist/create-task/">
                {% csrf_token %}
                <tr>
                    <td class="text_input">Title</td>
                    <td class="titik_koma">:</td>
                    <td><input type="text" name="task_title" placeholder="Your task title" class="form-control"></td>
                </tr>
                <tr>
                    <td class="text_input">Description</td>
                    <td class="titik_koma">:</td>
                    <td><textarea name="description" class="form-control" rows="4"></textarea></td>
                </tr>
        </table>
    </div>
```
<br>

**✅ Membuat routing sehingga fungsi show_todolist, login_user, register, create-task, dan logout_user dapat diakses.**

Menambahkan path fungsi-fungsi tersebut pada `urls.py` yang ada pada folder `todolist`.
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]
```
<br>

**✅ Membuat button untuk merubah status pengerjaan dan button untuk menghapus task**

Menambahkan button update dan delete pada `todolist.html`. Button tersebut akan pergi ke path `update_status/<int:id>` dan `delete/<int:id`> yang akan memanggil fungsi di `views.py` yang akan memproses update status task dan memproses penghapusan task.
```
<button class="update_btn">
    <a class="update_link" href="update_status/{{task.pk}}">{{task.status}}</a>
</button>

...

<button class="delete_btn">
    <a class="delete_link" href="delete/{{task.pk}}">❌</a>
</button>
```
```
urlpatterns = [
    ...
    path('delete/<int:id>', delete_task, name='delete'),
    path('update_status/<int:id>', update_status, name='update_status'),
]
```
```
def update_status(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')
```
```
def delete_task(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)
    task.delete()
    return redirect('todolist:show_todolist')
```
<br>

**✅ Contoh dua akun pengguna dan tiga atau lebih task**

<img width="950" alt="Screen Shot 2022-09-29 at 02 57 05" src="https://user-images.githubusercontent.com/88391977/192876968-fea9d722-5547-4032-92ab-76b9802e118f.png">
<img width="866" alt="Screen Shot 2022-09-29 at 02 57 24" src="https://user-images.githubusercontent.com/88391977/192876989-1b2ec578-1f0e-4eb7-b949-05fab09da08b.png">

<br>
<br>

# **PBP Tugas 5**

## Link deploy:
## 🔗 **[Tugas 5](http://pbp-tugas2-hadziq.herokuapp.com/todolist)**

<br>

# 💻 **Perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

**👍🏻 Inline CSS**

Inline CSS adalah styling yang dilakukan di dalam tag html.<br>
Contoh:
```
<h1 style="font-size: 25px; color: #38a863; text-align: center;">
    Lab 1 Assignment PBP/PBD
  </h1>
```
Kelebihan dari Inline CSS adalah kita tidak perlu repot membuat class untuk merefer styling pada suatu tag. Kekurangannya ada semakin banyak styling yang kita terapkan, maka semakin tidak rapi kode kita untuk dilihat.
<br>
<br>

**👍🏻 Internal CSS**

Internal CSS adalah styling yang dilakukan di dalam file html dengan membuat tag `<style>`.<br>
Contoh:
```
<style>
  .header {
    font-size: 30px;
  }
</style>
```
Kelebihan Internal CSS adalah lebih rapi dari Inline CSS tetapi masih dalam satu file dengan HTML. Kekurangannya adalah semakin banyak styling yang kita terapkan, maka ukuran file HTML semakin besar sehingga semakin lama untuk me-_load_ suatu halaman.
<br>
<br>

**👍🏻 External CSS**

External CSS adalah styling yang dilakukan di dalam file yang berbeda dari file html. Kita membuat file `.css` yang ada pada folder static. Dalam file tersebut sama dengan Internal hanya saja tanpa tag `<style>`.

Kelebihan dari External CSS adalah lebih mudah untuk meng-_update_ atau me-_maintain_ styling dari aplikasi kita karena file yang terpisah sehingga lebih bersih dan kita menjadi lebih fokus pada apa yang ingin kita kerjakan. Kekurangan dari External CSS adalah kita membutuhkan waktu yang lebih lama untuk memuat file CSS-nya.
<br>
<br>

# 💻 **Tag HTML5 yang kamu ketahui**
**`<button>`** untuk membuat tombol yang dapat diklik dan mengarahkan kita ke suatu halaman atau aksi.<br>
**`<body>`** mendefinisikan badan dari dokumen.<br>
**`<br>`** membuat sebuah _line break_.<br>
**`<dv>`** membuat sebuah divisi atau _section_ di dalam dokumen.<br>
**`<form>`** mendefinisikan form untuk input dari client.<br>
**`<h1> sampai <h6>`** mendefinisikan header dari dokumen.<br>
**`<p>`** mendefinisikan paragraf dalam dokumen.<br>
**`<style>`** tempat untuk Internal styling.<br>
**`<table>`** mendefinisikan tabel.<br>
**`<tr>`** mendefinisikan suatu baris tabel.<br>
<br>

# **💻 Tipe-tipe CSS selector yang kamu ketahui**
**👍🏻 Element Selector**

Menggunakan **tag** HTML untuk styling properti yang ada dalam **semua** tag tersebut.<br>
Contoh:
```
body {
    border-collapse: collapse;
    display: grid;
    justify-content: center;
    font-family: verdana;
}
```
<br>

**👍🏻 ID Selector**

Menggunakan ID yang ditambahkan pada tag properti yang ingin di-styling (ID harus **unik**). Menunjuk ID menggunakan `#` di dalam CSS.<br>
Contoh:
```
<div id="header">
    <h1>Tugas 5 PBP</h1>
</div>
```
```
#header {
    font-size: 30px;
    color: #000;
}
```
<br>

**👍🏻 Class Selector**

Menggunakan Class yang ditambahkan pada **semua** tag properti yang ingin di-styling. Menunjuk Class menggunakan `.` di dalam CSS.<br>
Contoh:
```
<td>
    <input type="text" name="username" placeholder="Username" class="form-control">
</td>
<td>
    <input type="password" name="password" placeholder="Password" class="form-control">
</td>
```
```
.form-control {
    border-style: hidden;
    background-color: #E8FFE8;
    border-radius: 2px 2px 2px 2px;
    overflow: hidden;
    padding: 5px 5px;
    width: 200px;
}
```
<br>

# 💻 **Cara Mengimplementasikan Langkah-Langkah Pengerjaan Tugas 5**

**✅ Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework**

Menggunakan External CSS untuk kustomisasi _template_ `todolist.html`, `login.html`, `register.html`, dan `create_task.html`. Menghubungkan file CSS dengan menambahkan ` load static link stylesheet` pada bagian `<head>` file HTML. Kemudian, menambahkan styling menggunakan CSS Selector-CSS Selector yang telah dijabarkan di atas.
```
<head>
  {% load static %}
  <link rel="stylesheet" href="{% static 'todolist.css' %}">
</head>
```
```
body {
    border-collapse: collapse;
    display: grid;
    justify-content: center;
    font-family: verdana;
}

.card_group {
    display: flex;
    justify-content: center;
}
```
<br>

**✅ Membuat keempat halaman yang dikustomisasi menjadi responsive**

Pertama-tama menambahkan meta `viewport` pada file `base.html` agar semua file HTML yang _extends_ file tersebut memiliki `viewport` Viewport bertujuan untuk menyesuaikan ukuran web dengan ukuran layar _gadget_ yang digunakan untuk membuka web tersebut.
```
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
```
<br>
Selanjutnya menggunakan `flex display` dan `wrap flex-wrap` pada Card Group. Display diatur menjadi flex agar card-card yang muncul akan secara _default_ menyamping. Flex-wrap diatur menjadi wrap agar ketika tidak cukup ruang untuk menampilkan card secara menyamping, maka card akan otomatis berpindah ke baris di bawahnya.

```
.card_group {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}
```
<br>

**✅ Menambahkan efek ketika melakukan hover pada cards di halaman utama todolist**
Menambahkan efek hover pada card pada file CSS dengan menunjuk ke class card tersebut.
```
.card:hover {
    box-shadow: 4px 4px 0px #00000098;
    background-color: #6ceab1;
    color: rgb(45, 45, 45);
    transition: .25s;
}
```

# 💻 **Hasil flex display dan efek hoever card**
<img width="1440" alt="Screen Shot 2022-10-06 at 11 36 22" src="https://user-images.githubusercontent.com/88391977/194215250-9646a3f0-5617-4143-b31c-337b4a6911c5.png">
<img width="1440" alt="Screen Shot 2022-10-06 at 11 36 28" src="https://user-images.githubusercontent.com/88391977/194215264-378b330e-5f26-417c-aae2-3e15d7477d17.png">
<img width="1440" alt="Screen Shot 2022-10-06 at 11 36 33" src="https://user-images.githubusercontent.com/88391977/194215267-fae4c108-69c7-4729-b69a-470e84df0653.png">
