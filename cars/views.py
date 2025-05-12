from django.shortcuts import render

def car_viw(request):
    return render(request,
                  'cars.html',
                  {'cars': {'model': 'Astra 2.0'}})
