# PBP Tugas 2

## **Nama**     : Muhammad Hadziq Razin
## **NPM**      : 2106707076

#

## Link deploy: **http://pbp-tugas2-hadziq.herokuapp.com/katalog/**

#

## **Bagan Alur Django Request Client**
![Gambar]('../../Bagan.png?raw=true')
Models tempat kita menyimpan data dalam bahasa Python. Data dari Models dapat disimpan ke dalam Databse.<br>

Views memiliki fungsi-fungsi yang dapat memanggil data dari Models dan me-render data tersebut ke template HTML.<br>

Templates berisikan file HTML yang menjadi kerangka yang ingin ditampilkan ke client. Template dapat menerima data yang dikirim dari Views untuk ditampilkan.<br>

Client dapat melihat tampilan web yang dikirim dari template. Client juga dapat melakukan request ke URL untuk memilih halaman mana yang ingin ditampilkan.<br>

URL menerima request dan memanggil fungsi yang ada di Views sesuai request client.

#

## **Kenapa menggunakan Virtual Environment?**
<p>Alasannya adalah untuk mengisolasi packages dan dependecies dari tiap app agar tidak bertabrakan dengan punya app lain. Hal itu karena, versi Django, packages, dependencies, dll. bisa berubah entah upgrade atau downgrade.<br><br> App bisa saja berjalan tanpa menggunakan virtual environment, akan tetapi, tentu akan repot jika kita harus terus mengubah versi dari app-app kita agar bisa tetap running. Oleh karena itu, virtual environment digunakan agar "lingkungan-lingkungan" tersebut dapat berjalan dengan versi masing-masing.</p>

#

## **Cara Mengimplementasikan Langkah-Langkah Pengerjaan Tugas 2**
1. Membuat fungsi `show_catalog()` pada `views.py` yang ada pada folder katalog. Fungsi `show_catalog()` mengambil semua objek dari `class CatalogItem` yang ada pada `models.py` dan memasukkannya ke dalam sebuah container, kemudian memasukkan container ke dalam sebuah dictionary bernama `context`. Dictionary `context` berisikan `data_catalog_item` (yang berisi CatalogItem), nama, dan id yang nantinya di-render ke dalam `katalog.html`.
    ```
    def show_catalog(request):
        data_catalog_item = CatalogItem.objects.all()
        context = {
            'list_catalog': data_catalog_item,
            'nama': 'Muhammad Hadziq Razin',
            'id': '2106707076',
        }
        return render(request, "katalog.html", context)
    ```
2. Melakukan routing dengan mengisi file `urls.py` yang ada pada folder katalog. Pertama-tama import fungsi `show_catalog()` dari file `views.py`. Kemudian, melakukan path pemanggilan fungsi `show_catalog()`, untuk me-rendernya ke `katalog.html`, pada urlpatterns.
    ```
    from django.urls import path
    from katalog.views import show_catalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_catalog, name='show_catalog'),
    ]
    ```
3. Memetakan data yang di-render dari fungsi `show_catalog()` yang ada di file `views.py` dengan sintaks Django seperti, {{nama}} memanggil key 'nama' dari `context` yang dikirim dari fungsi `show_catalog()`. Ada juga {{% for loop %}} yang mengiterasi container `data_catalog_item` yang dikirim dari fungsi `show_catalog()` dengan memanggil key-nya, 'list_catalog'.
    ```
    <tr>
        <td><b>Nama</b></td>
        <td>:</td>
        <td>{{nama}}</td>
      </tr>
    ```
    ```
    {% for catalog in list_catalog %}
      <tr>
        <td>{{catalog.item_name}}</td>
        <td style="text-align: right;">{{catalog.item_price}}</td>
        <td style="text-align: center;">{{catalog.item_stock}}</td>
        <td style="text-align: center;">{{catalog.rating}}</td>
        <td>{{catalog.description}}</td>
        <td><a href="{{catalog.item_url}}">{{catalog.item_url}}</a></td>
      </tr>
      {% endfor %}
    ```

4. Menambahkan Action Secrets (Secrets agar kita tidak perlu menaruh key kita pada repository, tetapi bisa dipanggil dari kode kita) berupa nama aplikasi yang kita buat di Heroku, dan API key Heroku kita agar terhubung dengan repository project ini. Dengan begitu kita bisa men-deploy aplikasi kita dan membukanya dengan `herokuapp.com` sehingga tidak perlu lagi menjalankan secara lokal dan orang lain pun bisa melihat hasil kerja kita.

5. Langkah tambahan yang saya lakukan adalah menambah file CSS sebagai styling web HTML. Saya menambahkan styling untuk tabel dan judul agar tampilan web lebih menarik. File CSS akan di-link dengan file HTML dengan menambahkan load static `katalog.css` pada head HTML. Saya mempelajari cara melakukan ini dari Youtube dan beberapa artikel. Berikut adalah link video Youtube yang saya tonton untuk mempelajari CSS dan cara menghubungkannya:
- https://www.youtube.com/watch?v=QLL4KzFMfVw&t=1s
- https://www.youtube.com/watch?v=biI9OFH6Nmg&t=130s
- https://www.youtube.com/watch?v=Oy9K7iz3aa4
