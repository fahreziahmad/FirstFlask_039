<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Form Input Sederhana</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Form Input Nama dan Umur</h1>
        <form method="POST">
            <div class="form-group">
                <label for="nama">Nama:</label>
                <input type="text" id="nama" name="nama" required>
            </div>
            <div class="form-group">
                <label for="umur">Umur:</label>
                <input type="text" id="umur" name="umur" required>
            </div>
            <button type="submit">Kirim</button>
        </form>

        {% if result %}
        <div class="result">
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html> 