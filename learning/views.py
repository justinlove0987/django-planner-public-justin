import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Learning, LearningDetail, LearningGroup
from .forms import LearningForm
import json

def count_completed_date(left_unit, everyday_to_do_unit):
    last_day_unit = (left_unit % everyday_to_do_unit)
    spent_days = (left_unit // everyday_to_do_unit)

    today_date = datetime.date.today()
    today_datetime = datetime.datetime(
        today_date.year, today_date.month, today_date.day, 23, 59)

    if last_day_unit != 0:
        spent_days += 1

    completed_date = today_datetime + datetime.timedelta(days=spent_days)

    return completed_date


def count_remaining_days(left_unit, everyday_to_do_unit):
    last_day_unit = (left_unit % everyday_to_do_unit)
    remaining_days = (left_unit // everyday_to_do_unit)

    if last_day_unit != 0:
        remaining_days += 1

    return remaining_days

def create_learning_detail(learning, left_unit, everyday_to_do_unit):
    last_day_unit = (left_unit % everyday_to_do_unit)
    spent_days = (left_unit // everyday_to_do_unit)

    if last_day_unit != 0:
        spent_days += 1

    today = datetime.datetime.today()
    expired_datetime = datetime.datetime(today.year, today.month, today.day, 23, 59, 0)

    # create days for adding learningDetial
    if last_day_unit != 0:
        days = spent_days - 1
    else:
        days = spent_days

    for _ in range(days):
        LearningDetail.objects.create(learning=learning, expired_datetime=expired_datetime,day_unit=everyday_to_do_unit)
        expired_datetime = expired_datetime + datetime.timedelta(days=1)
    
    if last_day_unit:
        LearningDetail.objects.create(learning=learning,expired_datetime=expired_datetime, day_unit=last_day_unit)


@login_required(login_url="login")
def create_plan(request):
    form = LearningForm()

    context = {
        "form": form,
    }

    return render(request, "learning/create_plan.html", context)


def calculate_complete_date(request):
    body = json.loads(request.body)
    learning_name = body["learning_name"]
    total_unit = int(body["total_unit"])
    total_progress = int(body["total_progress"])
    every_day_to_do_unit = int(body["every_day_to_do_unit"])

    remaining_unit = total_unit - total_progress
    remaining_days = count_remaining_days(remaining_unit, every_day_to_do_unit)
    completed_date = count_completed_date(remaining_unit, every_day_to_do_unit)

    learning = Learning.objects.create(
                                    user_id = request.user.id,
                                    learning_name=learning_name,
                                    total_unit=total_unit,
                                    total_progress=total_progress,
                                    left_day=remaining_days,
                                    every_day_to_do_unit=every_day_to_do_unit,
                                    completed_date=completed_date,
                                    )
    create_learning_detail(learning, remaining_unit, every_day_to_do_unit)

    data = {}

    return JsonResponse(data)

# ProgressBar Function
def change_unit(request):   
    body = json.loads(request.body)    
    current_day_progress = body["current_day_progress"]
    learning_detail_id = body["learning_detail_id"]

    learning_detail = LearningDetail.objects.get(id=learning_detail_id)
    learning_detail.day_progress = int(current_day_progress)
    learning_detail.save()
    
    data = {
        "day_percentage": learning_detail.get_day_percentage()
        }
    return JsonResponse(data)





@login_required(login_url="login")
def schedule(request):
    learning_items = Learning.objects.filter(user_id=request.user.id).order_by("group__group_order","group__group_task_order")
    
    group_items = {}
    learning_name_in_group = []
    learning_names = []

    for learning_item in learning_items:
        if learning_item.group != None:
            group_order = learning_item.group.group_order
            group_name = learning_item.group.group_name
            
            learning_name_in_group.append(learning_item.learning_name)

            if group_order in group_items:
                group_items[group_order][group_name].append(learning_item.learning_name)
            else:
                group_items[group_order] = {group_name: [learning_item.learning_name]}
    

    for learning in learning_items:
        if learning.learning_name not in learning_name_in_group:
            learning_names.append(learning.learning_name)
    

    context = {
        "learning_items": learning_items,
        "group_items": group_items,
        "learning_names": learning_names
    }

    return render(request, "learning/schedule.html", context)


def set_group(request):
    body = json.loads(request.body)

    for group_order, groups in body["group_items"].items():
        for group_name,learning_name_lst in groups.items():
            for group_task_order, learning_name in enumerate(learning_name_lst):
                learning = Learning.objects.get(user_id=request.user.id,learning_name=learning_name)
                group = learning.group
                
                if group != None:
                    learning.group.group_name = group_name
                    learning.group.group_order = group_order
                    learning.group.group_task_order = group_task_order
                    learning.save()
                    learning.group.save()
                else:
                    group = LearningGroup.objects.create(
                        group_name= group_name,
                        group_order = group_order,
                        group_task_order = group_task_order
                    )

                    learning.group = group
                    learning.save()
                    learning.group.save()

    data = {}
    return JsonResponse(data)

def onchange_group_name(request):
    body = json.loads(request.body)
    group_order = body["group_order"]
    group_name = body["group_name"]

    learnings = Learning.objects.filter(group__group_order=group_order)

    for learning in learnings:
        learning.group.group_name = group_name
        learning.group.save()

    data = {}
    return JsonResponse(data)

# Learning Detail

def learning_detail(request, learning_id):
    learning_detail_items = Learning.objects.get(id=learning_id).learningdetail_set.all()

    context = {
        "learning_id": learning_id,
        "learning_detail_items": learning_detail_items
    }
    
    return render(request, "learning/learning_detail.html", context)

def execute_detail_learning(request):
    body = json.loads(request.body)
    learning_detail_id = body["learningDetailID"]

    learning_detail = LearningDetail.objects.get(id=learning_detail_id)
    learning_detail.day_progress = learning_detail.day_unit
    learning_detail.save()

    data = {
        "day_progress":learning_detail.day_progress,
        "remaining_unit":learning_detail.get_remaining_unit()
        }
    
    return JsonResponse(data)


def get_learning_name_lst(request):
    body = json.loads(request.body)

    learning_name_lst = []
    learnings = Learning.objects.filter(user_id=request.user.id)

    for learning in learnings:
        learning_name_lst.append(learning.learning_name)
    
    data = {"learning_name_lst": learning_name_lst}

    return JsonResponse(data)



# def input_date_and_show_unit(request):
#     body = json.loads(request.body)
#     onchange_date_string = body["date"] + "-23-59-00"
#     learning_id = body["learning_id"]
#     onchange_datetime = datetime.datetime.strptime(onchange_date_string, "%Y-%m-%d-%H-%M-%S")
#     learning = Learning.objects.get(id=learning_id)

#     try:
#         learning_detail_item = LearningDetail.objects.get(learning=learning, expired_datetime=onchange_datetime)
#         learning_detail_every_day_unit = learning_detail_item.day_unit
#     except LearningDetail.DoesNotExist:
#         learning_detail_every_day_unit = None

#     data = {
#         "every_day_unit": learning_detail_every_day_unit,
#     }

#     return JsonResponse(data)


