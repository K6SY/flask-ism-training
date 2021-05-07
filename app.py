#Importation de la classe Flask du module flask
from flask import Flask, request, render_template, session, redirect, url_for
from custom_forms import *


#Instanciation d'un objet de la classe Flask. Cet objet est très utile pour la suite.
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Soroc2022@localhost/emarket'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'D2FGTHY67UJ_KLIO'
#db = SQLAlchemy(app)

'''
@app.route('/categorie', methods=['GET','POST'])
def manageCategorie():
    form = Categorie()
    data=[]
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        data.append(name)
        data.append(description)
        session['data'] = data
        return redirect(url_for('manageCategorie'))

    return render_template('gestion_stock/categorie/add.html', form=form, items=session.get('data'))

'''

@app.route('/news', methods=['GET','POST'])
def newletter():
    myform = Newsletter()
    name = myform.name.data
    email = myform.email.data
    mydate = myform.mydate.data
    print(f"Test : {name} - {email} - {mydate}")
    data=[]
    if myform.validate_on_submit():
        name = myform.name.data
        email = myform.email.data
        mydate = myform.mydate.data
        data.append(name)
        data.append(email)
        data.append(mydate)
        session['data'] = data
        print(f"Valide : {name} - {email} - {mydate}")
        return redirect(url_for('newletter'))
    return render_template('extra/news.html', form=myform, data=session.get('data'))

    '''
    data=[]
    if myform.validate_on_submit():
        name = myform.name.data
        email = myform.email.data
        #mydate = myform.mydate.data
        data.append(name)
        data.append(email)
        session['data'] = data
        return redirect(url_for('newletter'))
    '''



'''
Les routes dynamiques sont ajoutés au niveau de l'URI et contiennent des extraits placer entre <>.
Exemple: /<username>/<token>
Dans l'exemple ci-dessous, nous avons deux extraits: username et token. Chacun de ces extraits doivent en plus
être passé comme paramètre à la view fonction.

'''

@app.route('/account/<username>')
def account(username):
    return f'''
        <h1>My first page on flask</h1>
        <h2>Welcome {username} to your profile</h2>
        '''

'''
# Usage des paramètres passés au niveau de l'URL
# Usage de render_template pour renvoyer une vue
# Extraction des données du header 
'''
@app.route('/product/info')
def product():
    #Récupération des paramètres via l'URL
    _marque=request.args.get('marque')
    _type=request.args.get('type')
    _nom=request.args.get('nom')

    #Récupération du headers de la requête
    #Attention: L'attribut Sec-Ch-Ua est valable sur Chrome
    #header = request.headers.get('Sec-Ch-Ua')
    #info = header.split(';')
    #browser_info= info[0]+' '+info[1]

    return render_template('gestion_stock/produit/info.html')


@app.route('/')
def accueil():
    return render_template('accueil.html')


'''
class Produit(db.Model):
    __tablename__ = 'produits'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text, nullable=True)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text, nullable=True)
    produits = db.relationship('Produit', backref='produit',uselist=False)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<User %r>' % self.username

class ProduitForm():
    nom = StringField('Indiquer le nom du produit?', validators=[DataRequired()])
    description = StringField('Indiquer la description du produit?')
    submit = SubmitField('Submit')

'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)

