from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from datetime import date

def main_window():
    win = Tk()
    win.title("Date Calculator")
    win.geometry("350x200")
    win.configure(bg = "#abcdef")

    image_canvas = Canvas(win, height = 200, width = 200, bg = "#abcdef", highlightthickness = 0)
    image_canvas.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)
    photo = PhotoImage(file = "c://Users//Leo//Desktop//clock.png")
    image_canvas.create_image(0, 0, image = photo, anchor = NW)

    Label(win, text = "First Date", bg = "#abcdef").grid(row = 3, column = 8)
    first_date = DateEntry(win)
    #first_date = Entry(win)
    first_date.grid(row = 4, column = 8)

    Label(win, text = "Second Date", bg = "#abcdef").grid(row = 5, column = 8)
    second_date = DateEntry(win)
    #second_date = Entry(win)
    second_date.grid(row = 6, column = 8)

    Button(win, text = "Calculate", command = lambda: calculate(first_date, second_date)).grid(row = 7, column = 8)

    win.mainloop()

def calculate(first_date, second_date):
    try:
        difference = first_date.get_date() - second_date.get_date()
        messagebox.showinfo("Differece", f"{difference.days} days reamaining.")
    
    except:
        try:
            day_1, month_1, year_1 = first_date.get().split("-")
            day_2, month_2, year_2 = second_date.get().split("-")

            difference = date(int(year_1), int(month_1), int(day_1)) - date(int(year_2), int(month_2), int(day_2))
            messagebox.showinfo("Differece", f"{difference.days} days reamaining.")

        except ValueError as error:
            messagebox.showerror("ValueError", error)


if __name__ == "__main__":
    main_window()