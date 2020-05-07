from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.
def home(request):
	context = {}
	subject_list = Subject.objects.all().order_by('name')
	context['subject_list'] = subject_list
	return render(request, 'subjects/sample.html',context)

def detail_view(request,slug):
	context = {}
	subject_detail = Subject.objects.get(slug = slug)
	context['subject_detail'] = subject_detail
	return render(request, 'subjects/sample.html',context)
