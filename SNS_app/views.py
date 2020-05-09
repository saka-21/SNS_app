from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import SnsModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


def signup_func(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})


def login_func(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')

        else:
            return redirect('login')

    return render(request, 'login.html')


@login_required
def list_func(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logout_func(request):
    logout(request)
    return redirect('login')


def detail_func(request, pk):
    object = SnsModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def good_func(request, pk):
    post = SnsModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')


def read_func(request, pk):
    post = SnsModel.objects.get(pk=pk)
    post_un = request.user.get_username()
    if post_un in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext += '' + post_un
        post.save()
        return redirect('list')


class SnsCreate(CreateView):
    template_name = 'create.html'
    model = SnsModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')





