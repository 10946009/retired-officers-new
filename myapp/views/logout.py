from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    # logout the user
    request.session.flush()

    return redirect("index")