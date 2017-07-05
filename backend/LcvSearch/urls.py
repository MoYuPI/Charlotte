from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import SearchSuggest, SearchView, IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="searchindex"),

    url(r'^suggest/$', SearchSuggest.as_view(), name="suggest"),

    url(r'^search/$', SearchView.as_view(), name="lcvsearch"),
]
