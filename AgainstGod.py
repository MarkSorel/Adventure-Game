import time

names = ['sigfrid', 'sigfrido']
movements = ['r', 'l', 'j', 'a', 'A', 'b', 'db']
af_neg = ['yes', 'y', 'no', 'n']


# First function created for RUN alternative
def get_run():
    print('The dragon looks pretty strong, I will not be able to handle this...')
    time.sleep(3)
    print('I better walk carefully, before he realize I am here...')
    time.sleep(2)

    print()
    print('''
                        ....... * noise * .......
    ''')
    time.sleep(2)
    print()

    time.sleep(1)
    print('...Oh no, he has waken up, I better run right away..')
    time.sleep(3)

    print()
    print('''
                                ... Roaaaaaarr...
    
    ''')
    print()
    time.sleep(2)
    print('''
            * Inmediately the dragon rips you appart, and there is blood all over the place... *
     ''')
    time.sleep(2)
    print('''
            ... You are dead...
    ''')
    print()
    print('------------------------------ * GAME OVER * ------------------------------')
    print()

    print('''
Press 'X', if you want to restart or exit the game...
Press 'W', if you want to restart the battle...
        ''')
    print()
    option = input('>> ')
    print()

    while option.lower() != 'x' and option.lower() != 'w':
        print('''I do not know what you mean, say that again...''')
        print()
        option = input('>> ')
        print()

    if option.lower() == 'x':
        exit_game()
    elif option.lower() == 'w':
        check_cave2(2)


# Option to ask something to the Dragon...
def get_question():
    time.sleep(2)
    print('''As an ancient Dragon, he must have a wide knowledge about the world, and it's origins... ''')
    time.sleep(3)
    print()
    print('''I better kneel down, and show respect, otherwise I may end up dying horribly...
    ''')
    time.sleep(4)
    print()
    print('''
                        ... * Roaaaaaar *... 
    ''')
    print()
    time.sleep(3)
    print(''' 
            ..... * Humans are all the same, always stingy, greedy and cowards...
            But you are special, you must be Sigfrid, right? heh...
            Your reputation is vast... even I know who are you... 
            As I have the honor of meeting you, let me tell you a story, that you may consider 
                        vital for your race... *        
    ''')
    time.sleep(8)
    print('''
            ..... * Long time ago, my race was peacefully living 
                            in our own dimension, far away fron here... *

    ''')
    time.sleep(4)
    print('''
            ..... * until that day came... The demon race obliged us to 
                        abandon our home... When we refuse most of my camarades 
                            were killed, few of us manage to scape but wounded...  *       
    ''')
    time.sleep(5)
    print('''
            ..... * I was one of those that manage to survive, the rest are lost 
                        in every corner of this world... Those demons were really powerful, 
                            their abilities and weaponry were something we could not handle... *
    ''')
    time.sleep(6)
    print('''
            ...... * Am pretty old right now to do something about it, despite the fact 
                            I am fill with hatred...
                                I was just leaving till now for revenge, but ... *
    ''')
    time.sleep(5)
    print('''
            ..... * But now, dying would be the best medicine for my soul... *
    ''')
    time.sleep(3)
    print()
    print('------------------------------ * GAME OVER * ------------------------------')
    print()

    print('''
Press 'X', if you want to restart or exit the game...
Press 'W', if you want to restart the battle...
    ''')
    print()
    option = input('>> ')
    print()

    while option.lower() != 'x' and option.lower() != 'w':
        print('''I do not know what you mean, say that again...''')
        print()
        option = input('>> ')
        print()

    if option.lower() == 'x':
        exit_game()
    elif option.lower() == 'w':
        check_cave2(2)


def restart_game():
    play_again = 'yes'

    while play_again == 'yes' or play_again == 'y':
        cave_num = choose_cave()

        check_cave(cave_num)

        print('Do you want to play again? (yes or no)')
        print()
        play_again = input('>> ')
        print()

        while play_again not in af_neg:
            print('''I do not know what you mean, say that again...''')
            print()
            play_again = input('>> ')
            print()


