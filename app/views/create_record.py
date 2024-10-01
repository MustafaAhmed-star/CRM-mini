
from django.shortcuts import render, redirect
from app.forms import CreateRecordForm


from django.contrib.auth.decorators import login_required

from django.contrib import messages
from app.services import create_record

@login_required(login_url='my-login')
def create_record_view(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            create_record(form)

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)