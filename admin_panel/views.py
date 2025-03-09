from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from blog.models import Article, ArticleCategory, ArticleComment
from blog.forms import ArticleForm, ArticleCategoryForm, ArticleCommentFormAdmin
from utils.my_decoretors import permission_checker_decorator_factory
# Create your views here.


@permission_checker_decorator_factory({'permission': 'admin_index'})
def index(request: HttpRequest):
    return render(request, 'admin_panel/home/index.html')


@method_decorator(permission_checker_decorator_factory({'permission': 'article_list'}), name='dispatch')
class ArticleListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'admin_panel/blog/article_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected__categories__url__title__iexact=category_name)
        return query


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin_panel/blog/edit_articles.html'
    success_url = reverse_lazy('admin_articles')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        return super().form_valid(form)


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleAdd(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin_panel/blog/add_articles.html'
    success_url = reverse_lazy('admin_add_articles')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'admin_panel/blog/article_list.html'
    success_url = reverse_lazy('admin_articles')


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleCategoryAdmin(ListView):
    model = ArticleCategory
    paginate_by = 12
    template_name = 'admin_panel/blog/article_cat_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleCategoryAdmin, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticleCategoryAdmin, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected__categories__url__title__iexact=category_name)
        return query


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleCatUpdateView(UpdateView):
    model = ArticleCategory
    form_class = ArticleCategoryForm
    template_name = 'admin_panel/blog/edit_cat_article.html'
    success_url = reverse_lazy('admin_articles_category')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        return super().form_valid(form)


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class ArticleCommentAdmin(ListView):
    model = ArticleComment
    form_class = ArticleCommentFormAdmin
    template_name = 'admin_panel/blog/comment_list.html'
    success_url = reverse_lazy('admin_articles_comment')

    def get_queryset(self):
        query = super(ArticleCommentAdmin, self).get_queryset()
        status = self.request.GET.get('status')
        article_id = self.request.GET.get('article')

        if status:
            query = query.filter(status=status)
        if article_id:
            query = query.filter(article__id=article_id)

        return query.order_by('-create_date')


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class CommentDelete(DeleteView):
    model = ArticleComment
    template_name = 'admin_panel/blog/comment_list.html'
    success_url = reverse_lazy('admin_articles_comment')


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class CommentUpdateView(UpdateView):
    model = ArticleComment
    form_class = ArticleCommentFormAdmin
    template_name = 'admin_panel/blog/edit_comment.html'
    success_url = reverse_lazy('admin_articles_comment')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        return super().form_valid(form)


@method_decorator(permission_checker_decorator_factory(), name='dispatch')
class CommentAdd(CreateView):
    model = ArticleComment
    form_class = ArticleCommentFormAdmin
    template_name = 'admin_panel/blog/add_comment.html'
    success_url = reverse_lazy('admin_articles_comment')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        return super().form_valid(form)
