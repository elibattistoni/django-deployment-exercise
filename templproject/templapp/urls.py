from django.urls import path
from templapp import views

# SET UP TEMPLATE TAGGING!!
# django will automatically look for app_name
# tells django to look into templapp and find the urls that match
app_name = "templapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("filter", views.filter_example, name="filter_example"),
]