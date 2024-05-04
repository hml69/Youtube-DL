import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
from tkinter import ttk

def download_video():
    try:
        yt = YouTube(url_entry.get())
        if file_type_var.get() == "MP4":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            save_path = filedialog.asksaveasfilename(defaultextension=".mp4", initialfile=yt.title + ".mp4")
            if save_path:
                stream.download(output_path=save_path)
                messagebox.showinfo("Success", "Video downloaded successfully!")
        elif file_type_var.get() == "MP3":
            audio_stream = yt.streams.filter(only_audio=True).first()
            save_path = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile=yt.title + ".mp3")
            if save_path:
                audio_stream.download(output_path=save_path)
                messagebox.showinfo("Success", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Tải video Youtube nhanh")
root.geometry("400x250")

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = ttk.Label(main_frame, text="Tải video Youtube nhanh", font=("Helvetica", 20, "bold"), style='TLabel')
title_label.grid(row=0, column=0, columnspan=2, pady=10)

url_label = ttk.Label(main_frame, text="Nhập đường dẫn YouTube:", style='TLabel')
url_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

url_entry = ttk.Entry(main_frame, width=30)
url_entry.grid(row=1, column=1, padx=10, pady=5)

file_type_label = ttk.Label(main_frame, text="Chọn định dạng file:", style='TLabel')
file_type_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

file_type_var = tk.StringVar()
file_type_var.set("MP4")
file_type_menu = ttk.Combobox(main_frame, textvariable=file_type_var, values=["MP4", "MP3"], style='TCombobox', state='readonly')
file_type_menu.grid(row=2, column=1, padx=10, pady=5)

download_button = ttk.Button(main_frame, text="Tải xuống", command=download_video, style='TButton')
download_button.grid(row=3, column=0, columnspan=2, pady=10)

style = ttk.Style()
style.configure('TLabel', background="#f0f0f0")
style.configure('TEntry', background="white")
style.configure('TCombobox', background="white")

root.mainloop()
