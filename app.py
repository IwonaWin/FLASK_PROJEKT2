from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', the_title='Dodaj tekst!', active_menu='home')

@app.route('/teksty')
def teksty():
    return render_template('teksty.html', the_title='Przeglądaj i edytuj bazę tekstów!', the_tactive_menu='teksty')
    

@app.route('/grain')
def grain():
    return render_template('grain.html', the_title='Wybierz tekst i zagraj!', active_menu='grain')
    

@app.route('/graout', methods=['GET','POST'])
def graout():
    if request.method=="POST":
        return render_template('grain.html', the_title='Najpierw wybierz tekst!', active_menu='grain')
    else:
        return render_template('graout.html', the_title='Gramy!', active_menu='graout')
    
@app.route('/historia')
def historia():
    return render_template('historia.html', the_title='Przejrzyj swoje podejścia!', active_menu='historia')
if __name__ == "__main__":
    app.run()