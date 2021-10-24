from django.urls import path
from .views import home, todo_list, todo_update, todo_delete

urlpatterns = [
    path('', home, name='home'),
    path('list/', todo_list, name='list'),
    path('<int:id>/update/', todo_update, name='update'),
    path('<int:id>/delete/', todo_delete, name='delete'),
]