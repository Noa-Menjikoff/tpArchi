from .app import app, db

@app.cli.command()
def syncdb():
    db.create_all()
    ajouter_donnees_initiales()

def ajouter_donnees_initiales():
    db.create_all()