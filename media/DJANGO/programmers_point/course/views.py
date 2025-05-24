from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python_course(request):
    course_name="python"
    course_fees=50000
    course_duration="8 Month"
    course_time="2pm-3pm"
    info={'cn':course_name,'cf':course_fees,'cd':course_duration,'ct':course_time}
    return render(request,'python_course/py.html',info)
