from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from article.models import Article, Summary
from .models import Category
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, user_id):
    user = User.objects.get(id = user_id)
    try:
        profile = Profile.objects.get(user = user)
    except:
        return redirect('home')
    user_cat_list = profile.category.all()
    other_cat_list = []
    for cat in Category.objects.all():
        if cat not in user_cat_list:
            other_cat_list.append(cat)

    return render(request, 'mypage.html', {'user_cat_list' : user_cat_list, 'other_cat_list':other_cat_list, 'profile_id':profile.id})

def cat_add(request, user_id, category_id):
    user = User.objects.get(id = user_id)
    profile = Profile.objects.get(user = user)
    profile.category.add(Category.objects.get(id=category_id))
    return redirect('mypage', user_id= user.id)

def cat_remove(request, user_id, category_id):
    user = User.objects.get(id = user_id)
    profile = Profile.objects.get(user = user)
    profile.category.remove(Category.objects.get(id=category_id))
    return redirect('mypage', user_id= user.id)   

def cat_detail(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    article_list = Article.objects.filter(category=category_id)
    best_summ_list = dict()

    for article in article_list:
        try:
            best_summ_list[article.id] = Summary.objects.filter(belongsto_article=article.id).latest('obj_count')
            # result['best_summ'] = Summary.objects.get(belongsto_article = article.id )
        except: #요약이 하나도 없을 경우
            best_summ_list[article.id] = '아직 요약이 없습니다!'

    context = {
    'category':category,
    'article_list':article_list,
    'best_summ_list' : best_summ_list,
    }

    
    from django.template.defaulttags import register

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, 'category/category_detail.html', context)