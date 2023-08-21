from . import views
from django.urls import path

app_name = "food_menu"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.Item, name='item'),
    # for adding items
    path('add/', views.create_item, name='create_item'),
    # for editing items
    path('edit/<int:id>', views.edit_item, name='edit_item'),
    # for deleting items
    path('delete/<int:item_id>', views.delete_item, name='delete_item'),
]
