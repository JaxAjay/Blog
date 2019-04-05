from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,CreateView,
                                  UpdateView,ListView,DeleteView,DetailView)
from .models import Blog
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')

    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


class IndexView(TemplateView):
    template_name = 'index.html'

class BlogCreateView(CreateView):
    template_name = 'create.html'

    fields = ('author','title','description')
    model = Blog

class BlogListView(ListView):
    template_name = 'Bloglist.html'
    context_object_name = 'list'
    model = Blog

class BlogDetailView(DetailView):
    template_name = 'Blogdetail.html'
    context_object_name = 'detail'
    model = Blog

class UserLogin(LoginView):
    template_name = 'login.html'


class UserLogout(LogoutView):
    template_name = 'logout.html'

class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    fields = ('title', 'description')
    model = Blog

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('blog-list')