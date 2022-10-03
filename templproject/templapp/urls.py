from django.urls import path
from templapp import views

# SET UP TEMPLATE TAGGING!!
# django will automatically look for app_name
# tells django to look into templapp and find the urls that match
app_name = "templapp"

urlpatterns = [
    path("other", views.other, name="other"),
    path("relative", views.relative, name="relative"),
    path("base", views.base, name="base"),
    path("inheriting",views.inheriting, name="inheriting"),
    path("index_inheriting",views.index_inheriting, name="index_inheriting"),
    path("index_filter",views.index_filter, name="index_filter"),
]