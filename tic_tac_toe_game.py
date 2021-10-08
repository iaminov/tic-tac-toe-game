Isakhar (Alex) Aminov

Tic-Tac-Toe

import tkFont
from Tkinter import *
from random import Random,random

#Sets up global variables for the current turn and the status of the game (using a list).
turn = 1
gameList = [['','',''] ,['','',''],['','','']]

#Sets up the initial screen which contains a button for versus play and a button for computer play.
def addWidgets_firstScreen(window):
    versusButton = Button(window, text='Press for Versus Play', command = versus_grid_maker)
    compButton = Button(window, text='Press to play against the computer', command = CPU_grid_maker)
    versusButton.pack()
    compButton.pack()

#Takes the current status of the game and returns either who won, if it is a tie,
#or if the game is still in progress.
def gameWinner(gameList,turn):
    if gameList[0][0]==gameList[0][1]==gameList[0][2]!='':
        return "Player %s wins." % gameList[0][0].upper()
    elif gameList[1][0]==gameList[1][1]==gameList[1][2]!='':
        return "Player %s wins." % gameList[1][0].upper()
    elif gameList[2][0]==gameList[2][1]==gameList[2][2]!='':
        return "Player %s wins." % gameList[2][0].upper()
    elif gameList[0][0]==gameList[1][0]==gameList[2][0]!='':
        return "Player %s wins." % gameList[0][0].upper()
    elif gameList[0][1]==gameList[1][1]==gameList[2][1]!='':
        return "Player %s wins." % gameList[0][1].upper()
    elif gameList[0][2]==gameList[1][2]==gameList[2][2]!='':
        return "Player %s wins." % gameList[0][2].upper()
    elif gameList[0][0]==gameList[1][1]==gameList[2][2]!='':
        return "Player %s wins." % gameList[0][0].upper()
    elif gameList[0][2]==gameList[1][1]==gameList[2][0]!='':
        return "Player %s wins." % gameList[0][2].upper()
    elif turn == 10:
        return "The game is a tie."
    else:
        return "not done"

#Takes the current turn and determines if X is going or if O is going (X always goes first).    
def currentLetter(turn):
    current=''
    if turn == 1:
        current = 'x'
    elif turn%2 == 0:
        current = 'o'
    else:
        current = 'x'
    return current
        
