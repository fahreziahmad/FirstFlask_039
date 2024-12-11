from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Parsing parameter dari form
        nama = request.form.get('nama')
        umur = request.form.get('umur')
        
        # Validasi input
        if nama and umur:
            try:
                umur = int(umur)
                result = f"Halo {nama}, umur Anda adalah {umur} tahun"
            except ValueError:
                result = "Umur harus berupa angka"
        else:
            result = "Silakan isi semua field"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)