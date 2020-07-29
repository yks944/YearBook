from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile,CustomUser
from .models import TeacherEvents,StudentEvents
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        utype = request.user.utype
        if utype.lower() == 'admin':
            return render(request,'year_book/admin.html',{'user':request.user,'type':utype.upper()})
        return render(request,'year_book/dashboard.html',{'user':request.user,'type':utype.upper()})
    else:
        return render(request,'year_book/home.html')

@login_required(login_url='/accounts/signin/')
def profile(request):
    user = request.user

    info = Profile.objects.filter(profile=user)
    l=[]
    l2=['Name','Enroll Id','Email','Address','Mobile']
    for i in info:
        l.append(user)
        l.append(i.enroll_id)
        l.append(i.email)
        l.append(i.address)
        l.append(i.mobile)
    return render(request,'year_book/profile.html',{'name':l[0],'enroll':l[1],'email':l[2],'add':l[3],'mob':l[4]})
@login_required(login_url='/accounts/signin/')
def updateprofile(request):
    name = request.POST['username']
    address = request.POST['address']
    mobile = str(request.POST['mobile'])
    x = Profile.objects.update(address=address,mobile=mobile)
    y = CustomUser.objects.get(username=request.user)
    y.username=name
    y.save()
    user = request.user

    info = Profile.objects.filter(profile=user)
    l = []
    l2 = ['Name', 'Enroll Id', 'Email', 'Address', 'Mobile']
    for i in info:
        l.append(user)
        l.append(i.enroll_id)
        l.append(i.email)
        l.append(i.address)
        l.append(i.mobile)
    return render(request, 'year_book/profile.html',{'name': l[0], 'enroll': l[1], 'email': l[2], 'add': l[3], 'mob': l[4],'updated':'updated'})

@login_required(login_url='/accounts/signin/')
def options(request):
    return render(request,'year_book/achv_options.html')
@login_required(login_url='/accounts/signin/')
def category(request,cate):
    cate = cate.upper()
    return render(request,'year_book/achv_get.html',{'achv_of':cate})
@login_required(login_url='/accounts/signin/')
def achv_list(request,cate):
    year = request.POST['year']
    branch = request.POST['branch']
    x=None
    if cate.lower() == 'teacher':
        x = TeacherEvents.objects.filter(year=year,branch=branch)
    elif cate.lower() == 'student':
        x = StudentEvents.objects.filter(year=year,branch=branch)
    l = []
    if x is not None:
        for i in x:
            l.append(i)
        return render(request,'year_book/achv_list.html',{'list':l,'utype':cate.lower()})
    else:
        return render(request,'year_book/achv_list.html',{'empty':'Nothing to display!!!'})

@login_required(login_url='/accounts/signin/')
def getdetails(request,utype,username):
    print(username)
    # print(id)
    # return HttpResponse(utype+" "+username)
    x = None
    l=[]
    d = {}
    if utype.upper() == 'STUDENT':
        x = StudentEvents.objects.filter(username=username)
        for i in x:
            d['Username'] = i.username
            d['Enrollment No'] = i.enroll
            d['Branch'] = i.branch
            d['Year'] = i.year
            d['Dob'] = i.dob
            d['Email'] = i.email
            d['Mobile'] = i.mobile
            d['Address'] = i.address
            d['Achievements'] = i.achievements
    elif utype.upper() == 'TEACHER':
        x = TeacherEvents.objects.filter(username=username)
        for i in x:
            d['Username'] = i.username
            d['Designation'] = i.designation
            d['Branch'] = i.branch
            d['Year'] = i.year
            d['Dob'] = i.dob
            d['Qualification'] = i.qualification
            d['Email'] = i.email
            d['Mobile'] = i.mobile
            d['Experience'] = i.experience
            d['Subjects'] = i.subjects
    return render(request,'year_book/user_detail.html',{'detail':d,'imgtype':utype.upper(),'length':len(d)+1})

