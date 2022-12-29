from django.shortcuts import render


from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.now()
    return render(request=request, template_name="newyear/index.html",context={"newyear": now.day == 1 and now.month ==1})