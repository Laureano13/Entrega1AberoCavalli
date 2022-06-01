from django.urls import path
from FoodTaster import views

app_name='FoodTaster'
urlpatterns = [
    path('', views.index, name='home'),
    path('dish', views.dish, name='dish'),

    path('dishes', views.dishListView.as_view(), name='dish-list'),
    path('dish/add/', views.dishCreateView.as_view(), name='dish-add'),
    
    path('dish/<int:pk>/detail', views.dishDetailView.as_view(), name='dish-detail'),
    path('dish/<int:pk>/update', views.dishUpdateView.as_view(), name='dish-update'),
    path('dish/<int:pk>/delete', views.dishDeleteView.as_view(), name='dish-delete'),

    path('formHTML', views.form_hmtl),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),

]