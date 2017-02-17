import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    valid = 0
    if type(lettersGuessed) == list:
        for guess in lettersGuessed:
            for letter in secretWord:
                if guess == letter:
                    valid += 1
    if valid >= len(secretWord):
        return True
    else: 
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = []
    answer = ""
    for i in secretWord:
        result.append(" _ ")
    if type(lettersGuessed) == list:
        for guess in lettersGuessed:
            count = 0
            for letter in secretWord:
                if guess == letter:
                    result[count] = guess
                count += 1
            
    for length in range(len(result)):
        answer += result[length]
    return answer  


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lowercase = string.ascii_lowercase
    if type(lettersGuessed) == list:
        for i in lettersGuessed:
            lowercase = lowercase.replace(i,"")
    return lowercase
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

   
    '''
    lettersGuessed = []
    left = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word", len(secretWord), "letters long.")
    print("-----------")
    while left > 0:
        if isWordGuessed(secretWord,lettersGuessed):
            return("Congratulations, you won!")

        print("You have", left, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        
        guess = input("Please guess a letter:")
        guess = guess.lower()
        
        while guess not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
            print("You have", left, "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter:")
            
        lettersGuessed.append(guess)
        
        if guess in secretWord:
            print("Good guess:", getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
        elif guess not in secretWord:
            left -= 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord,lettersGuessed))
            print("-----------")
    return("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")


secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))