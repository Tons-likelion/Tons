from django.shortcuts import render
from accounts.models import Profile
# Create your views here.


def home(request):
    return render(request, 'home.html')

#상세 글 - 별점 기능?
def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'base_app/detail.html', {'article':article})




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


