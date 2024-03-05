# forms.py
from django import forms

from user.models import Student
from .models import *
from user.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        # 設定css
        labels = {
            "username": "姓名",
            "email": "電子郵件地址e-mail",
            "password": "密碼",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        exclude = ["user", "activity"]
        # 設定css
        labels = {
            "sex": "性別",
            "date_of_birth": "出生年月日",
            "phone": "電話",
            "address": "地址",
            "postal_code": "郵遞區號",
            "identity": "身分證字號",
            "home_phone": "家用電話",
            "mobile_phone": "手機",
            "graduated_school": "畢業學校",
            "is_graduated": "畢肄業",
            "graduated_department": "畢業部別",
            "graduated_year": "年制",
            "education": "學歷",
            "school_department": "畢業系所組",
            "emergency_contact": "緊急聯絡人",
            "emergency_contact_phone": "緊急聯絡人電話",
            "emergency_contact_relationship": "緊急聯絡人關係",
            "service_years": "服役年資",
            "military_service_number": "兵籍號碼",
            "military_service": "軍種",
            "military_rank": "階級",
            "military_retired_date": "退伍日期",
            "military_service_years": "服役年資",
            "identity_front": "身分證正面",
            "identity_back": "身分證反面",
        }
        widgets = {
            "sex": forms.Select(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "identity": forms.TextInput(attrs={"class": "form-control"}),
            "home_phone": forms.TextInput(attrs={"class": "form-control"}),
            "graduated_school": forms.Select(attrs={"class": "form-control"}),
            "is_graduated": forms.Select(attrs={"class": "form-control"}),
            "graduated_department": forms.Select(attrs={"class": "form-control"}),
            "graduated_year": forms.Select(attrs={"class": "form-control"}),
            "education": forms.Select(attrs={"class": "form-control"}),
            "school_department": forms.TextInput(attrs={"class": "form-control"}),
            "mobile_phone": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact_phone": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact_relationship": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "service_years": forms.Select(attrs={"class": "form-control"}),
            "education": forms.Select(attrs={"class": "form-control"}),
            "military_service_number": forms.TextInput(attrs={"class": "form-control"}),
            "military_service": forms.TextInput(attrs={"class": "form-control"}),
            "military_rank": forms.TextInput(attrs={"class": "form-control"}),
            "military_retired_date": forms.DateInput(attrs={"class": "form-control"}),
            "military_service_years": forms.Select(attrs={"class": "form-control"}),
            "identity_front": forms.FileInput(attrs={"class": "form-control"}),
            "identity_back": forms.FileInput(attrs={"class": "form-control"}),
        }
