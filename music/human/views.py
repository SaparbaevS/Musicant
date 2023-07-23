from django.shortcuts import render

from human.models import Student


def show_students(request):
    context = {'students': Student.objects.all()}
    return render(request, 'index.html', context=context)


def show_student(request, student_id):
    context = {'student': Student.objects.get(pk=student_id)}
    return render(request, 'show.html', context=context)

def register(request):
    return render(request, 'register.html')