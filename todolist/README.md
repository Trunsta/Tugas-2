# Tugas 4
### **Link aplikasi Heroku**
https://pbp-tugas-2-app.herokuapp.com/todolist<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/login/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/register/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/create-task/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/logout/<br>

Username    Password<br>
user1       passpbp1<br>
user2       passpbp2<br>

### **Apa kegunaan `{% csrf_token %}` pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**
CSRF token berguna untuk menangkal CSRF attack, yang merupakan sebuah bentuk serangan pada sebuah website. CSRF token adalah sebuah token dengan nilai unik random yang di-*generate* pada setiap session user. Token ini akan disisipkan pada parameter yang *hidden* pada form HTML, yang kemudian akan dikirimkan ke browser client. Jika tidak ada CSRF token di form kita maka tentu website kita menjadi tidak aman karena menjadi sangat rentan terhadap serangan CSRF.

### **Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.**
Bisa, pertama kita harus membuat sebuah form pada `templates` yang mengirim sebuah request POST. Lalu pada `views.py` kita harus membuat fungsi yang menerima POST tersebut dan harus di-validasi data formnya sesuai atau belum.

### **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
User akan mengisi form dan ketika di-submit, maka website akan me-request POST dan data POST tersebut akan diterima dan di-handle di `views.py`. Setelah itu data akan divalidasi apakah sudah sesuai dengan field yang dibutuhkan, jika valid maka data form tersebut akan di-save ke database. Lalu `views.py` akan mengembalikan hasilnya dalam bentuk website yang sesuai dengan struktur templates HTML dan data pada `context`.   

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- Buat app dengan `python manage.py startapp todolist`, add ke `settings.py`. 
- Membuat model Task dengan fields yang sesuai, kemudian migrate models tersebut.
- Pada `views.py` membuat fungsi register, login, dan logout.
- Buat file HTML register, login dan logout.
- Membuat file `forms.py` yang berisi form untuk pembuatan task baru.
- Buat file `create_task.html` untuk halaman tambah task baru.
- Tambah path di `urls.py` yang sesuai untuk setiap fungsi di `views.py`.
- Add, commit, dan push ke GitHub. Otomatis akan men-deploy ke Heroku.
- Buat test user dan data yang diperlukan.

### Collaborated with: Alvaro Austin
### https://github.com/Emilicos/Tugas2_PBP/

# Tugas 5
 ### **Apa perbedaan dari Inline, Internal, dan External CSS? ### Apa saja kelebihan dan kekurangan dari masing-masing style?**
 Inline CSS adalah CSS yang digunakan pada satu elemen HTML yang spesifik. Kita bisa memberi style pada tiap elemen dengan menambahkan atribut **style** pada tag HTML yang kita inginkan.<br>
 Kelebihan : Bisa memberi style yang berbeda pada tiap elemen yang diinginkan dan mudah untuk dilihat informasinya.<br>
 Kekurangan : Jika terdapat banyak elemen yang butuh styling, maka banyak styling yang harus kita lakukan satu persatu sehingga memakan waktu. Kita juga tidak memiliki akses ke CSS file eksternal untuk menggunakan styling.

 Internal CSS dilakukan dengan menambahkan style pada bagian `head` di file HTML. Internal CSS dilakukan ketika kita ingin styling satu halaman HTML (single page).<br>
 Kelebihan : Tidak perlu membuat file baru dan styling yang dilakukan teraplikasi ke halaman HTML sehingga tidak perlu di-style tiap elemen.<br>
 Kekurangan : Tidak bisa diaplikasikan untuk 2 halaman HTML yang berbeda.

 External CSS menggunakan suatu file `.css` yang terpisah yang berisi custom styling yang dapat kita aplikasikan ke file HTML apapun.<br>
 Kelebihan : Kita hanya perlu membuat styling di file terpisah dan dapat kita gunakan di HTML apapun. <br>
 Kekurangan : Kita harus membuat file eksternal, sehingga kita belum tentu mengerti apa styling yang dilakukan jika hanya melihat dari file HTML-nya.
 ### **Jelaskan tag HTML5 yang kamu ketahui.**
` <p></p> `Membuat paragraf<br>
` <h1></h1>` Membuat heading<br>
Ukuran-ukuran heading : `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`<br>
`<a></a>` Membuat referensi ke link<br>
`<button></button>` Membuat button<br>
`<img></img>` Menampilkan sebuah gambar<br>
`<div></div>` Menggabungkan beberapa elemen ke satu elemen gabungan<br>
 ### **Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
 Element selector menggunakan tag HTML sebagai selector untuk mengubah properti pada tag tersebut.<br>
 ID selector menggunakan ID pada tag sebagai selectornya.<br>
 Class selector dilakukan dengan menambah class pada tag HTML, lalu class tersebut perlu ditambahkan pada file eksternal CSS.
 ### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
 - Menambahkan CSS Bootstrap pada `base.html`.
 - Merubah desain dari `login.html` dan `create_task.html` dengan mengganti header, mengubah input field menjadi floating form, mengubah warna button dan memposisikan ke tengah.
 - Pada `registrasi.html` mengubah header dan memposisikan ke tengah.
 - Pada `todolist.html` mengubah header, membuat setiap task pada sebuah card, memposisikan ke tengah dan mengganti beberapa warna.