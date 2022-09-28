### **Link aplikasi Heroku**
https://pbp-tugas-2-app.herokuapp.com/todolist<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/login/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/register/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/create-task/<br>
https://pbp-tugas-2-app.herokuapp.com/todolist/logout/<br>

Username    Password
user1       passpbp1
user2       passpbp2

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