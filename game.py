
import random
import time

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

def clear_screen():
    print("\033[2J\033[H" , end="")

def show_hud(room, moves, inventory):
    name = room.replace("_", " ")
    print(CYAN + "=" * 50 + RESET)
    print(CYAN + " room: " + BOLD + name.ljust(20) + RESET + CYAN + "moves: " + str(moves).ljust(4) + RESET)
    print(CYAN + "   items: " + str(len(inventory)) + RESET)
    print(CYAN + "=" * 50 + RESET)
    print()


def mansion_game():
    clear_screen()
    room = "living_room"
    inventory = []
    moves = 0

    print()
    print(CYAN + BOLD + "============== escape the mantion ==========" + RESET)
    print()
    print(YELLOW + BOLD + "you wake up in a strange mansion, find the key to escape" + RESET)
    print()

    while True:
        time.sleep(2)
        moves = moves + 1
        
        clear_screen()
        show_hud(room, moves, inventory)


        if room == "living_room":
            print(MAGENTA + BOLD + "------ living room ------" + RESET)
            print()
            print("dusty sofas, broken tv , and a cold fireplace")
            print(BOLD + "exits: " + RESET + "north, south")
            print(BOLD + " you can see : " + RESET + "note, log")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET ).strip().lower()

            if cmd == "north":
                room = "hallway"
            elif cmd == "south":
                if "key" in inventory:
                    print()
                    print(GREEN + BOLD + "you slide the key into the lock----" + RESET)
                    print(GREEN + BOLD + "the door swings open, you escaped!!!" + RESET)
                    print(YELLOW + "you did it in" + str(moves) + " moves" + RESET)
                    print(GREEN + BOLD + " ------ you win ------")
                    return
                else:
                    print(RED + "the front door is locked, u need a key" + RESET)
            elif cmd == "take note":
                if "note" in inventory:
                    print(YELLOW + "you already hvae the note "+ RESET)
                else:
                    inventory.append("note")
                    print(GREEN + "picked up note. it says: 'the key is under the bed" + RESET)
            elif cmd == "take log":
                if "log" in inventory:
                    print(YELLOW + "you already have the log" + RESET)
                else:
                    inventory.append("log")
                    print(GREEN + "picked up the wooden log" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pokets are empty" + RESET)
                else:
                    print(YELLOW + BOLD + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you gave up and now u die, bye!!" + RESET)

                return
            elif cmd == "help":
                print(YELLOW + BOLD + "commands: north south east west up down take search inventory quit")
            else:
                print(RED + "you cant do that here" + RESET)
            print() 
        elif room == "hallway":
            print(MAGENTA + BOLD + "_______hallway______" + RESET)
            print("a long hallway with creepy paintings, the floor creaks")
            print(BOLD + "exits:" + RESET + " north south east west up")
            print("you can see: painting")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "north":
                room = "kitchen"
            elif cmd == "south":
                room = "living_room"
            elif cmd == "east":
                room = "bedroom"
            elif cmd == "west":
                room = "bathroom"
            elif cmd == "up":
                room = "attic"
            elif cmd == "take painting":
                print(RED + BOLD + "the paintings are screwed to the wall")
            elif cmd == "search painting":
                print(YELLOW + BOLD + "behind the painting: its just a old wallpaper , nothing good" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + BOLD + "yur pokets are empty" + RESET)
                else:
                    print(YELLOW + BOLD + "you have:  " + str(inventory) + RESET)
            elif cmd == "quit":
                print(YELLOW + BOLD + "you gave up")
            elif cmd == "help":
                print(YELLOW + "commands : north south east west up down take search inventory quit " + RESET)
            else:
                print(RED + "you cant do that here" + RESET)
            print()
        elif room == "kitchen":
            print(MAGENTA + BOLD  + "-----kitchen-------" + RESET )
            print("an old kitchen , pots everywhere, smeels weird")
            print(BOLD + "exits: " + RESET + "south, east, down")
            print("you can see: knife, apple")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()


            if cmd == "south":
                room = "hallway"
            elif cmd == "east":
                room = "dining_room"
            elif cmd == "down":
                room = "cellar"
            elif cmd == "take knife":
                if "knife" in inventory:
                    print(YELLOW + BOLD + "you already have the knife" + RESET)
                else:
                    inventory.append("knife")
                    print(GREEN + "picked up the knife")
            elif cmd == "take apple":
                if "apple" in inventory:
                    print(YELLOW + BOLD + "you already have the apple")
                else:
                    inventory.append("apple")
                    print(GREEN + BOLD + "you picked up the apple")
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + BOLD + "your pokets are empty" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + "you gave up, u die byeee")
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit")
            else:
                print(RED + "you cant do that here" + RESET)
            print()
        elif room == "bedroom":
            print(MAGENTA + BOLD + "=========== bed room =========")
            print(" a bed room with an old bed and a dusty lamp")
            print(BOLD + "exits: " + RESET + "west, east")
            print(BOLD + "you can see:" + RESET + "bed, lamp")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "west":
                room = "hallway"
            elif cmd == "east":
                room = "study"
            elif cmd == "search bed":
                if "key" in inventory:
                    print(YELLOW + BOLD + "you already have the key" + RESET)
                else:
                    inventory.append("key")
                    print(GREEN + BOLD + "you found a small bras key")
            elif cmd == "take lamp":
                if "lamp" in inventory:
                    print(YELLOW + BOLD + "you already have the lamp")
                else:
                    inventory.append("lamp")
                    print(GREEN + "picked up the dusty lamp" + RESET)
            elif cmd == "search lamp":
                print(YELLOW + "just dust inside" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + BOLD + "yor pokets are empty" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET )
            elif cmd == "quit":
                print(RED + BOLD + "you gave up in the bed room (dang it sunds way worse lol ) bye" + RESET)
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east east up down take search inventory quit" + RESET)
            else:
                print(RED + BOLD + "you cant do that here" + RESET)
            print() 
        elif room == "bathroom":
            print(MAGENTA +  BOLD + "------------- bathroom -----------" + RESET)
            print(" a small bathroom, cracked mirror, weaird smell")
            print(BOLD + "exits: " + RESET + "east")
            print(BOLD + "you can see: " + RESET + "towel, soap")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "east":
                room = "hallway"
            elif cmd == "take towel":
                if "towel" in inventory:
                    print(YELLOW + BOLD + "you already have the towel" + RESET)
                else:
                    inventory.append("towel")
                    print(GREEN + BOLD + "picked up the towel")

            elif cmd == "take soap":
                if "soap" in inventory:
                    print(YELLOW + BOLD + "you already have the soap in ur poket")
                else:
                    inventory.append("soap")
                    print(GREEN + "picked up the soap" + RESET)

            elif cmd == "search mirror":
                print(YELLOW + "you see your tried face, nothing hidden")
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pokes are empty" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you gave up in tha bathroom" + RESET)
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit")
            else:
                print(RED + BOLD + "you cant do that here")
        elif room == "cellar":
            print(MAGENTA +  BOLD + "=========== cellar =========" + RESET)
            print("a dark damp cellar, selv of old wine")
            print(BOLD + "exits: " + RESET + "up")
            print(BOLD + "you can see: " + RESET + "up" )
            print()

            cmd = input(GREEN+ BOLD + "> " + RESET).strip().lower()

            if cmd == "up":
                room = "kitchen"
            elif cmd == "take wine":
                if "wine" in inventory:
                    print(YELLOW + BOLD + "you already have wine" + RESET)
                else:
                    inventory.append("wine")
                    print(GREEN + "picked up a dusty old wine bottle" + RESET)
            elif cmd == "take chesse":
                if "cheese" in inventory:
                    print(YELLOW + BOLD + "you already have cheese" + RESET)
                else:
                    inventory.append("cheese")
                    print(GREEN + "picked up some chesse")
            elif cmd == "search shelves":
                print(YELLOW + "just more wine, nothing usefull" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pokets are empty" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you gave up, happy dying")
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit" + RESET)
            else:
                print(RED + BOLD + "you cant do that here" + RESET)
            print()
        elif room == "dining_room":
            print(MAGENTA + BOLD + "=============== dining room ===============" + RESET)
            print("a big dining table, chairs knowked over, candles burded out")
            print(BOLD + "exits: " + RESET + "west")
            print(BOLD + "you can see: " + RESET + "candle, plate")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "west":
                room = "kitchen"
            elif cmd == "take candle":
                if "candle" in inventory:
                    print(YELLOW + BOLD + "you already have the candle" + RESET)
                else:
                    inventory.append("candle")
                    print(GREEN + "picke up a burning candle (that means ur poket is burning , lol)" + RESET)
            elif cmd == "take plate":
                if "plate" in inventory:
                    print(YELLOW + BOLD + "you already have plate" + RESET)
                else:
                    inventory.append("plate")
                    print(GREEN + "picked up a dusty plate" + RESET)
            elif cmd == "search table":
                print(YELLOW + "a single coin , not really usefull")
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pockets are empty")
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "bye" + RESET)
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit")
            else:
                print(RED + "you cant do that here")
        elif room == "study":
            print(MAGENTA + BOLD + "============== study room =========")
            print("a small study room with a desk and a book shelf, papers everywhere")
            print(BOLD + "exits: " + RESET + "west, east")
            print(BOLD + "you can see: " + RESET + "book, pen")
            print()


            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()
            if cmd == "west":
                room = "bedroom"
            elif cmd == "east":
                room = "library"
            elif cmd == "take book":
                if "book" in inventory:
                    print(YELLOW + "you already have the book" + RESET)
                else:
                    inventory.append("book")
                    print(GREEN + "picked up the book, titlr: how to escape " + RESET)
            elif cmd == "take pen":
                if "pen" in inventory:
                    print(YELLOW + "you already have the pen")
                else:
                    inventory.append("pen")
                    print(GREEN + "u picked up the pen now")

            elif cmd == "search desk":
                print(YELLOW + "just old papers, nothing usefull" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pokets are empty" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "help":
                print("commands: north south east west up down take search inventory quit" + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "u gave up in study room,  have fun studing with the monster")
                return
            else:
                print(RED + BOLD + "you cant do that here")
            print()
        elif room == "library":
            print(MAGENTA + BOLD + "============ library =========" + RESET)
            print("floor to ceiling bookshelves, dust everywhere, silent but fees noisy")
            print(BOLD + "exits: " + RESET + "west")
            print(BOLD + "you can see: " + RESET + "tome , ladder")

            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "west":
                room = "study"
            elif cmd == "take tome":
                if "tome" in inventory:
                    print(YELLOW + BOLD + "you already have the tome" + RESET)
                else:
                    inventory.append("tome")
                    print(GREEN + "picked up a dusty tome, i hums quitly" + RESET)
            elif cmd == "take ladder":
                print(RED + BOLD +"isnt it too big for ur poket?? lol")
            elif cmd == "search shelves":
                print(YELLOW + "thousands of books, all too dusty to read and half are burned " + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "you have nothing (not the phone compony)" + RESET)
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you gave up, read books with the monsters" + RESET)
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit" + RESET)
            else:
                print(RED + BOLD + "you cant do that here" + RESET)
        elif room == "attic":
            print(MAGENTA + BOLD + "=========== attic ========" + RESET)
            print("a dark attic, old boxes stacked high, dust in the air")
            print(BOLD + "exits: " + RESET + "down")
            print(BOLD + "you can see: " + RESET + "box, cloths")
            print()


            cmd = input(GREEN + BOLD + "> " + RESET).strip().lower()

            if cmd == "down":
                room = "hallway"
            elif cmd == "take box":
                if "box" in inventory:
                    print(YELLOW + "you already have the box")
                else:
                    inventory.append("box")
                    print(GREEN + "picked up the box") 
            elif cmd == "take cloths":
                if "cloths" in inventory:
                    print(YELLOW + "you alredy have cloths" + RESET)
                else:
                    inventory.append("cloths")
                    print(GREEN + "picked up cloths" + RESET)
            elif cmd == "search box":
                print(YELLOW + BOLD + "box is locked , you need a key to open this shi" + RESET)
            elif cmd == "open box":
                print(GREEN + BOLD + "in the box there is nothing but just some old photos" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your poket is empty")
                else:
                    print(YELLOW + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you died")
                return
            elif cmd == "help":
                print(YELLOW + "commands: north south east west up down take search inventory quit" + RESET)
            else:
                print(RED + "you cant do that here" + RESET)
            print()
        else:
            print(RED + "nothing here lol i am going to run a test" + RESET)
            return
            
def scramble_game():
    words = ["python", "antique", "guitar", "planet", "castle", "dragon", "silver", "garden"]


    print()
    print(CYAN + BOLD + "word scramble - unscramble 3 words" + RESET)
    print()

    score = 0
    rounds = 3
    for i in range(rounds):
        word = random.choice(words)

        letters = list(word)
        random.shuffle(letters)

        scrambled = ""
        for ch in letters:
            scrambled = scrambled + ch

        tries = 0
        while scrambled == word and tries < 20:
            random.shuffle(letters)
            scrambled = ""
            for ch in letters:
                scrambled = scrambled + ch
            tries = tries + 1
        print(MAGENTA + BOLD + "round " + str(i + 1) + " of " + str(rounds) + RESET)
        print(YELLOW + BOLD + "  scrambled word: " + scrambled + RESET)

        guess = input(GREEN + BOLD + "  ur guess>>> " + RESET ).strip().lower()

        if guess == word:
            score = score + 1
            print(GREEN + BOLD + "   correct" + RESET)
        else:
            print(RED + BOLD + "  nope, it was:  " + word + RESET)


    print(CYAN + BOLD + " you got " + str(score) + " out of " + str(rounds) + RESET)

    if score == rounds:
        print(GREEN + BOLD + " perfect score!!!" + RESET)
    elif score >= 2:
        print(YELLOW + BOLD + " not badd" + RESET )
    else:
        print(RED + BOLD + "study ur words lol" + RESET)

    
def rock_game():
    print()
    print(CYAN + BOLD + "rock paper scissors - first to 3 wins" + RESET)


    wins = 0
    losses = 0

    while wins < 3 and losses < 3:
        print()
        player = input(CYAN + BOLD + "rock (r), paper (p) or scissors (s)>> " + RESET).lower()
        print()
        print()

        if player != "r" and player != "p" and player != "s":
            print(RED + BOLD + "thats not a move" + RESET)


        computer = random.choice(["rock" , "paper" , "scissors"])
        print(MAGENTA + BOLD + "computer picked "+ computer + RESET)
        
        if player == computer:
            print()
            print(YELLOW + BOLD + "tiee" + RESET)
            


        elif player == "r" and computer == "scissors":
            wins = wins + 1
            print()
            print(GREEN + BOLD + "you won!!!!" + RESET)
            


        elif player == "p" and computer == "rock":
            wins =wins + 1
            print()
            print(GREEN + BOLD +  "you won that round" + RESET)
            


        elif player == "s" and computer == "paper":
            wins = wins + 1
            print()
            print(GREEN + BOLD + "you won this round" + RESET)
            


        else:
            losses = losses +1
            print()
            print(RED + BOLD + "you lost this round" + RESET)
        print()   
        print()
        print(GREEN + BOLD + "score : you >> " + str(wins)  + "  -  " + str(losses) + "<< computer" + RESET)

    if wins == 3:
        print(GREEN + BOLD + " you won the match!!!!11" + RESET)
        print()
    else:
        print(RED + BOLD + "computer won , rematch????" + RESET)
        print()          


def number_game():
    secret = random.randint(1 , 100)
    tries = 0

    print()
    print(CYAN + BOLD +  " i picked a number between 1 and 100" + RESET)
    print()


    while True:
        print()
        guess = input(GREEN + BOLD + "ur guess>>>" + RESET)
        print()

        try:
            guess = int(guess)
        except ValueError:
            print(RED + BOLD + "please use a number between 1 to 100" + RESET)
            continue

        tries = tries + 1


        if guess < secret:
            print(YELLOW + BOLD +  "too low" + RESET)
            print()

        elif guess > secret:
            print(YELLOW + BOLD + "too high" + RESET)
            print()
        else:
            print(GREEN + BOLD + "you got it!!!!!! " + "  " + " it took u " + str(tries) + " tries" + RESET)
            return


def menu():
    while True:

        print()
        print(CYAN + BOLD +  "===========  game zone  ===========" + RESET)
        print()
        print()
        print( RED + BOLD +  "chose the game and type the degit")
        print()
        print(YELLOW + BOLD + "||  " + "0" + "  " + RESET + MAGENTA + BOLD + "escpae the mansion || main  game" + RESET)
        print()
        print(YELLOW + BOLD + "||  " + "1" + "  " + RESET + MAGENTA + BOLD + "guess the number" + RESET)
        print()
        print(YELLOW + BOLD + "||  " + "2" + "  " + RESET + MAGENTA + BOLD + "scrambled words"+ RESET)
        print()
        print(YELLOW + BOLD + "||  " + "3" + "  " + RESET + MAGENTA + BOLD + "rock paper scirrors" + RESET)
        print()
        print(YELLOW + BOLD + "||  " + "4" + "  " + RESET + MAGENTA + BOLD + "quit" + RESET)
        print()
        print()
        
        choice = input(GREEN + BOLD + "chose the desired game>  ")

        if choice == "1":
            number_game()
        elif choice == "4":
            print("bye!!!")
            break
        elif  choice == "3":
            rock_game()
        elif choice == "2":
            scramble_game()
        elif choice == "0":
            mansion_game()
        else:
            print("chose a appropite option")

menu()