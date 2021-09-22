from django.shortcuts import render
from newsblog.models import Newsblog
from studyblog.models import Studyblog
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    subjects = Studyblog.objects.order_by('-list_date').filter(is_published=True)[:3]
    articles = Newsblog.objects.order_by('list_date').filter(is_published=True)[:3]
    context = {
        'subjects': subjects,
        'articles': articles
    }
    return render(request, 'simpleblog/index.html', context)

def about(request):
    self = 'self'
    context = {
        'self': self,
    }
    return render(request, 'simpleblog/about.html', context)

def blogs(request):
    subjects = Studyblog.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(subjects, 3)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'subjects': paged_articles,
    }
    return render(request, 'simpleblog/blog.html', context)