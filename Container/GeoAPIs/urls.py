from django.urls import path
from GeoAPIs import views

urlpatterns = [
    # path(r'^typeProducer$', views.type_producer_list),
    # path(r'^typeProducer/([0-9]+)$', views.type_producer_list)
    path('typeProducer/', views.type_producer_list, name='type_producer_list'),
    # path('typeProducer/<int:pk>/', views.type_producer_detail, name='type_producer_detail'),
    # path('userProducer/', views.user_producer_list, name='user_producer_list'),
    # path('userProducer/<int:pk>/', views.user_producer_detail, name='user_producer_detail'),
]
