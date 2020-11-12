"""member URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import single_member,new_member,user_list,single_user,search_user,search_member

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/members/$',search_member.as_view()),
    url(r'^api/member/(?P<pk>[0-9]+)/$',single_member.as_view()),
    url(r'^api/member/new/$',new_member.as_view()),
    url(r'^api/users/$',search_user.as_view()),
    url(r'^api/user/new/$',user_list.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$',single_user.as_view())
]
