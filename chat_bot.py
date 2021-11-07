from tkinter import *                       
from random import choice    
import webbrowser                   

with open('greetings.txt') as f:
    greetings = [line.rstrip() for line in f]

with open('greeting_response.txt') as f:
    greeting_response = [line.rstrip() for line in f]

with open('symptoms.txt') as f:
    urgent_symptoms = [line.rstrip() for line in f]

with open('symptoms_response.txt') as f:
    symptoms_response = [line.rstrip() for line in f]

                         
error = ["please type something else", "invalid text","try again please" ]            
                                                                    
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
                                    
root.title("*Brain Health*")                     
Label(root, text=" You : ").pack(side=LEFT)                
Entry(root, textvariable=user).pack(side=LEFT)          
Label(root, text=" Helper  : ").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT)   
                               
                                
def main():                             
    question = user.get()                        
    if question in greetings:                      
        bot.set(choice(greeting_response))
    elif question in urgent_symptoms:
        bot.set(choice(symptoms_response))
    elif question == "Queen's University" or question in "St Lawrence College" or question in "RMC":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/kingston?authuser=0"))
    elif question in "Concordia" or question in "McGill":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/montreal?authuser=0"))
    elif question == "University of Toronto" or question in "OCAD" or question in "Ryerson" or question in "University of Trinity College" or question in "York University":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/toronto?authuser=0"))
    elif question == "McMaster":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/hamilton?authuser=0"))
    elif question == "Western" or question in "Huron University College" or question in "King’s University College":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/london?authuser=0"))
    elif question == "Carleton" or question in "University of Ottawa":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/ottawa?authuser=0"))
    elif question == "University of Waterloo" or question in " Wilfrid Laurier University":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/waterloo?authuser=0"))
    elif question == "Brock University":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/st-catherines?authuser=0"))
    elif question == "Nipissing University":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/north-bay?authuser=0"))
    elif question == "Trent":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/peterborough?authuser=0"))
    elif question == "University of Guelph":
        bot.set(webbrowser.open("https://sites.google.com/view/brainhealthresources/guelph?authuser=0"))
    else:                                
        bot.set(choice(error))                 
                                
Button(root, text="SEND", command=main).pack(side=LEFT)        
                                    
mainloop()                              