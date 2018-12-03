from django.urls import path, re_path
from cmdb import api, idc, asset, group, cabinet


urlpatterns = [
    path('asset/', asset.asset, name='cmdb'),
    path('asset/add/', asset.asset_add, name='asset_add'),
    path('asset/del/', asset.asset_del, name='asset_del'),
    re_path(r'^asset/edit/(?P<ids>\d+)/$', asset.asset_edit, name='asset_edit'),
    re_path(r'^asset/detail/(?P<ids>\d+)/$', asset.server_detail, name='server_detail'),
    #path('asset/save/', asset.asset_save, name='asset_save'),
    path('group/', group.group, name='group'),
    path('group/add/', group.group_add, name='group_add'),
    path('group/del/', group.group_del, name='group_del'),
    re_path(r'^group/server_list/(?P<group_id>\d+)/$', group.server_list, name='group_server_list'),
    re_path(r'^group/edit/(?P<group_id>\d+)/$', group.group_edit, name='group_edit'),
    # path('group/save/', group.group_save, name='group_save'),
    path('cabinet/', cabinet.cabinet, name='cabinet'),
    path('cabinet/del/', cabinet.cabinet_del, name='cabinet_del'),
    path('cabinet/add/', cabinet.cabinet_add, name='cabinet_add'),
    re_path(r'^cabinet/server_list/(?P<cabinet_id>\d+)/$', cabinet.server_list, name='cabinet_server_list'),
    re_path(r'^cabinet/edit/(?P<cabinet_id>\d+)/$', cabinet.cabinet_edit, name='cabinet_edit'),
    path('idc/', idc.idc, name='idc'),
    path('idc/add/', idc.idc_add, name='idc_add'),
    path('idc/del/', idc.idc_del, name='idc_del'),
    re_path(r'^idc/edit/(?P<idc_id>\d+)/$', idc.idc_edit, name='idc_edit'),
    re_path(r'^idc/cabinetlist/(?P<idc_id>\d+)/$', idc.cabinet_list, name='idc_cabinet_list'),
    path('collect', api.collect, name='update_api'),
    path('get/host/', api.get_host, name='get_host'),
    path('get/group/', api.get_group, name='get_group'),
]
