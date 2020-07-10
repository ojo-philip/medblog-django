from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm, UserAuthenticationForm
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home_page(request):
    post = Post.objects.all()
    paginator = Paginator(post, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        'posts': items,
        'page_range': page_range
    }
    return render(request, 'blog/home_page.html', context)


def about_page(request):
    context = {}
    return render(request, 'blog/about.html', context)


def post_detail(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, pk=pk)
    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)


class UsersPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


def user_post_list(request):
    if request.user.is_authenticated:
        user = request.user
        user_post = Post.objects.filter(user=user)
    else:
        user_post = Post.objects.all()
    paginator = Paginator(user_post, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'posts': items,
        'page_range': page_range
    }
    return render(request, 'blog/user_post_list.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, f'Post created successfully.')
            return redirect('blog:home_page')
        else:
            for msg in form.error_messages:
                messages.warning(request, f'Error: {form.error_messages}')
    else:
        form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'blog/post_form.html', context)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update_form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def login_page(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f'You have logged in successfully as {username}')
                return redirect('blog:home_page')
            else:
                messages.warning(
                    request, 'Username or password is incorrect, please provide the valid data')
        else:
            messages.warning(
                request, 'Username or password is incorrect, please provide the valid data')

    form = UserAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'blog/login.html', context)


def logout_page(request):
    if request.user:
        logout(request)
        messages.info(
            request, 'You have been logged out successfully. Please login again')
        return redirect('blog:login_page')


@login_required
def comment_page(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.post = post
            obj.save()
            messages.success(request, 'Your comment is saved successfully')
            return redirect('blog:post_detail', slug=post.slug, pk=post.id)
    else:
        form = CommentForm()
        context = {
            'form': form
        }
    return render(request, 'blog/comment_page.html', context)
