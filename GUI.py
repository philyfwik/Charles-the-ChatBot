# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:12:45 2019

@author: fbobo
"""

from PIL import *
from tkinter import *
#import convoDemo


charles = Tk()
charles.title("Charles the ChatBot")
charles.geometry("515x400")
charles.wm_iconbitmap('robocharles.ico')

#charles.configure(background= "black")
        
#displays and sends user input to system
def send(event=None):
    msg = "You: " + user_entry.get()
    #print(user_entry.get())
    
    if msg == "{quit}" or 'bye' in msg:
        charles.quit()
    else:
        call()
        msg_list.insert(END, msg)
        msg_list.yview(END)
        user_entry.delete(0, 'end')
        
def call(event=None):
    print (user_entry.get()) #mirrors in console
        
#displays chatbot's response
# =============================================================================
# sub = ""
# def bot(event=None):
#     response = convoDemo.getResponse(msg, sub)
#     msg = "Charles: " + response
#     print(msg)
#     msg_list.insert(END, msg)
#     msg_list.yview(END)
#     user_entry.delete(0, 'end')
# =============================================================================
        
#def close(evenet=None):
    #user_entry.set
        
#conversation history
msg_frame = Frame(charles, height=340, width=450, bg="navy", cursor="star", bd=10, relief="ridge")
msg_frame.grid(row=0, column=0)
#user_msg = StringVar()
#user_msg.set("Type here")
scrollbar = Scrollbar(msg_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list = Listbox(msg_frame, height=20, width=70, yscrollcommand=scrollbar.set)
msg_list.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=msg_list.yview)

#user entry & handling
user_frame = Frame(charles, height=60, width=420, bg="blue", bd=5, relief="groove")
user_frame.grid(row=1, column=0)
lab = Label(user_frame, padx=10, text="reply here:")
lab.pack(side=LEFT)
user_entry = Entry(user_frame,width=70, textvariable="type here")
user_entry.bind("<Return>", send)
user_entry.pack(side=RIGHT)


#user reply
user_button = Button(charles, text="click here to reply", bg="blue", fg="white", relief="groove", command=send)
user_button.grid(row=2)

        

charles.mainloop()