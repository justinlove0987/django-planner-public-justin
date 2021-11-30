from django.urls import path
from . import views

urlpatterns = [
    path("create_plan/", views.create_plan, name="create_plan"),
    path("calculate_complete_date", views.calculate_complete_date, name="calculate_complete_date"),
    path("learning_detail/<int:learning_id>/", views.learning_detail, name="learning_detail"),
    path("schedule/",views.schedule, name="schedule"),
    path("change_unit/",views.change_unit, name="change_unit"),
    path("set_group",views.set_group, name="set_group"),
    path("onchange_group_name",views.onchange_group_name, name="onchange_group_name"),
    path("get_learning_name_lst",views.get_learning_name_lst, name="get_learning_name_lst"),
    path("execute_detail_learning/", views.execute_detail_learning, name="execute_detail_learning"),
    # path("input_date_and_show_unit/", views.input_date_and_show_unit, name="input_date_and_show_unit"),
    # path("get_learning_name_lst",views.get_learning_name_lst, name="get_learning_name_lst"),
]
