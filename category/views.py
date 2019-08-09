from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from article.models import Article, Summary
from .models import Category

# Create your views here.
def mypage(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    user_cat_list = user.category.all()
    other_cat_list = []
    for cat in Category.objects.all():
        if cat not in user_cat_list:
            other_cat_list.append(cat)

    return render(request, 'mypage.html', {'user_cat_list' : user_cat_list, 'other_cat_list':other_cat_list})

# def add_cat(request):
#     pass

def cat_detail(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    article_list = Article.objects.filter(category=category_id)

    def best_summ():
        pass

    best_summ_list = dict()
    for article in article_list:
            if Summary.objects.filter(belongsto_article=article.id):
                best_summ_list[article.id] = Summary.objects.filter(belongsto_article=article.id).latest('obj_count')
    context = {
        'category':category,
        'article_list':article_list,
        # 'best_summ_list' : best_summ_list,
    }
    return render(request, 'category/category_detail.html', context)