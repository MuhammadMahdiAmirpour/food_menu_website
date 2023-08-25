from . import views
from django.urls import path

app_name = "food_menu"
urlpatterns = [
#     path('', views.index, name='index'),
    path('', views.IndexClassView.as_view(), name='index'),
#     path('<int:item_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.Item, name='item'),
    # for adding items
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # for editing items
    path('edit/<int:pk>', views.EditItem.as_view(), name='edit_item'),
    # for deleting items
    path('delete/<int:pk>', views.DeleteItem.as_view(), name='delete_item'),
]