def t_achv(request):
    return render(request, 'year_book/t_add_view.html', {'user': 'Teacher'})
def s_achv(request):
    return render(request, 'year_book/s_add_view.html', {'user': 'Student'})
@login_required(login_url='/accounts/signin/')
def category2(request,cate):
    cate = cate.upper()
    return render(request,'year_book/admin_teacher_get.html',{'achv_of':cate})
@login_required(login_url='/accounts/signin/')
def category3(request,cate):
    cate = cate.upper()
    return render(request,'year_book/admin_student_get.html',{'achv_of':cate})

@login_required(login_url='/accounts/signin/')
def achv_list2(request,cate):
    year = request.POST['year']
    branch = request.POST['branch']
    x=None
    if cate.lower() == 'teacher':
        x = TeacherEvents.objects.filter(year=year,branch=branch)
    elif cate.lower() == 'student':
        x = StudentEvents.objects.filter(year=year,branch=branch)
    l = []
    if x is not None:
        for i in x:
            l.append(i)
        return render(request,'year_book/admin_achv_list.html',{'list':l,'utype':cate.lower()})
    else:
        return render(request,'year_book/admin_achv_list.html',{'empty':'Nothing to display!!!'})

@login_required(login_url='/accounts/signin/')
def getdetails2(request,utype,username):
    print(username)
    # print(id)
    # return HttpResponse(utype+" "+username)
    x = None
    l=[]
    d = {}
    if utype.upper() == 'STUDENT':
        x = StudentEvents.objects.filter(username=username)
        for i in x:
            d['Username'] = i.username
            d['Enrollment No'] = i.enroll
            d['Branch'] = i.branch
            d['Year'] = i.year
            d['Dob'] = i.dob
            d['Email'] = i.email
            d['Mobile'] = i.mobile
            d['Address'] = i.address
            d['Achievements'] = i.achievements
    elif utype.upper() == 'TEACHER':
        x = TeacherEvents.objects.filter(username=username)
        for i in x:
            d['Username'] = i.username
            d['Designation'] = i.designation
            d['Branch'] = i.branch
            d['Year'] = i.year
            d['Dob'] = i.dob
            d['Qualification'] = i.qualification
            d['Email'] = i.email
            d['Mobile'] = i.mobile
            d['Experience'] = i.experience
            d['Subjects'] = i.subjects
    return render(request,'year_book/admin_user_detail.html',{'detail':d,'imgtype':utype.upper(),'length':len(d)+1})
def add_s_achv(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            enroll = request.POST['enroll']
            year = request.POST['year']
            branch = request.POST['branch']
            dob = request.POST['dob']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address = request.POST['address']
            achv = request.POST['achv']
            x = StudentEvents(username=username, enroll=enroll, year=year, branch=branch, dob=dob, email=email,
                              mobile=mobile, address=address, achievements=achv)
            x.save()
            return render(request, 'year_book/add_s_achv.html', {'Success': 'Added Successfully!!!'})
        except:
            return render(request,'year_book/add_s_achv.html',{'Success':"Already Addedd"})
    else:
        print('hello in add')
        return render(request,'year_book/add_s_achv.html')
def add_t_achv(request):
    if request.method == 'POST':
        username = request.POST['username']
        desig = request.POST['desig']
        year = request.POST['year']
        branch = request.POST['branch']
        dob = request.POST['dob']
        qual = request.POST['qual']
        email = request.POST['email']
        mobile = request.POST['mobile']
        exp = request.POST['exp']
        spec = request.POST['spec']
        subj = request.POST['subj']
        x = TeacherEvents(username=username,designation=desig,year=year,branch=branch,dob=dob,qualification=qual,email=email,mobile=mobile,experience=exp,specialization=spec,subjects=subj)
        x.save()
        return render(request, 'year_book/add_s_achv.html', {'Success': 'Added Successfully!!!'})
    else:
        return render(request,'year_book/add_t_achv.html')