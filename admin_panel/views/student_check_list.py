from django.shortcuts import render
from user.models import ActivityStudents
from django.contrib.auth.decorators import permission_required
from admin_panel.forms import StudentFormSet
from django.urls import reverse
@permission_required("myapp.view_activity", login_url="/403")
def student_check_list(request, activity_id):
    activity_students = ActivityStudents.objects.filter(activity=activity_id).order_by('id')
    
    if request.method == "POST":
        formset = StudentFormSet(request.POST)
        # print(formset.is_valid())

        if formset.is_valid():
            formset.save()
            return render(request, "message.html", {"next":reverse('student_check_list', args=[activity_id]), "message": "儲存成功"})
        else:
            return render(request, "message.html", {"next":reverse('student_check_list', args=[activity_id]), "message": "儲存失敗"})
            # Redirect or show a success message

    else:
        formset = StudentFormSet(queryset=activity_students)

    content = {"formset": formset,"activity_students":activity_students}

    return render(request, "student_check_list.html",content)
