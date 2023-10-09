import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

FONT_NAME = "Ariel"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    # to copy immediately the password after clicking generate password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left the any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?')
        if is_ok:
            try:
                with open("Data.json", mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("Data.json", mode='w') as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("Data.json", mode='w') as file:
                    json.dump(data, file, indent=4)
                # To clear the field once we click Add button.
            finally:
                # no matter try, except or else work or not, finally will trigger anyway
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- Search Email ------------------------------- #
def search_password():
    website = website_input.get().title()
    try:
        with open("Data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Sorry No Data Found.")
    else:
        # Note, Better to use if else statements rather than try,except when we are dealing frequent errors.
        if website in data:
            messagebox.showinfo(title=website,
                                message=f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
        else:
            messagebox.showerror(title=website, message=f"Sorry website '{website}' does not exist.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="FILE PATH OF IMAGE")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
# because this text is in the middle it edges from website and password.
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_input = Entry(width=31)
# columnspan= expands input label to 2 columns
website_input.grid(row=1, column=1)
# this will focus the cursor
website_input.focus()

email_input = Entry(width=50)
email_input.grid(column=1, columnspan=2, row=2)
# to have the most common email popped up .insert(index, "text")
email_input.insert(0, 'YOUR EMAIL')
pass_generate_button = Button(text="Generate Password", command=generate_pass)
pass_generate_button.grid(column=2, row=3)

password_input = Entry(width=31)
password_input.grid(row=3, column=1)

add_button = Button(text="Add", width=43, command=save_pass)
add_button.grid(column=1, columnspan=2, row=4)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()
