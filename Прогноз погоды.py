import requests
from bs4 import BeautifulSoup
from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Прогноз погоды")
root.geometry("400x200")
root["bg"] = "red"

Label(root, text = "Прогноз погоды", font="Consolas 15 italic").pack(pady=5)
Label(root, text = "Введите город: ", font="Consolas 11 italic").pack(pady=5)

city = Entry(root, width=40)
city.pack()

def temp():
    a = str(city.get())
    search = f'Погода в {a}'

    url = f'https://www.google.com/search?&q={search}'

    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    update = s.find("div", class_="BNeawe").text

    messagebox.showinfo("Погода", "В городе " + a + " температура " + update)

    city.delete(0, END)

Button(root, text="Узнать погоду", command= temp).pack()


root.mainloop()
