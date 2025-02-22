import pyttsx3
import gtts
import os
import pygame
import soundfile as sf
import librosa
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
voice_options = ["Male", "Female", "Robot", "Alien"]

# Initialize pygame mixer
pygame.mixer.init()

# Function to change voice type
def set_voice():
    choice = voice_var.get()
    if choice == "Male":
        engine.setProperty('voice', voices[0].id)
    elif choice == "Female":
        engine.setProperty('voice', voices[1].id)
    elif choice == "Robot":
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 100)
    elif choice == "Alien":
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 60)

# Function to convert text to speech
def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Enter some text!")
        return
    
    set_voice()
    engine.setProperty('rate', speed_slider.get())
    engine.setProperty('volume', volume_slider.get())
    
    engine.say(text)
    engine.runAndWait()

# Function to save as MP3
def save_as_mp3():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Enter text before saving!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 files", "*.mp3")])
    if save_path:
        tts = gtts.gTTS(text)
        tts.save(save_path)
        messagebox.showinfo("Success", "MP3 saved successfully!")

# Function to play an MP3 file
def play_audio():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        messagebox.showinfo("Playing", "Playing MP3!")

# Function to clear text field
def clear_text():
    text_entry.delete("1.0", tk.END)

# GUI Setup
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("450x500")
root.config(bg="#222831")

# Title
tk.Label(root, text="🔊 Text-to-Speech Converter", font=("Arial", 18, "bold"), fg="white", bg="#222831").pack(pady=10)

# Text Entry
text_entry = tk.Text(root, height=5, width=50, font=("Arial", 12))
text_entry.pack(pady=5)

# Voice Selection
tk.Label(root, text="Select Voice:", font=("Arial", 12), fg="white", bg="#222831").pack()
voice_var = tk.StringVar(value="Male")
voice_menu = ttk.Combobox(root, textvariable=voice_var, values=voice_options, state="readonly")
voice_menu.pack(pady=5)

# Speed Control
tk.Label(root, text="Speed:", font=("Arial", 12), fg="white", bg="#222831").pack()
speed_slider = tk.Scale(root, from_=50, to=250, orient="horizontal", bg="#393E46", fg="white")
speed_slider.set(150)
speed_slider.pack()

# Volume Control
tk.Label(root, text="Volume:", font=("Arial", 12), fg="white", bg="#222831").pack()
volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal", bg="#393E46", fg="white")
volume_slider.set(1)
volume_slider.pack()

# Buttons
btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🎙 Convert", command=text_to_speech, width=15, bg="#00ADB5", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="💾 Save as MP3", command=save_as_mp3, width=15, bg="#00ADB5", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="🎵 Play MP3", command=play_audio, width=15, bg="#00ADB5", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="🗑 Clear", command=clear_text, width=15, bg="#FF5722", fg="white").grid(row=1, column=1, padx=5, pady=5)

# Exit Button
tk.Button(root, text="❌ Exit", command=root.quit, width=20, bg="red", fg="white").pack(pady=10)

# Run the Application
root.mainloop()

