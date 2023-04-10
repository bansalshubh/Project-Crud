from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Employee
from datetime import datetime
from django.db.models import Q


# Create your views here.

# Function Based views
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request ,"Invalid Username or Password")
            return redirect('/')
            # return render(request, 'login.html',context)
    else:
        return render(request,'login.html',context)

def create_employee(request):
    if request.method == 'GET':
        return render(request,'employeeform.html')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        city = request.POST['city']
        country = request.POST['country']
        address = request.POST['address']
        aws = request.POST.get('aws',None)
        devops = request.POST.get('devops',None)
        web = request.POST.get('web',None)
        qa = request.POST.get('qa',None)
        middleware = request.POST.get('middleware',None)
        skills = [aws,devops,web,qa,middleware]
        for skill in skills:
            if skill is None:
                skills.remove(skill)
        gender =''
        if(request.POST.get('male', False) == "on"):
            gender = 'M'
        else:
            gender = 'F'
        timestamp = datetime.now()

        employee = Employee(emp_fame=fname,emp_lame=lname,emp_email=email,emp_phone=mobile,emp_address=address,emp_city=city,emp_country=country,emp_gender=gender,emp_skills=skills,timestamp=timestamp)
        employee.save()

    return redirect('/employee/search')

def search_employee(request):
    if request.method == 'GET':
        all_employees = Employee.objects.all().values()
        all_employees = list(all_employees)
        context = {'employee_list' : all_employees}
        return render(request,'employeeSearch.html',context)
    else:
        mobile = request.POST.get('mobile',None)
        name = request.POST.get('name',None)
        employees = []
        context = dict()
        if mobile != '':
            context.update({'mobile':mobile})
            employees = list(Employee.objects.filter(emp_phone=mobile).values())
            if name != '':
                context.update({'name':name})
                for i in employees:
                    if str(i['emp_fame']).lower() == str(name).lower() or str(i['emp_lame']).lower() == str(name).lower() or (str(i['emp_fame'])+" "+str(i['emp_fame'])).lower() == str(name).lower():
                        pass
                    else:
                        employees.remove(i)
        else:
            if name != '':
                context.update({'name':name})
                employees = list(Employee.objects.filter(Q(emp_fame=name) | Q(emp_lame=name)).values())
            else:
                employees = []
        context.update({'employee_list' : employees})
        print(context)
        return render(request,'employeeSearch.html',context)

def edit_employee(request,id):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        city = request.POST['city']
        country = request.POST['country']
        address = request.POST['address']
        aws = request.POST.get('aws',None)
        devops = request.POST.get('devops',None)
        web = request.POST.get('web',None)
        qa = request.POST.get('qa',None)
        middleware = request.POST.get('middleware',None)
        skills = [aws,devops,web,qa,middleware]
        for skill in skills:
            if skill is None:
                skills.remove(skill)
        Employee.objects.filter(emp_id=id).update(emp_fame=fname,emp_lame=lname,emp_email=email,emp_phone=mobile,emp_city=city,emp_country=country,emp_address=address,emp_skills=skills)
        return redirect('/employee/search')
    employee = Employee.objects.filter(emp_id=id)
    context = {"employee":employee}
    return render(request, 'employeeedit.html',context)

def delete_employee(request,id):
    Employee.objects.filter(emp_id=id).delete()
    return redirect('/employee/search')

def logout(request):
    auth.logout(request)
    return redirect('/')