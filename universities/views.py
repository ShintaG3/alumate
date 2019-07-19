from django.shortcuts import render

def University(request):
    context = {

    }
    return render(request, 'universities/university.html', context)
