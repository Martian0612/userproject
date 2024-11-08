from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        # return redirect('/')
        #  return redirect('index.html')
         return render(request, 'index.html')
    print("user iss ", request.user)
    # else:
    #     return render(request, 'login.html')
    # if user is not logged in, so he/she can't directly access the index page
    return render(request, 'login.html')

# def Userlogin(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print("username is ", username)
#         print("password is ", password)
#         user = authenticate(username = username, password = password)
#         # basically it means user will contain some value or maybe true or false
#         print("user is ", user)
#         if user is not None:
#             login(request,user)
#             print(user)
#             return redirect('/')
#         else:
#             # can display message that wrong username or password
#             return render(request, 'login.html')
#     # else:
#     # after login, it will come to index page
#     return render(request, 'login.html')

def Userlogin(request):
    if request.user.is_authenticated:
            # redundant 
        # if request.path == "/login":
            return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print("username is ", username)
            print("password is ", password)
            user = authenticate(username = username, password = password)
            # basically it means user will contain some value or maybe true or false
            print("user is ", user)
            if user is not None:
                login(request,user)
                print(user)
                return redirect('/')
            else:
                # can display message that wrong username or password
                return render(request, 'login.html')
    # else:
    # after login, it will come to index page
    return render(request, 'login.html')

# it started working by using forms, over directly using link-button for logout., using forms after logout user can't access the main page.
def Userlogout(request):
    # user authenticated hai means login kiya hai, then only hi woh logout kar sakta hai
    # below if condition maybe redundant because logout button is present only inside the index page
    # if request.user.is_authenticated:
    #     logout(request)

    # directly logout function run hoga and then login page pe redirect kar denge
    logout(request)
    
    # after logout it will redirect to login page
    return redirect('/login')


# for proper logout -> this deleting cookie thing was not working

# def Userlogout(request):


#     logout(request)
#     response = HttpResponseRedirect('/login')
#     response.delete_cookie('sessionid')
#     return response