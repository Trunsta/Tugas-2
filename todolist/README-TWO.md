### **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
Asynchronous programming adalah sebuah teknik programming yang dilakukan sehingga saat kita melakukan perubahan pada kode, website akan memperbarui elemen data dan menampilkannya tanpa harus me-*refresh* halaman. Synchronous programming adalah kebalikan dari asynchronous programming, website harus  di-*refresh* terlebih dahulu agar bisa menampilkan data baru dari perubahan yang kita lakukan.

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-Driven Programming adalah sebuah paradigma programming yang berarti alur program ditentukan dengan event/peristiwa. Pada tugas ini, salah satu penerapannya adalah pada bagian *create task*. Ketika *user* mengisi *field* dan menekan tombol *submit*, maka akan muncul *task* baru. Aksi menekan tombol *submit* tersebut merupakan contoh sebuah event yang menyebabkan sebuah perubahan pada website. 

### **Jelaskan penerapan asynchronous programming pada AJAX.**
Potongan kode berikut merupakan salah satu penerapan asynchronous programming pada tugas ini.
```
    <script>
        $(document).ready(function () {
            $("#new-task").submit(function (e) {
                e.preventDefault()
                var form = $(this)
                $.ajax({
                    type: "POST",
                    url: "add/",
                    data: form.serialize(),
                    success: function (data) {
                        $('#tasks').html("")
                        show()
                    }
                });
            })
        })
    </script>
```
Pertama kode tersebut akan berjalan ketika DOM sudah di-*load* dan button submit sudah ditekan. Kode tersebut merupakan AJAX POST dengan URL create task dan data isi dari form yang sudah diisi. Ketika sudah sukses maka `div` dengan ID `tasks`(yang berisi card task) pertama akan dijadikan kosong, lalu akan dipanggil fungsi `show()` yang berfungsi untuk menampilkan kumpulan card task yang baru.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- Membuat view baru yang mengembalikan data dalam bentuk JSON.
- Menambahkan path ke view yang baru dibuat.
- Mengambil dan menampilkan data tersebut menggunakan AJAX GET.
- Memodifikasi tombol create task sehingga membuka sebuah modal.
- Membuat view baru yang menyimpan isi form ke database dan me-*return* sebuah *response* dalam bentuk JSON.
- Membuat AJAX POST untuk menampilkan data baru secara asinkronus.