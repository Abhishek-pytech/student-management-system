from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student, Attendance


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_list')

        return render(request, 'students/login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'students/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD / STUDENT LIST
@login_required
def student_list(request):

    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    today = date.today()

    total_students = Student.objects.count()

    present_today = Attendance.objects.filter(
        date=today,
        status='Present'
    ).count()

    absent_today = Attendance.objects.filter(
        date=today,
        status='Absent'
    ).count()

    total_attendance = Attendance.objects.count()

    return render(request, 'students/student_list.html', {
        'students': students,
        'total_students': total_students,
        'present_today': present_today,
        'absent_today': absent_today,
        'total_attendance': total_attendance
    })


# ADD STUDENT
@login_required
def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            course=request.POST['course'],
            age=request.POST['age'],
            photo=request.FILES.get('photo')
        )

        return redirect('student_list')

    return render(request, 'students/add_student.html')


# EDIT STUDENT
@login_required
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

    return render(request, 'students/edit_student.html', {
        'student': student
    })


# DELETE STUDENT
@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('student_list')


# ATTENDANCE PAGE
@login_required
def attendance_page(request):

    students = Student.objects.all()

    return render(request, 'students/attendance.html', {
        'students': students
    })


# MARK ATTENDANCE
@login_required
def mark_attendance(request, student_id, status):

    student = get_object_or_404(Student, id=student_id)

    Attendance.objects.create(
        student=student,
        status=status
    )

    return redirect('student_list')


@login_required
def student_profile(request, id):

    student = get_object_or_404(Student, id=id)

    attendance = Attendance.objects.filter(student=student)

    present_count = attendance.filter(status='Present').count()
    absent_count = attendance.filter(status='Absent').count()

    return render(request, 'students/student_profile.html', {
        'student': student,
        'present_count': present_count,
        'absent_count': absent_count
    })