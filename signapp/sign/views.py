from django.shortcuts import render
from .models import Signup
from .forms import SignForm


# Create your views here.

def index(request):
	signup = Signup.objects.order_by('-id')
	context = {'signup':signup}
	return render(request, 'sign/index.html', context)

def sign(request):
	if request.method == 'POST':
		form = SignForm(request.POST)

		if form.is_valid():
			new_comment = Signup(name=request.POST['name'], phone=request.POST['phone'], email=request.POST['email'])
			new_comment.save()

			return redirect('index')
	else:
		form = SignForm()

	context = {'form':form}
	return render(request, 'sign/sign.html', context)