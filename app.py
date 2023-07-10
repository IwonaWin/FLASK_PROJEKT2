from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class Teksty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data=db.Column(db.Date())
    text = db.Column(db.String(1000))
    ilosc=db.Column(db.Integer)
    edytowanie = db.Column(db.Integer)
    usuwanie = db.Column(db.Boolean)
   

    def __repr__(self):
        return 'Teksty: {}/{}'.format(self.id, self.name)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', the_title='Dodaj tekst!', active_menu='home', the_current_time=datetime.utcnow())

@app.route('/teksty')
def teksty():
    db.create_all()
    teksty = Teksty.query.all()
    return render_template('teksty.html', the_title='Przeglądaj i edytuj bazę tekstów!', active_menu='teksty', the_teksty=teksty)

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500


if __name__ == "__main__":
    app.run()