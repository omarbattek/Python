from tkinter import *



window = Tk()

window.title("My first GUI ")
window.minsize(width=200, height=100)
window.config(padx=15, pady=15)
window.config(background="white")


my_label = Label(text= "is equal to", font= ("Arial", 14, "bold"))
my_label.grid(column=0, row=1)
my_label.config(background="white")

label_miles = Label(text="Miles", font=("Arial", 10, "bold"))
label_miles.grid(column=3, row=0)
label_miles.config(background="white")

label_num = Label(text=0, font=("Arial", 10, "bold"))
label_num.grid(column=1, row=1)
label_num.config(background="white")

label_km = Label(text="Km", font=("Arial", 10, "bold"))
label_km.grid(column="2", row=1)
label_km.config(background="white")
def button_clicked():
    my_text = input.get()
    kilometer = int(my_text)* 1.609344
    kilometer = round(kilometer, 3)
    label_num.config(text=kilometer)

button = Button(text= "click me", command = button_clicked)
button.grid(column=1, row=2)
button.config(background="white")


input = Entry(width="10")
input.grid(column=1, row=0)
input.config(background="white")

window.mainloop()