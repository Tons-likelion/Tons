from django.shortcuts import render
from accounts.models import Profile
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

#상세 글 - 별점 기능?
def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'article_detail.html', {'article':article})


#로그인 기능
def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request, 'logout.html')

#회원가입
def signup(request):
    #기본 정보 입력 후, 마이페이지로 redirect 해서 카테고리 선택?
    return render(request, 'signup.html')

#마이페이지
def mypage(request):
    return render(request, 'mypage.html')

def choose_category(request):
    pass


#요약 작성, 수정, 삭제 기능 - 좋/싫 기능
def summary_create(request, article_id):
    pass

def summary_edit(request, article_id, sum_id):
    pass

def summary_delete(request, article_id, sum_id):
    pass


# 카테고리 디테일 페이지 - 수정 필요
# def category_detail(request, cat_id):
#     cat_detail = get_object_or_404(Category, pk=cat_id)
#     return render(request, 'base_app/category_detail.html', {'cat_detail':cat_detail})
def category_detail(request):
    return render(request, 'category_detail.html')
