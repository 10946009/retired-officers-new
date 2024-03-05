from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="")


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


class ScoreLabel(models.Model):
    label1 = models.CharField(max_length=100, blank=False, null=False, default="")
    score1_weight = models.IntegerField(blank=False, null=False, default=0)
    label2 = models.CharField(max_length=100, blank=False, null=False, default="")
    score2_weight = models.IntegerField(blank=False, null=False, default=0)
    label3 = models.CharField(max_length=100, blank=False, null=False, default="")
    score3_weight = models.IntegerField(blank=False, null=False, default=0)


class Score(models.Model):
    student = models.ForeignKey("user.Student", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    score1 = models.IntegerField(blank=False, null=False, default=0)
    score2 = models.IntegerField(blank=False, null=False, default=0)
    score3 = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        unique_together = ("student", "activity")
