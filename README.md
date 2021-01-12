# Numerical-Methods
 
Kalkulator berbagai metode dalam [Metode Numerik](https://bookdown.org/moh_rosidi2610/Metode_Numerik/numericmethod.html). Apliasi berbasis web ini menggunakan 
[Flask](https://flask.palletsprojects.com/en/1.1.x/) sebagai Backend Framework yang ditulis dalam bahasa pemrograman Python. Web ini dihosting pada 
[Heroku](https://www.heroku.com/) yang memanfaatkan [Gunicorn](https://gunicorn.org/) sebagai server deployment-nya Flask. Aplikasi ini bisa diakses secara 
langsung melalui [met-num.herokuapp.com](https://met-num.herokuapp.com).

## Tampilan Aplikasi

![](/static/images/preview.png)

## Fitur

Melakukan berbagai macam perhitungan dalam metode numerik, diantaranya :

<table>
  <thead>
    <tr>
      <th> Metode </th>
      <th> Terdiri Dari </th>
    <tr>
  </thead>
  <tbody>
    <tr>
      <td>Metode Tertutup</td>
      <td>Metode Tabel, Metode Biseski, Metode Regula Falsi</td>
    </tr>
    <tr>
      <td>Metode Terbuka</td>
      <td>Metode Newton Raphson, Metode Secant, Metode Iterasi Sederhana</td>
    </tr>
    <tr>
      <td>Diferensiasi Numerik</td>
      <td>Metode Selisih Mundur, Metode Selisih Tengah, Metode Selisih Maju</td>
    </tr>
    <tr>
      <td>Integrasi Numerik</td>
      <td>Metode Riemann, Metode Trapezoida, Metode Simpson 1/3, Metode Simpson 3/8</td>
    </tr>
  <tbody>
</table>

## Libraries
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) adalah Microframework Python untuk membuat website.
- [Pandas](https://pandas.pydata.org/) digunakan untuk membuat DataFrame.
- [SymPy](https://www.sympy.org/en/index.html) digunakan untuk mencari persamaan dan menghitung suatu fungsi turunan maupun integral.
- [Gunicorn](https://gunicorn.org/) (Green Unicorn) adalah sebuah WSGI (Web Server Gateway Interface) HTTP Server untuk bahasa pemrograman Python.

## Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

## Kontak

Mochammad Arya Salsabila - Aryasalsabila789@gmail.com
