import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from learning.models import Learning, LearningDetail
import json


def get_today_learning_progress_unit(learning_items):
    today_date = datetime.date.today()
    learning_detail_lst = []

    for learning_item in learning_items:
        
        learning_details = learning_item.learningdetail_set.all()
        for learning_detail in learning_details:
            expired_date = datetime.date(learning_detail.expired_datetime.year,
                                         learning_detail.expired_datetime.month, 
                                         learning_detail.expired_datetime.day)
            if today_date == expired_date:
                learning_detail_lst.append(learning_detail)

    return learning_detail_lst


def introduction(request):
    return render(request, "introduction.html")


def portfolio(request):
    return render(request, "portfolio.html")


@login_required(login_url="login")
def home(request):
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    learning_items = Learning.objects.filter(user_id=request.user.id)
    learning_detail_items = LearningDetail.objects.filter(learning__user_id=request.user.id)
    today_learning_detail_items = get_today_learning_progress_unit(learning_items)
    
    context = {
        "today_date": today_date,
        "learning_items": learning_items,
        "learning_detail_items": learning_detail_items,
        "today_learning_detail_items": today_learning_detail_items,
    }

    return render(request, "home.html", context)

def search_learning_detail(request):
    body = json.loads(request.body)
    input_date_str = body["inputDate"]
    input_date =  datetime.datetime.strptime(input_date_str, '%Y-%m-%d').date()
    learning_details = LearningDetail.objects.filter(learning__user_id=request.user.id)
    learning_data = []

    for learning_detail in learning_details:
        date = learning_detail.expired_datetime.date()
        if input_date == date:
            learning_data.append({
                "learning_detail_id": learning_detail.id,
                "learning_name":learning_detail.learning.learning_name,"learning_detail_day_percentage":learning_detail.get_day_percentage(),
                "learning_detail_day_progress":learning_detail.day_progress,
                "learning_detail_day_unit":learning_detail.day_unit})

    data = {"learning_data":learning_data}

    return JsonResponse(data) 