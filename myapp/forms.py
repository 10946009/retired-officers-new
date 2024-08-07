# forms.py
from typing import Any
from django import forms

from user.models import Student
from .models import *
from user.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class UserForm(forms.ModelForm):
    password2 = forms.CharField(label="確認密碼", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["email", "password"]
        # 設定css
        labels = {
            "email": "電子郵件地址e-mail",
            "password": "密碼",
        }
        widgets = {
            
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}),
        }
        error_messages = {
            "email": {
                "required": "請輸入電子郵件地址",
                "invalid": "請輸入有效的電子郵件地址",
                "unique": "此電子郵件地址已被註冊過了",
            },
            "password": {
                "required": "請輸入密碼",
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            self.add_error("password2", "密碼和確認密碼不匹配")

        return cleaned_data

        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        # 設定css
        labels = {
            "username": "姓名",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }
        help_texts ={
            "username": None,
        } 



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        exclude = ["user", "activity"]
        # 設定css
        labels = {
            "gender": "性別",
            "date_of_birth": "出生年月日(西元)",
            "address": "地址",
            "postal_code": "郵遞區號",
            "identity": "身分證字號",
            "home_phone": "家用電話",
            "mobile_phone": "手機",
            "graduated_school": "畢業學校",
            "is_graduated": "畢肄業",
            "graduated_year_month": "畢(肄)業 年 月",
            "graduated_department": "畢業部別",
            "graduated_year": "年制",
            "graduated_educational": "學歷",
            "education": "同等學力",
            "school_notes": "備註",
            "school_department": "畢業系所組",
            "emergency_contact": "緊急聯絡人",
            "emergency_contact_phone": "緊急聯絡人電話",
            "emergency_contact_relationship": "緊急聯絡人關係",
            "military_service_number": "兵籍號碼",
            "military_service": "軍種",
            "military_rank": "階級",
            "military_retired_date": "退伍日期",
            "military_service_years_int": "服役年資",
            "military_service_years": "取得報考學歷資格後年資計分",
            "military_type": "類別",
            "military_card_type": "檢附卡別",
            "identity_front": "身分證正面(選填)",
            "identity_back": "身分證反面(選填)",
        }
        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(format=('%Y-%m-%d'),attrs={"class": "form-control" ,"type":"date"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "identity": forms.TextInput(attrs={"class": "form-control"}),
            "home_phone": forms.TextInput(attrs={"class": "form-control"}),
            "graduated_school": forms.Select(attrs={"class": "form-control choices"}),
            "is_graduated": forms.Select(attrs={"class": "form-control"}),
            "graduated_year_month": forms.DateInput(format=('%Y-%m-%d'),attrs={"class": "form-control" ,"type":"date"}),
            "graduated_department": forms.Select(attrs={"class": "form-control"}),
            "graduated_year": forms.Select(attrs={"class": "form-control"}),
            "graduated_educational": forms.Select(attrs={"class": "form-control"}),
            "education": forms.Select(attrs={"class": "form-control"}),
            "school_notes": forms.TextInput(attrs={"class": "form-control"}),
            "school_department": forms.TextInput(attrs={"class": "form-control"}),
            "mobile_phone": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact_phone": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact_relationship": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "education": forms.Select(attrs={"class": "form-control"}),
            "military_service_number": forms.TextInput(attrs={"class": "form-control"}),
            "military_service": forms.TextInput(attrs={"class": "form-control"}),
            "military_rank": forms.TextInput(attrs={"class": "form-control"}),
            "military_retired_date": forms.DateInput(format=('%Y-%m-%d'),attrs={"class": "form-control" ,"type":"date","type":"date"}),
            "military_service_years_int": forms.TextInput(attrs={"class": "form-control"}),
            "military_service_years": forms.Select(attrs={"class": "form-control"}),
            "military_card_type": forms.Select(attrs={"class": "form-control"}),
            "military_type": forms.Select(attrs={"class": "form-control"}),
            "identity_front": forms.FileInput(attrs={"class": "form-control","accept":".jpg, .jpeg, .png"}),
            "identity_back": forms.FileInput(attrs={"class": "form-control","accept":".jpg, .jpeg, .png"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['graduated_school'].queryset = School.objects.order_by('id')
    def clean_identity_front(self):
        file = self.cleaned_data.get('identity_front')
        if file:
            ext = file.name.split('.')[-1]  # Get the file extension
            if ext.lower() not in ['jpg', 'png', 'jpeg']:
                raise ValidationError('Unsupported file extension.')
        return file

    def clean_identity_back(self):
        file = self.cleaned_data.get('identity_back')
        if file:
            ext = file.name.split('.')[-1]  # Get the file extension
            if ext.lower() not in ['jpg', 'png', 'jpeg']:
                raise ValidationError('Unsupported file extension.')
        return file

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        error_messages={"required": "請輸入帳號"},
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}),
        error_messages={"required": "請輸入密碼"},
    )
    captcha = CaptchaField(label='')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = CaptchaField(label='')  # 動態添加 CAPTCHA 字段
class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
        # 設定css
        labels = {
            "email": "Email",
        }
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "email": {
                "required": "請輸入帳號",
            },
        }