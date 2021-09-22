from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Newsblog
# Create your views here.
def news(request):
    article = Newsblog.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(article, 9)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        'articles': paged_articles
    }

    return render(request, 'newsblog/newsblog.html', context)

def article(request, news_id):
    article = get_list_or_404(Newsblog, pk=news_id)
    context = {
        'article': article
    }
    return render(request, 'newsblog/article.html', context)