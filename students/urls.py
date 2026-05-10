from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

     # login system
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('attendance/', views.attendance_page),

    path(
    'mark-attendance/<int:student_id>/<str:status>/',
    views.mark_attendance
    ),
    path('student/<int:id>/', views.student_profile, name='student_profile'),
]