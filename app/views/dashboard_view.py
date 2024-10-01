
from django.contrib.auth.decorators import login_required
from app.models import Record
from django.shortcuts import render, redirect
from app.selectors import getAllRecords


@login_required(login_url='my-login')
def dashboard_view(request):

    my_records = getAllRecords()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)