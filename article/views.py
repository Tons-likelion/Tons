from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Article, Summary

# Create your views here.

def detail(request, article_id):
    article_list = Article.objects.all()
    summary_list = Summary.objects.filter(belongsto_article=article_id)
    context = {
        'article_list':article_list,
        'summary_list':summary_list,
    }

    return render(request,"article/detail.html", context)

def summary(request, article_id):

    if request.method == "POST":
        summary = Summary()
        summary.belongsto_article = Article.objects.get(id=article_id)
        summary.content = request.POST['content']
        summary.save()
        return redirect('article:detail', article_id)
    else:
        return render(request, 'article/summary.html')

def summary_obj_toggle(request, summary_id):
    
    summary = Summary.objects.get(id=summary_id)
    author = request.user.author

    check_obj_summary = author.obj_summary.filter(id=summary_id)
    if check_obj_summary.exists():
        author.obj_summary.remove(summary)
        summary.obj_count -= 1
        summary.save()
    else:
        author.obj_summary.add(summary)
        summary.obj_count += 1
        summary.save()

    return redirect('home')

def summary_sbj_toggle(request, summary_id):
    
    summary = Summary.sbjects.get(id=summary_id)
    author = request.user.author

    check_sbj_summary = author.sbj_summary.filter(id=summary_id)
    if check_sbj_summary.exists():
        author.sbj_summary.remove(summary)
        summary.sbj_count -= 1
        summary.save()
    else:
        author.sbj_summary.add(summary)
        summary.sbj_count += 1
        summary.save()

    return redirect('home')