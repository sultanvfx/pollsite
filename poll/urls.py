from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^login', views.fn_login_page, name='login_page'),
    # url(r'^auth', views.fn_auth_view),
    # # -------------------------------------------------------
    # url(r'^welcome', views.fn_welcome_page, name='welcome_page'),
    # url(r'^sorry', views.fn_sorry_page, name='sorry_page'),
    # url(r'^logout', views.fn_logout_page, name='logout_page'),
    # url(r'^session_expired', views.fn_session_expired, name='session_expired_page'),
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url(r'^$', views.index, name='poll_index_page'),  # 127:0:0:1:8000/polls
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),  # 127:0:0:1:8000/polls/0-9
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),  # 127:0:0:1:8000/polls/0-9/results
    url(r'^(?P<question_id>[0-9]+)/vote', views.vote, name='vote'),  # 127:0:0:1:8000/polls/0-9/results

    ]
