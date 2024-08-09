# Python Project Time
#! Python Quiz project!
#TODO - 1. Welcome Message: Display a welcome message to the user.
# - Simple welcome message, explain quiz topics, how many questions. 
#TODO - 2. Display Questions: Show a series of multiple-choice questions (at least 5).
# - 10 Q's - set up placeholder to start, can think of questions later
#   - Maybe set up options for number of questions? Easy/Medium/Hard? 
#       - Perhaps setting up the question diffs as their own modules? 
#TODO - 3. User Input: Allow the user to select an answer for each question.
# - Simple input 
#   - Create exception handling for user inputting anything other than 1, 2, 3 or 4 - integer check is easiest.
#TODO - 4. Calculate Score: Keep track of the user's correct answers and calculate the final score.
# - Create a variable for score. Add to each question result an if/else? Might just need an if. On correct answer, score var +1. 
#TODO - 5. Display Results: Show the user's total score and a message based on their performance.
# - Case? Look at the example a few days ago for grade - have multiple messages for scoring from 0-10?
#   - Looking into it, whilst we could literally do a "if score = X then print(Y)" it's not the most elegant thing. Perhaps look into custom messages based on % / fraction of total score answered correctly?
#TODO - 6. Data Validation: Ensure valid input by checking that the user selects an answer within the given choices.
# - Covered in exception handling for 3
#TODO - 7. Thank You Message: Thank the user for taking the quiz.
# - hopefully straightforward, just something for the very end. 
#   - perhaps offer a loop around to allow users to re-do? 

#? _________________________________________________________________________________________________________________________________

#! Starting off by importing modules
import custom_exceptions        #* This doesn't actually get used, but I've left it imported and the file saved in the same folder to practice
import easy
import medium
import hard
import os
os.system('color')              #* Bonus formatting - importing colours to make correct/incorrect text stand out more in the terminal.
BACKGROUND_RED = '\033[41m'
BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'


#! 1 - Welcome Message
print("Hello! Welcome to my little quiz!", "\n", "In this quiz I'll be asking you a few questions based around Sci-Fi media properties.")
print("My hope is to help you get to know my interests a little better whilst showing off some Python knowledge.")

name = input("Now then, what is your name? ")

print(f"Great! Thanks {name}. So we have 3 difficulty options for you to choose from. Easy, medium or hard.")
print("These are as you would think.", "\n", "Easy is a quiz based on general pop culture knowledge.", "\n", "Medium will involve some general and some more niche topics.", "\n", "Hard will cover what I consider to be niche topics in more niche franchises.")

#! 2, 3, 4 & 5 - Difficulty Selection, display questions & user input, calculating score


def diff_select():
    diff = input("Choose difficulty (easy, medium, hard): ").lower()                #! Diff selection
    score = 0                                                                       #! Calculating score
    
    if diff == "easy":                                                              #! display Q's and Input are in their own modules
        print("Always good to start off slow, let's get started then shall we?")    
        for question, data in easy.easy_quiz.items():
            score += easy.ask_multiple_choice_question_easy(question, data["options"], data["correct_option"])  #! Checks if the result of each question matches "correct_option". If it does, increase score by 1
            
    elif diff == "medium":                                                          #! display Q's and Input are in their own modules
        print("Easy sound too easy? Or perhaps you've been through once already? Okay, let's see how you handle these.")
        for question, data in medium.medium_quiz.items():
            score += medium.ask_multiple_choice_question_medium(question, data["options"], data["correct_option"])

    elif diff == "hard":                                                            #! display Q's and Input are in their own modules
        print("Ready for a challenge? Let's see how you do with these.")
        for question, data in hard.hard_quiz.items():
            score += hard.ask_multiple_choice_question_hard(question, data["options"], data["correct_option"])
            
    else:
        print("Hmm, that doesn't match any of the difficulty options listed, try again - remember your options are easy, medium, or hard.") 
        diff_select()
        return

#! 5 - Display results

    total_questions = len(easy.easy_quiz) if diff == 'easy' else len(medium.medium_quiz) if diff == 'medium' else len(hard.hard_quiz)   #! setting up our final score to give a custom result message based on %. Specific scoring for difficulty using an if/else argument (if diff var is easy, use the length of that specific quiz for the total length value).
    score_msg = score / total_questions     #! Set up the variable for determining % as our score/total questions value above.

    if score_msg == 1:
        print(f"Perfect score! Your final score is: {score}/{total_questions}")
    elif score_msg >= 0.75:
        print(f"Great job! Your final score is: {score}/{total_questions}")
    elif score_msg >= 0.5:
        print(f"Good effort! Your final score is: {score}/{total_questions}")
    else:
        print(f"Better luck next time. Your final score is: {score}/{total_questions}")

if __name__ == "__main__":      #! Using for editing - just to avoid accidentally starting the quiz when checking other functions in test files. 
    diff_select()

#* Wanted to demonstrate custom exception handling, but not needed here as covered by the else statement above. 
    # try:
    #     diff_select()
    # except custom_exceptions.Invalid_diff_exception:                                #? Remember this - was screwing up because you didn't have the module.exception format set
    #     print("Incorrect input detected. Choose difficulty (easy, medium, hard): ") 
    #     diff_select()

print(f"Congrats, {name} on getting through this quiz. I hope that was an enjoyable look into subjects and topics I enjoy!")
print("Would you like to try again? Perhaps try another difficulty option this time round? ")

def game_end():
    retry = input(f"{name}, would you like to go again? ").lower()

    if retry == "yes":
        print("Great! let's take you back to the difficulty selection.")
        diff_select()
        game_end()
    elif retry == "no":
        print(f"I suppose you're right {name}, this is a strange game. Perhaps the only winning move is not to play.")
        print("I hope you enjoyed yourself though! Feel free to come back another time!") #! 7 - Thank you message
    else:
        print("I need a yes or a no.")
        game_end()
        return

game_end()