from .models import Record


from django.shortcuts import get_object_or_404


def getAllRecords():
    return Record.objects.all()
    
    
    
def getRecord(record_id):
    '''Returns a record'''


    record = get_object_or_404(Record,id=record_id)
    
    
    
    