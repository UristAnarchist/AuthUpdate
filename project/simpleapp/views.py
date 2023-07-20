from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .filters import NewsFilter
from .forms import NewsForm

class NewssList(ListView):
    model = News
    ordering = '-date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class NewsDetail(DetailView):
    model = News
    text = News.text
    template_name = 'post.html'
    context_object_name = 'post'

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception = True
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
