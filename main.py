#--------------------------------------------------------------------------------------------------------------
"""
Date: 09/07/2023
Developed by: Dinesh Singh

About the project:- In this project you have to guess all the states of india and every time your guess will correct,
the guessed state name will locate to the map. You have to guess as many as possible but when you stuck you can exit by
giving "exit" command. The remaining state will saved to state to lear.csv
if file:
"""
#--------------------------------------------------------------------------------------------------------------
#TODO 1: Import necessary modules
import turtle
from turtle import Turtle, Screen
import pandas as pd
#--------------------------------------------------------------------------------------------------------------
#TODO 2(a): Initialize map
map = Screen()
map.title("Guess the Indian States")
map.setup(width=410,height=470)
map.cv._rootwindow.resizable(False,False)
map._root.iconbitmap("AppIcon.ico")
map_image = "India-state.gif"
map.addshape(map_image) #adding map_image as shape
turtle.shape(map_image)
turtle.shapesize(stretch_wid=2,stretch_len=2)
#--------------------------------------------------------------------------------------------------------------
#Get the x and y value where we click on the turtle screen
# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor) #important
#--------------------------------------------------------------------------------------------------------------
#TODO 4: Load and create a list of states
states_df = pd.read_csv("states_data.csv")
state_list = states_df["state"].to_list()
#--------------------------------------------------------------------------------------------------------------
total_states = len(state_list)
guess_states = 0
#--------------------------------------------------------------------------------------------------------------
#TODO 6: Create Iteration
while state_list:
    #--------------------------------------------------------------------------------------------------------------
    #TODO 3: Prompt player to guess state
    answer = map.textinput(f"{guess_states}/{total_states}","What's another state's name?").title()
    #--------------------------------------------------------------------------------------------------------------
    #TODO 7: code to exit the game and generate state_to_learn.csv of all missed states
    if answer == "Exit":
        state_dict = {
                        "state": [],
                        "x" : [],
                        "y" : []
                      }
        for state in state_list:
            state_dict["state"].append(state)
            state_dict["x"].append(states_df[states_df["state"] == state]["x"].item())
            state_dict["y"].append(states_df[states_df["state"] == state]["y"].item())
        state_to_learn = pd.DataFrame(state_dict)
        state_to_learn.to_csv("state_to_learn")
        exit()
    #--------------------------------------------------------------------------------------------------------------
    if answer in state_list:
        #TODO 5: get the coordinate of the state
        x = states_df[states_df["state"] == answer]["x"].item()
        y = states_df[states_df["state"] == answer]["y"].item()
        coor = (x,y)
        #TODO 6: Create state pointer and point the state in map
        state_pointer = Turtle()
        state_pointer.seth(90)
        state_pointer.penup()
        state_pointer.fillcolor("black")
        state_pointer.goto(coor)
        state_pointer.write(f"{answer}",align="center",font=("courier",8,"bold"))
        state_list.remove(answer)
        guess_states += 1

#TODO 8: clear state_to_clearn.csv to empty when guessed all
state_to_learn = pd.DataFrame({})
state_to_learn.to_csv("state_to_learn")
#--------------------------------------------------------------------------------------------------------------
#TODO 2(b): make screen visible until close
turtle.mainloop()
#--------------------------------------------------------------------------------------------------------------
