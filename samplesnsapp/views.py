from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import PostModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


def signupfunc(request):

    print('##################')
    print(request.POST)
    print('##################')

    if request.method == "POST":
        username = request.POST['username']
        print('sername:'+ username)
        password = request.POST['password']
        print('password:' + password)

        #重複したユーザーあった場合
        try:
            user = User.objects.create_user(username,'', password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは使われている'})
    else:
        print('-------------')
        print('not post method')
        print('-------------')
    return render(request, 'signup.html', {})

def loginfucn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            #ユーザーがマッチしたら
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})


#こっちの方法でもできる
#@login_required
def listfunc(request):
    object_list = PostModel.objects.all()
    return render(request, 'list.html',{'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request,pk):
    print('-------------')
    print(pk)
    print('-------------')

    #こっちの方が一般的に使われるらしい
    object =  get_object_or_404(PostModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):

    object = PostModel.objects.get(pk = pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')



def readfunc(request, pk):
    object = PostModel.objects.get(pk = pk)

    #login している　user の情報を取得することができる
    #Dajngo がデフォルトで持っているメソッド
    username = request.user.get_username()
    if username in object.read_text:
        return redirect('list')
    else:
        object.read = object.read + 1

        ##今回は空白で　実装向きではないが・・・
        object.read_text = object.read_text + ' ' + username
        object.save()
        return redirect('list')

class ImgCreate(CreateView):
    print('----create----')
    print('--------')
    print('--------')
    template_name = 'create.html'
    model = PostModel
    fields = ('title', 'content', 'poster', 'sns_image')
    success_url = reverse_lazy('list')