def exit_game():
    print()
    time.sleep(2)
    print('''
            ... Thanks for playing...
    ''')
    print()
    time.sleep(1)


def display_intro():

    time.sleep(2)
    print('''
    Our hero, Sigfrid, son of Sigmund and Sigelinda, was born in Niderland, north of Denmark.
            Being a kid, he left the castle looking for adventures... 
                soon became famous because of his amazing feats... 
        thanks to the bright and powerful sword, Belmung, that was given by his father.
    ''')
    time.sleep(8)
    print('''
    After having defeated most of the heros of Denmark, our hero was summoned by the king of
    Iceland, called Hagen The Wise, due to his inmense knowledge and great advices...
    ''')
    time.sleep(6)
    print('''
    His daughter is in great danger, she was poisoned by a dark magician in revenge against
            the king, and the only cure was the blood of an ancient Dragon.   
    ''')
    time.sleep(6)
    print('''
    This enormous task was entrusted to Sigfrid, who get on board to this adventure, and
    found himself at the hills of Worms. There are, before him, 3 caves where he is 
                        going to face his destiny... 
    ''')
    time.sleep(6)


# Defining cave of three paths
def choose_cave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1, 2 or 3)')
        print()
        cave = input('>> ')
        print()
    return cave


# Defining cave of two paths
def choose_secondcave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        print()
        cave = input('>> ')
        print()
    return cave


# Let's choose a new path
def choose_path():
    path = ''
    while path != '1' and path != '2':
        print('Which path you want to take? (1 or 2)')
        print()
        path = input('>> ')
        print()

    return path


# Let's check the first cave
def check_cave1(cave):
    print('What a weird cave...')
    time.sleep(2)
    print("It's getting darker..")
    time.sleep(3)
    print()
    print()
    print(''' 
... Whew!! Hopefully I manage to see it, a huge abyss...
    ''')
    time.sleep(3)
    print()
    print('''
This is going to be tough... I better try to do something to get to the extreme of the abyss...
    ''')
    time.sleep(4)
    print('''
What is this? Something is getting stuck in my feet...
... I cannot get away...
    ''')
    time.sleep(3)
    print('''
                    ... Your are dead..
    ''')
    time.sleep(2)
    print()
    print()
    print('------------------------------ * GAME OVER * ------------------------------')
    print()


