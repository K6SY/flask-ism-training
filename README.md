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

# Usage of dynamic routes

1. start the flask light server: python app.py

2. Navigate throught this URL: http://127.0.0.1:5000/account/k6SY

3. Replace in the above URL "K6SY" with another word and show the difference