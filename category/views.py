from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile

# Create your views here.
def mypage(request, user_id):
    user = get_object_or_404(Profile, pk = user_id)
    cat_list = user.category.all()
    return render(request, 'mypage.html', {'cat_list' : cat_list})

# def add_cat(request):
#     pass