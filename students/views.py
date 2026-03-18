from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
from django.db.models import Q

def student_list(request):

    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        course=request.POST['course']
        age=request.POST['age']
    


        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            course=course,
            age=age,
            

        )

        return redirect('student_list')
    return render(request, 'students/add_student.html')

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')