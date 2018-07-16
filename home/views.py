from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.

def index(request):
	return render(request, 'home/index.html', {})

def form_test(request):
	from django import forms
	class NameForm(forms.Form):
		your_name = forms.CharField(label='Your name', max_length=100)

	context = { "form" : NameForm() }
	return render(request, 'home/home.html', context)

def home(request):
	result = {'request': 'test', 'response': 200}
	return JsonResponse(result)
