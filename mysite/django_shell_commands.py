
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Load all questions in the database 'Questions':
import django
django.setup()
#
import json
questions_json_file = '/home/sultan.bal/Desktop/website/poll/poll/static/poll/poll_questions.json'
with open(questions_json_file, 'r') as fileobj:
    j_dict = json.load(fileobj)
print j_dict
#
from poll.models import Questions
for k, val in j_dict.iteritems():
    q = Questions()
    q.var_question_title = k
    q.var_question_description = val
    q.save()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Load all artists in the database 'Choices':
from . import utilities
user_info_list = utilities.get_user_info_from_ldap()
from poll.models import Choices
questions_obj_list = Questions.objects.all()
for each_question in questions_obj_list:
    for each_user in user_info_list:
        username = each_user['uid']
        each_question.choices_set.create(var_choice_text=username, var_votes_int=0)



