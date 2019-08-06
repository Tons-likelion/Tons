from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Article, Summary
from accounts.models import Profile

# Create your views here.

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    summary_list = Summary.objects.filter(belongsto_article=article_id)
    context = {
        'article':article,
        'summary_list':summary_list,
    }

    return render(request,"article/article_detail.html", context)

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
    user = request.user
    profile = Profile.objects.get(user=user)

    check_obj_summary = profile.obj_summ.filter(id=summary_id)

    if check_obj_summary.exists():
        profile.obj_summ.remove(summary)
        summary.obj_count -= 1
        summary.save()
    else:
        profile.obj_summ.add(summary)
        summary.obj_count += 1
        summary.save()

    return redirect('article:detail', summary.belongsto_article.id)

def summary_sbj_toggle(request, summary_id):
    
    summary = Summary.objects.get(id=summary_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    check_sbj_summary = profile.sbj_summ.filter(id=summary_id)
    if check_sbj_summary.exists():
        profile.sbj_summ.remove(summary)
        summary.sbj_count -= 1
        summary.save()
    else:
        profile.sbj_summ.add(summary)
        summary.sbj_count += 1
        summary.save()

    return redirect('article:detail', summary.belongsto_article.id)