from __future__ import unicode_literals

from django.db import models
from django.utils import timezone  # Timezone
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Question(models.Model):
    """
    # Question Text
    # Publish Date
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    # Choice Text
    # Number of Votes
    # Link (This link for question with its appropriate choices)
    """
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Questions(models.Model):
    """
    # Question Text
    # Publish Date
    """
    var_question_description = models.CharField(max_length=200)
    var_question_title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.var_question_title + '(' + self.var_question_description + ')'


class Choices(models.Model):
    """
    # Choice Text
    # Number of Votes
    # Link (This link for question with its appropriate choices)
    """
    var_choice_text = models.CharField(max_length=200)
    var_votes_int = models.IntegerField(default=0)
    var_question_obj = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.var_choice_text + '(' + self.var_question_obj.var_question_title + ')'


"""
class Question(models.Model):
    question_title = models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.question_title)


class Choice(models.Model):

    # question = models.ForeignKey(Question, null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.choice_text)


class Vote(models.Model):
    user = models.ForeignKey(User)
    # user = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question, null=True)
    choice = models.ForeignKey(Choice, null=True)
    pub_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.user.username + ':' + self.question.question_title + ':' + self.choice.choice_text
"""

"""
Shell commands:

# Get all Questions:
from pollapp.models import Question
questions_list = Question.objects.all()
questions_dict = dict()
for each_question in questions_list:
    questions_dict[each_question.id] = each_question.question_title


# Get all Votes
total_votes = Vote.objects.all()

question_answer_dict = dict()
statistics_dict = dict()
for idx, each_vote in enumerate(total_votes):
    print str(idx) + 50 * '-'
    # Get information from votes
    question_id = int(each_vote.question.id)
    choice_str = str(each_vote.choice.choice_text)
    # Get the Question Title
    question_title_str = questions_dict[question_id]
    print "%s. \t%s" % (question_title_str, choice_str)

    # Save 
    if question_title_str not in statistics_dict: 
        statistics_dict[question_title_str] = dict()
    if choice_str not in statistics_dict[question_title_str]:
        statistics_dict[question_title_str][choice_str] = 1
    else:
        statistics_dict[question_title_str][choice_str] = statistics_dict[question_title_str][choice_str] + 1
"""
