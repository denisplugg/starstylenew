from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from USERSdatabase import Users
from CARDdatabase import ForeignCelebrities, ForeignOutfits, CISCelebrities, CISOutfits, RuBrands, RuOutfits
from ALLSTARSdatabase import AllStars

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases.db'
app.secret_key = 'fhggk90@#1041,v;gh432!?'
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/base")
@app.route("/")
def index():
    fcelebrities = ForeignCelebrities.query.all()
    foutfits = ForeignOutfits.query.all()
    ciscelebrities = CISCelebrities.query.all()
    cisoutfits = CISOutfits.query.all()
    rubrands = RuBrands.query.all()
    ruoutfits = RuOutfits.query.all()
    return render_template("index.html", fcelebrities=fcelebrities, foutfits=foutfits, ciscelebrities=ciscelebrities, cisoutfits=cisoutfits, rubrands=rubrands, ruoutfits=ruoutfits)

@app.route("/WesternStars")
def Western_Stars():
    return render_template("Western_Stars.html")

@app.route("/RuStreetwear")
def Ru_Streetwear():
    return render_template("Ru_Streetwear.html")

@app.route("/CISStars")
def CIS_Stars():
    return render_template("CIS_Stars.html")

@app.route("/Stars", methods=['GET'])
def Stars():
    allstars = AllStars.query.all()
    return render_template("Stars.html", allstars=allstars)

@app.route('/starsinfo')
def Stars_info():
    allstars = AllStars.query.all()
    return render_template('starsinfo.html', allstars=allstars)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
    
        hashed_password = generate_password_hash(password)

        user = Users(username=username, email=email, password=hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
            flash('Регистрация успешна! Пожалуйста, войдите.')
            return redirect('/login')
        except Exception as e:
            db.session.rollback()
            flash('Ошибка регистрации: {}'.format(str(e)))

    return render_template('register.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id 
            return redirect('/profile')

        flash('Неверное почта или пароль.')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user_id' in session:
        user = Users.query.get(session['user_id'])
        return render_template('profile.html', user=user)
    return redirect('/login')

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/contacts")
def Contacts():
    return render_template("contacts.html")


if __name__ == '__main__':
    app.run(debug=True)