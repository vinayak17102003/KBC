from django.shortcuts import render
from datetime import datetime
# Create your views here.
def mannu(request):
    b_name="manoj"
    b_age=23
    b_address="Multai"
    d_date=datetime.now()
    bdict={'bn':b_name,'ba':b_age,'badd':b_address,'dt':d_date}
    return render(request,'bhanja.html',bdict)