from django.urls import path
from GeoAPIs import views

urlpatterns = [
    path('userProducer/', views.user_producer_list, name='user_producer_list'),
    path('token/', views.CreateTokenView.as_view(), name='user_token'),
    path('userProducer/<int:pk>/', views.user_producer_detail,
         name='user_producer_detail'),
]
