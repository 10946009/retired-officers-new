from django import forms

from myapp.models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()
