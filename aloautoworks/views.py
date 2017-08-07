
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserDataForm

def index(request):
	return render(request,"index.html")


def services(request):
	return render(request,"service.html")


def blogs(request):
	return render(request,"blog.html")


def thanks(request):
	return render(request,"thanks.html")

def blog_detail(request):
	return render(request,"blog_detail.html")


def appointment_book(request):
	form = UserDataForm()
	if request.method=='POST':
		form = UserDataForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,"thanks.html")
		else:
			messages.add_message(request, messages.INFO, 'please check whether the form has been filled expected format')


	return render(request,"appointment.html",{"form":form})


def contact(request):
	return render(request,"contact.html")
def checkcontact(request):
	form = UserDataForm
	if request.method == 'POST':
            form = UserDataForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "thanks.html")
            else:
                messages.error(request, "Error")

	return render(request,"checkcontact.html",{'form':form})


#def post_appointment(request):
	#qdict = request.POST
	#first_name = qdict.get("first_name")
	#instance = TestModel(
	#	first_name = first_name,
	##)
	#instance.save()