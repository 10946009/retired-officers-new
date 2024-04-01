from django.utils import timezone
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="")
    def __str__(self):
        return self.name

# 活動
class Activity(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="")
    score_label = models.ForeignKey(
        "ScoreLabel",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="score_label",
    )
    activity_start_time = models.DateTimeField(blank=False, null=False)
    activity_end_time = models.DateTimeField(blank=False, null=False)
    sign_up_start_time = models.DateTimeField(blank=False, null=False)
    sign_up_end_time = models.DateTimeField(blank=False, null=False)
    sign_up_print_end_time = models.DateTimeField(blank=False, null=False)
    score_open_time = models.DateTimeField(blank=False, null=False)
    score_min = models.FloatField(blank=False, null=False, default=0)

    def __str__(self):
        return self.name

    def get_year_tw(self):
        return self.activity_start_time.year - 1911
    
    def get_student_in_activity(self):
        return self.student.all()
    
    def is_show(self):
        now = timezone.now()
        return now >= self.activity_start_time and now < self.activity_end_time

    def get_status(self):
        now = timezone.now()
        print(now,"and",self.activity_start_time)
        if now < self.sign_up_start_time:
            return "尚未開始"
        elif now >= self.sign_up_start_time and now < self.sign_up_end_time:
            return "報名中"
        else:
            return "報名截止"

    def is_score_open(self):
        now = timezone.now()
        return now > self.score_open_time
        
    def is_sign_up_open(self):
        now = timezone.now()
        return now >= self.sign_up_start_time and now < self.sign_up_end_time
    def is_sign_up_print_open(self):
        now = timezone.now()
        return now >= self.sign_up_start_time and now < self.sign_up_print_end_time
    
class ScoreLabel(models.Model):
    label1 = models.CharField(max_length=100, blank=False, null=False, default="")
    label2 = models.CharField(max_length=100, blank=False, null=False, default="")
    label3 = models.CharField(max_length=100, blank=False, null=False, default="")
    def __str__(self):
        return self.label1 + " " + self.label2 + " " + self.label3

class Score(models.Model):
    student = models.ForeignKey("user.Student", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    score1 = models.FloatField(blank=False, null=False, default=0)
    score2 = models.FloatField(blank=False, null=False, default=0)
    score3 = models.FloatField(blank=False, null=False, default=0)

    def get_total_score(self):
        return self.score1 + self.score2 + self.score3
    class Meta:
        unique_together = ("student", "activity")
