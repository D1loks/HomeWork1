import tkinter as tk


def main():
    global root, label
    root.geometry("300x300")
    root.title("Hello World")
    label = tk.Label(root, text="First entry", font=("Arial", 16))
    button = tk.Button(root, text="Hello World", command=button_click, font=("Arial", 16))
    label.pack(pady=20)
    button.pack(pady=20)
    root.mainloop()


if __name__ == '__main__':
    main()
