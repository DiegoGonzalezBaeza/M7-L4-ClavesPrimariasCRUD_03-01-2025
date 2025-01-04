from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

#CRUD COURSE
# CREATE COURSE
# READ COURSE
# UPDATE COURSE
# DELETE COURSE

# READ COURSE (leer todos los registros)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app2/course_list.html', {'courses': courses})

# READ Course (lee un registro)
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'app2/course_detail.html', {'course': course})

# CREATE Course
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'app2/course_form.html', {'form': form})

# UPDATE Estudiante
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'app2/course_form.html', {'form': form})

# DELETE Estudiante
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'app2/course_confirm_delete.html', {'course': course})

# Create your views here.
def student_list(request):
    return render(request, 'app1/student_list.html')