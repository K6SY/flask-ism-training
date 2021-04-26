# Préparation de l'environnement

1. Supprimer le dossier .env

2. Recréer l'environnement virtuel : 
    *`python -m venv environment_name`*

3. Activation de l'evironnement virtuel
 
    1. **Windows cmd**
        *`.\environment_name\Scripts\activate.bat`*

    2. **Windows Powershell**
        *`.\environment_name\Scripts\Activate.ps1`*

        NB: Powershell bloque par défaut l'execution de scripts. Pour autoriser l'execution des scripts:
            * Executer powershell en tant qu'Administrateur 
            * Taper puis valider la commande suivante : *`Set-ExecutionPolicy RemoteSigned`*
    3. **Linux / Mac Terminal**

        *`source environment_name/bin/activate`*

4. Installer les requirements
    *`pip install -r requirement.txt`*

# Templating

## Création des vues

1. Tous les templates (fichier html) sont dans un répértoire templates (Obligatoire)

2. Je peux organiser mes fichiers html dans des sous-repertoires du répertoire template

3. Créer un fichier template de base (base.html) qui sera hérité par les autres fihciers html

4. Créer un fichier html (gestion_stock/produit/info.html) qui va hériter du fichier de base

5. Modifier la view-function pour retourner le fichier info.html

6. Définir des block au niveau du fichier de base. Les block facilitent la rédifinition d'un contenu d'une page à l'autre

`{% block nom_block%}
    contenu du block
{% endblock %}`

## Création et importation des ressources statiques

1. Tous les ressources statiques (css/js/images) sont dans un répértoire static (obligatoire)

2. Vous pouvez structurer vos ressources static comme vous voulez

3. Pour importer une ressource :

    1. **Ressource js**

        `<script src="{{url_for('static',filename='js/main.js')}}"></script>`

        NB: Pour plus de performance, importez les fichiers js à la fin du fichier html

    2. **Ressource css**

        `<link rel="stylesheet" href="{{url_for('static',filename='css/main.css')}}">`

    3. **Ressource image**

        `<img href="{{url_for(filename='image/logo.png')}}">`