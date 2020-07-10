from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile, SearchQuery
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post

from django.contrib import messages


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account has been created for {username}')
            return redirect('blog:login_page')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'userprofile/user_registration.html', context)


@login_required
def user_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        u_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(
                request, 'Your Profile has been updated successfully')

    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form
    }
    return render(request, 'userprofile/profile.html', context)


def search_query(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {
        'query': query
    }
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = Post.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'userprofile/search_query.html', context)
