from django.http import HttpResponse

def index(request):
	return  HttpResponse('Hello, I am a django Developer')

# Create your views here.
