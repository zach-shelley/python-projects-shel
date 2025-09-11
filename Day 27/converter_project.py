import tkinter
from tkinter import Entry

FONT = ('Calibre', 16)

window = tkinter.Tk()
window.title('Miles to Km Converter')
window.minsize(width= 100, height=80)
window.config(padx=50, pady=50)


equal_label = tkinter.Label(text='Is equal to', font=FONT)
equal_label.grid(column=0, row=2)

miles_label = tkinter.Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=1)

km_label = tkinter.Label(text='Km', font=FONT)
km_label.grid(column=2, row=2)

conv_label = tkinter.Label(text= 0, font=FONT)
conv_label.grid(column=1, row=2)

def button_clicked():
    miles = float(miles_input.get())
    km_conv = miles * 1.60934
    conv_label.config(text=km_conv)


calculate_button = tkinter.Button(text= 'Calculate', command=button_clicked)
calculate_button.grid(column=1, row=3)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=1)




window.mainloop()