#Sets up grid for versus play.
def versus_grid_maker():
    
    #Defines what happens when a box is pressed.
    def press(event):
        global turn
        global gameList
        if gameWinner(gameList,turn) == 'not done':
            if event.x>30 and event.x<143 and event.y>30 and event.y<143 and gameList[0][0]=='':
                grid.create_text(86,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>30 and event.y<143 and gameList[0][1]=='':
                grid.create_text(189,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>30 and event.y<143 and gameList[0][2]=='':
                grid.create_text(312,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][2]=currentLetter(turn)
                turn = turn + 1
            if event.x>30 and event.x<143 and event.y>143 and event.y<256 and gameList[1][0]=='':
                grid.create_text(86,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>143 and event.y<256 and gameList[1][1]=='':
                grid.create_text(189,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>143 and event.y<256 and gameList[1][2]=='':
                grid.create_text(312,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][2]=currentLetter(turn)
                turn = turn + 1
            if event.x>30 and event.x<143 and event.y>256 and event.y<370 and gameList[2][0]=='':
                grid.create_text(86,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>256 and event.y<370 and gameList[2][1]=='':
                grid.create_text(189,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>256 and event.y<370 and gameList[2][2]=='':
                grid.create_text(312,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][2]=currentLetter(turn)
                turn = turn + 1
            if gameWinner(gameList,turn) != 'not done':
                grid.create_text(100,394,text=gameWinner(gameList,turn))
        
    #Gets rid of the original window and creates a Tic-Tac-Toe grid.
    global game_window
    game_window.destroy()
    global new_window
    new_window=Tk()
    grid=Canvas(new_window,height=400,width=400)
    grid.pack()
    grid.create_line(143,30,143,370)
    grid.create_line(256,30,256,370)
    grid.create_line(30,143,370,143)
    grid.create_line(30,256,370,256)
    grid.bind('<Button-1>',press)
    new_window.title("Tic-Tac-Toe")
    new_window.mainloop()


#Sets up the game for computer play. The person always goes first.
def CPU_grid_maker():
    
    #Converts an index in gameList to a graphical coordinate.
    def listToCoordinate(location):
        box1=[86,86]
        box2=[189,86]
        box3=[312,86]
        box4=[86,189]
        box5=[189,189]
        box6=[312,189]
        box7=[86,312]
        box8=[189,312]
        box9=[312,312]
        if location==[0,0]:
            return box1
        elif location==[0,1]:
            return box2
        elif location==[0,2]:
            return box3
        elif location==[1,0]:
            return box4
        elif location==[1,1]:
            return box5
        elif location==[1,2]:
            return box6
        elif location==[2,0]:
            return box7
        elif location==[2,1]:
            return box8
        elif location==[2,2]:
            return box9

    #Takes string, which is either an 'x' or an 'o', and determines if that letter
    #occupies two boxes in a row. It then returns the location of the unoccupied box.
    def row_2_checker(string):
        global gameList
        location1 = []
        if gameList[0][0] == gameList[0][1] == string and gameList[0][2]=='':
            location1=[0,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][0] == gameList[0][2] == string and gameList[0][1]=='':
            location1=[0,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][1] == gameList[0][2] == string and gameList[0][0]=='':
            location1=[0,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][0] == gameList[1][1] == string and gameList[1][2]=='':
            location1=[1,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][0] == gameList[1][2] == string and gameList[1][1]=='':
            location1=[1,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][1] == gameList[1][2] == string and gameList[1][0]=='':
            location1=[1,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[2][0] == gameList[2][1] == string and gameList[2][2]=='':
            location1=[2,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[2][0] == gameList[2][2] == string and gameList[2][1]=='':
            location1=[2,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[2][1] == gameList[2][2] == string and gameList[2][0]=='':
            location1=[2,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][0] == gameList[1][1] == string and gameList[2][2]=='':
            location1=[2,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][0] == gameList[2][2] == string and gameList[1][1]=='':
            location1=[1,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][1] == gameList[2][2] == string and gameList[0][0]=='':
            location1=[0,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][2] == gameList[1][1] == string and gameList[2][0]=='':
            location1=[2,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[2][0] == gameList[0][2] == string and gameList[1][1]=='':
            location1=[1,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[2][0] == gameList[1][1] == string and gameList[0][2]=='':
            location1=[0,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][0] == gameList[1][0] == string and gameList[2][0]=='':
            location1=[2,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][0] == gameList[2][0] == string and gameList[1][0]=='':
            location1=[1,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][0] == gameList[2][0] == string and gameList[0][0]=='':
            location1=[0,0]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][1] == gameList[1][1] == string and gameList[2][1]=='':
            location1=[2,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][1] == gameList[2][1] == string and gameList[0][1]=='':
            location1=[0,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][1] == gameList[2][1] == string and gameList[1][1]=='':
            location1=[1,1]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][2] == gameList[1][2] == string and gameList[2][2]=='':
            location1=[2,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[0][2] == gameList[2][2] == string and gameList[1][2]=='':
            location1=[1,2]
            return 'true',location1,listToCoordinate(location1)
        elif gameList[1][2] == gameList[2][2] == string and gameList[0][2]=='' :
            location1=[0,2]
            return 'true',location1,listToCoordinate(location1)
        else:
            return 'false'
        
    #Checks to see if the computer occupies 2 boxes in a row and returns the value of the unoccupied
    #box (both the index in gameList and the graphical coordinates).
    def computer_2_row():
        return row_2_checker('o')
        
    #Checks whether the opponent occupies 2 boxes in a row and returns the value of the unoccupied
    #box (both the index in gameList and the graphical coordinates).
    def opponent_2_row():
        return row_2_checker('x')

    #Checks to see if the center is occupied or not.
    def center_open():
        global gameList
        if gameList[1][1] == '':
            return 'true'
        else:
            return 'false'

    #Checks to see if opponent has two opposite corners taken (which will allow an easy victory) and
    #returns any available side box that can be taken.
    def opposites_taken():
        if gameList[0][0]==gameList[2][2]=='x':
            if gameList[0][1]=='':
                return 'true',[0,1],listToCoordinate([0,1])
            elif gameList[1][0]=='':
                return 'true',[1,0],listToCoordinate([1,0])
            elif gameList[1][2]=='':
                return 'true',[1,2],listToCoordinate([1,2])
            elif gameList[2][1]=='':
                return 'true',[2,1],listToCoordinate([2,1])
        elif gameList[2][0]==gameList[0][2]=='x':
            if gameList[0][1]=='':
                return 'true',[0,1],listToCoordinate([0,1])
            elif gameList[1][0]=='':
                return 'true',[1,0],listToCoordinate([1,0])
            elif gameList[1][2]=='':
                return 'true',[1,2],listToCoordinate([1,2])
            elif gameList[2][1]=='':
                return 'true',[2,1],listToCoordinate([2,1])
        else:
            return 'false'
        
    #Checks to see if any corner is open and returns the value of the first available corner.     
    def corner_open():
        global gameList
        location3 = []
        if gameList[0][0]=='':
            location3 = [0,0]
            return 'true',location3,listToCoordinate(location3)
        elif gameList[2][0]=='':
            location3 = [2,0]
            return 'true',location3,listToCoordinate(location3)
        elif gameList[0][2]=='':
            location3 = [0,2]
            return 'true',location3,listToCoordinate(location3)
        elif gameList[2][2]=='':
            location3 = [2,2]
            return 'true',location3,listToCoordinate(location3)
        else:
            return 'false'
            
        
        
    #Returns a random index to be used in gameList and the associated coordinate in the grid.
    def random_grid():
        box1=[86,86]
        box2=[189,86]
        box3=[312,86]
        box4=[86,189]
        box5=[189,189]
        box6=[312,189]
        box7=[86,312]
        box8=[189,312]
        box9=[312,312]
        listGrid1=[0,0]
        listGrid2=[0,1]
        listGrid3=[0,2]
        listGrid4=[1,0]
        listGrid5=[1,1]
        listGrid6=[1,2]
        listGrid7=[2,0]
        listGrid8=[2,1]
        listGrid9=[2,2]
        random_number = Random()
        box=[]
        listGrid=[]

        if random_number.random() < .1:
            box=box1
            listGrid=listGrid1
        elif random_number.random() < .2:
            box=box2
            listGrid=listGrid2
        elif random_number.random() < .3:
            box=box3
            listGrid=listGrid3
        elif random_number.random() < .4:
            box=box4
            listGrid=listGrid4
        elif random_number.random() < .5:
            box=box5
            listGrid=listGrid5
        elif random_number.random() < .6:
            box=box6
            listGrid=listGrid6
        elif random_number.random() < .7:
            box=box7
            listGrid=listGrid7
        elif random_number.random() < .8:
            box=box8
            listGrid=listGrid8
        else:
            box=box9
            listGrid=listGrid9
        return box, listGrid

    #Defines the strategy that the computer takes. **This strategy is unbeatable.** The computer
    #will always either win or tie.
    #
    #First the computer checks whether it occupies two boxes in a row. If it does, it takes the
    #third box and wins.
    #Then the computer checks whether the opponent occupies two boxes in a row. If it does,
    #it blocks the opponent from winning by taking the third box.
    #Then the computer checks whether the center is available, and takes it if it is.
    #The computer then checks to see if the opponent has taken 2 opposite corners, allowing
    #an easy victory, and stops it by taking an empty side box (side box meaning
    #non-corner and non-center).
    #The computer then checks to see if a corner is available, and takes the first available corner.
    #If none of these moves is possible, the computer goes to a random box.
    def cpu_turn():
        global gameList
        global turn
        locationFinal=[]
        comp2row=computer_2_row()
        opp2row=opponent_2_row()
        opp_taken=opposites_taken()
        corn=corner_open()
        txt=''
        
        if gameWinner(gameList,turn)=='not done':
            if comp2row[0]=='true':
                locationFinal=comp2row[1]
                gameList[locationFinal[0]][locationFinal[1]]=currentLetter(turn)
                graph=comp2row[2]
                grid2.create_text(graph[0],graph[1],font=tkFont.Font(size=100),text=currentLetter(turn))
            elif opp2row[0]=='true':
                locationFinal=opp2row[1]
                gameList[locationFinal[0]][locationFinal[1]]=currentLetter(turn)
                graph=opp2row[2]
                grid2.create_text(graph[0],graph[1],font=tkFont.Font(size=100),text=currentLetter(turn))
            elif center_open()=='true':
                gameList[1][1]=currentLetter(turn)
                grid2.create_text(189,189,font=tkFont.Font(size=100),text=currentLetter(turn))
            elif opp_taken[0]=='true':
                locationFinal=opp_taken[1]
                gameList[locationFinal[0]][locationFinal[1]]=currentLetter(turn)
                graph=opp_taken[2]
                grid2.create_text(graph[0],graph[1],font=tkFont.Font(size=100),text=currentLetter(turn))
            elif corn[0]=='true':
                locationFinal=corn[1]
                gameList[locationFinal[0]][locationFinal[1]]=currentLetter(turn)
                graph=corn[2]
                grid2.create_text(graph[0],graph[1],font=tkFont.Font(size=100),text=currentLetter(turn))
            else:
                infoList = random_grid()
                while gameList[infoList[1][0]][infoList[1][1]]!='':
                    infoList = random_grid()
                grid2.create_text(infoList[0][0],infoList[0][1],font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[infoList[1][0]][infoList[1][1]]=currentLetter(turn)
        else:
            if gameWinner(gameList, turn)=='Player X wins.':
                txt='You win.'
            elif gameWinner(gameList, turn)=='Player O wins.':
                txt='The computer wins.'
            elif gameWinner(gameList, turn)=='The game is a tie.':
                txt='The game is a tie.'
            grid2.create_text(100,394,text=txt)
            
        turn = turn + 1
        
            

        
    #Defines what happens when a box is pressed. The computer goes after the player goes.
    def press(event):
        global turn
        global gameList
        txt=''
        
        if gameWinner(gameList,turn) == 'not done':
            if event.x>30 and event.x<143 and event.y>30 and event.y<143 and gameList[0][0]=='':
                grid2.create_text(86,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>30 and event.y<143 and gameList[0][1]=='':
                grid2.create_text(189,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>30 and event.y<143 and gameList[0][2]=='':
                grid2.create_text(312,86,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[0][2]=currentLetter(turn)
                turn = turn + 1
            if event.x>30 and event.x<143 and event.y>143 and event.y<256 and gameList[1][0]=='':
                grid2.create_text(86,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>143 and event.y<256 and gameList[1][1]=='':
                grid2.create_text(189,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>143 and event.y<256 and gameList[1][2]=='':
                grid2.create_text(312,189,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[1][2]=currentLetter(turn)
                turn = turn + 1
            if event.x>30 and event.x<143 and event.y>256 and event.y<370 and gameList[2][0]=='':
                grid2.create_text(86,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][0]=currentLetter(turn)
                turn = turn + 1
            if event.x>143 and event.x<256 and event.y>256 and event.y<370 and gameList[2][1]=='':
                grid2.create_text(189,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][1]=currentLetter(turn)
                turn = turn + 1
            if event.x>256 and event.x<370 and event.y>256 and event.y<370 and gameList[2][2]=='':
                grid2.create_text(312,312,font=tkFont.Font(size=100),text=currentLetter(turn))
                gameList[2][2]=currentLetter(turn)
                turn = turn + 1
            cpu_turn()
        if gameWinner(gameList,turn)!='not done':
            if gameWinner(gameList, turn)=='Player X wins.':
                txt='You win.'
            elif gameWinner(gameList, turn)=='Player O wins.':
                txt='The computer wins.'
            elif gameWinner(gameList, turn)=='The game is a tie.':
                txt='The game is a tie.'
            grid2.create_text(100,394,text=txt)
            

                    
    
    #Gets rid of the original window and creates a Tic-Tac-Toe grid.
    global game_window
    game_window.destroy()
    cpu_window = Tk()
    grid2 = Canvas(cpu_window,height=400,width=400)
    grid2.pack()
    grid2.create_line(143,30,143,370)
    grid2.create_line(256,30,256,370)
    grid2.create_line(30,143,370,143)
    grid2.create_line(30,256,370,256)
    grid2.bind('<Button-1>',press)
    cpu_window.title("Tic-Tac-Toe")
    cpu_window.mainloop()

#main() creates a window which runs the start screen.
def main():
    global game_window
    game_window = Tk()
    game_window.title("Tic-Tac-Toe")
    addWidgets_firstScreen(game_window)
    game_window.mainloop()


main()
