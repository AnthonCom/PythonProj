BACKGROUND_RED = '\033[41m'         #! Formatting, using Chris' lesson formatting for inspiration. ANSI sequences provide background colour for correct/incorrect responses. 
BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'                   #! Need to reset back to the standard terminal colour or everything after will be the same colour. 

def ask_multiple_choice_question_hard(question, options, correct_option):
    while True:                                                 #! using the while True: loop to repeat the question if the player inputs an answer incorrectly
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")                             #! This iterates our options so the answer can be input as 1,2,3,4

        answer = input("Please enter the number of your answer: ")

        try:
            answer_index = int(answer) - 1                      #! Sets the answer as an integer -1 to make it correspond with the correct item in the dictionary
            if options[answer_index] == correct_option:         #! If the answer given matches the "correct option" key:value in the dictionary, print "correct" and add 1 to score
                print(BRIGHT_BLUE + "Correct!" + RESET)
                return 1  # Return 1 for a correct answer                   #! Calculating score
            else:                                               #! Otherwise, print "incorrect" and move on.
                print(BACKGROUND_RED + "Incorrect." + RESET)
                return 0  # Return 0 for an incorrect answer
        except (ValueError, IndexError):                        #! unless the player screws up and mistypes, in which case print error message and loop back to the start of that question.
            print("Invalid input. Please enter a number corresponding to one of the options.")  #! 6 - Data validation



hard_quiz = {
    "What is the name of the desert planet that is the primary setting of the 'Dune' series?": {
        "options": ["Arrakis", "Caladan", "Giedi Prime", "Earth"],
        "correct_option": "Arrakis"
    },
    "What relation is Dark Helmet to Lone Starr?": {
        "options": ["His Father", "His Uncle's Father's Brother's Accountant", "His Father's Brother's Nephew's Cousin's former roommate", "His Wife's Brother's Son's previous employer"],
        "correct_option": "His Father's Brother's Nephew's Cousin's former roommate"
    },
    "Helldivers, from the series of the same name, are a a military branch of which faction?": {
        "options": ["Mega Earth", "Hyper Earth", "Super Earth", "Ultra Earth"],
        "correct_option": "Super Earth"
    },
    "What is the name of the alien species that Ender Wiggins is trained to fight?": {
        "options": ["Formics", "Buggers", "Xenomorphs", "Klingons"],
        "correct_option": "Formics"
    },
    "What is the name of the mysterious home planet discovered by the Kushan at the beginning of 'Homeworld'?": {
        "options": ["Taiidan", "Reach", "Foundation", "Hiigara"],
        "correct_option": "Hiigara"
    },
    "What was the original name of the ship captained by James Holden?": {
        "options": ["Rocinante", "Screaming Firehawk", "Pinus Contorta", "Tachi"],
        "correct_option": "Tachi"
    },
    "The character Mengsk, abandons Sarah Kerrigan to the Zerg in Starcraft. What was Kerrigan's unit type?": {
        "options": ["Marine", "Phantom", "Spectre", "Ghost"],
        "correct_option": "Ghost"
    },
    "Mass Effect's galactic government is located where?": {
        "options": ["Earth, Sol system", "Virmire, Hoc system", "Citadel, Widow System", "Palaven, Trebia system"],
        "correct_option": "Citadel, Widow System"
    },
    "The Brotherhood of Nod's motto is": {
        "options": ["Command and Conquer", "Glory through deception", "Peace through power", "Time is relative"],
        "correct_option": "Peace through power"
    },
    "SG-1's Jack O'Neill makes remarks to another character with a similar name to him multiple times throughout the series, what does he refer to each time?": {
        "options": ["His lack of fashion sense", "His hatred of The Simpsons", "His lack of Humour", "His betrayal"],
        "correct_option": "His lack of Humour"
    },
    "Babylon 5's main antagonists throughout the series are who?": {
        "options": ["Shadows", "Vorlon", "Minbari", "Centauri"],
        "correct_option": "Shadows"
    },
    "What was the main goal of Project Zero Dawn?": {
        "options": ["To create a weapon capable of destroying the machines fighting humanity", "To colonise another planet", "To recolonise earth in the distant future", "To stop Earth's rotation"],
        "correct_option": "To recolonise earth in the distant future"
    },
    "The 'Crimson Fleet' is lead by who?": {
        "options": ["Admiral Nguyen", "Delgado", "Crimsonbeard", "Cheyenne"],
        "correct_option": "Delgado"
    },
    "The Power Armour you're directed to by Sturges, in Fallout 4, is of which model?": {
        "options": ["T-60", "X-01", "T-45", "F-15"],
        "correct_option": "T-45"
    },
    "Sol 1's full name in the Ace Combat series is:": {
        "options": ["Rannadril Ghan Swa Fulsoom Karaten Narr Eadi Bel Anoleis", "Joaquin Jocinto De Meara Alphonso D'Oro", "Mihaly Dumitru Margareta Corneliu Leopold Blanca Karol Aeon Ignatius Raphael Maria Niketas A. Shilage", "Jonathan Ferguson, the keeper of firearms and artillery at the Royal Armouries Museum in the UK, which houses a collection of thousands of iconic weapons from throughout history"],
        "correct_option": "Mihaly Dumitru Margareta Corneliu Leopold Blanca Karol Aeon Ignatius Raphael Maria Niketas A. Shilage"
    }
}

