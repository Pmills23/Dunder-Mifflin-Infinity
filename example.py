#These lines import the tkinter and Pil module for use in this GUI
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#Create a window
root = tk.Tk()
root.title("Dunder Mifflin Infinity")

#Set the window size
root.geometry("800x600")

#Create a header label
header_label = tk.Label(root, text="Dunder Mifflin Infinity", font=("Helvetica", 24))
header_label.pack()

#Create a navigation bar
nav_bar = tk.Frame(root, bg="gray", height=50)
nav_bar.pack(fill=tk.X)

#Add navigation buttons to the navigation bar
home_button = tk.Button(nav_bar, text="Home", padx=10, pady=5)
home_button.pack(side=tk.LEFT)
products_button = tk.Button(nav_bar, text="Products", padx=10, pady=5, command=lambda: show_products())
products_button.pack(side=tk.LEFT)
about_button = tk.Button(nav_bar, text="About", padx=10, pady=5)
about_button.pack(side=tk.LEFT)
contact_button = tk.Button(nav_bar, text="Contact", padx=10, pady=5, command=lambda: show_contact())
contact_button.pack(side=tk.LEFT)

#Add exit button to the navigation bar
exit_button = tk.Button(nav_bar, text="Exit", padx=10, pady=5)
exit_button.pack(side=tk.RIGHT)

# Create a main content area
content_area = tk.Frame(root, bg="white", height=500)
content_area.pack(fill=tk.BOTH, expand=True)

# Add some sample text to the home page
home_text_label = tk.Label(content_area, text="Welcome to Dunder Mifflin Infinity!")
home_text_label.pack(pady=50)

# Create a sign-in form
sign_in_frame = tk.Frame(content_area, bg="white")
sign_in_frame.pack(pady=50)
username_label = tk.Label(sign_in_frame, text="Username:")
username_label.pack()
username_entry = tk.Entry(sign_in_frame)
username_entry.pack(pady=5)
password_label = tk.Label(sign_in_frame, text="Password:")
password_label.pack()
password_entry = tk.Entry(sign_in_frame, show="*")
password_entry.pack(pady=5)
sign_in_button = tk.Button(sign_in_frame, text="Sign In", padx=10, pady=5)
sign_in_button.pack(pady=10)

#This function shows the products when that button is clicked
def show_products():
    #Clears the information on the screen
    for child in content_area.winfo_children():
        child.destroy()
    #Fake products for the product page are displayed
    product1_label = tk.Label(content_area, text="High quality printer paper")
    product1_label.pack(pady=10)
    product2_label = tk.Label(content_area, text="Legal Envelopes")
    product2_label.pack(pady=10)
    product3_label = tk.Label(content_area, text="Crumpled up paper balls")
    product3_label.pack(pady=10)

#This function shows the contact information when the button is clicked
def show_contact():
    #Clears the information on the screen
    for child in content_area.winfo_children():
        child.destroy()
    #Adds contact information to the screen
    name_label = tk.Label(content_area, text="Paul Mills", font=("Helvetica", 16))
    name_label.pack(pady=10)
    phone_label = tk.Label(content_area, text="(827)-274-5526", font=("Helvetica", 12))
    phone_label.pack(pady=5)
    bio_label = tk.Label(content_area,
        text="Paul Mills has been working for Dunder Mifflin for over 10 years. He is dedicated to providing excellent customer service and is always available to answer any questions you may have.",
        wraplength=600, justify="center")
    bio_label.pack(pady=20)

#This function shows the home sign in information when pressed
def show_home():
    #Clears the information on the screen
    for widget in content_area.winfo_children():
        widget.destroy()
    #Recreates the home page
    text_label = tk.Label(content_area, text="Welcome to Dunder Mifflin Infinity!")
    text_label.pack(pady=50)
    sign_in_frame = tk.Frame(content_area, bg="white")
    sign_in_frame.pack(pady=50)
    username_label = tk.Label(sign_in_frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(sign_in_frame)
    username_entry.pack(pady=5)
    password_label = tk.Label(sign_in_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(sign_in_frame, show="*")
    password_entry.pack(pady=5)
    sign_in_button = tk.Button(sign_in_frame, text="Sign In", padx=10, pady=5)
    sign_in_button.pack(pady=10)
    sign_in_button.configure(command=lambda: handle_login(username_entry, password_entry))

#Configures home button to show home content
home_button.configure(command=show_home)

#This function shows the about page when clicked
def show_about():
    #Clears the information on the screen
    for widget in content_area.winfo_children():
        widget.destroy()
    #Displays the information regarding Dunder Mifflin
    about_label = tk.Label(content_area,
        text="Dunder Mifflin is a fictional paper company from the television show 'The Office'. It is known for its unique brand of humor and its eclectic cast of characters.")
    about_label.pack(pady=50)
    #This displays the image
    image2 = Image.open("d:/Users/Valued Customer/Downloads/p185008_b_h10_ai (1).jpg")
    photo2 = ImageTk.PhotoImage(image2)
    image2_label = tk.Label(content_area, image=photo2)
    image2_label.image = photo2
    image2_label.pack()

#Configures about button to show about content
about_button.configure(command=show_about)

#Function to exit the GUI
def exit_app():
    root.destroy()

#This function shows the TV quote when the sign-in process is accepted
def show_quote():
    #Clears the information on the screen
    for widget in content_area.winfo_children():
        widget.destroy()
    #This displays the quote
    quote_label = tk.Label(content_area, text="That's what she said!", font=("Helvetica", 24))
    quote_label.pack(pady=50)
    #This displays the image under the quote
    image = Image.open("d:/Users/Valued Customer/Downloads/maxresdefault (2).jpg")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(content_area, image=photo)
    image_label.image = photo
    image_label.pack()

#This function handles checking the information upon clicking the log-in button
def handle_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if username == "Michael" and password == "1234":
        show_quote()
    else:
        tk.messagebox.showerror("Error", "Invalid username or password.")

#Configures log-in button to show log-in content
sign_in_button.configure(command=lambda: handle_login(username_entry, password_entry))

#Configures exit button to exit the GUI
exit_button.configure(command=exit_app)

#Runs the application and tells it to listen to button clicks and user input
root.mainloop()