# We define the function which is going to kill the dragon
def kill_dragon():
    print()
    print()
    time.sleep(3)
    print('''
... Where am I? ...
    ''')
    time.sleep(2)
    print('''
 ... It's getting too hot over here...    
    ''')

    print('''
                  --- * INSTRUCTIONS * ---
                For moving to the right: 'r'
                For moving to the left: 'l'
                For jumping: 'j'
                For attacking with sword: 'a'
                For double attack with swords: 'A'
                For using Belmung's special ability: 'b'
                For using Double sword special ability: 'db'
                            
        ''')
    time.sleep(9)

    print()
    print('''
... I'm starting this, as I'm going to end it as well...
        ''')
    time.sleep(3)

    print('''
                .... * Ohh, Sigfrid!! I knew you would come one day... 
             I did not believe Nibelung's words when they tried to warn me...*
        ''')
    time.sleep(3)
    print('''
... I'm here for your blood, Fafnir, you...    
    ''')
    time.sleep(0.5)
    print('''
                 ... * Roaaaaar.....* ...
    ''')
    time.sleep(2)
    print('''
... Here's coming, and is quite fast, I must do something quickly...
        ''')
    print()
    decision = input('>> ')
    print()

    # LEFT DECISION AND ATTACK WITH ONE SWORD DECISION
    while decision == 'l' or decision == 'a' or decision == 'A' or decision not in movements or decision == 'j':
        if decision == 'l':
            print('''
... There's a path covered by rocks that way, I must do something else...
            ''')
            print()
            decision = input('>> ')
            print()

        elif decision == 'j':
            print('''
... I'm  going to run out of energy pretty soon, I must choose something else...
                        ''')
            print()
            decision = input('>> ')
            print()

        elif decision == 'a':
            print('''
... If I attack that way, I'll going to get caught in his flames...
                        ''')
            print()
            decision = input('>> ')
            print()

        elif decision == 'A':
            print('''
... I must wait for the right time to use Notung, otherwise he's goint to notice it...
            ''')
            time.sleep(2)
            print('''
... Yeah, another choice would be better...
            ''')
            time.sleep(1)
            print()
            decision = input('>> ')
            print()

        elif decision == 'db':
            print('''
... Fafnir must not see my final attack, till I got the chance to do show it...
            ''')
            print()
            decision = input('>> ')
            print()


        elif decision not in movements:
            print('''I do not know what you mean, say that again...''')
            print()
            decision = input('>> ')
            print()

    # RIGHT DECISION
    if decision == 'r':
        print('''
... A small lake in this part of the cave... I hadn't seen it before here...
                ''')
        time.sleep(4)
        print('''
 Better I hide for a sec... and wait till he gets distracted...
        ''')
        time.sleep(4)
        print('''
                    .... * Where are you, Sigfrid?? Are you a coward?..
                            ... Come here and fight properly...
            ''')
        time.sleep(4)
        print('''
... Here's my chance...
            ''')
        time.sleep(3)
        print('''
                    ..... * I see you, damn human...
                            ... Die....
                                    --- Roaaar....
            ''')
        time.sleep(3)
        print('''
                ... You are dead...
        ''')
        time.sleep(2)
        print('------------------------------ * GAME OVER * ------------------------------')
        print()

        print('''
Press 'X', if you want to restart or exit the game...
Press 'W', if you want to restart the battle...
            ''')
        print()
        option = input('>> ')
        print()

        while option.lower() != 'x' and option.lower() != 'w':
            print('''I do not know what you mean, say that again...''')
            print()
            option = input('>> ')
            print()

        if option.lower() == 'x':
            exit_game()
        elif option.lower() == 'w':
            kill_dragon()

    # JUMPING DECISION -----------------------------------------------------------------
    if decision == 'b':
        time.sleep(2)
        print(''' 
... Wait... I can remember my father saying something about Belmung... 
            ''')
        time.sleep(2)
        print('''
... I must say the right words otherwise I'll die...
        ''')
        print()
        time.sleep(2)
        print('''
 ... 'Belmung... fulgebunt et Destroy caelum..' ...
        ''')
        time.sleep(3)
        print('''
                    ... * Damn human... You dare to wound me, you better prepare for this ...* ...
        ''')
        time.sleep(2)
        print('''
...If I don't do something fast, I'll be just ashes later on...
        ''')
        value = input('>> ')
        print()

        while value != 'A':
            print('''
.. This is my chance, I must use both swords...
                ''')
            print()
            value = input('>> ')
            print()

        if value == 'A':
            print()
            time.sleep(2)
            print('''
... I'm sorry, Fafnir, I made my own destiny...
                ''')
            time.sleep(2)
            print('''
 ... And is defeat you...
            ''')
            time.sleep(3)
            print('''
                ..... * Stupid human, did you really think I would let you harm me again?..
                         ----- Roar -----
                                    ... Die .... *
                ''')
            time.sleep(2)
            print('''
... I get it, his chest... That must be the weakest part...
            ''')
            time.sleep(2)
            time.sleep(3)
            print()
            value = input('>> ')
            print()

            while value != 'db':
                print('''
...Using both swords is my last choice... I'm must use that ability..
                ''')
                print()
                value = input('>> ')
                print()

            if value == 'db':
                time.sleep(2)
                print('''
                      ... * That ability... Is going to reduce the time of living you have ..
                ''')
                time.sleep(3)
                print('''
                        ... * I admire you, human... no... Sigfrid..
                ''')
                print()
                time.sleep(1)
                print('''
...It's your end Fafnir...
                ''')
                time.sleep(2)
                print('''
                            ..... ... .. . ..... ... .. .. .
                ''')
                time.sleep(4)
                print('''
                        ... * Finally, my desire.. has been completed...
                    ... I'm really glad of dying by the hands o someone like you... *
                ''')
                time.sleep(3)
                print(''' 
                        ... * Good luck... hero... you were born to succed...
                                Demons must not return...
                ''')
                time.sleep(2)
                print('''
                           ...
                ''')
                time.sleep(1)
                print('''
                            ..
                ''')
                time.sleep(1)
                print('''
                             .
                ''')
                time.sleep(1)

                print('''
Press 'W' to exit of the cave...
    ''')
                print()
                option = input('>> ')
                print()

                while option.lower() != 'w':
                    print('''I do not know what you mean, say that again...''')
                    print()
                    option = input('>> ')
                    print()

                if option.lower() == 'w':
                    print()
                    time.sleep(2)
                    print('''
...Finally I get the blood, but... What that Dragon said at the end...
 ... If Demons return, I'll be waiting for them...
                ''')

                print()
                print('------------------------------ * GAME OVER * ------------------------------')
                print()


