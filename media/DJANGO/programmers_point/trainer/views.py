from django.shortcuts import render

# Create your views here.
def trainer(request):
    trainer_name="prasant"
    trainer_experiance="10 year"
    trainer_behaviour="good"
    tdic={'tn':trainer_name,'te':trainer_experiance,'tb':trainer_behaviour}
    return render(request,'python_trainer/trainer.html',tdic)