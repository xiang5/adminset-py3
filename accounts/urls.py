from django.urls import path, re_path
#from accounts import user, role, permission, gldap
from accounts import user, role, permission


urlpatterns = [
    # path('', user.user_list, name='accounts'),
    path('login/', user.login, name='login'),
    path('logout/', user.logout, name='logout'),
    path('user/list/', user.user_list, name='user_list'),
    path('user/add/', user.user_add, name='user_add'),
    re_path(r'^user/delete/(?P<ids>\d+)/$', user.user_del, name='user_del'),
    re_path(r'^user/edit/(?P<ids>\d+)/$', user.user_edit, name='user_edit'),
    re_path(r'^reset/password/(?P<ids>\d+)/$', user.reset_password, name='reset_password'),
    path('change/password/', user.change_password, name='change_password'),
    path('change/ldap/password/', user.change_ldap, name='change_ldap_password'),
    path('role/add/', role.role_add, name='role_add'),
    path('role/list/', role.role_list, name='role_list'),
    re_path(r'^role/edit/(?P<ids>\d+)/$', role.role_edit, name='role_edit'),
    re_path(r'^role/delete/(?P<ids>\d+)/$', role.role_del, name='role_del'),
    path('permission/deny/', permission.permission_deny, name='permission_deny'),
    path('permission/add/', permission.permission_add, name='permission_add'),
    path('permission/list/', permission.permission_list, name='permission_list'),
    re_path(r'^permission/edit/(?P<ids>\d+)/$', permission.permission_edit, name='permission_edit'),
    re_path(r'^permission/delete/(?P<ids>\d+)/$', permission.permission_del, name='permission_del'),
    path('permission/user_permission/', permission.get_user_permission, name='get_user_permission'),
]
