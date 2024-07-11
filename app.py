from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(open('index.html').read())

@app.route('/cek_khodam', methods=['POST'])
def cek_khodam():
    name = request.form['name']
    birthdate = request.form['birthdate']
    
    # Logika sederhana untuk "cek khodam"
    khodam = random.choice(['Ada Khodam', 'Tidak Ada Khodam'])
    
    return f"<h1>Hasil Cek Khodam</h1><p>Nama: {name}</p><p>Tanggal Lahir: {birthdate}</p><p>Hasil: {khodam}</p>"

if __name__ == '__main__':
    app.run(debug=True)