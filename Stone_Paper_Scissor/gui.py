import game
import customtkinter as ctk

#Theme 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#window 
app = ctk.CTk()
app.title("Stone Paper Scissor Game")
app.geometry("400x400")

#TItle Label

title = ctk.CTkLabel(app, text="Stone Paper Scissor Game" , font=("Arial", 20, "bold"))
title.pack(pady=20)

computer_choice = ctk.CTkLabel(app, text="Computer : ? ", font=("Arial", 16))
computer_choice.pack(pady=10)

player_choice = ctk.CTkLabel(app, text="Player : ? ", font=("Arial", 16))
player_choice.pack(pady=10)

winner_label = ctk.CTkLabel(app, text="Winner : ? ", font=("Arial", 16))
winner_label.pack(pady=10)

#Fucnctions

def stone():
    player_choice.configure(text="Player : Stone ")
    computer , winner = game.game(1)
    computer_choice.configure(text=f"Computer : {game.Choice[computer]}")
    winner_label.configure(text=f"Winner : {winner}")

def paper():
    player_choice.configure(text="Player : Paper ")
    computer , winner = game.game(2)
    computer_choice.configure(text=f"Computer : {game.Choice[computer]}")
    winner_label.configure(text=f"Winner : {winner}")

def scissor():
    player_choice.configure(text="Player : Scissor ")
    computer , winner = game.game(3)
    computer_choice.configure(text=f"Computer : {game.Choice[computer]}")
    winner_label.configure(text=f"Winner : {winner}")

#Buttons

Stone_button = ctk.CTkButton(app , text="Stone", command=stone)
Paper_button = ctk.CTkButton(app , text="Paper", command=paper) 
Scissor_button = ctk.CTkButton(app , text="Scissor", command=scissor)

Stone_button.pack(pady=10)
Paper_button.pack(pady=10)
Scissor_button.pack(pady=10)

app.mainloop()