from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
#from django.utils import timezone
#from .models import Post
#from django.shortcuts import render, get_object_or_404
#from .forms import PostForm
#from .forms import EquipamentoForm
#from django.shortcuts import redirect

#pagina inicial do site
def index(request):
	#return HttpResponse("<h2>HEY!</h2>")
	return render(request, 'siobra/home.html',{'content':['Qualquer duvida, contate-me','theosribeiro@gmail.com']})

def contact(request):
	return render(request,'siobra/contact.html',{'content':['Qualquer duvida, contate-me','theosribeiro@gmail.com']})  #{'form': form,}
	#return HttpResponse("<h2>HEY!</h2>")






