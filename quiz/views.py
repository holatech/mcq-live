from django.shortcuts import render, redirect
from .models import Story, Question, Answer


# Create your views here.

def index(request):
    return render(request, 'quiz/index.html')

def takeQuiz(request):
    score = 0
    
    if request.method == 'POST':
        for i in range(1, len(request.POST)):
           if request.POST.get('option'+ str(i)) == str(Question.objects.get(pk=i).answer):
               score = score + 1
           else:
               continue
        return redirect(result, pk=score)
     
    questions = Question.objects.all()
    stories = Story.objects.all()
    context = {
        'stories' : stories,
        'questions': questions
    }
    return render(request, 'quiz/take_quiz.html', context)
    
def result(request, pk):
    score = pk
    return render(request, 'quiz/result.html', {'score':score})