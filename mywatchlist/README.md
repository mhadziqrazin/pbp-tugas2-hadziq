# PBP Tugas 3

## **Nama**     : Muhammad Hadziq Razin
## **NPM**      : 2106707076

#

## Link deploy: **http://pbp-tugas2-hadziq.herokuapp.com/mywatchlist/**

#
Jelaskan perbedaan antara JSON, XML, dan HTML!

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 3 di atas.

## **Perbedaan antara JSON, XML, dan HTML**
<br>

### **JSON (JavaScript Object Notation)**
Adalah format penulisan data yang berbasis JavaScript. JSON memiliki format penulisan yang sangat mudah dibaca dan dipahami manusia. Sintaks JSON merupakan turunan dari Object pada JavaScript sehingga cukup intuitif.
```
{
    "model": "mywatchlist.mywatchlist", "pk": 1,
    "fields": {
        "watched": "Already",
        "title": "The Hobbit",
        "rating": "5",
        "release_date": "November 28th, 2012",
        "review": "This movie is so surprising, intense, fierce, magical, stunning and so much more! This movie is so nostalgic since it was released when I was 9 years old."
    }
}
```
<br>

### **XML (Extensible Markup Language)**
Berbeda dengan JSON, XML lebih fokus untuk menyimpan data, bukan untuk menampilkan data sehingga tidak semudah JSON untuk memahaminya. XML didesain agar mudah dipahami mesin, tetapi tetap bisa dibaca oleh manusia. XML dibuat dengan kegunaannya, kesederhanaannya, dan keumumannya sehingga digunakan hampir di seluruh internet.
```
<django-objects version="1.0">
    <object model="mywatchlist.mywatchlist" pk="1">
        <field name="watched" type="CharField">Already</field>
        <field name="title" type="CharField">The Hobbit</field>
        <field name="rating" type="CharField">5</field>
        <field name="release_date" type="CharField">November 28th, 2012</field>
        <field name="review" type="TextField"> This movie is so surprising, intense, fierce, magical, stunning and so much more! This movie is so nostalgic since it was released when I was 9 years old.</field>
    </object>
</django-objects>
```

<br>

### **HTML (HyperText Markup Language)**
Jika JSON dan XML untuk menyimpan data, HTML biasa digunakan sebagai penggambaran atau pendefinisian struktur dari sebuah website. HTML menggunakan tag-tag yang punya kegunaan masing-masing seperti tag untuk paragraf, link, header, tabel, gambar, dan masih banyak lagi.
```
<table class="katalog">
    <thead>
      <trbox-shadow:0 5px 10px #ababab;>
        <th>Watched</th>
        <th>Movie Title</th>
        <th>Rating</th>
        <th>Release Date</th>
        <th>Review</th>
      </tr>
    </thead>
</table>
```
#

## **Urgensi data delivery dalam pengimplementasian sebuah platform**
<p>Sebelum itu, dalam pengimplementasian sebuah platform, kita memisahkan penulisan data dengan penulisan struktur tampilan web. Dengan begitu, kita dapat lebih fokus dalam pengembangan atau pemeliharaan (maintain) program dari segi data dan tampilan. Misalnya ketika kita ingin mengubah atau memperbarui suatu aspek, kita akan lebih mudah melakukannya dengan pemisahan tersebut.<br><br>
Karena terpisah, data yang sudah disimpan perlu dikirim atau ditransfer ke file yang digunakan untuk menampilkan struktur tampilan web agar dapat dilihat dalam format yang mudah dibaca dan dipahami oleh manusia. Di sinilah pentingnya data delivery, kita bisa 'mengoper-oper' data yang mau ditampilkan. Selain itu karena penulisan data dalam format yang umum digunakan, data delivery dapat mengirimkan data ke berbagai platform dengan mudah sehingga dapat diakses di mana saja meskipun dengan struktur web yang berbeda.</p>

#

## **Cara Mengimplementasikan Langkah-Langkah Pengerjaan Tugas 3**
1. Membuat aplikasi baru dengan menjalankan startapp di terminal dalam folder proyek Tugas 2. Kemudian membuat fungsi di dalam `views.py` untuk mengirim data watchlist ke html dan mengecek conditional case untuk pesan sebagai bonus pada tugas kali ini. Tidak lupa untuk menambahkan mywatchlist di `INSTALLED_APP` pada file `settings.py`.
    ```
    python manage.py startapp mywatchlist
    ```

2. Menambahkan path watchlist pada `urls.py` project django dan path fungsi `views.py` pada `urls.py` mywatchlist.
    ```
    path('mywatchlist/', include('mywatchlist.urls')),
    ```
    ```
    path('', show_watchlist, name='show_watchlist'),
    ```

3. Membuat class `MyWatchlist` dalam file `models.py` yang berisikan objek-objek data yang ingin ditampilkan.
    ```
    from django.db import models

    class MyWatchlist(models.Model):
        watched = models.CharField(max_length=20)
        title = models.CharField(max_length=150)
        rating = models.CharField(max_length=1)
        release_date = models.CharField(max_length=40)
        review = models.TextField()
    ```

4. Memasukkan data-data dari objek `models.py` dalam file `initial_watchlist_data.json` menggunakan format yang sesuai dengan JSON.
    ```
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": "Already",
            "title": "The Hobbit",
            "rating": 5,
            "release_date": "November 28th, 2012",
            "review": "This movie is so surprising, intense, fierce, magical, stunning and so much more! This movie is so nostalgic since it was released when I was 9 years old."
        }
    },
    ```

5. Menambahkan fungsi di `views.py` untuk bisa menyajikan data dalam format HTML, XML, dan JSON.
    ```
    def show_watchlist_xml(request):
        data = MyWatchlist.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_watchlist_json(request):
        data = MyWatchlist.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

6. Jangan lupa membuat routing dengan menambahkan path ke fungsi di atas pada `urls.py` my watchlist.
    ```
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json'),
    ```

7. Terakhir tinggal melakukan git add, commit, push, dan app akan otomatis di-deploy karena berada pada proyek yang sama dengan Tugas 2 yang sudah pernah berhasil di-deploy.