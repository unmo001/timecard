from django import forms

from registration.models import CommutingTime


class TimeForm(forms.Form):
    class Meta:
        model = CommutingTime
        fields = ()
        widgets = {

        }
