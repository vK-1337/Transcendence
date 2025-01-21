# Utilise une image Python officielle comme base
FROM python:3.11-slim

# Définit le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copie le fichier de dépendances dans le conteneur
COPY tools/requirements.txt /app/

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port 8000 pour le serveur de développement Django
EXPOSE 8000

# Définit la commande de démarrage par défaut
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
