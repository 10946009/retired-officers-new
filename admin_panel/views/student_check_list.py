from django.shortcuts import render
from user.models import ActivityStudents
from django.contrib.auth.decorators import permission_required
from admin_panel.forms import StudentFormSet


@permission_required("myapp.view_activity", login_url="/403")
def student_check_list(request, activity_id):
    activity_students = ActivityStudents.objects.filter(activity_id=activity_id)
    if request.method == "POST":
        formset = StudentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            # Redirect or show a success message
    else:
        formset = StudentFormSet(queryset=activity_students)

    content = {"formset": formset,"activity_students":activity_students}

    return render(request, "student_check_list.html",content)
