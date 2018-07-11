from django.shortcuts import render
from django.http import HttpResponseRedirect
from emaillist.models import Emaillist
# Create your views here.

def index(request):
    emaillist_list = Emaillist.objects.all().order_by('-id')
    data = {'emaillist_list' : emaillist_list}
    return render(request, 'emaillist/index.html', data) # html 응답 넘겨줄 데이터가 없을 땐 data없이 사용가능

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']
    emaillist.save()

    return HttpResponseRedirect('/emaillist') # 리다이렉트 응답
    # return render(request, 'success.html')