import json
# ----------------------------------------------------------------------------------------------
import os

from django.http import HttpResponse


def get_questions():
    # Get Poll Questions .json file
    current_file_dir_path = os.path.abspath(os.path.dirname(__file__))
    questions_file = str(os.path.join(current_file_dir_path, "static", "poll_questions.json"))

    # questions_dict = dict()
    # with open(questions_file, "r") as questions_file_obj:
    #     questions_dict = json.load(questions_file_obj)
    questions_file_obj = open(questions_file, "r")
    questions_dict = json.load(questions_file_obj)
    questions_file_obj.close()

    # print type(questions_dict), questions_dict
    # questions_dict = sorted(questions_dict, key=lambda k: questions_dict.keys()[0])
    # print questions_dict
    return questions_dict

# ----------------------------------------------------------------------------------------------

# def submit_page(request):
#     if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
#         username = request.COOKIES['username']
#
#         last_connection = request.COOKIES['last_connection']
#         last_connection_time = datetime.datetime.strptime(last_connection[:-7],
#                                                           "%Y-%m-%d %H:%M:%S")
#
#         if (datetime.datetime.now() - last_connection_time).seconds < 10:
#             return render(request, 'poll/login.html', {"username": username})
#         else:
#             return render(request, 'poll/submit.html', {})
#     else:
#         return render(request, 'poll/login.html', {})


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from .models import Questions

# def index(request):
#     questions_list = Question.objects.all()
#     msg = "<div><h2>Welcome to Polling of 2017 !!!</h2></div><br><br>"
#     for each_question in questions_list:
#         msg += "<div>" + each_question.question_text + "</div></br>"
#     return HttpResponse(msg)
# ------------------------------------------------------
# from django.template import loader, RequestContext
# def index(request):
#     latest_questions = Question.objects.order_by('pub_date')  # or use '-pub_date'
#     template = loader.get_template('poll/index.html')
#     context = RequestContext(request, {'latest_questions': latest_questions})
#     return HttpResponse(template.render(context))
from django.shortcuts import render
def index(request):
    # latest_questions = Questions.objects.order_by('pub_date')
    latest_questions = Questions.objects.all()
    context = {'latest_questions': latest_questions}
    return render(request, 'poll/index.html', context)


# ****************************************************************************
# ****************************************************************************
# def detail(request, question_id):
    # return HttpResponse("This is the detail view of the question: %s" % question_id)
# ------------------------------------------------------
# def detail(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     return render(request, 'poll/detail.html', {'question': question})
# ------------------------------------------------------
from django.shortcuts import get_object_or_404
def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})

# ****************************************************************************
# ****************************************************************************
# def results(request, question_id):
#     return HttpResponse("These are the results of the questions: %s" % question_id)
# ------------------------------------------------------
def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})

# ****************************************************************************
# ****************************************************************************
# def vote(request, question_id):
#     return HttpResponse("Vote on question: %s" % question_id)
# ------------------------------------------------------
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'poll/detail.html', {'question': question, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('poll:results', args=(question.id, )))  # to avoid having hard-coded url.
    # Note: It's very important to add a comma in the args parameters, otherwise there will be an error.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
