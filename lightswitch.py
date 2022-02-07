import tkinter as tk
window = tk.Tk()

# schijf hier tussen je code

def clickyOnOff():
    if button.config('text')[-1] == 'Switch light off':
        button.config(text='Switch light on', bg='white', fg='black')
        window.config(bg='black')
    else:
        button.config(text='Switch light off', bg='white', fg='black')
        window.config(bg='yellow')

# schijf hier tussen je code

button = tk.Button(window, text='Switch light on', bg="white", fg="black", command=clickyOnOff)
button.pack(pady = 20, padx = 20)
window.config(bg='black')

window.mainloop()