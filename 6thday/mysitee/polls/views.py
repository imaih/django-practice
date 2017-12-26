from django.shortcuts import render, HttpResponse
from .models import Message


def index(request):
	all_message = Message.objects.all()
	return render(request, 'index.html', {'message': all_message})

