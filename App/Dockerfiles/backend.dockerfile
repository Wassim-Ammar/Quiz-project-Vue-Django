# Utilisez l'image Python officielle comme image parent
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY App/Dockerfiles/requirements.txt .

# Installez les dépendances
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
# Copiez le contenu du répertoire actuel dans le conteneur à /app
COPY App/backend .
# Commande à exécuter lorsque le conteneur démarre
CMD ["python3", "app.py"]
