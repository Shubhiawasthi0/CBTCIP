import random
import tkinter as tk

window = tk.Tk()
window.title("GAME")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]

def number_to_choice(number):
    rps = {0: 'ROCK', 1: 'PAPER', 2: 'SCISSOR'}
    return rps[number]

def random_computer_choice():
    return random.choice(['ROCK', 'PAPER', 'SCISSOR'])

def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    global USER_CHOICE
    global COMP_CHOICE

    USER_CHOICE = human_choice.lower()
    COMP_CHOICE = comp_choice.lower()

    user = choice_to_number(USER_CHOICE)
    comp = choice_to_number(COMP_CHOICE)

    result_text = ""
    if user == comp:
        result_text = "TIE"
    elif (user - comp) % 3 == 1:
        result_text = "YOU WIN"
        USER_SCORE += 1
    else:
        result_text = "Comp wins"
        COMP_SCORE += 1

    text_area.delete(1.0, tk.END)
    answer = f"YOUR CHOICE: {USER_CHOICE.capitalize()}\nComputer's Choice: {COMP_CHOICE.capitalize()}\nResult: {result_text}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}"
    text_area.insert(tk.END, answer)

def ROCK():
    comp_choice = random_computer_choice()
    result('ROCK', comp_choice)

def PAPER():
    comp_choice = random_computer_choice()
    result('PAPER', comp_choice)

def SCISSOR():
    comp_choice = random_computer_choice()
    result('SCISSOR', comp_choice)

# Configure grid weights to make elements expand to fill the screen
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

button1 = tk.Button(text="ROCK", bg="#ECCBF9", command=ROCK)
button1.grid(row=1, sticky="nsew")  # Use sticky to expand buttons
button2 = tk.Button(text="PAPER", bg="#FA8072", command=PAPER)
button2.grid(row=2, sticky="nsew")
button3 = tk.Button(text="SCISSOR", bg="#CBF9F9", command=SCISSOR)
button3.grid(row=3, sticky="nsew")

text_area = tk.Text(master=window, height=12, width=30, bg="#EDEA50")
text_area.grid(row=4, sticky="nsew")

# Add padding to the buttons and text area
pad = 10
button1.grid(pady=pad)
button2.grid(pady=pad)
button3.grid(pady=pad)
text_area.grid(padx=pad, pady=pad)

window.mainloop()