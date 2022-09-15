from flask import Flask, render_template, request

app = Flask(__name__, static_folder='css/')

@app.route('/<vardas>')
def home(vardas):
    return f'''<h1>{vardas}</h1><br>
                <h2>{vardas}</h2><br>
                <h3>{vardas}</h3><br>
                <h4>{vardas}</h4><br>
                <h5>{vardas}</h5><br>'''

@app.route('/', methods=['GET', 'POST'])
def funkc():
    return render_template('index.html')

@app.route('/keliamieji')
def keliamieji():
    return render_template('keliamieji.html')

@app.route('/keliami')
def keliami():
    return render_template('keliami.html')

@app.route('/keliami', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if (int(text) % 400 == 0) and (int(text) % 100 == 0):
        return f'{text} yra keliamieji metai'
    elif (int(text) % 4 == 0) and (int(text) % 100 != 0):
        return f'{text} yra keliamieji metai'
    else:
        return f'{text} nera keliamieji metai'

if __name__ == '__main__':
    app.run(debug=True)



