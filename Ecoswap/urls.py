from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import user_add_item
from django.conf import settings
from django.conf.urls.static import static
from .views import submit_query

urlpatterns = [
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('approve/<int:item_id>/', views.approve_item, name='approve_item'),
    path('user_dashboard/add_item/', user_add_item, name='user_add_item'),
    path('login/', views.login_view, name='login'),
    path('items/', views.item_list, name='item_list'),
    path('', views.welcome, name='home'),
    path('my_items/', views.my_items, name='my_items'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('profile/', views.profile_view, name='profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('registration/register/', views.register, name='register'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('login/redirect/', views.login_redirect, name='login_redirect'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path("manage_items/", views.manage_items, name="manage_items"),
    path('admin_dashboard/manage_user/', views.manage_user, name='manage_user'),
    path('admin_dashboard/manage_items/', views.manage_items, name='manage_items'),
    path('admin_dashboard/settings/', views.settings_view, name='admin_settings'),
    path('admin_dashboard/logistic/', views.logistic_view, name='admin_logistic'),
    path('logistic/', views.logistic_view, name='logistic_dashboard'),
    path('add_user/', views.add_user, name='add_user'),
    path('settings/', views.settings_view, name='settings'), 
    path('welcome/', views.welcome, name='welcome'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user/<int:id>/', views.user_details, name='user_details'), 
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('add_item/', views.add_item, name='add_item'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("approve/<int:item_id>/", views.approve_item, name="approve_item"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path('item/donate/<int:item_id>/', views.donate_item, name='donate_item'),
    path('item/trade/<int:item_id>/', views.trade_item, name='trade_item'),
    path('chat/', views.message_view, name='chat_user'),
    path('user_add_item/', views.user_add_item, name='user_add_item'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('submit-query/', submit_query, name='submit_query'),
    path('trading/', views.trade_item_view, name='trading'),
    path('donation/', views.donation_view, name='donation'),   
    path('donation/<int:item_id>/', views.donation_view, name='donation'), 
    path('search/', views.search_items, name='search_items'),
    path('filter/', views.filter_items, name='filter_items'),
    path('chat/<int:user_id>/', views.message_view, name='chat_user'),
    path('export_users/', views.export_users_excel, name='export_users'),
    path('export_items/', views.export_items_excel, name='export_items'),
    path('donation_requests/', views.donation_requests, name='donate_requests'),
    path('my_donations/', views.my_donations, name='my_donations'),
    path('donation_requests/approve/<int:request_id>/', views.approve_donation, name='approve_donation'),
    path('donation_requests/decline/<int:request_id>/', views.decline_donation, name='decline_donation'),
    path('export-donations/', views.export_donations, name='export_donations'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)