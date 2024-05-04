import tkinter as tk
import pygame

def play_background_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 to play the music indefinitely

# Create the main window
root = tk.Tk()
root.title("Background Music Example")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the window
root.geometry(f"{screen_width}x{screen_height}")

# Create a canvas with black background
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack()

# Play background music
background_music_file = "soundd.wav"  # Replace with your music file
play_background_music(background_music_file)

# Run the application
root.mainloop()
