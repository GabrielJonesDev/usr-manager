from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy admin login (da sostituire con un sistema di autenticazione reale)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# Pagina di login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('username') == ADMIN_USERNAME:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['username'] = username
            return redirect(url_for('admin'))
        else:
            return "Login fallito. Riprova."
    return render_template('usr-manager/templates/login.html')

# Pagina admin con la foto
@app.route('/admin')
def admin():
    if session.get('username') == ADMIN_USERNAME:
        return render_template('usr-manager/templates/admin.html')
    else:
        return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
