from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student

# LIST + SEARCH
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


# ADD STUDENT
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            course=request.POST['course'],
            age=request.POST['age']
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html')


# EDIT STUDENT
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})


# DELETE STUDENT
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')