import random
import sys


def rules():
    print("..................................")
    print("You have to guess a five letter word🙂")
    print("You will be given 6 tries to do so")
    print("here are the conventions👇")
    print("Letter is not there - !letter!")
    print("Letter is present but at wrong place - *letter*")
    print("Letter is correct and present at correct place")
    print("...................................")
    play()


def word_selection():

    #Words in Wordle
    words=['abuse', 'adult', 'agent', 'anger', 'award',  'beach', 'birth', 'block', 'board',
    'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child', 'china', 
    'claim', 'clock', 'coach', 'coast', 'court', 'cover', 'cream', 'crime',  'crowd', 'crown', 
    'dance', 'death', 'depth', 'doubt', 'draft', 'drama', 'dream',  'drink', 'drive', 'earth', 'enemy', 
    'entry','faith', 'fault', 'field', 'fight', 'fianl', 'focus', 'force', 'frame', 
    'frank', 'front', 'fruit',  'grant',  'group', 'guide', 'heart', 'henry', 'horse',
    'hotel', 'house', 'image', 'index', 'input', 'japan', 'jones', 'judge', 'knife', 'laura', 'layer',
    'lewis', 'light', 'lunch', 'major', 'march', 'match', 'metal', 'money', 'month', 'music',
    'night', 'noise', 'north', 'novel', 'nurse', 'other', 'owner', 'panel',  'party',
    'peace',  'phase', 'phone', 'piece', 'pilot', 'pitch', 'place', 'plane', 'plant', 'plate', 'point', 
    'pound', 'power', 'price', 'pride', 'prize',   'radio', 'range', 'ratio', 'reply',
    'right', 'river', 'round', 'route', 'rugby', 'scale', 'scope', 'score', 'shape', 'share',
    'shift', 'shirt', 'shock', 'sight', 'simon',  'smile', 'smith', 'smoke', 
    'sound', 'south', 'space','spite', 'sport', 'squad',  'stage', 'steam', 
    'stock', 'stone', 'store', 'study', 'style', 'sugar', 'table',  'theme', 
    'thing', 'touch', 'tower', 'track', 'trade', 'train', 'trend', 'uncle',  
    'unity', 'value', 'video',  'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman',
    'world', 'youth']

    #choosing a word randomly from the list
    return random.choice(words)


def play():
    today_word=word_selection()

    #It will give 6 tries
    for i in range(6): 
        print("Try number",i+1)                                      
    
    
        #Code begins here
        input_word=input("Enter ")
        #It sets every letter status to false and will store the changes to true or partial true accordingly
        correct=[False,False,False,False,False]
        #It comapare the letters of the today's word to the word entered one by one
        #and assigns them whether they are true or partial true or false
        for j in range(5):
            for k in range(5):
                if today_word[j]==input_word[k]:
                    if k==j:
                        correct[k]=True
                        break
                    else:
                        correct[k]="Partial True"
        
        #Checks whether all the letters are correct
        count=0
        for i in range(5):
            if correct[i]==True:
                count+=1

        #if all the letters are correct, then it prints You Won   
        if count==5:
            print("You Won")
            sys.exit(0)

        #else it prints the status of every letter using the specified symbols
        for i in range(5):
            if correct[i]==True:
                print("@"+input_word[i]+"@",end=' ')
            elif correct[i]=="Partial True":
                print("*"+input_word[i]+"*",end=' ')
            else:
                print("!"+input_word[i]+"!",end=' ')

    if (count!=5):
        print("Sorry ! try again")
        print("The word was",today_word)     
                         
#User code
print("Enter")
print("Play-P")
print("Rules-R")
command_1=input()

if command_1=='R':
    rules()
elif command_1=='P':
    play()
else:
    print("Wrong Command")