# In case cave3 was checked, and want to check again..
def alternative_cave3():

    print()
    print('... Would that dwarf want to recieve me.. ?..')
    time.sleep(3)
    print('''
            ... Ohh, are you again here Sigfrid, heh?..
    ''')
    time.sleep(1)
    print()
    print('''
            I want you to promise me something, would you dare? (yes or no)..
    ''')
    print()

    time.sleep(2)

    decision = input('>> ')

    while decision != 'yes' and decision != 'y' and decision != 'no' and decision != 'n':
        print('I do not know what you mean, say that again...')
        print()
        decision = input('>> ')
        print()

    print()
    time.sleep(1)
    if decision == 'yes' or decision == 'y':
        print('''
            ...I knew you were brave, son of Sigmund... I know you well...
                Let me tell you a short story... I was the best blacksmith, 
                         no one better than me...
        ''')
        time.sleep(4)
        print('''
            My race exile me from the Underground Realm, 
                    where all the dwarfs live...
        ''')
        time.sleep(2)
        print('''
                just because I oppose our king against economic decisions 
                        that were dangerous to our way of living... 
        ''')
        time.sleep(2)
        print('''
            As you see, heh, they refuse, and exile me here, forever. 
                    Since that day and on, I swore myself one day to avenge me..
        ''')
        time.sleep(3)
        print('''
                    ... And I knew that day would come...
        ''')
        time.sleep(2)
        print('''
                The Dragon called Fafnir is the guardian of the treasure, 
                    his skin is so strong, that a normal sword cannot harm him, 
                        but with the sword Notung, and yours, Balmung...
                    ... you will be able to defeat the dragon... no one else can... 
        ''')
        time.sleep(6)
        print('''
                This is your destiny, now, accept it...
        ''')
        time.sleep(2)
        print()
        print('.....Start forging sword.....')
        time.sleep(2)
        print('.....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('.')
        time.sleep(2)

        print('''
              ... Now, take it, feel the power... running through your veins..
        ''')

        print()
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('..')
        print('.')
        time.sleep(1)
        print('''
... They won't believe me, I manage to get Notung, the soul of my sword, Belmung...
  ... This would probably be enough to take down that Dragon..
            ''')
        time.sleep(3)
        print('''
               ... Let me show you the way out... now you're ready to face that Dragon...
        ''')
        time.sleep(2)
        print('..')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('''
... Let's do it...
            ''')
        print()
        time.sleep(5)
        kill_dragon()

        # This statement is in the case you say NO to the dwarf
    else:
        time.sleep(1)
        print('Very dissapointing...')
        time.sleep(1)
        print('I did not know you were a coward...')
        time.sleep(2)
        print('...Anyway, you have two paths...')
        time.sleep(1)
        print('Choose one and get out of here...')
        print()

        chosenPath = choose_path()

        if chosenPath == '1':
            print()
            print('Is getting darker again... weird...')
            time.sleep(2)
            print('The flow of air has changed...')
            time.sleep(2)
            print('And this smell...')
            time.sleep(2)
            print('... I recognize it, is the venom Racksha of the dragon Fafnir... ')
            time.sleep(2)
            print('I cannot breath...')
            time.sleep(2)
            print('Ahhhhh.....')
            print()
            print('''
                                ... Your are dead..

            ''')
            print()
            print()
            time.sleep(2)
            print('------------------------------ * GAME OVER * ------------------------------')
            print()
            print('''
If you want to restart the game or exit, press 1..
If you want to talk again with the dwarf, press 2..      
                    ''')
            value = input('>> ')
            print()
            print()

            if value == '1':
                exit_game()
            elif value == '2':
                check_cave3(3)

        if chosenPath == '2':
            time.sleep(2)
            print('Ohh, am I at the exit of the cave?..')
            time.sleep(1)
            print('Better I choose my words, talking with that dwarf... ')
            print()
            print()
            print('------------------------------ * GAME OVER * ------------------------------')
            print()
            print('''
If you want to restart the game or exit, press 1..
If you want to talk again with the dwarf, press 2..      
            ''')
            value = input('>> ')
            print()
            print()

            if value == '1':
                exit_game()
            elif value == '2':
                alternative_cave3()


# Check of cave 3
def check_cave3(cave):

    print('This cave looks suspicious, lets get in anyway...')
    time.sleep(2)
    print('Amazingly, the cave is lightened by someone...')
    time.sleep(2)
    print('''
            .... Over here... young man..
    ''')
    time.sleep(1)
    print('''
            ... How should I call you?...
    ''')
    print()

    name = input('>> ')
    print()

    if name.lower() in names:
        time.sleep(1)
        print('''
            Well, %s, my name is Mimir, I am the guardian of this cave...
                I belong to Nibelung's race, I know what you are looking for, 
        the legendary sword, Notung, that belongs to Odín, and I know how to
            forge it, as a sacred backsmith, you do not need to hesitate...''' % name)
        print()
        print('''
                ... But I want you to promise me something, would you dare? (yes or no)... 
        ''')
        print()

        decision = input('>> ')

        while decision != 'yes' and decision != 'y' and decision != 'no' and decision != 'n':
            print('I do not know what you mean, say that again...')
            print()
            decision = input('>> ')
            print()

        print()
        time.sleep(1)
        if decision == 'yes' or decision == 'y':
            print('''
                    I knew you were brave, son of Sigmund... I know you well...
                Let me tell you a short story... I was the best blacksmith, 
                                no one better than me...
            ''')
            time.sleep(4)
            print('''
                    My race exile me from the Underground Realm, 
                            where all the dwarfs live...
            ''')
            time.sleep(4)
            print('''
                    just because I oppose our king against economic decisions 
                        that were dangerous to our way of living... 
            ''')
            time.sleep(4)
            print('''
                    As you see, heh, they refuse, and exile me here, forever. 
                        Since that day and on, I swore myself one day to avenge me..
            ''')
            time.sleep(4)
            print('''
                    ... And I knew that day would come...
            ''')
            time.sleep(3)
            print('''
                    The Dragon called Fafnir is the guardian of the treasure, 
                         his skin is so strong, that a normal sword cannot harm him, 
                    but with the sword Notung, and yours, Balmung...
                    ... you will be able to defeat the dragon... no one else can... 
            ''')
            time.sleep(8)
            print('''
                        ... This is your destiny, now, accept it...
            ''')
            time.sleep(3)
            print()
            print('..... -- Start forging sword -- .....')
            time.sleep(2)
            print('.....')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('..')
            time.sleep(1)
            print('.')
            time.sleep(2)

            print('''
             ... Now, take it, feel the power... running through your veins..     
            ''')
            print()
            time.sleep(2)
            print('...')
            time.sleep(1)
            print('..')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('''
... They won't believe me, I manage to get Notung, the soul of my sword ,Belmung...
 ... This would probably be enough to take down that Dragon..
                ''')
            time.sleep(1)
            print('''
... Let's do it...
                ''')
            print()
            time.sleep(5)
            kill_dragon()

        # This statement is in the case you say NO to the dwarf
        else:
            time.sleep(1)
            print('''
                Very dissapointing...
            ''')
            time.sleep(1)
            print(''''
                ... I did not know you were a coward...
            ''')
            time.sleep(2)
            print('''
                ... Anyway, you have two paths...
            ''')
            time.sleep(1)
            print('''
                ... Choose one and get out of here...
            ''')
            print()

            chosenPath = choose_path()


            if chosenPath == '1':
                print()
                print('Is getting darker again... weird...')
                time.sleep(2)
                print('The flow of air has changed...')
                time.sleep(2)
                print('And this smell...')
                time.sleep(2)
                print('... I recognize it, is the famous venom called Racksha of the dragon Fafnir... ')
                time.sleep(2)
                print('I cannot breath...')
                time.sleep(2)
                print('.....')
                time.sleep(2)
                print('...')
                time.sleep(2)
                print()
                print('You are dead...')
                time.sleep(2)
                print()
                print('------------------------------ * GAME OVER * ------------------------------')
                print()
                time.sleep(2)
                print('''
If you want to restart the game or exit, press 1..
If you want to talk again with the dwarf, press 2..      
                ''')
                value = input('>> ')
                print()
                print()

                if value == '1':
                    exit_game()
                elif value == '2':
                    check_cave3(3)

            if chosenPath == '2':
                time.sleep(2)
                print('Oh, am I at the exit of the cave?..')
                time.sleep(2)
                print('If I want to talk again with that dwarf, I better choose the right words...')
                time.sleep(2)
                print()
                print('------------------------------ * GAME OVER * ------------------------------')
                print()
                print('''
If you want to restart the game or exit, press 1..
If you want to talk again with the dwarf, press 2..      
                ''')
                value = input('>> ')
                if value == '1':
                    exit_game()
                elif value == '2':
                    alternative_cave3()

    else:
        time.sleep(1)
        print('%s?...' % name)
        time.sleep(1)
        print('... Get out of here, I do not know who you are, never come back..')
        print()
        time.sleep(1)
        print()
        print('------------------------------ * GAME OVER * ------------------------------')
        print()
        time.sleep(1)
        print()


def check_cave2(cave):
    print('Oh, I do not know if I am lucky or if I am going to die... ')
    time.sleep(1)
    print('... He is here, Fafnir, the most powerful of all dragons...')
    time.sleep(2)
    print('What should I do?..')
    time.sleep(1)
    print()
    print('''
For running, press 1
For fighting, press 2
For asking about knowledge, press 3
    ''')
    print()
    value = input('>> ')
    print()

    while value != '1' and value != '2' and value != '3':
        print('''
... Invalid choice, try again...
        ''')
        print()
        value = input('>> ')
        print()

    if value == '1':
        get_run()
    if value == '2':
        get_fight()
    if value == '3':
        get_question()


# Checking which cave the user have chosen..
def check_cave(chosenCave):
    if chosenCave == '1':
        check_cave1(chosenCave)

    if chosenCave == '2':
        check_cave2(chosenCave)

    if chosenCave == '3':
        check_cave3(chosenCave)
# In case you want to fight, we choose this alternative...


def get_fight():
    print('''
              --- * INSTRUCTIONS * ---
            For moving to the right: 'r'
            For moving to the left: 'l'
            For jumping: 'j'
            For atacking with sword: 'a'            
    ''')
    time.sleep(5)

    print()
    print('''
... This is going to be hard, I must..
    ''')
    time.sleep(1)

    print('''
                .... * Human, you dare to bother me while I am sleeping...
                            Your are looking for your dead... *
    ''')
    time.sleep(3)

    print('''
... What do I do now? That huge current of fire is going to kill me..
    ''')
    print()
    decision = input('>> ')
    print()

    # WHILE DECISION IS NOT IN THE LIST OF MOVEMENTS...
    while decision not in movements:
        print('''I do not know what you mean, say that again...''')
        print()
        decision = input('>> ')
        print()


    # LEFT DECISION AND ATTACK WITH ONE SWORD DECISION
    while decision == 'l' or decision == 'a':
        if decision == 'l':
            print('''
... There's a path covered by rocks that way, I must do something else...
        ''')
            print()
            decision = input('>> ')
            print()

        elif decision == 'a':
            print('''
... If I attack now, I'll going to get caught in his flames...
                    ''')
            print()
            decision = input('>> ')
            print()



    # RIGHT DECISION
    if decision == 'r':
        print('''
... I was lucky, if that huge rock hadn't been there...
                    I would've died under those flames ...
            ''')
        time.sleep(4)
        print('''
                .... * All humans are the same, always looking for treasure and benefits...
                            I'm the guardian of Nibelung's treasure, 
                                    ... And no one has scape from my flames before...
        ''')
        time.sleep(5)
        print('''
... I'm taking that as a compliment,..
            but I don't care about tresures...
        ''')
        time.sleep(3)
        print('''
                ..... * As I would believe that... But I can see you are brave...
                        ... I won't kill you today, get away from here, and never come back..
        ''')
        time.sleep(5)
        print('------------------------------ * GAME OVER * ------------------------------')
        print()

        print('''
Press 'X', if you want to restart or exit the game...
Press 'W', if you want to restart the battle...
        ''')
        print()
        option = input('>> ')
        print()

        while option.lower() != 'x' and option.lower() != 'w':
            print('''I do not know what you mean, say that again...''')
            print()
            option = input('>> ')
            print()

        if option.lower() == 'x':
            exit_game()
        elif option.lower() == 'w':
            check_cave2(2)

    # JUMPING DECISION -----------------------------------------------------------------
    if decision == 'j':
        time.sleep(2)
        print(''' 
Uff! Fortunately I was at the top, of that rock, otherwise I would have died...
        ... Now, is my oportunity to attack... 
        ''')
        print()
        value = input('>> ')
        print()

        while value != 'a':
            print('''If I have the chance to attack, Belmung, sword of swords...
                        I'll do it now...
            ''')
            print()
            value = input('>> ')
            print()

        if value == 'a':
            print()
            time.sleep(2)
            print('''
Oh no!! His skin if so hard, a common sword won't be able to harm him,
I must find a weak point, otherwise, I'll die...
            ''')
            print()
            time.sleep(2)
            print('''
            ..... * Stupid human, did you really think I would let you harm me?..
                     ----- Roar -----
                                ... Die .... *
            ''')
            time.sleep(2)
            print()
            print('''
Ahhhhh...
            ''')
            print()
            time.sleep(1)
            print(''' 
                    ... You are dead...
            ''')

            print()
            print('------------------------------ * GAME OVER * ------------------------------')
            print()

            print('''
Press 'X', if you want to restart or exit the game...
Press 'W', if you want to restart the battle...
''')
            print()
            option = input('>> ')
            print()

            while option.lower() != 'x' and option.lower() != 'w':
                print('''I do not know what you mean, say that again...''')
                print()
                option = input('>> ')
                print()

            if option.lower() == 'x':
                exit_game()
            elif option.lower() == 'w':
                check_cave2(2)


# Let's see the indroductory text
display_intro()

# We start the game from the beginning
restart_game()



















