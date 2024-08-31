from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Project
from .forms import ExaminerEvaluationForm, GuideEvaluationForm
def home(request):
    return render(request,'mtechMinorEval/home.html')

def projectsList(request):
    return render(request,'mtechMinorEval/projectsList.html')

def evaluate(request):
    formExaminer=ExaminerEvaluationForm()
    formGuide=GuideEvaluationForm
    context={'formExaminer':formExaminer ,'formGuide':formGuide}
    return render(request,'mtechMinorEval/projectEvaluation.html',context=context)