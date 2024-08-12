from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PostForm,GroupForm
from .models import Post,CustomUser,Group
from .forms import CustomUserChangeForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# POST
class IndexViews(ListView):
    template_name = 'index.html'
    queryset = Post.objects.order_by('-posted_at')
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Post.objects.order_by('-posted_at')
        search_query = self.request.GET.get('search', '')
        if search_query:
             # キーワードをスペースで分割
            keywords = search_query.split()
            # 複数のキーワードで検索条件を作成
            query = Q()
            for keyword in keywords:
                query |= Q(title__icontains=keyword) | Q(text__icontains=keyword)
            queryset = queryset.filter(query)
        return queryset

class DetailView(DetailView):
    template_name='detail.html'
    model = Post
class MypageView(ListView):
    template_name='mypage.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = Post.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blogapp:index')  # 適切なリダイレクト先を設定してください
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

#User
class SignUpView(CreateView):
    form_class  = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('blogapp:signup_success')
    
    def form_valid(self,form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blogapp:mypage')  # プロフィールページにリダイレクト
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form': form})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogapp:mypage')
    def delete(self,request,*args,**kwargs):
        return super(request,*args,**kwargs)

def user_posts_and_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = Post.objects.filter(user=user)
    paginator = Paginator(posts, 10) 
    page = request.GET.get('page')
    
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        # ページが整数でない場合は最初のページを返す
        post_page = paginator.page(1)
    except EmptyPage:
        # ページが空の場合は最後のページを返す
        post_page = paginator.page(paginator.num_pages)
    
    context = {
        'user_name': user,
        'posts': post_page,
    }
    
    return render(request, 'user_posts_and_profile.html', context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('some_error_page')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogapp:user_posts_and_profile', user_id=request.user.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'edit_post.html', context)

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blogapp:group_list')  # 適切なリダイレクト先を設定してください
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})

class GroupList(ListView):
    template_name = 'group.html'
    queryset = Group.objects.order_by('-posted_at')
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Group.objects.order_by('-posted_at')
        search_query = self.request.GET.get('search', '')
        if search_query:
             # キーワードをスペースで分割
            keywords = search_query.split()
            # 複数のキーワードで検索条件を作成
            query = Q()
            for keyword in keywords:
                query |= Q(title__icontains=keyword) | Q(text__icontains=keyword)
            queryset = queryset.filter(query)
        return queryset

def user_group_and_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    groups = Group.objects.filter(user=user)
    paginator = Paginator(groups, 10) 
    page = request.GET.get('page')
    try:
        groups_page = paginator.page(page)
    except PageNotAnInteger:
        # ページが整数でない場合は最初のページを返す
        groups_page = paginator.page(1)
    except EmptyPage:
        # ページが空の場合は最後のページを返す
        groups_page = paginator.page(paginator.num_pages)
    
    context = {
        'user_name': user,
        'groups': groups_page,
    }
    
    return render(request, 'user_groups_and_profile.html', context)

class MypageGroupView(ListView):
    template_name='mypage-group.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = Group.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group_delete.html'
    success_url = reverse_lazy('blogapp:mypage-group')
    def delete(self,request,*args,**kwargs):
        return super(request,*args,**kwargs)