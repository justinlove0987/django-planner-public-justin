from django import forms
from .models import Account


class RegistreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
    }))

    class Meta:
        model = Account
        fields = ["email","password"]

    def __init__(self, *args, **kwargs):
        super(RegistreationForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "classic-input"

