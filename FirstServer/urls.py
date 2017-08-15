"""FirstServer URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from FirstServer import tests,tests1,mapshow,mapcanvas,md5encode,pyton_get_or_post,mysqlEx,mysql_table_show,tst_post,table_name_post,hplus_show,\
    mysql_index,upfile
from FirstServer.login import login
urlpatterns = [
    url(r'^login/', login.test,name='login'),
    url(r'^login_post/', login.loginJ,name='login_post'),
    url(r'^index/', mysql_index.test,name='index'),
    url(r'^blog/', tests.test,name='blog'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', tests1.test,name='test1'),
    url(r'^insert/', tests.insert,name='insert'),
    url(r'^get/', tests.get,name='get'),
    url(r'^insertArr/', tests.insertArr,name='insertArr'),
    url(r'^map/', mapshow.test,name='map'),
    url(r'^mapcanvas/', mapcanvas.test,name='mapcanvas'),
    url(r'^md5/', md5encode.test,name='md5'),
    url(r'^urlget/', pyton_get_or_post.test,name='urlget'),
    url(r'^urlpostp', pyton_get_or_post.testP,name='urlpostp'),
    url(r'^urlpost/', pyton_get_or_post.testPost,name='urlpost'),
    url(r'^tstpost/', tst_post.search_post,name='tstpost'),
    url(r'^mysql/', mysqlEx.show,name='mysqlEx'),
    url(r'^mysql_table/', mysql_table_show.show,name='mysql_table'),
    url(r'^table_name_post/', table_name_post.testPost,name='table_name_post'),
    url(r'^hplus/', hplus_show.test,name='hplus'),
    url(r'^upfile/', upfile.upload_file,name='upfile'),
]
