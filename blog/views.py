from django.shortcuts import render, get_object_or_404
from blog.models import Article, ArticleComment
from django.views.generic import ListView, DetailView
from jalali_date import date2jalali, datetime2jalali


class ArticleListView(ListView):
    template_name = 'post.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 1

    def get_queryset(self):
        base_query = super(ArticleListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['data'] = date2jalali(self.request.user.date_joined)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'single_blog.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id,
                                                            parent=None).perfetch_related('articlecomment.set')
        return context
