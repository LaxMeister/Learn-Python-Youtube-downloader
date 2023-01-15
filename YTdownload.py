import tkinter
import customtkinter
from PIL import Image, ImageTk
from pytube import YouTube
import wget
import time


def getUtubeTitle():
    try:
        ytTitleLink = link.get()
        ytTitleObject = YouTube(ytTitleLink)
        newTitle = ytTitleObject.title
        ytImg = ytTitleObject.thumbnail_url
        title.configure(text=newTitle)
        image_filename = wget.download(ytImg, "./Assets/img1.jpg")
        print('Image Successfully Downloaded: ', image_filename)
        newImg = "./Assets/img1.jpg"
        time.sleep(2)
        img_url = newImg

        img = customtkinter.CTkImage(light_image=Image.open(img_url),
                                     dark_image=Image.open(img_url),
                                     size=(300, 210))
        thumbImg = customtkinter.CTkLabel(
            app, text="", image=img, width=150, height=80)
        thumbImg.grid(row=1, column=1, columnspan=2,
                      padx=2, pady=2, sticky="ns")

        # Progress %
        # pProcentage.grid(row=3, column=3, columnspan=2,
        #                  padx=10, pady=5, sticky="w")

        pBar = customtkinter.CTkProgressBar(app, width=400)
        pBar.set(0)
        pBar.grid(row=3, column=1, columnspan=2,
                  padx=10, pady=5, sticky="ew")

        download = customtkinter.CTkButton(
            app, text="Download", command=startDownload)
        download.grid(row=5, column=2, padx=20, pady=10, sticky="w")

    except:
        finishedLabel.configure(
            text="Something went wrong with the Title (>.<)", text_color="red")
        print(ytImg)


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()
        video.download()

        finishedLabel.configure(text="Download Complete!", text_color="white")
    except:
        finishedLabel.configure(
            text="Something went wrong (>.<)", text_color="red")


def onProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    completeProcentage = bytes_download / total_size * 100
    procentageString = str(int(completeProcentage))
    pProcentage.configure(text=procentageString + "%")
    pProcentage.update()


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("The YouTube Downloader")
app.grid_rowconfigure(0, weight=2)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=3)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

# UI Elements
title = customtkinter.CTkLabel(
    app, text="Instert Video URL", font=("Impact", 28), wraplength=300, justify="center")

title.grid(row=0, column=1, columnspan=2,
           padx=10, pady=20, sticky="ns")

# Link-input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(
    app, width=350, height=40, textvariable=url_var)
link.grid(row=2, column=1, columnspan=2,
          padx=10, pady=5, sticky="ew")


# Finished downloading
finishedLabel = customtkinter.CTkLabel(
    app, text="this is a YouTube downloader", font=("Consolas", 16))
finishedLabel.grid(row=4, column=1, columnspan=2,
                   padx=10, pady=10, sticky="nsew")

# Check URL Button
checkURL = customtkinter.CTkButton(
    app, text="Check URL", command=getUtubeTitle)
checkURL.grid(row=5, column=1, padx=20, pady=10, sticky="e")

# procentage
totalProcentage = "0%"
pProcentage = customtkinter.CTkLabel(app, text=totalProcentage)
pProcentage.grid(row=3, column=3, columnspan=2,
                 padx=10, pady=5, sticky="w")


# Run app
app.mainloop()
