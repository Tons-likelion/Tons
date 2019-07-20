from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

#상세 글 - 별점 기능?
def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'base_app/detail.html', {'article':article})


#로그인 기능
def login(request):
    return render(request,'base_app/login.html')

def logout(request):
    return render(request, 'base_app/logout.html')

#회원가입
def signup(request):
    #기본 정보 입력 후, 마이페이지로 redirect 해서 카테고리 선택?
    return render(request, 'base_app/signup.html')

#마이페이지
def mypage(request):
    return render(request, 'base_app/mypage.html')

def choose_category(request):
    pass


#요약 작성, 수정, 삭제 기능 - 좋/싫 기능
def summary_create(request, article_id):
    pass

def summary_edit(request, article_id, sum_id):
    pass

def summary_delete(request, article_id, sum_id):
    pass


