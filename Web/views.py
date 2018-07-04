from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from Web.models import *

# Create your views here.

def index(request):#用户的验证
    context={}
    if request.method =='GET':
        if isinstance(request.user,User):
            user = UserProfile.objects.get(belong_to = request.user)
        else:
            user = None
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        k1 = server_choices.objects.get(ex_ser_name='定制婚礼')
        k2 = server_choices.objects.get(ex_ser_name='婚礼服饰')
        k3 = server_choices.objects.get(ex_ser_name='其他')
        kind1 = C_S.objects.filter(service_kind = k1).order_by('public_like')[:3]
        kind2= C_S.objects.filter(service_kind = k2).order_by('public_like')[:3]
        kind3 = C_S.objects.filter(service_kind = k3).order_by('public_like')[:3]
        context['User']=user
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
        return redirect(to='/index/')


def backWeb(request):
    context={}
    if request.method == 'GET':
        if isinstance(request.user,User):
            user = UserProfile.objects.get(belong_to=request.user)
            if user.is_C_man:
                cities = City.objects.all()
                ser_kind = server_choices.objects.all()
                context['User'] = user
                context['city']=cities
                context['s_kind'] = ser_kind
                return render(request,'back_manage.html',context=context)
    return redirect(to='/index/')

def single(request,id):
    context={}
    if request.method =='GET':
        if isinstance(request.user,User):
            user = UserProfile.objects.get(belong_to = request.user)
        else:
            user = None
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        server= C_S.objects.get(id=id)
        company = server.belong
        images = Graph.objects.filter(belong=server).order_by('order_number')
        otherserver = C_S.objects.filter(belong=company)
        flags = flag.objects.all()
        context['User']=user
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
        return redirect(to='/index/')

def server(request,site,kind):
    context={}
    if request.method =='GET':
        if isinstance(request.user,User):
            user = UserProfile.objects.get(belong_to = request.user)
        else:
            user = None
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
        context['User'] = user
        context['city'] =cities
        context['s_kind'] = ser_kind
        context['servers'] = servers
        context['site'] = tsite
        context['kind'] = tkind
        print(context)
    return render(request,'server.html',context=context)

def person(request):
    context={}
    if isinstance(request.user,User):
        user = UserProfile.objects.get(belong_to = request.user)
    else:
        return redirect(to='/index/')
    if request.method == 'GET':
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        context['User'] = user
        context['city'] =cities
        context['s_kind'] = ser_kind
        return render(request,'person.html',context=context)
    elif request.method =='POST':
            form = request.POST
            user.belong_to.username = form['User_name']
            user.email = form['User_email']
            user.location.id = int(form['city'])
            user.sex = bool(form['sex'])#  error!
            user.phone = form['User_phone']
            user.save()
            cities = City.objects.all()
            ser_kind = server_choices.objects.all()
            context['User'] = user
            context['city'] =cities
            context['s_kind'] = ser_kind
            return render(request,'person.html',context=context)
    else:   
        return redirect(to='/index/')

def person_fav(request):
    context={}
    if isinstance(request.user,User):
        user = UserProfile.objects.get(belong_to = request.user)
    else:
        return redirect(to='/index/')
    cities = City.objects.all()
    ser_kind = server_choices.objects.all()
    favs = Fav.objects.filter(fav_user = user)
    print(favs)
    context['User']=user
    context['city']=cities
    context['favs']=favs
    return render(request,'person-fav.html',context=context)

def person_list(request):
    context={}
    if isinstance(request.user,User):
        user = UserProfile.objects.get(belong_to = request.user)
    else:
        return redirect(to='/index/')
    cities = City.objects.all()
    ser_kind = server_choices.objects.all()
    lists = Order_list.objects.filter(Username = user)
    print(lists)
    context['lists'] = lists
    context['user'] = user
    context['city'] = cities
    context['s_kind'] = ser_kind
    return render(request,'person-list.html',context=context)

def company(request,id):
    context={}
    if request.method =='GET':
        if isinstance(request.user,User):
            user = UserProfile.objects.get(belong_to = request.user)
        else:
            user = None
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        com = Company.objects.get(id = id)
        sers = C_S.objects.filter(belong = com)
        context['com'] = com
        context['sers'] = sers
        context['user'] = user
        context['city'] = cities
        context['s_kind'] = ser_kind
    return render(request,'company.html',context=context)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

def index_login(request):
    context = {}
    other = "Register"
    url="../../register/"
    context['other'] = other
    context['url'] = url
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='/index/')
    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    other = "Login"
    url="../../login/"
    context['other'] = other
    context['url'] = url
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new = form.save()
            user = UserProfile(belong_to=new)
            user.save()
            return redirect(to='/login/')
    context['form'] = form
    return render(request, 'register_login.html', context)
