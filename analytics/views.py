from django.shortcuts import render
from learning.models import Learning
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import datetime

# Create your views here.
@login_required(login_url="login")
def analytics(request):
    learnings = Learning.objects.filter(user_id=request.user.id)

    context = {
        "learnings": learnings,
    }
    return render(request, "analytics/analytics.html", context)


def update_chart(request):
    body = json.loads(request.body)
    left_date = body["leftDate"]
    right_date = body["rightDate"]
    learning_name = body["learning_name"]
    week_date_range = []
    learning_date_range = {}

    left_date = datetime.datetime.strptime(left_date,"%Y/%m/%d")
    right_date = datetime.datetime.strptime(right_date,"%Y/%m/%d")

    for i in range(7):
        day = left_date + datetime.timedelta(days=i)
        week_date_range.append(day.date())

    learning = Learning.objects.get(user_id=request.user.id,learning_name=learning_name)
    learning_details = learning.learningdetail_set.all().order_by("expired_datetime")

    date_progresses = {}

    for learning_detail in learning_details:
        learning_date = learning_detail.expired_datetime.date()
        learning_date_range[learning_date] = learning_detail.day_progress
    

    for week_date in week_date_range:
        date_string = week_date.strftime("%Y/%m/%d")
        if week_date in learning_date_range:
            date_progresses[date_string] = learning_date_range[week_date]
        else:
            date_progresses[date_string] = None

    print(date_progresses)
    
    data = {"date_progresses": date_progresses}
    return JsonResponse(data)