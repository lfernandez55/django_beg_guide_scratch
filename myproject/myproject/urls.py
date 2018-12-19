"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from boards import views

urlpatterns = [
    #path(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
    # path('boards/', views.home, name='home'),
    path('', views.home, name='home'),
    #url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    #path('<int:question_id>/results/', views.results, name='results'),
]

#From codeanywhere weber gmail githut
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('<int:foo_id>/foo/', views.foo, name='foo'),
#     path('foolistview/', views.FooListView.as_view(), name='foolist'),
#     path('<int:pk>/foodetailview/', views.FooDetailView.as_view(), name='foodetail'),
#     path('<int:question_id>/baz/', views.baz, name='baz'),
#     path('baz2/', views.baz2, name='baz2_nickname'),
#     path('users/',views.users, name='users'),
#     path('userlistview/',views.UserListView.as_view(), name='userlist'),
#     path('emails/',views.emails,name='emails'),
#     path('employees/',views.employees,name='employees'),
# ]
