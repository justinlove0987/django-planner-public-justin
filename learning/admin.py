from django.contrib import admin
from .models import Learning, LearningDetail, LearningGroup


class LearningDetailAdmin(admin.ModelAdmin):
    list_display = ["learning","expired_datetime"]

class LearningGroupAdmin(admin.ModelAdmin):
    list_display = ["group_name",]

admin.site.register(Learning)
admin.site.register(LearningDetail, LearningDetailAdmin)
admin.site.register(LearningGroup,LearningGroupAdmin)
