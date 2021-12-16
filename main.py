from tkinter import *
from tkinter import filedialog

from pytube import YouTube
from pytube import Search
import os

root = Tk()
root.title("YP3")
root.geometry("800x450")

folder_path = StringVar()

def browse_file(folder, folder_directory_label):
    global folder_path
    filename = filedialog.askdirectory()
    folder.set(filename)
    folder_path = str(filename)
    folder_directory_label.config(text="Current Directory is: " + folder_path)

def yp3_download(messageBox):
    textBox = messageBox.get("1.0", "end")

    for line in textBox.splitlines():
        s = Search(line + " audio")
        resultID = str(s.results[0])[-12:-1]
        yt = YouTube('https://www.youtube.com/watch?v=' + resultID)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=str(folder_path))

        out_file = video.download(output_path=str(folder_path))
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

    return


my_text = Text(root, width=60, height=20, font=("Helvetica",12))
my_text.grid(row=0, column=0, pady=20, padx=30, columnspan=3, rowspan=3)


browse_file_button = Button(text="Browse", command=lambda: browse_file(folder_path, file_directory_label))
browse_file_button.grid(row=0, column=4, pady=1, padx=5, rowspan=2)

file_directory_label = Label(text="No directory selected")
file_directory_label.grid(row=1, column=4, pady=2, padx=5)

start_procedure_button = Button(text="Download", command=lambda: yp3_download(my_text))
start_procedure_button.grid(row=2, column=4, pady=2, padx=5)

root.mainloop()
