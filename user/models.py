from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.forms import ValidationError
from user.check_identity import is_valid_id_or_rc_number
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, max_length=10, blank=False, null=False)
    objects = UserManager()

class ActivityStudents(models.Model):
    activity = models.ForeignKey('myapp.Activity', on_delete=models.CASCADE)
    student = models.ForeignKey('user.Student', on_delete=models.CASCADE)
    join_time = models.DateTimeField(auto_now_add=True)
    join_number = models.IntegerField(blank=False, null=False)
    is_get_print = models.BooleanField(default=False) # 已收到報名資料
    is_checked = models.BooleanField(default=False) # 已審核
    checked_number = models.CharField(max_length=6, blank=True, null=False, default="") # 審核編號


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.ManyToManyField("myapp.Activity", related_name="student",through='ActivityStudents')
    # 服役年資
    SERVICE_YEARS_CHOICES = [
        (1, "未滿3年者"),
        (2, "滿3年未滿6年者"),
        (3, "滿6年未滿9年者"),
        (4, "滿9年未滿12年者"),
        (5, "滿12年未滿15年者"),
        (6, "滿15年未滿18年者"),
        (7, "滿18年未滿21年者"),
        (8, "滿21年未滿24年者"),
        (9, "滿24年以上者"),
    ]
    EDUCATION_CHOICES = [
        (1, "無"),
        (2, "二年制專科學校及進修學校肄業學生"),
        (3, "三年制專科學校及進修學校肄業學生"),
        (4, "五年制專科學校及進修學校肄業學生"),
        (5, "大學學士班（不包括空中大學）肄業"),
        (6, "自學進修學力鑑定考試通過"),
        (7, "國家考試及格，持有及格證書"),
        (8, "技能檢定合格"),
        (
            9,
            "符合年滿22歲、高級中等學校畢（結）業或修滿規定修業年限，且已修畢畢業應修學分80學分以上",
        ),
        (10, "持有高級中等學校畢業證書後，從事相關工作經驗五年以上"),
        (
            11,
            "曾於大學校院擔任專業技術人員、於專科學校或高級中等學校擔任專業及技術教師",
        ),
        (12, "持國外或香港、澳門專科以上學校畢（肄）業學歷"),
    ]
    gender_CHOICES = [(1, "男"), (2, "女")]
    DEPARTMENT_CHOICES = [(1, "日間部"), (2, "進修部")]
    IS_GRADUATED_CHOICES = [(1, "畢業"), (2, "應屆畢業"), (3, "未畢業(肄業或結業)")]
    GRADUATED_YEAR_CHOICES = [
        (1, "二年制"),
        (2, "三年制"),
        (3, "四年制"),
        (4, "五年制"),
    ]
    SERVICE_TYPE_CHOICES = [(1, ""), (2, "一類"), (3, "二類")]

    # 性別,出生年月日,身分證字號,地址,郵遞區號,家用電話,手機
    gender = models.IntegerField(choices=gender_CHOICES, blank=False, null=False)
    date_of_birth = models.DateField()
    identity = models.CharField(max_length=15, blank=False, null=False, default="")
    address = models.CharField(max_length=150, blank=False, null=False, default="")
    postal_code = models.CharField(max_length=15, blank=False, null=False, default="")
    home_phone = models.CharField(max_length=15, blank=False, null=False, default="")
    mobile_phone = models.CharField(max_length=15, blank=False, null=False, default="")

    # 畢業學校,畢肄業,畢業部別,畢業年制,同等學力,畢業系所組,學校備註
    graduated_school = models.ForeignKey(
        "myapp.School", on_delete=models.SET_NULL, blank=False, null=True
    )
    is_graduated = models.IntegerField(
        choices=IS_GRADUATED_CHOICES, blank=False, null=False
    )
    graduated_department = models.IntegerField(
        choices=DEPARTMENT_CHOICES, blank=False, null=False
    )
    graduated_year = models.IntegerField(
        choices=GRADUATED_YEAR_CHOICES, blank=False, null=False
    )
    education = models.IntegerField(
        choices=EDUCATION_CHOICES, blank=False, null=False, default=1
    )
    school_department = models.CharField(
        max_length=50, blank=False, null=False, default=""
    )
    graduated_year_month = models.DateField()
    school_notes = models.CharField(max_length=150, blank=True, null=False, default="")

    # 緊急聯絡人,緊急聯絡人電話,緊急聯絡人關係
    emergency_contact = models.CharField(
        max_length=50, blank=False, null=False, default=""
    )
    emergency_contact_phone = models.CharField(
        max_length=15, blank=False, null=False, default=""
    )
    emergency_contact_relationship = models.CharField(
        max_length=15, blank=False, null=False, default=""
    )

    # 兵籍號碼 軍種 階級 退伍日期 服役年資  年資(數字) 幾類
    military_service_number = models.CharField(max_length=15, blank=False, null=False)
    military_service = models.CharField(max_length=15, blank=False, null=False)
    military_rank = models.CharField(max_length=15, blank=False, null=False)
    military_retired_date = models.DateField(blank=False, null=False)
    military_service_years = models.IntegerField(
        choices=SERVICE_YEARS_CHOICES, blank=False, null=False
    )
    military_service_years_int = models.IntegerField(blank=False, null=False)
    # 第一類 第二類
    military_type = models.IntegerField(
        choices=SERVICE_TYPE_CHOICES, blank=False, null=False, default=1
    )

    # 身分證正面 身分證反面
    identity_front = models.ImageField(blank=True, null=False, default="")
    identity_back = models.ImageField(blank=True, null=False, default="")

    notes = models.CharField(max_length=150, blank=True, null=False, default="")

    def __str__(self):
        return self.user.email
    
    def date_of_birth_tw(self):
        return (
            self.date_of_birth.year - 1911,
            self.date_of_birth.month,
            self.date_of_birth.day,
        )


    def date_of_military_retired_tw(self):
        return (
            self.military_retired_date.year - 1911,
            self.military_retired_date.month,
            self.military_retired_date.day,
        )

    def get_birth_tw(self):
        return f"{self.date_of_birth.year - 1911}年{self.date_of_birth.month}月{self.date_of_birth.day}日"
    
    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_graduated_year_month_tw(self):
        return f'{self.graduated_year_month.year - 1911}年{self.graduated_year_month.month}月'

    def get_join_time(self, activity_id):
        join_time = ActivityStudents.objects.get(activity_id=activity_id, student_id=self.id).join_time
        # 格式為2022/5/23 下午 07:11:49
        join_time = join_time.strftime("%Y/%m/%d %p %I:%M:%S")
        join_time = join_time.replace("AM", "上午").replace("PM", "下午")
        return join_time
    
    def clean(self):
        if not is_valid_id_or_rc_number(self.identity):
            raise ValidationError({"identity": "身分證字號格式錯誤"})
    def get_join_number(self,activity_id):
        join_number = self.activitystudents_set.get(activity_id=activity_id).join_number
        return join_number
    
    def get_checked_number(self,activity_id):
        checked_number = self.activitystudents_set.get(activity_id=activity_id).checked_number
        return checked_number
        
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
