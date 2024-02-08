from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("resume_2.html")

@app.route('/consultation/5625719273')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

if(__name__ == "__main__"):
    app.run()
