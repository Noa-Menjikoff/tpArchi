from .app import app, db
from .models import Questionnaire, Question,SimpleQuestion, MultipleQuestion

@app.cli.command()
def syncdb():
    db.create_all()
    ajouter_donnees_initiales()

def ajouter_donnees_initiales():
    db.create_all()

    db.session.add(Questionnaire(name="Salade"))
    db.session.add(Questionnaire(name="Pizza"))
    db.session.add(Questionnaire(name="Burger"))

    db.session.add(SimpleQuestion(title="Question 1", question_type="simplequestion", questionnaire_id=1))
    db.session.add(SimpleQuestion(title="Question 2", question_type="simplequestion", questionnaire_id=1))
    db.session.add(SimpleQuestion(title="Question 3", question_type="simplequestion", questionnaire_id=1))
    db.session.add(SimpleQuestion(title="Question 4", question_type="simplequestion", questionnaire_id=2))
    db.session.add(SimpleQuestion(title="Question 6", question_type="simplequestion", questionnaire_id=2))

    db.session.add(MultipleQuestion(title="Question 5", proposition1="Proposition 1", proposition2="Proposition 2", reponse="Réponse 5", questionnaire_id=3))

    db.session.commit()