BACKGROUND_RED = '\033[41m'         #! Formatting, using Chris' lesson formatting for inspiration. ANSI sequences provide background colour for correct/incorrect responses. 
BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'                   #! Need to reset back to the standard terminal colour or everything after will be the same colour. 

def ask_multiple_choice_question_easy(question, options, correct_option):
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


easy_quiz = {
    "1 - In 'Star Wars', Who is Luke Skywalker's father?": {
        "options": ["Dark Helmet", "Darth Vader", "Jar Jar Binks", "Rick the Door Technician"],
        "correct_option": "Darth Vader"
    },
    "2 - In 'Star Trek: The Next Generation', what is the name of Captain Picard's ship?": {
        "options": ["USS Enterprise", "USS Voyager", "ISS Defiant", "USS Shippy McShipface"],
        "correct_option": "USS Enterprise"
    },
    "3 - In 'The Expanse', The primary factions in the Sol system are": {
        "options": ["The Federation, Confederacy, Xenos and Independents", "The Alliance and The Browncoats", "Earth, Mars and The Belt", "Sainsburys, Tesco and ASDA"],
        "correct_option": "Earth, Mars and The Belt"
    },
    "4 - In the 'Halo' franchise, what is the player character in 'Halo: Combat Evolved' referred to as?": {
        "options": ["John Halo", "John Spartan", "Master Chief", "Project: Halo"],
        "correct_option": "Master Chief"
    },
    "5 - In 'Dune', the primary Protagonist, Paul, is from which House?": {
        "options": ["House Harkonnen", "House Ordos", "House, M.D.", "House Atreides"],
        "correct_option": "House Atreides"
    }
}
