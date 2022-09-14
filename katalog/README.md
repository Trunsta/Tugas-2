### Link aplikasi Heroku
https://pbp-tugas-2-app.herokuapp.com/katalog/

### Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`;
https://github.com/Trunsta/Tugas-2/blob/main/Bagan_MVT.png?raw=true

### Jelaskan kenapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?
Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer, hal ini dilakukan dengan cara membuat satu virtual environment yang terisolasi.
Kita tetap bisa membuat aplikasi Django tanpa virtual environment, namun lebih baik menggunakan virtual environment karena hal tersebut merupakan _best practice_ saat  membuat sebuah aplikasi.

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Pertama kita import *models* ke dalam file `views.py`. Kita akan menggunakan class pada `models` untuk mengambil data dari *database*. Kemudian kita membuat fungsi pada `views.py` yang bernama `show katalog` dengan parameter `request` yang me-return `render(request, "katalog.html", context)`. Kemudian kita akan memanggil fungsi *query* ke *database* dan menyimpan *query* tersebut pada sebuah variabel. Pada bagian return terdapat `context` sebagai parameter ketiga, hal ini bertujuan agar data pada variabel `context` di-*render* oleh Django dan dikembalikan pada sebuah HTML.
```
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'katalog_item' : data_catalog_item,
        'nama' : 'Nikolas Reva Bellie',
        'NPM' : '2106750212'
    }
    return render(request, "katalog.html", context)
```

2. Kita akan membuat kode pada `urls.py` di dalam folder aplikasi kita untuk melakukan *routing* dengan fungsi pada `views.py`.
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog')
]
```
Kemudian kita juga mendaftarkan aplikasi `katalog` pada `urls.py` yang ada di folder `project_django` dengan cara menambahkan potongan kode berikut pada variabel `urlpatterns`.
```
path('katalog/', include('katalog.urls')),
```

3. Untuk melakukan mapping, bukalah file `katalog.html` di folder `templates` dan ubahlah potongan kode yang sesuai dengan sintaks khusus *template* pada Django, yaitu {{data}}. Data yang dapat kita gunakan bisa dilihat di file `views.py` pada variabel `context`.
```
<h5>Name: </h5>
<p>{{nama}}</p>

<h5>Student ID: </h5>
<p>{{NPM}}</p>
```

Untuk menampilkan items pada tabel, kita harus melakukan iterasi pada `katalog_item` yang berada di dalam variabel `context` dan memanggil atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut.
```
{% for item in katalog_item %}
  <tr>
    <th>{{item.item_name}}</th>
    <th>{{item.item_price}}</th>
    <th>{{item.item_stock}}</th>
    <th>{{item.description}}</th>
    <th>{{item.rating}}</th>
    <th>{{item.item_url}}</th>
  </tr>
{% endfor %}
```
4. Buatlah sebuah app baru di website Heroku, lalu bukalah repositori GitHub dan pergi ke `Settings -> Secrets -> Actions -> New repository secret`. Lalu isi field `Name` dengan `HEROKU_APP_NAME` dan field `Secret` dengan nama app yang sudah dibuat `pbp-tugas-2-app`. Buatlah secret baru satu lagi yang bernama `HEROKU_API_KEY` dan memiliki value API key akun Heroku yang dapat dilihat di `Account settings` pada profile Heroku.
