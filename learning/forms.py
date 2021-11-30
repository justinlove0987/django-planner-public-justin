from django import forms
from .models import Learning


class LearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = ["learning_name", "total_unit",
                  "total_progress", "every_day_to_do_unit"]



    def __init__(self, *args, **kwargs):
        super(LearningForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "classic-input"

