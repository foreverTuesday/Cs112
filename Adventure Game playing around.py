
while True:
    print("Welcome to Kingdom Explorer, programmed by readinginthestarlight")
    print("Laura, please do not use capital letters or punctuation anywhere after entering your name.  I know you're an English major, but this game only responds to simple commands, so if you actually want to play, you have to keep your answers as short and simple as possible.")
    print("please press enter to begin")
    value = input()
    if value == "":
        break

    
while True:
    third_quest = "null"
    in_town = "null"
    real_duckling = "null"



    print("You are a wizard")
    name = input("What is your name? ")
    print("    ")
    print(name + ", where do you want to go?")
    first_quest = input("forest or castle? ")
    print("    ")

    if first_quest == "forest" or first_quest == "castle":
        print(name + ", you walk into the " + first_quest)
    else:
        print("ERROR")
        
    if first_quest == "forest":
        print(name + ", you see a cave")
    if first_quest == "castle":
        print(name + ", you see the princess.")
    


    if first_quest == "forest":
        second_quest = input(name + ", do you enter? ")
        print("    ")
    if first_quest == "castle":
        second_quest = input(name + ", do you bow? ")
        print("    ")


    if first_quest == "forest" and second_quest == "yes":
        print("You see a dragon")
    if first_quest == "castle" and second_quest == "yes":
        print("Good job being polite")
    if first_quest == "castle" and second_quest == "no":
        print(name + ", you are beheaded for impoliteness.  You lose.")
        print("    ")


    if first_quest == "forest" and second_quest == "no":
        while True:
            if first_quest == "forest" and second_quest == "no":
                print("That cave is probably the only exciting thing in the whole forest.  Do you want to go in?")
                value = input()
                if value == "yes":
                    break
                print(name + ", you might not be making the right choice.")
        print("You found a cave full of treasure!  Congradulations, you win, " + name + "!!!!!!!!!!!!!!!!!!")
        print("    ")


    if first_quest == "forest" and second_quest == "yes":
        print("The dragon rears up and snorts smoke out of his nostrils.")
        print("-cue epic fighting music-")
        print("it's time to fight the dragon")
        third_quest = input(name + ", you have a wand and a sword.  Do you want to fight with your wand or with your sword?  or would you rather run away? ")
        print("    ")
    if first_quest == "castle" and second_quest == "yes":
        print("The princess tells you that she has a super secret mission for you")
        third_quest = input(name + ", do you accept the princess's mission? ")
        print("    ")


    if third_quest == "sword":
        print("You valiantly draw your sword and brandish it at the dragon.")
        print("The dragon advances toward you.")
        print("You swing your sword and it goes flying out of your hand.")
        print("You're a wizard, " + name + ", you idiot.  You don't know how to use a sword.")
        print("The dragon eats you.  You're dead.  You lose.")
        print("    ")
    if third_quest == "wand":
        print("You point your wand at the dragon.")
        print("The dragon breathes fire at you.  You defend yourself with a fireproofing spell.")
        print("You use your wand to transform the dragon into a harmless newt.")
        print("The newt scurries away.")
        print("You have defeated the dragon!")
        print("Congradulations, " + name + ", you win!!!!!!!!!!!!")
        print("    ")
    if third_quest == "run away":
        print("You swish your awesome wizard cloak behind you as you flee in terror.")
        print("+2 style points.")
        print("The dragon throws treasure after you in an attempt to knock you out.")
        print("fortunately, you remembered to wear your wizard hat, which gives you +5 dodge, so you're fine.")
        print("You manage to catch a small treasure chest from the air.")
        print("You finally reach the edge of the forest.  Breathing heavily, you whipe your brow and look behind you.")
        print("The dragon didn't follow you, which is good because, if he had, the princess would be pretty upset with you, " + name)
        print("You open the treasure chest.  It's full of gold coins.  You're rich!")
        print("You head into the village market to spend your newfound wealth.")
        print("When you get there, you see some rad +4 spell damage wizard sneakers that you've been eyeing for a while.")
        print("You're about to buy them when you notice some homeless children looking sadly up at you.")
        in_town = input("Do you want to donate or spend? ")
        print("    ")
        
    if third_quest == "yes":
        print("The quest is to rescue the royal duckling from the lair of the EVIL BEAST.")
        print("The EVIL BEAST is the most terrifying creature in the whole kingdom.")
        print("You sit on the castle steps and think about what you want to do.")
        print("You're pretty sure you can defeat the EVIL BEAST with your wizard skills.")
        print("but you're also pretty sure you could just buy a replacement duckling.")
        print("You doubt the princess would notice the difference and then you could get your reward without putting yourself in any danger.")
        real_duckling = input("Do you want to rescue or replace the royal duckling? ")
        print("    ")

        
    if third_quest == "no":
        print("The princess gives you a disaproving look.")
        print("She sighs dejectedly.  \"I suppose I should have expected this from you, " + name + ".  This is why we didn't make you the royal wizard.\"")
        print("You leave the castle feeling dejected.")
        print("You'd better do something to cheer yourself up before you die of sadness.")
        print("Shopping has always cheered you up.")
        print("You head into the village market to do some shopping.")
        print("When you get there, you see some super cool wizard supplies.")
        print("You're about to buy them when you notice some homeless children looking sadly up at you.")
        in_town = input("Do you want to donate or spend? ")
        print("    ")


    if in_town == "donate" and third_quest == "run away":
        print("You give each child several gold coins.")
        print("It warms your heart to see how happy you've made them and you have plenty of gold left over to buy those new wizard sneakers.")
        print("You head home with your new sneakers on your feet and a smile on your face.")
        print("Congradulations, " + name + ", you've won!!!!!!")
        print("    ")
    if in_town == "spend" and third_quest == "run away":
        print(name + ", you heartless monster.  You just found a treasure chest full of gold and you can't find it in your heart to feed starving children.")
        print("You lose because you're being mean.")
        print("    ")
    if in_town == "donate" and third_quest == "no":
        print("You pull your wallet out of your pocket.")
        print("It's woefully light.")
        print("You hand your last gold and silver coins to the children, leaving yourself with just a few coppers.")
        print("You're a wizard.  If you can gather the courage to stop turning down jobs, you'll get plenty of money in no time.")
        print("You sigh and turn away.")
        print("Someone taps you on the shoulder.")
        print("You whirl back.  The children have transformed into magical fairies.")
        print("\"Thank you, " + name + ",> they all say in perfect unison.\"")
        print("Your kindness deserves to be rewarded.")
        print("Take this firestarting stick as a gift of our gratitude.")
        print("You take the stick.")
        print("You don't have the heart to tell them that you already know how to start fires with your wand.")
        print("You sell the firestarting stick and end up with enough money to at least buy yourself food.")
        print("You... win?????????")
        print("    ")
    if in_town == "spend" and third_quest == "no":
        print("You pull your wallet out of your pocket.")
        print("It's woefully light.")
        print("If you want to be able to buy cool wizarding supplies and food, there's no way you have enough to also help the kids.")
        print("Maybe you can come back in a few days when you've gotten your paycheck from Mediocre Wizards Inc.")
        print("You try not to make eye contact with them as you walk by.")
        print("Unfortunately, it doesn't really work.")
        print("The children surround you, chanting in some long-dead language.")
        print("Your mother always warned to you pay poor people to prevent something like this from happening.")
        print("You should have listened.")
        print("You end up cursed")
        print("...with mediocre hair.  Which is better than your previous baldness, so you suppose you should try to avoid breaking it.")
        print("You have neither won nor lost.")
        print("    ")
    if real_duckling == "rescue":
        print("You make your way toward the lair of the EVIL BEAST")
        print("
        print("    ")
    if real_duckling == "replace":
        print("    ")





    print("you have finished the game")
    endgame = input("Would you like to play again? ")
    print("    ")
    if endgame == "no":
        break


print("Thank you for playing")
