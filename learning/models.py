from django.db import models
from accounts.models import Account


class LearningGroup(models.Model):
    group_order = models.IntegerField(null=True)
    group_name = models.CharField(max_length=100, null=True)
    group_task_order = models.IntegerField(null=True)
    def __str__(self) -> str:
        return self.group_name

class Learning(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    learning_name = models.CharField(max_length=100)
    total_unit = models.IntegerField()
    total_progress = models.IntegerField(default=0)
    left_day = models.IntegerField()
    every_day_to_do_unit = models.IntegerField()
    completed_date = models.DateTimeField()

    group = models.ForeignKey(LearningGroup, null=True, on_delete=models.CASCADE)

    def get_total_progress(self):
        learning_details = self.learningdetail_set.all()
        total_progress = self.total_progress
        for learning_detail in learning_details:
            total_progress += learning_detail.day_progress
        return total_progress

    def get_remaining_unit(self):
        return self.total_unit - self.get_total_progress()

    def get_progress_percentage(self):
        return int((self.get_total_progress() / self.total_unit)*100)
    
    def get_complete_status(self):
        learning_details = self.learningdetail_set.all()
        for learning_detail in learning_details:
            if learning_detail.day_progress != learning_detail.day_unit:
                return False
        return True

    
    def __str__(self) -> str:
        return self.learning_name


class LearningDetail(models.Model):
    learning = models.ForeignKey(Learning, null=True, on_delete=models.CASCADE)
    day_unit = models.IntegerField()
    day_progress = models.IntegerField(default=0)
    expired_datetime = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def get_day_percentage(self):
        return int((self.day_progress / self.day_unit)*100)
    
    def get_complete_status(self):
        if self.day_progress == self.day_unit:
            return True
        return False
    
    def get_remaining_unit(self):
        return self.day_unit - self.day_progress

    
    def __str__(self) -> str:
        return self.learning.learning_name
        




