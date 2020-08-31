from django.contrib import admin
from .models import Story, Question, Answer

# Register your models here.
admin.site.register(Story)

admin.site.register(Question)
admin.site.register(Answer)

