import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry("300x500")
win.title("megajy")
win.configure(bg="white")

image_logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(image_logo)

label_logo = tk.Label(win, image=logo) #type: ignore
label_logo.image = logo
label_logo.pack()

def generator():
    num_generator = random.randint(1, 100)
    selection = Elements.curselection()
    if selection:
        messagebox.showinfo("Попавшее число", f"{Elements.get(selection)} попалось число {num_generator}")
    else:
        messagebox.showerror("Ошибка!", "не выбран элемент пожалуйста выбирите элемент!")

def create():
    text = element_name.get()
    num = Elements.size() + 1
    Elements.insert(tk.END, f"{num}. {text}")
    element_name.delete(0, tk.END)

answer_start = tk.Button(text="генерировать число", bg="red", fg="white", relief="flat", command=generator, cursor="hand2")
answer_start.place(x=85, y=360)
create_element = tk.Button(text="создать элемент", bg="red", fg="white", relief="flat", command=create, cursor="hand2")
create_element.place(x=25, y=260)
element_name = tk.Entry()
element_name.configure(bg="#ebebeb")
element_name.place(x=130, y=266)
Elements = tk.Listbox(win, height=14, width=60, relief="flat")
Elements.configure(bg="#ebebeb")
Elements.pack(pady=7)

items = []

for i, item in enumerate(items, start=1):
    Elements.insert(tk.END, f"{i}. {item}")

tk.mainloop()