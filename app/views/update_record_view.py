from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import UpdateRecordForm
from app.selectors import getRecord
from app.services import create_record

@login_required(login_url='my-login')
def update_record_view(request, pk):
    """
    View for updating an existing record.
    """
    record = getRecord(pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            create_record(form)  
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)
