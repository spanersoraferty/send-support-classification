from django.shortcuts import render
from datetime import datetime

# Create your views here.
def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def chart_view(request):
    return render(request, 'chart.html')

