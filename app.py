#Importation de la classe Flask du module flask
from flask import Flask, request

#Instanciation d'un objet de la classe Flask. Cet objet est très utile pour la suite.
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

