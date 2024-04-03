from flask import jsonify, url_for
from .app import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self , name):
        self.name = name
        
    def __repr__(self):
        return "<Questionnaire(%d) %s>" %(self.id , self.name)

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'url': 'http://127.0.0.1:5000'+url_for('get_questionnaire', id_quiz=self.id),
            'questions_url': [question.to_json()['url'] for question in self.questions]
        }
        return json

    def get_questionnaires():
        questionnaires = Questionnaire.query.all()
        result = []
        for questionnaire in questionnaires:
            result.append(questionnaire.to_json())
        return jsonify(result)
    
    def get_questionnaire(id):
        questionnaire = Questionnaire.query.get(id)
        return jsonify(questionnaire.to_json())

    def create_questionnaire(name):
        new_questionnaire = Questionnaire(name=name)
        db.session.add(new_questionnaire)
        db.session.commit()
        return jsonify(new_questionnaire.to_json())

    def update_questionnaire(id, name):
        questionnaire = Questionnaire.query.get(id)
        questionnaire.name = name
        db.session.commit()
        return jsonify(questionnaire.to_json())

    def delete_questionnaire(id):
        questionnaire = Questionnaire.query.get(id)
        db.session.delete(questionnaire)
        db.session.commit()
        return jsonify({"message": "Questionnaire supprimer"})
    



class Question(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    
    title = db.Column(db.String(120))

    questionnaire_id = db.Column(db.Integer , db. ForeignKey('questionnaire.id'))

    questionnaire = db.relationship("Questionnaire", backref = db.backref("questions", lazy="dynamic"))

    question_type = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'with_polymorphic': '*',
        'polymorphic_on': question_type
    }

    def __init__(self , title,question_type,questionnaire_id):
        self.title = title
        self.question_type = question_type
        self.questionnaire_id = questionnaire_id


    def to_json(self):
        json = {
            'url': 'http://127.0.0.1:5000'+url_for('get_question', id_quiz=self.questionnaire_id,id_question=self.id),
            'title': self.title,
        }
        return json
    
    def get_questions(id):
        question = Question.query.get(id)
        return jsonify(question.to_json())

    def get_questions_for_questionnaire(id_quiz):
        questions = Question.query.filter_by(questionnaire_id=id_quiz).all()
        result = [question.to_json() for question in questions]
        return jsonify(result)
    
    def get_question(id_question,id_quiz):
        question = Question.query.filter_by(id=id_question, questionnaire_id=id_quiz).first()
        return jsonify(question.to_json())
    
    def create_question(title, question_type, questionnaire_id, **kwargs):
        if question_type == 'simplequestion':
            new_question = SimpleQuestion(title=title, question_type=question_type, questionnaire_id=questionnaire_id, **kwargs)
        elif question_type == 'mutiplequestion':
            new_question = MultipleQuestion(title=title, question_type=question_type, questionnaire_id=questionnaire_id, **kwargs)
        else:
            return jsonify({'error': 'Invalid question type'}), 400

        db.session.add(new_question)
        db.session.commit()
        return jsonify(new_question.to_json())
    


class SimpleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'simplequestion',
        'with_polymorphic': '*',
        'polymorphic_load': 'inline'
    }

class MultipleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    proposition1 = db.Column(db.String(120))
    proposition2 = db.Column(db.String(120))
    reponse = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'mutiplequestion',
        'with_polymorphic': '*',
        'polymorphic_load': 'inline'
    }  
