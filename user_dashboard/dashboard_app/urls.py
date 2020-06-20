from django.urls import path
from . import views as db_views

urlpatterns =[
    path('',db_views.home,name="home"),
    path('dashboard/',db_views.dashboard, name="dashboard"),
    path('users/edit/', db_views.profile, name="profile"),
    path('users/edit/update_info/', db_views.update_info, name="update_info"),
    path('users/edit/update_description/', db_views.update_description, name="update_description"),
    path('users/edit/update_password/', db_views.update_password, name="update_password"),
    path('users/new/', db_views.new_user, name="new_user"),
    path('users/edit/<int:user_id>/', db_views.edit_user, name="edit_user"),
    path('users/edit/<int:user_id>/info/', db_views.edit_user_info, name="edit_user_info"),
    path('users/edit/<int:user_id>/password/', db_views.edit_user_password, name="edit_user_password"),
    path('users/show/<int:user_id>/', db_views.message_board, name="message_board"),
    path('users/show/<int:user_id>/post/', db_views.make_post, name="make_post"),
    path('users/show/<int:post_id>/comment/', db_views.make_comment, name="make_comment"),
    


]