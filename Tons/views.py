from django.shortcuts import render, redirect
from accounts.models import Profile
from article.models import Article, Summary
from category.models import Category
from django.contrib.auth.models import User

def home(request, user_id = None):

    # from django.template.defaulttags import register
    # @register.filter
    # def get_item(dictionary, key):
    #     return dictionary.get(key)

    top10_article = Article.objects.order_by('-stars')[:10]
    top10_best_summ_list = dict()
    for article in top10_article:
        try:
            top10_best_summ_list[article.id] = Summary.objects.filter(belongsto_article=article.id).latest('obj_count')
        except: #요약이 하나도 없을 경우
            top10_best_summ_list[article.id] = '아직 요약이 없습니다!'

    if user_id: #유저가 선택한 카테고리
        user = User.objects.get(id = user_id)
        try:
            profile = Profile.objects.get(user = user)
        except: #어드민계정예외
            user_id = None
            return redirect('home')
        
        user_cat_list = profile.category.all()
        user_category = dict()
        best_summ_list = dict()
        for category in user_cat_list:
            try:
                article = Article.objects.filter(category=category.id).latest('stars')
                user_category[category] = article
                try:
                    best_summ_list[article.id] = Summary.objects.filter(belongsto_article=article.id).latest('obj_count')
                except: #요약이 하나도 없을 경우
                    best_summ_list[article.id] = '아직 요약이 없습니다!'
            except: # 하나도 없을 경우
                best_summ_list = None
                user_category[category] = '기사가 없습니다.'            
        return render(request, 'home.html', {'top10_article' : top10_article,'article_by_category': user_category, 'best_summ_list':best_summ_list, 'top10_best_summ_list':top10_best_summ_list})

    else: #최신 기사가 올라온 카테고리 3개
        new_article = Article.objects.order_by('-pub_date')[:3]
        rand_category_list = []
        
        for article in new_article:
            rand_category_list.append(article.category)

        rand_category = dict()
        for category in rand_category_list:
            try:
                article = Article.objects.filter(category=category.id).latest('stars')
                rand_category[category] =article
                try:
                    best_summ_list[article.id] = Summary.objects.filter(belongsto_article=article.id).latest('obj_count')
                except: #요약이 하나도 없을 경우
                    best_summ_list[article.id] = '아직 요약이 없습니다!'
            except: # 하나도 없을 경우
                best_summ_list = None
                rand_category[category] = '기사가 없습니다.'

        return render(request, 'home.html', {'top10_article' : top10_article,'article_by_category': rand_category, 'best_summ_list':best_summ_list, 'top10_best_summ_list':top10_best_summ_list})



    
    

