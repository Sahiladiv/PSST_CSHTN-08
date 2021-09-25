from django.shortcuts import render,redirect
from firebase_admin import *
from firebase_admin import firestore
from django.contrib import auth
import pyrebase
import time


def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def courses(request):
    return render(request,'courses.html')

def trainers(request):
    return render(request,'trainers.html')

def events(request):
    return render(request,'events.html')

def forum(request):

    
    forum_db = general_db.collection("Discussion")
    

    message_id_list = []

    forum_database = forum_db.get()
    for i in forum_database:
            message_id_list.append(i.id)

    message_details_list = []

    for i in message_id_list:
        course_details = general_db.collection("Discussion").document(i)
        message_details_list.append(course_details)
        
    message_list = []
    for i in message_details_list:
        message_list.append(i.get().to_dict())

    if request.method == "POST":
        user_db = general_db.collection("Users").document(uid).get().to_dict()
        uid = request.session['uid']
        current_timestamp = time.time()
        message = request.POST.get('message')
        chat_forum = forum_db.document(str(current_timestamp))
        sender = user_db['Username']
        forum_message = {
            "Sender":sender,
            "Message": message
        }
        chat_forum.set(forum_message)
        
        return redirect('/general/forum')
        
    else:
        return render(request,'general_forum.html',{'message_list':message_list})







