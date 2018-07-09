from django.urls import path
from catalog.views import (
    articles_list, articles_detail
)

urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('<slug:id>/', articles_detail, name='articles_detail'),
    # path('archive/<int:year>', some_view)  # in case we want to add archive by year
]
