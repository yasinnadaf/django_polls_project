import logging
from django.http import JsonResponse
import json
from questions.models import Question, Choice

logging.basicConfig(filename='file.log', filemode='w', level=logging.DEBUG)


def index(request):
    print(dir(request))
    print(json.loads(request.body))
    return JsonResponse({'message': 'hello its polls index'})


def create(request):
    """
        Function for creating request to perform create operation in Question model
    """
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            ques = Question.objects.create(question_text=data.get("question_text"))
            return JsonResponse(
                {"message": "question created", "data": {"id": ques.id, "question_text": ques.question_text,
                                                         "pub_date": ques.pub_date}}, status=201)
        return JsonResponse({"message": "method not allowed"}, status=400)
    except Exception as e:
        logging.exception(e)


def update(request):
    """
    Function for updating request to perform update operation in Question model
    """
    try:
        data = json.loads(request.body)
        if request.method == 'PUT':
            id = data.get('id')
            obj = Question.objects.get(id=id)
            obj.question_text = data.get('question_text')
            obj.save()
            return JsonResponse(
                {"message": "question created", "data": {"id": obj.id, "question_text": obj.question_text}})
        return JsonResponse({"message": "method not allowed"}, status=400)
    except Exception as e:
        logging.exception(e)


def get(request):
    """
    Function for getting request to perform all data in Question model
    """
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            ques = Question.objects.filter(id=data.get('id'))
            return JsonResponse(
                {"message": "all data are", "data": [{"id": q.id, "question": q.question_text} for q in ques]})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as e:
        logging.exception(e)


def delete(request):
    """
    Function for deleting request to perform delete operation in Question model
    """
    try:
        data = json.loads(request.body)
        if request.method == 'DELETE':
            id = data.get('id')
            Question.objects.get(id=id).delete()
            return JsonResponse({"message": "data deleted"})
        return JsonResponse({'message': 'Method not allowed'})
    except Exception as e:
        logging.exception(e)


def create_choice(request):
    """
    Function for creating request for create operation using Choice model
    """
    try:
        data = json.loads(request.body)
        if request.method == "POST":
            choice = Choice.objects.create(question_id=data.get("question"), choice_text=data.get("choice_text"),
                                           votes=data.get("votes"))
            return JsonResponse({"meassage": "created choice",
                                 "data": {"id": choice.id, "choice_text": choice.choice_text, "votes": choice.votes}})
    except Exception as e:
        logging.exception(e)


def update_choice(request):
    """
        Function for creating request to perform update operation in Choice model
    """
    try:
        data = json.loads(request.body)
        if request.method == "PUT":
            id = data.get("id")
            choice_obj = Choice.objects.get(id=id)
            choice_obj.choice_text = data.get('choice_text')
            choice_obj.votes = data.get("votes")
            choice_obj.save()
            return JsonResponse({"message": "update choice",
                                 "data": {"id": choice_obj.id, "choice_text": choice_obj.choice_text,
                                          "votes": choice_obj.votes}})
        return JsonResponse({"message": "method not allowed"})
    except Exception as e:
        logging.exception(e)


def get_choice(request):
    """
    Function for creating request to get all data from Choice model

    """
    try:
        if request.method == "GET":
            data = json.loads(request.body)
            quest = Question.objects.get(id=data.get('id'))
            choice = quest.choice_set.all()
            return JsonResponse({"Message": "choice all data are",
                                 "data": [{"id": q.id, "choice_text": q.choice_text, "votes": q.votes} for q in
                                          choice]}, status=200)
        return JsonResponse({"Message": "Method not allowed"}, status=204)
    except Exception as e:
        logging.exception(e)


def delete_choice(request):
    """
        Function for creating request to delete data from Choice model
    """
    try:
        data = json.loads(request.body)
        if request.method == "DELETE":
            id = data.get("id")
            Choice.objects.get(id=id).delete()
            return JsonResponse({"message": "data deleted"})
    except Exception as e:
        logging.exception(e)
