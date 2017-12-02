from django.contrib import admin

# Register your models here.
from .models import Question, Choice
from .models import Questions, Choices
# from .models import Vote

admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(Vote)

admin.site.register(Questions)
admin.site.register(Choices)
