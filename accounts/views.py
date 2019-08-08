from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == "POST": #회원가입버튼 클릭 시
        username = request.POST.get('username')
        password = request.POST.get('password')
        psudo_password = request.POST.get('psudo_password')
        if password == psudo_password :
            user = User.objects.create_user(username=username, password=password) #장고의 createsuperuser 을 가져옴. admin 페이지에서 User테이블 확인
            author = Profile()
            author.user = user
            author.email = request.POST.get('email')
            author.save() #저장꼭!
        else : #TODO 비밀번호가 틀릴 시
            pass
        return redirect('home') #render()가 아님!!
    else:   #TODO 회원가입 페이지로 접속할때
        pass
    return render(request, 'accounts/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password) #로그인 정보 확인
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:   #TODO 로그인 정보가 없을때
            pass
        return render(request,'accounts/login.html')
    else:   #TODO 회원가입 페이지로 접속할때
        pass
    return render(request,'accounts/login.html')