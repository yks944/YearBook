from django.shortcuts import render,redirect
from .models import CustomUser,Profile
from django.contrib.auth import login,logout
import django.contrib.auth as i
# Create your views here.
def signup(request):
    if request.method=='POST':
        enroll = request.POST['enroll']
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['email']
        address = request.POST['address']
        mob = str(request.POST['mobile'])
        utype = request.POST['user_type']
        print(utype)
        try:
            CustomUser.objects.get(username=username)
            return render(request,'signup.html',{'msg':'Username is already taken'})

        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(username=username, password=password, utype=utype)
            user.save()
            print("after signup", user)
            profile = Profile(email=mail, address=address, mobile=mob, profile=user, enroll_id=enroll)
            profile.save()
            print("line1")
            # login(request, user)
            print("line 2")
            return render(request, 'login.html',{'msg': 'Your Account Created Successfully!!!Now you are ready to login'})

    elif request.method=='GET':
        return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        u_type = request.POST['user_type']
        print(u_type)

        try:
            user = i.authenticate(username=username,password=password,utype=u_type)
            print('error1')
            print("han ya na",user.is_superuser)
            print("hello",user)
            usertype = user.utype
            print('error1hello')
            print(u_type, " ",usertype )
            # typ = usertype.upper()
            if u_type != usertype:
                print('error2')
                print(usertype)
                return render(request, 'login.html', {'msg': 'Wrong Credentials'})
            # if(usertype.lower() == 'admin'):
            #     return redirect('home')
            print("1")
            login(request,user)
            print('user object',user)
            print("2")
            # return render(request,'year_book/dashboard.html',{'user':user,'type':typ})
            return redirect('home')
        except:
            return render(request,'login.html',{'msg':'Wrong Credentials'})
    else:
        return render(request,'login.html')
def signout(request):
    logout(request)
    return render(request,'login.html')