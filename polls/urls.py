from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    # /polls
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/question_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'choice'),
    url(r'^(?P<pk>[0-9]+)/result/$', views.ResultsView.as_view(), name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote')
]
