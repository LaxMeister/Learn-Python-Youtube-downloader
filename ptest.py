import tkinter
import customtkinter
from pytube import YouTube
import traceback
import threading


def startDownload():
    def on_Progress(stream, chunk, bytes_remaining):
        print("callbacking")

        bytes_download = stream.filesize - bytes_remaining
        completeProcentage = bytes_download / stream.filesize * 100
        print(completeProcentage)
        procentageString = str(int(completeProcentage))
        print(procentageString)
        pProcentage.configure(text=procentageString + '%')
        pProcentage.update()
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_Progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()

        finishedLabel.configure(text="Download Complete!", text_color="white")
    except:
        traceback.print_exc()
        finishedLabel.configure(
            text="Something went wrong (>.<)", text_color="red")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("The YouTube Downloader")


# UI Elements
title = customtkinter.CTkLabel(
    app, text="Instert Video URL", font=("Impact", 28), wraplength=300, justify="center")

title.pack(padx=20, pady=20)

# Link-input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(
    app, width=350, height=40, textvariable=url_var)
link.pack(padx=20, pady=20)
# Finished downloading
finishedLabel = customtkinter.CTkLabel(
    app, text="this is a YouTube downloader", font=("Consolas", 16))
finishedLabel.pack(padx=20, pady=20)
# Check URL Button
checkURL = customtkinter.CTkButton(
    app, text="Check URL", command=(threading.Thread(target=startDownload).start))
checkURL.pack(padx=20, pady=20)

# procentage
pProcentage = customtkinter.CTkLabel(app, text='0%')
pProcentage.pack(padx=20, pady=20)


# Run app
app.mainloop()
