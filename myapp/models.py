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
    activity_start_time = models.DateTimeField(blank=True, null=True)
    activity_end_time = models.DateTimeField(blank=True, null=True)
    sign_up_start_time = models.DateTimeField(blank=True, null=True)
    sign_up_end_time = models.DateTimeField(blank=True, null=True)
    score_open_time = models.DateTimeField(blank=True, null=True)
    def get_year_tw(self):
        return self.activity_start_time.year - 1911
    
    def get_student_in_activity(self):
        return self.student.all()
    
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
    
class ScoreLabel(models.Model):
    label1 = models.CharField(max_length=100, blank=False, null=False, default="")
    score1_weight = models.IntegerField(blank=False, null=False, default=0)
    label2 = models.CharField(max_length=100, blank=False, null=False, default="")
    score2_weight = models.IntegerField(blank=False, null=False, default=0)
    label3 = models.CharField(max_length=100, blank=False, null=False, default="")
    score3_weight = models.IntegerField(blank=False, null=False, default=0)
    def __str__(self):
        return "label" + str(self.id)

class Score(models.Model):
    student = models.ForeignKey("user.Student", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    score1 = models.IntegerField(blank=False, null=False, default=0)
    score2 = models.IntegerField(blank=False, null=False, default=0)
    score3 = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        unique_together = ("student", "activity")
