from django.urls import path 
from user_data import views


urlpatterns = [
    

    path('',views.index,name='index'),
    path('user',views.user,name='user'),
    path('delete/<int:id>',views.destroy,name='update'),
    path('update/<int:id>',views.update,name='update'),
    path('user_login',views.user_login,name='login'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('log_out',views.log_out,name="log_out")
    
    
    
    
    
    

    
]