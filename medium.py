BACKGROUND_RED = '\033[41m'         #! Formatting, using Chris' lesson formatting for inspiration. ANSI sequences provide background colour for correct/incorrect responses. 
BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'                   #! Need to reset back to the standard terminal colour or everything after will be the same colour. 

def ask_multiple_choice_question_medium(question, options, correct_option):
    while True:                                                 #! using the while True: loop to repeat the question if the player inputs an answer incorrectly
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")                             #! This iterates our options so the answer can be input as 1,2,3,4

        answer = input("Please enter the number of your answer: ")

        try:
            answer_index = int(answer) - 1                      #! Sets the answer as an integer -1 to make it correspond with the correct item in the dictionary
            if options[answer_index] == correct_option:         #! If the answer given matches the "correct option" key:value in the dictionary, print "correct" and add 1 to score
                print(BRIGHT_BLUE + "Correct!" + RESET)
                return 1  # Return 1 for a correct answer       #! Calculating score
            else:                                               #! Otherwise, print "incorrect" and move on.
                print(BACKGROUND_RED + "Incorrect." + RESET)
                return 0  # Return 0 for an incorrect answer
        except (ValueError, IndexError):                        #! unless the player screws up and mistypes, in which case print error message and loop back to the start of that question.
            print("Invalid input. Please enter a number corresponding to one of the options.")  #! 6 - Data validation


medium_quiz = {
    "Han Solo's ship, first seen in Star Wars Episode IV: A New Hope, is called what?": {
        "options": ["The Millennium Falcon", "Razorcrest", "The Century Eagle", "Eagle 1"],
        "correct_option": "The Millennium Falcon"
    },
    "Spock's home planet in Star Trek, is called what?": {
        "options": ["Vulcan", "Klingon", "Romulus", "Earth"],
        "correct_option": "Vulcan"
    },
    "Neo's 'real' name in The Matrix, is what?": {
        "options": ["Thomas Anderson", "John Wick", "Spike Spiegel", "Agent Smith"],
        "correct_option": "Thomas Anderson"
    },
    "The Doctor's time-traveling ship, from Doctor Who, is called what?": {
        "options": ["TARDIS", "Enterprise", "Serenity", "Millennium Falcon"],
        "correct_option": "TARDIS"
    },
    "Firefly's 'hero ship', Serenity, is captained by who?": {
        "options": ["Malcolm Reynolds", "Elisabet Sobeck", "The Doctor", "Benjamin Sisko"],
        "correct_option": "Malcolm Reynolds"
    },
    "The human-like robots in Battlestar Galactica are called what?": {
        "options": ["Cylons", "Replicants", "Terminators", "Droids"],
        "correct_option": "Cylons"
    },
    "Blade Runner's synthetic humans are called what?": {
        "options": ["Replicants", "Synths", "Droids", "Clones"],
        "correct_option": "Replicants"
    },
    "Stargate SG-1's first antagonist faction, a parasitic race of aliens that take humans as hosts, are called what?": {
        "options": ["Goa'uld", "Wraith", "Asgard", "Ori"],
        "correct_option": "Goa'uld"
    },
    "The Hitchhiker's Guide to the Galaxy, asks the ultimate question of life, the universe, and everything, what is the answer?": {
        "options": ["42", "Infinity", "Love", "Peace"],
        "correct_option": "42"
    },
    "Halo 2 shows us the inner-workings of 'The Covenant', an alien species determined to wipe out humanity. Who are their leaders?": {
        "options": ["The Shadow Council", "Matriarch Benezia, Sovereign and Saren", "The Prophets of Truth, Mercy and Regret", "Empire, Empire and Empire"],
        "correct_option": "The Prophets of Truth, Mercy and Regret"
    }
}

