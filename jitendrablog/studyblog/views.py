from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Studyblog
# Create your views here.
def study(request):
    subjects = Studyblog.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(subjects, 3)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'subjects': paged_articles,
    }
    return render(request, 'simpleblog/blog.html', context)

def article(request, study_id):
    subject = get_list_or_404(Studyblog, pk=study_id)
    context = {
        'subject': subject,
    }
    return render(request, 'studyblog/article.html', context)