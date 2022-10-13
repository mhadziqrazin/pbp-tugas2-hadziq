# **PBP Tugas 6**

## **Nama**     : Muhammad Hadziq Razin
## **NPM**      : 2106707076
## **Kelas**    : D

#

## Link deploy:
## 🔗 **[Tugas 6](http://pbp-tugas2-hadziq.herokuapp.com/todolist/json)**

<br>

# **💻 Perbedaan antara `asynchronous` _programming_ dengan `synchronous` _programming_.**

**⏳ Synchronous**

Pekerjaan/proses pada _client side_ akan ditunda sementara ketika terjadi _request_ dari _client_. Server akan memproses _request_ sementara pekerjaan/proses yang sedang berjalan pada _client side_ akan di-_pause_ menunggu _response_ dari server.

**⏳ Asynchronous**

Pekerjaan/proses pada _client side_ akan tetap berjalan ketika terjadi _request_ dari _client_. Server akan memproses _request_ dan tetap akan melanjutkan pekerjaan/proses yang sedang berjalan pada _client side_ tanpa menunggu _response_ dari server.

<br>

# **💻 Event-Driven Programming**

Paradigma untuk meng-_handle_ aksi yang dilakukan oleh _client_ pada _website_ kita. Contohnya ketika _client_ menekan suatu tombol, _event_ akan terjadi dan suatu kode yang sesuai akan berjalan sebagai _response_ dari terjadinya hal tersebut. _Page_ akan ter-_update_ atau termodifikasi berdasarkan hasil dari kode tersebut. Contoh:
```
document.getElementById('add_btn').onclick = show_modal

function show_modal() {
    document.getElementById('modal_container').style.display = "flex"
}
```

<br>

# 💻 **`Asynchronous` _programming_ pada Ajax**

Fungsi dilakukan secara _asynchronous_ di belakang layar sementara proses pada _client side_ akan tetap berjalan. Contohnya, fungsi di bawah yang mengambil data dan mengubahnya menjadi Json dan menampilkan _cards_ berdasarkan data yang baru diambil pada Todolist secara _asynchronous_ dengan menggunakan JavaScript.
```
async function getDataJson() {
    return fetch("{% url 'todolist:get_todolist_json' %}").then((result) => result.json())
}

async function refreshTodolist() {
    document.getElementById('card_group').innerHTML = ""
    const todolist = await getDataJson()
    let card = ``
    todolist.forEach((task) => {
        card += `\n
        <div class="card">
            <div class="title">
                ${task.fields.title}
            </div>
            ...
        </div>`
    });
    document.getElementById('card_group').innerHTML = card
}
```
<br>

# 💻 **Cara Mengimplementasikan Langkah-Langkah Pengerjaan Tugas 6**

**✅ AJAX GET**

Membuat fungsi pada `views.py` yang mengambil data dan mengembalikannya dalam bentuk Json. Kemudian membuat fungsi Ajax yang mengambil data tersebut, kemudian menampilkan datanya dalam bentuk _cards_. Terakhir, menambahkan path pada `urls.py`
```
def get_todolist_json(request):
    tasks = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', tasks))
```
```
async function getDataJson() {
    return fetch("{% url 'todolist:get_todolist_json' %}").then((result) => result.json())
}

async function refreshTodolist() {
    document.getElementById('card_group').innerHTML = ""
    const todolist = await getDataJson()
    let card = ``
    todolist.forEach((task) => {
        card += `\n
        <div class="card">
            <div class="title">
                ${task.fields.title}
            </div>
            ...
        </div>`
    });
    document.getElementById('card_group').innerHTML = card
}
```
```
urlpatterns = [
    ...
    path('json/', todolist_ajax, name='todolist_ajax'),
]
```

<br>

**✅ AJAX POST**

Membuat tombol untuk menampilkan modal, kemudian membuat fungsi pada `views.py` yang memproses _form_ dari modal, kemudian menambahkan path pada `urls.py`, kemudian membuat fungsi Ajax yang melakukan proses menyimpan form, tutup modal, dan terakhir _refresh_ page secara _asynchronous_.
```
<button id="add_btn" class="add_btn">Create New Task</button>

document.getElementById('add_btn').onclick = show_modal

function show_modal() {
    document.getElementById('modal_container').style.display = "flex"
}
```
```
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        description = request.POST.get('description')

        task = Task(title=task_title, description=description)
        task.user = request.user
        task.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponse(b"ADDING", status=200)
```
```
urlpatterns = [
    ...
    path('create-task/', create_task, name='create_task'),
]
```
```
<input id="create_btn" class="create_btn" type="submit" value="Create">

document.getElementById('create_btn').onclick = addTodolist

function addTodolist() {
    document.getElementById('modal_container').style.display = "none"
    fetch("{% url 'todolist:create_task' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form_new'))
    }).then(refreshTodolist)
    return false
}
```
<br>

**✅ Implementasi Delete Button😎**

Membuat tombol delete, kemudian membuat fungsi pada `views.py` yang memproses penghapusan, kemudian menambahkan path pada `urls.py`, kemudian membuat fungsi Ajax yang memproses penghapusan, dan terakhir _refresh_ page secara _asynchronous_.
```
<button class="delete_btn">
    <a class="delete_link" onclick="delete_todolist(${task.pk})">❌</a>
</button>

function delete_todolist(id) {
    let url = "/todolist/delete/" + id;
    fetch(url).then(refreshTodolist)
}
```
```
@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)
    task.delete()
    return HttpResponse(b"DELETED", status=204)
```
```
urlpatterns = [
    ...
    path('delete/<int:id>', delete_task, name='delete'),
]
```
<br>

## **Sekian terima kasih Django atas 6 minggu indahnya🥺🙏🏻**