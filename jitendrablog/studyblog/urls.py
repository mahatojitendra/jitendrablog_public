from django.urls import path
from . import views
urlpatterns = [
    path('', views.study, name='study'),
    path('<int:study_id>', views.article, name='article'),
]