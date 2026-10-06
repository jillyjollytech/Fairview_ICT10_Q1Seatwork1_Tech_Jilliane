from pyscript import document, display

display(target="div1") #literal object

#variable objects

name = "Jilliane Tech" #string 

age = 15 #int 

height1 = 165 #float 

dream_destination = ["China", "Japan", "Italy"] #list 

student_type = False #boolean

preferences = {"color" : "sage green",
     "car_brand" : "Aston Martin",
     "shoe_size" : "8",
     "best_friend" : "TJ Sales"
} #dictionary 

favorite_fruits = {"grapes", 
"mango", 
"pomegranate",
"passion fruit"
} #set 

daysoftheweek = (
"Monday", 
"Tuesday", 
"Wednesday", 
"Thursday", 
"Friday", 
"Saturday", 
"Sunday"
) #tuple 

display("Name: " + name, target="div1")
display("Age: " + str(age), target="div1")
display("Height(cm): " + str(height1), target="div1")
display("Dream Destinations: " + str(dream_destination), target="div1")
display("Student Type: " + str(student_type), target="div1")
display("Preferences: " + str(preferences), target="div1")
display("Favorite Fruits: " + str(favorite_fruits), target="div1")
display("Days of the Week: " + str(daysoftheweek), target="div1")

def adding_numbers(e):
    document.getElementById("div2").innerHTML = "" # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st input
    num2 = float(document.getElementById('input2').value) # get 2nd input
    result = num1 + num2 #use operator to compute/add
    display(result, target = "div2") #display output in div
