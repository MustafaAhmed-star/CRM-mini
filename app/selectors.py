from .models import Record




def getAllRecords():
    return Record.objects.all()