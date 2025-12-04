# Rock-Paper-Scissors GUI version by Debroop
# Roll Number: 235/UCS/049

import tkinter as tk
import random

choices = ["rock", "paper", "scissor"]
emoji_map = {
    "rock": "🗿",
    "paper": "📄",
    "scissor": "✂️"
}

score = {"wins": 0, "losses": 0, "ties": 0}


def play(user_choice):
    computer_choice = random.choice(choices)

    # Update computer choice display
    computer_label.config(text=f"Computer: {emoji_map[computer_choice]} ({computer_choice})")

    # Determine result
    if user_choice == computer_choice:
        result = "Tie!"
        score["ties"] += 1
        result_color = "blue"

    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "You Win!"
        score["wins"] += 1
        result_color = "green"

    else:
        result = "You Lose!"
        score["losses"] += 1
        result_color = "red"

    # Update result text
    result_label.config(text=result, fg=result_color)

    # Update scoreboard
    score_label.config(
        text=f"Wins: {score['wins']}   Losses: {score['losses']}   Ties: {score['ties']}"
    )

window = tk.Tk()
window.title("Rock Paper Scissor by Debroop")
window.geometry("520x480")
window.config(bg="#1e1e1e")

title_label = tk.Label(
    window, 
    text="Rock • Paper • Scissor", 
    font=("Arial", 24, "bold"), 
    bg="#1e1e1e", 
    fg="white"
)
title_label.pack(pady=15)


score_label = tk.Label(
    window, 
    text="Wins: 0   Losses: 0   Ties: 0", 
    font=("Arial", 14), 
    bg="#1e1e1e", 
    fg="#00d4ff"
)
score_label.pack(pady=10)


computer_label = tk.Label(
    window, 
    text="Computer: ❓", 
    font=("Arial", 16), 
    bg="#1e1e1e", 
    fg="white"
)
computer_label.pack(pady=10)


result_label = tk.Label(
    window, 
    text="", 
    font=("Arial", 20, "bold"), 
    bg="#1e1e1e"
)
result_label.pack(pady=15)


button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=20)

rock_btn = tk.Button(
    button_frame, 
    text="🗿 Rock", 
    font=("Arial", 16), 
    width=10, 
    command=lambda: play("rock"),
    bg="#444", fg="white"
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame, 
    text="📄 Paper", 
    font=("Arial", 16), 
    width=10, 
    command=lambda: play("paper"),
    bg="#444", fg="white"
)
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(
    button_frame, 
    text="✂️ Scissor", 
    font=("Arial", 16), 
    width=10, 
    command=lambda: play("scissor"),
    bg="#444", fg="white"
)
scissor_btn.grid(row=0, column=2, padx=10)

quit_btn = tk.Button(
    window,
    text="Exit",
    font=("Arial", 14),
    width=12,
    bg="#d11a2a",
    fg="white",
    command=window.destroy
)
quit_btn.pack(pady=20)


window.mainloop()

