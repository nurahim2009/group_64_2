import tkinter as tk

root = tk.Tk()
root.title("Счётчик")

count = 0

def on_click():
    global count
    count += 1
    text_hello.config(text=f"Нажато: {count} раз")

text_hello = tk.Label(root, text="Нажато: 0 раз", font=("Arial", 14))
text_hello.pack(pady=10)

btn = tk.Button(root, text="Нажми меня", command=on_click)
btn.pack(pady=10)

root.mainloop()