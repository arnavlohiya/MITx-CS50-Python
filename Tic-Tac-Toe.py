#!/usr/bin/env python
# coding: utf-8

# In[7]:


class tictactoe(object):
    
    def __init__(self):
        self.starting_board=[0,1,2,3,4,5,6,7,8,9]
        
    def gameOver(self,current_board):
        #horitontal sequence check
        if (self.starting_board[1]==self.starting_board[2]==self.starting_board[3]):
            return (True,self.starting_board[1])
        
        elif(self.starting_board[4]==self.starting_board[5]==self.starting_board[6]):
            return (True,self.starting_board[4])
        
        elif(self.starting_board[7]==self.starting_board[8]==self.starting_board[9]):
            return (True,self.starting_board[7])
        
        #vertical sequence check
        elif(self.starting_board[1]==self.starting_board[4]==self.starting_board[7]):
            return (True,self.starting_board[1])
        
        elif(self.starting_board[2]==self.starting_board[5]==self.starting_board[8]):
            return (True,self.starting_board[2])
        
        elif(self.starting_board[3]==self.starting_board[6]==self.starting_board[9]):
            return (True,self.starting_board[3])
        
        #diagonal sequence check
        elif(self.starting_board[1]==self.starting_board[5]==self.starting_board[9]):
            return (True,self.starting_board[1])
        
        elif(self.starting_board[3]==self.starting_board[5]==self.starting_board[7]):
            return (True,self.starting_board[3])
        else:
            return False
        
        
        
    def gameTie(self):
        element_counter=0
        for element in self.starting_board:
            if str(element).isnumeric():
                element_counter+=1
        if element_counter==1:
            return True
        else:
            return False
    
    
    def playGame(self):
        check=True
        while(check):
            player1_letter=str(input("Player 1, Please Enter your preference (O or X):"))
            if player1_letter.upper()=='X':
                player2_letter='O'
                check=False
            elif player1_letter.upper()=='O':
                player2_letter="X"
                check=False
            else:
                print('Please make sure you have entered a valid letter and try again')
                
        print('Welcome to tic tac toe! Each player will have to enter a position on the board as an integer based on where they would like to place their letter.')
        print('The game would be won if a player successfully places 3 consecutive letters on the board in any direction')        
        
        player_counter=1
        while((self.gameOver(self.starting_board))==False):
            if (self.gameTie()):
                break
            print(self.starting_board[1],'|',self.starting_board[2],'|',self.starting_board[3])
            print(self.starting_board[4],'|',self.starting_board[5],'|',self.starting_board[6])
            print(self.starting_board[7],'|',self.starting_board[8],'|',self.starting_board[9])
            if(player_counter%2==0):
                self.player_to_play=2
            else:
                self.player_to_play=1
                
            if(self.player_to_play==1):
                print_letter=player1_letter
            else:
                print_letter=player2_letter
                
            player_move=int(input('Player '+str(self.player_to_play)+',('+print_letter+') please make a move:'))
            
            if(player_move in self.starting_board):
                index_to_change=self.starting_board.index(player_move)
                if self.player_to_play==1:
                    self.starting_board[index_to_change]=player1_letter
                    player_counter+=1
                else:
                    self.starting_board[index_to_change]=player2_letter
                    player_counter+=1
            else:
                print('Please enter a valid input')
        
        
        if self.gameTie():
            print('The game has been tied..')
        else:
            player_counter-=1  
            print(self.starting_board[1],'|',self.starting_board[2],'|',self.starting_board[3])
            print(self.starting_board[4],'|',self.starting_board[5],'|',self.starting_board[6])
            print(self.starting_board[7],'|',self.starting_board[8],'|',self.starting_board[9])
            print('Congratulations player '+str(self.player_to_play)+' you have won the game!!')
        
testGame=tictactoe()
testGame.playGame()

