from django import forms

from myapp.models import Activity,ScoreLabel
from user.models import ActivityStudents


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        widgets = {
            "score_label": forms.Select(attrs={"class": "form-control","id":"dateInput"}),
        }
        

class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()

class ActivityStudentJoinForm(forms.ModelForm):
    is_get_print = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((False, '未收到'), (True, '收到')),
        widget=forms.RadioSelect(attrs={"class": "is-get-print"}),
        initial='False',
    )
    is_checked = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((False, '待審'), (True, '審畢')),
        widget=forms.RadioSelect(attrs={"class": "is-checked"}),
        initial='False',
    )
    class Meta:
        model = ActivityStudents
        fields = ["is_get_print", "is_checked", "checked_number"]
        
        widgets={
            "checked_number": forms.NumberInput(attrs={"class": "form-control, checked-number-input"}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        is_checked = cleaned_data.get("is_checked")
        checked_number = cleaned_data.get("checked_number")
        if is_checked and not checked_number:
            raise forms.ValidationError("請輸入審核編號")
        return cleaned_data

StudentFormSet = forms.modelformset_factory(ActivityStudents, form=ActivityStudentJoinForm, extra=0)


class ScoreLabelForm(forms.ModelForm):
    class Meta:
        model = ScoreLabel
        fields = "__all__"
        widgets = {
            "label": forms.TextInput(attrs={"class": "form-control"}),
            "score1": forms.NumberInput(attrs={"class": "form-control"}),
            "score2": forms.NumberInput(attrs={"class": "form-control"}),
            "score3": forms.NumberInput(attrs={"class": "form-control"}),
        }