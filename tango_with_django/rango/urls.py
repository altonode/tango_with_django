from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from tango_with_django.rango import views

app_name = 'rango'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^add_category/$', login_required(views.AddCategoryView.as_view()),
        name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.ShowCategoryView.as_view(), name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        login_required(views.AddPageView.as_view()), name='add_page'),
    url(r'^restricted/$', login_required(views.RestrictedView.as_view()),
        name='restricted' ),
    url(r'^search/$', login_required(views.PageSearchView.as_view()), 
		name='search'),
    url(r'^goto/$', views.TrackUrlView.as_view(), name='goto'),
    url(r'^register_profile/$', login_required(views.RegisterProfile.as_view()),
        name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^like/$', views.like_category, name='like_category'),
    url(r'^suggest/$', views.suggest_category, name='suggest_category'),
    url(r'^add/$', views.auto_add_page, name='auto_add_page')
]
