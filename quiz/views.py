from flask import jsonify, abort, make_response, request
from .app import app
from .models import Questionnaire, Question

# Error handlers (as provided in your code)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/quiz/api/v1.0/quiz', methods=['GET'])
def get_questionnaires():
    return Questionnaire.get_questionnaires()

@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>', methods=['GET'])
def get_questionnaire(id_quiz):
    return Questionnaire.get_questionnaire(id_quiz)

@app.route('/quiz/api/v1.0/quiz', methods=['POST'])
def create_questionnaire():
    if not request.json or 'name' not in request.json:
        abort(400)
    name = request.json['name']
    return Questionnaire.create_questionnaire(name)

@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>', methods=['PUT'])
def update_questionnaire(id_quiz):
    if not request.json:
        abort(400)
    name = request.json.get('name', None)
    return Questionnaire.update_questionnaire(id_quiz, name)

@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>', methods=['DELETE'])
def delete_questionnaire(id_quiz):
    return Questionnaire.delete_questionnaire(id_quiz)




@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>/questions', methods=['GET'])
def get_questions_for_questionnaire(id_quiz):
    return Question.get_questions_for_questionnaire(id_quiz)

@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>/questions/<int:id_question>', methods=['GET'])
def get_question(id_question,id_quiz):
    return Question.get_question(id_question,id_quiz)

@app.route('/quiz/api/v1.0/quiz/<int:id_quiz>/questions', methods=['POST'])
def create_question(id_quiz):
    if not request.json or 'title' not in request.json or 'question_type' not in request.json:
        abort(400)

    title = request.json['title']
    question_type = request.json['question_type']

    kwargs = {}
    if question_type == 'simplequestion':
        kwargs['reponse'] = request.json.get('reponse', None)
    elif question_type == 'mutiplequestion':
        kwargs['proposition1'] = request.json.get('proposition1', None)
        kwargs['proposition2'] = request.json.get('proposition2', None)
        kwargs['reponse'] = request.json.get('reponse', None)

    return Question.create_question(title, question_type, id_quiz, **kwargs)


