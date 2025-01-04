from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

#CRUD Estudiante
# CREATE Estudiante
# READ Estudiante
# UPDATE Estudiante
# DELETE Estudiante

# READ Estudiante (leer todos los registros)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'app1/student_list.html', {'students': students})

# READ Estudiante (lee un registro)
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'app1/student_detail.html', {'student': student})

# CREATE Estudiante
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'app1/student_form.html', {'form': form})

# UPDATE Estudiante
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'app1/student_form.html', {'form': form})

# DELETE Estudiante
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'app1/student_confirm_delete.html', {'student': student})

# Create your views here.
def course_list(request):
    return render(request, 'app2/course_list.html')
