from flask import Flask, render_template, request, redirect, flash, session, Blueprint
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_msearch import Search
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from USERSdatabase import Users
from CARDdatabase import ForeignCelebrities, ForeignOutfits, CISCelebrities, CISOutfits, RuBrands, RuOutfits
from ALLSTARSdatabase import AllStars

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases.db'
app.config['MSEARCH_ENABLE'] = True 
app.config['MSEARCH_INDEX_NAME'] = 'msearch'
app.secret_key = 'fhggk90@#1041,v;gh432!?'

db.init_app(app)
migrate = Migrate(app, db)
search = Search(app, db)


with app.app_context():
    db.create_all()

user_settings_bp = Blueprint('user_settings', __name__)


@app.route("/base")
@app.route("/", methods=['GET'])
def index():
    query = request.args.get('query', '')
    if query:
        fcelebrities = ForeignCelebrities.query.msearch(query, fields=['celebrity_name']).all()
        ciscelebrities = CISCelebrities.query.msearch(query, fields=['celebrity_name']).all()
        rubrands = RuBrands.query.msearch(query, fields=['brand_name']).all()
    else:
        fcelebrities = ForeignCelebrities.query.all()
        ciscelebrities = CISCelebrities.query.all()
        rubrands = RuBrands.query.all()

    combined_celebrities = []

    for celebrity in fcelebrities:
        combined_celebrities.append(celebrity)

    for celebrity in ciscelebrities:
        combined_celebrities.append(celebrity)

    for brand in rubrands:
        combined_celebrities.append(brand)

    random.shuffle(combined_celebrities)

    return render_template('index.html', celebrities=combined_celebrities, query=query)


@app.route("/WesternStars", methods=['GET'])
def Western_Stars():
    fcelebrities = ForeignCelebrities.query.all()
    foutfits = ForeignOutfits.query.all()
    return render_template("Western_Stars.html",fcelebrities=fcelebrities, foutfits=foutfits)

@app.route("/RuStreetwear", methods=['GET'])
def Ru_Streetwear():
    rubrands = RuBrands.query.all()
    ruoutfits = RuOutfits.query.all()
    return render_template("Ru_Streetwear.html",rubrands=rubrands, ruoutfits=ruoutfits)

@app.route("/CISStars", methods=['GET'])
def CIS_Stars():
    ciscelebrities = CISCelebrities.query.all()
    cisoutfits = CISOutfits.query.all()
    return render_template("CIS_Stars.html",ciscelebrities=ciscelebrities, cisoutfits=cisoutfits)

@app.route("/Stars", methods=['GET'])
def Stars():
    foreign_celebrities = AllStars.query.filter_by(nation=0).all()
    russian_celebrities = AllStars.query.filter_by(nation=1).all() 
    return render_template("Stars.html", foreign_celebrities=foreign_celebrities, russian_celebrities=russian_celebrities)

@app.route("/starsinfo", methods=['GET'])
def Stars_info():
    allstars = AllStars.query.all()
    return render_template('starsinfo.html', allstars=allstars)
    

@app.route("/register", methods=['GET', 'POST'])
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

@user_settings_bp.route('/profile', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        new_username = request.form.get('new-username')
        new_password = request.form.get('new-password')


        user_id = session.get('user_id')
        if not user_id:
            flash('Необходимо войти в систему.', 'error')
            return redirect('/login')

        user = Users.query.get(user_id)
        if not user:
            flash('Пользователь не найден.', 'error')
            return render_template('profile.html')

        user.username = new_username

        hashed_password = generate_password_hash(new_password)
        user.password = hashed_password

        try:
            db.session.commit()
            flash('Настройки успешно обновлены.', 'success')
            return redirect('/profile')
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при обновлении настроек: {str(e)}', 'error')
            return render_template('profile.html',username=user.username, favorites=user.favorites)
        
    return render_template('profile.html')

app.register_blueprint(user_settings_bp)

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/contacts")
def Contacts():
    return render_template("contacts.html")

@app.route("/forstars", methods=['GET'])
def Forstars():
    foreign_celebrities = AllStars.query.filter_by(nation=0).all()
    return render_template("forstars.html", foreign_celebrities=foreign_celebrities)

@app.route("/rustars", methods=['GET'])
def Rustars():
    russian_celebrities = AllStars.query.filter_by(nation=1).all()
    return render_template("rustars.html", russian_celebrities=russian_celebrities)

@app.route("/starsinfo")
def Starsinfo():
    return render_template("starsinfo.html")


if __name__ == '__main__':
    app.run(debug=True)