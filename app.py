#Importation de la classe Flask du module flask
from flask import Flask, request, render_template

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




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

