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
    if isinstance(request.user,User):
        user = UserProfile.objects.get(belong_to = request.user)
    else:
        user = None
    if request.method =='GET':
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        server= C_S.objects.get(id=id)
        company = server.belong
        images = Graph.objects.filter(belong=server).order_by('order_number')
        flags = flag.objects.all()
        if user:
            fav = Fav.objects.filter(fav_ser = server, fav_user = user)
        else:
            fav = None
        context['fav'] = fav
        context['User']=user
        context['city'] =cities
        context['s_kind'] = ser_kind
        context['server'] = server
        context['company'] = company
        context['images'] = images
        context['tags'] = flags
        return render(request,'single.html',context=context)
    elif request.method =='POST':
        if user:
            ser = C_S.objects.get(id = id)
            new = Order_list(Username = user,needlist = ser,price=ser.minprice)
            new.save()
            return redirect(to="/person-list/")
        else:
            return redirect(to="/single/"+id)
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
        if site == '0' and kind == '0':
            servers = C_S.objects.all()
            tsite = City.objects.filter(id = site)
            tkind = server_choices.objects.filter(id = kind)
        elif site == '0':
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
    if request.method == 'GET':
        cities = City.objects.all()
        ser_kind = server_choices.objects.all()
        lists = Order_list.objects.filter(Username = user)
        context['lists'] = lists
        context['User'] = user
        context['city'] = cities
        context['s_kind'] = ser_kind
        return render(request,'person-list.html',context=context)
    elif request.method == 'POST':
        ser_id = request.POST['ser_id']
        user_id = request.POST['user_id']
        the_list = Order_list.objects.get(id = ser_id,Username=user_id)
        if the_list.status.id < 7:
            the_list.status = status.objects.get(status_level = the_list.status.next_2)
            the_list.save()
        return redirect(to="/person-list/")

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

def favfunction(request,ser_id,msg,way):
    if isinstance(request.user,User):
        user = UserProfile.objects.get(belong_to = request.user)
        ser = C_S.objects.get(id = ser_id)
        if msg =='put':
            fav = Fav(fav_user = user,fav_ser = ser)
            fav.save()
        elif msg =='del':
            fav = Fav.objects.filter(fav_user = user,fav_ser = ser)
            fav.delete()
        else:
            return redirect(to='/index/')
        if way == 'single':
            return redirect(to='/single/'+ser_id)
        elif way == 'personfav':
            return redirect(to='/person-fav/')
        else:
            return redirect(to='/index/')
    else:
        return redirect(to='/login/')

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
