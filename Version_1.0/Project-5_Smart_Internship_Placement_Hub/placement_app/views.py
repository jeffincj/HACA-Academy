from django.shortcuts import render
from .models import Student, Internship, Application
from django.shortcuts import render, redirect

def home(request):
    return render(request,'home.html')

def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        college = request.POST.get("college")
        branch = request.POST.get("branch")
        password = request.POST.get("password")

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            college=college,
            branch=branch,
            password=password
        )

        return redirect('home')

    return render(request,'register.html')

from .models import Student

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(
                email=email,
                password=password
            )

            request.session['student_id'] = student.id
            request.session['student_name'] = student.name

            return redirect('dashboard')

        except:
            return render(
                request,
                'login.html',
                {'error':'Invalid Email or Password'}
            )

    return render(request,'login.html')

def dashboard(request):

    name = request.session.get('student_name')

    internships = Internship.objects.all()

    return render(
        request,
        'dashboard.html',
        {
            'name': name,
            'internships': internships
        }
    )

from .models import Internship

def internships(request):

    all_internships = Internship.objects.all()

    return render(
        request,
        'internships.html',
        {'internships': all_internships}
    )

def applications(request):

    if 'student_id' not in request.session:
        return render(
            request,
            'login_required.html'
        )

    student_id = request.session.get('student_id')

    student = Student.objects.get(id=student_id)

    applications = Application.objects.filter(
        student=student
    )

    return render(
        request,
        'applications.html',
        {'applications': applications}
    )

def logout(request):

    request.session.flush()

    return redirect('home')


def apply_internship(request,id):

    if 'student_id' not in request.session:
        return render(
            request,
            'login_required.html'
        )

    student_id = request.session.get('student_id')

    student = Student.objects.get(id=student_id)

    internship = Internship.objects.get(id=id)

    already_applied = Application.objects.filter(
        student=student,
        internship=internship
    ).exists()

    if already_applied:
        return render(
            request,
            'already_applied.html'
        )

    Application.objects.create(
        student=student,
        internship=internship,
        status="Processing",
        feedback="Application Under Review"
    )

    return redirect('applications')