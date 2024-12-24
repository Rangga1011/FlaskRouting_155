# Import Flask dan modul terkait
from flask import Flask, redirect, url_for, request, render_template_string

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Template HTML untuk halaman login disimpan sebagai string
login_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        /* Gaya CSS untuk halaman login */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
            padding: 50px;
        }
        .form-container {
            background-color: #ffffff;
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 20px;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            width: 80%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Login Form</h2>
        <!-- Form login dengan metode POST -->
        <form action="{{ url_for('login') }}" method="post">
            <p>Enter Name:</p>
            <input type="text" name="nm" placeholder="Your Name" required> <!-- Input untuk nama -->
            <br>
            <input type="submit" value="Submit"> <!-- Tombol submit -->
        </form>
    </div>
</body>
</html>
"""

# Template HTML untuk halaman sukses disimpan sebagai string
success_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        /* Gaya CSS untuk halaman sukses */
        body {
            font-family: Arial, sans-serif;
            background-color: #dff9fb;
            text-align: center;
            padding: 50px;
        }
        .welcome-message {
            color: #2ecc71;
            font-size: 24px;
            font-weight: bold;
        }
        .button-container {
            margin-top: 20px;
        }
        .button-container a {
            text-decoration: none;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            font-size: 16px;
        }
        .button-container a:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="welcome-message">
        <!-- Pesan selamat datang dengan nama pengguna -->
        Welcome, {{ name }}!
    </div>
    <div class="button-container">
        <!-- Tombol untuk kembali ke halaman login -->
        <a href="{{ url_for('login') }}">Go Back to Login</a>
    </div>
</body>
</html>
"""

# Route utama yang mengarahkan ke halaman login
@app.route('/')
def home():
    # Fungsi untuk mengarahkan pengguna dari '/' ke '/login'
    return redirect(url_for('login'))

# Route untuk halaman login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # Jika metode POST
        user = request.form['nm']  # Ambil nama dari input form
        return redirect(url_for('success', name=user))  # Arahkan ke halaman sukses
    return render_template_string(login_template)  # Render halaman login

# Route untuk halaman sukses
@app.route('/success/<name>')
def success(name):
    return render_template_string(success_template, name=name)  # Render halaman sukses

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    # Aplikasi berjalan dalam mode debug
    app.run(debug=True)
