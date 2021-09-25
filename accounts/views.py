from django.shortcuts import render,redirect
from firebase_admin import *
from firebase_admin import firestore
from django.contrib import auth
import pyrebase


class General_Users(General_Details):
    
    
    def __init__(self):

        self.gen_user = General_Details()

    def signup(self,request):
        
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
        
            if password == confirm_password:
                user = self.gen_user.general_auth_user.create_user_with_email_and_password(email, password)
                self.uid = user['localId']
                data = {
                    
                    "Id":self.uid,
                    "First_Name" : first_name,
                    "Last_Name" : last_name,
                    "Username":username,
                    "Email" : email,
                    "Phone_Number" : phone_number,
                    
                }

                docs = self.gen_user.general_db.collection("Users").document(self.uid)
                user = self.gen_user.general_auth_user.sign_in_with_email_and_password(email,password)
                
                docs.set(data)
                request.session['uid']=str(self.uid)
                return redirect("/")

            else:
                print("Password not matched")
                return render(request,"signup.html")
            
        else:
            return render(request,"signup.html")

    def login(self,request):

        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
        
            try:
                user = self.gen_user.general_auth_user.sign_in_with_email_and_password(email,password)
                self.uid = user['localId']
                request.session['uid'] = str(self.uid)

                print(request.session['uid'])
                return redirect("/")

            except Exception as ex:
                print(ex)
                return render(request,"login.html")
            
        
        else:
            return render(request,"login.html")
        
      
    def logout(self,request):
        
        # auth.logout(request)

        try:
            del request.session['uid']
        except:
            pass
            
        return redirect("/")
        
                

        

            
            
            
    

#     def search_video(self,request):
        
        
#         search_v = request.GET.get('search')
        
        
        
