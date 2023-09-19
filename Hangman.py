#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    a=''
    for letters in secretWord:
        if letters in lettersGuessed:
            a=a+letters
        else:
            a=a+ ' _'
    return a



secretWord='arnav'
lettersGuessed=[]
def hangman(secretWord):
    import string
    
    global availableLetters
    availableLetters= string.ascii_lowercase
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+ ' letters long')
    print('-----------')
    guesses_left=8
    while guesses_left>0:
        print('You have '+str(guesses_left)+' guesses left')
        print('Available letters: '+str(availableLetters))
        guess_word= input('Please guess a letter: ')
        
        if guess_word in lettersGuessed:
            print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord,lettersGuessed))
        elif guess_word in secretWord:
            lettersGuessed.append(guess_word)
            print('Good guess: '+ getGuessedWord(secretWord,lettersGuessed))
        
        elif guess_word not in secretWord:
            print('Oops! That letter is not in my word: '+getGuessedWord(secretWord,lettersGuessed))
            guesses_left-=1
        if isWordGuessed(secretWord,lettersGuessed):
            print('-----------')
            print('Congratulations, you won!')
            break
            
        a=''
        for letter in availableLetters:
            if guess_word!=letter:
                a+=letter
        availableLetters=a
        
    
    if guesses_left==0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was '+secretWord)
        
        
hangman('Computer')

