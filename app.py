#Importation de la classe Flask du module flask
from flask import Flask

#Instanciation d'un objet de la classe Flask. Cet objet est très utile pour la suite.
app = Flask(__name__)


'''
Définition d'une view function hello par annotation.
Format annotation: @app.route(URI,method)
NB: app represente le nom de l'objet instance de la classe Flask
'''

@app.route('/')
def hello():
    return "<h1>My first page on flask</h1>"


'''
Le code ci-dessous permet de démarrer l\'application en executant: python app.py
Assurez vous que l'environnnement virtuel est bien activé
- app.run() prend en paramètre (facultatif) 
     - host= ip/fqdn de la machine
     - port = port sur lequel tourne l\'application
     - debug = permet d'activer/désactiver le mode debug (hot-reloading garanti)  
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

