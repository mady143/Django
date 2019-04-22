from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AcessRecord,Webpage,Topic,Users
def index(request):

	webpages_list = AcessRecord.objects.order_by('date')
	date_dict     = {'acess_records':webpages_list}
	

	return render(request,'first_app/index.html',context = date_dict)


def users(request):
	users_list  = Users.objects.order_by('first_name')
	user_dict   = {'users':users_list}

	return render(request,'first_app/users.html',context = user_dict)