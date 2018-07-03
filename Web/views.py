from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from Web.models import *

# Create your views here.

def index(request):
    context={}
    if request.method =='GET':
        # try :
        #     User=UserProfile.objects.get(id=request.user.id)
        #     print(User)
        # else:
        #     User = None
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        k1 = server_choices.objects.get(ex_ser_name='定制婚礼')
        k2 = server_choices.objects.get(ex_ser_name='婚礼服饰')
        k3 = server_choices.objects.get(ex_ser_name='其他')
        kind1 = C_S.objects.filter(service_kind = k1).order_by('public_like')[:3]
        kind2= C_S.objects.filter(service_kind = k2).order_by('public_like')[:3]
        kind3 = C_S.objects.filter(service_kind = k3).order_by('public_like')[:3]
        context['User']=User
        context['city']=cities
        context['s_kind'] = ser_kind
        context['favor1'] = kind1
        context['k1'] = k1
        context['favor2'] = kind2
        context['k2'] = k2
        context['favor3'] = kind3
        context['k3'] = k3
        print(context)
        return render(request,'index.html',context=context)
    else:
        return redirect(to='index')


def backWeb(request):
    context={}
    if request.user:
        if request.method == 'GET':
            cities = City.objects.all()
            ser_kind = server_choices.objects.all()
    return render(request,'Back_Manage.html',context=context)

def single(request,id):
    context={}
    if request.method =='GET':
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        server= C_S.objects.get(id=id)
        company = server.belong
        images = Graph.objects.filter(belong=server).order_by('order_number')
        otherserver = C_S.objects.filter(belong=company)
        flags = flag.objects.all()
        context['city'] =cities
        context['s_kind'] = ser_kind
        context['server'] = server
        context['company'] = company
        context['images'] = images
        context['other'] = otherserver
        context['tags'] = flags
        print(context)
        return render(request,'single.html',context=context)
    else:
        return redirect(to='index')

def server(request,site,kind):
    context={}
    if request.method =='GET':
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        if site == '0':
            servers = C_S.objects.filter(service_kind__id=kind)
            tsite = City.objects.filter(id = site)
            tkind = server_choices.objects.get(id = kind)
        elif kind == '0':
            servers = C_S.objects.filter(belong__adress=site)
            tsite = City.objects.get(id = site)
            tkind = server_choices.objects.filter(id = kind)
        else:
            servers = C_S.objects.filter(belong__adress=site,service_kind=kind)
            tsite = City.objects.get(id = site)
            tkind = server_choices.objects.get(id = kind)
        context['city'] =cities
        context['s_kind'] = ser_kind
        context['servers'] = servers
        context['site'] = tsite
        context['kind'] = tkind
        print(context)
    return render(request,'server.html',context=context)

def person(request):
    cities = City.objects.all()
    ser_kind = server_choices.objects.all()
    
    context['city'] =cities
    context['s_kind'] = ser_kind
    return render(request,'person.html',context=None)

def person_fav(request):
    context={}
    if request.user:
        User=UserProfile.objects.get(id=request.user.id)
        print(User)
    else:
        User = None
    cities = City.objects.all()
    ser_kind = server_choices.objects.all()
    favs = Fav.objects.filter(fav_user = User)
    print(favs)
    context['User']=User
    context['city']=cities
    context['favs']=favs
    return render(request,'person-fav.html',context=context)

def person_list(request):
    return render(request,'person-list.html',context=None)

def retrun_index(request):
    return index(request)

def company(request):
    return render(request,'company.html',context=None)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
        other = "Register"
        url="../../register/"
        context['other'] = other
        context['url'] = url
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='index')
    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
        other = "Login"
        url="../../login/"
        context['other'] = other
        context['url'] = url
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)
