from tkinter import messagebox
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from customtkinter import *
import customtkinter as ctk

def setup_background(master, image_path):
    screen_width = 412
    screen_height = 917
    image = Image.open(image_path).resize((screen_width, screen_height))
    photo = ImageTk.PhotoImage(image)
    label = Label(master, image=photo)
    label.image = photo  # Prevent garbage collection
    #label.place(x=0, y=0)
    label.place(relx=0.5, rely=0.5, anchor="center")

def configure_background(widget, color="black"):
    widget.configure(bg=color)

class EzploreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ezplore App")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.configure=("black")
        self.master.geometry(f"{screen_width}x{screen_height}")
        self.master.resizable(True, True)
        #self.master.state("zoomed")

        self.canvas = Canvas(master, width=412, height=917, bg="black")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.android_frame = Frame(self.canvas, width=412, height=917, bg="black")
        self.android_frame.place(x=0, y=0)

        self.current_frame = None
        self.show_frame(LoginPage)

    def show_frame(self, frame_class):
        #Switch to a new frame.
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        configure_background(self.current_frame, "black")
        self.current_frame.pack(fill="both", expand=True)


class LoginPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page1.jpg")

        #CTkLabel(self, text="Username:").place(x=500, y=300)
        self.entry_nama_pengguna = CTkEntry(self)
        self.entry_nama_pengguna.place(x=575, y=300)
        self.entry_password = CTkEntry(self, show="*")
        self.entry_password.place(x=575, y=350)

        CTkButton(self, text="Login", command=self.login).place(x=550, y=400)
        CTkButton(self, text="Sign Up", command=lambda: app.show_frame(ValidationAge)).place(x=650, y=400)

    def login(self):
        username = self.entry_nama_pengguna.get()
        password = self.entry_password.get()
        if username == "admin" and password == "password":  # Placeholder validation
            self.app.show_frame(DashboardPage)
        else:
            messagebox.showerror("Error", "Invalid credentials")

class ValidationAge(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page2.jpg")

        CTkLabel(self, text="Create an Account").pack(pady=20)

        CTkButton(self, text="Selanjutnya", command=lambda: app.show_frame(RegistrationPage)).place(x=550, y=400)
        CTkButton(self, text="Back to Login", command=lambda: app.show_frame(DashboardPage)).place(x=650, y=400)

class RegistrationPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page3.jpg")

        CTkButton(self, text="Register", command=lambda: app.show_frame(DashboardPage)).place(x=550, y=400)
        CTkButton(self, text="Back to Login", command=lambda: app.show_frame(DashboardPage)).place(x=650, y=400)

    def register(self):
        username = self.entry_nama_pengguna.get()
        password = self.entry_password.get()
        # Implement actual registration logic
        messagebox.showinfo("Success", "Registration Successful!")
        self.app.show_frame(LoginPage)


class DashboardPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page4.jpg")

        CTkLabel(self, text="Welcome to Ezplore Dashboard").pack(pady=20)

        CTkButton(self, text="Booking", command=lambda: app.show_frame(BookingPage)).pack(pady=10)
        CTkButton(self, text="Logout", command=lambda: app.show_frame(LoginPage)).pack(pady=10)


class BookingPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page5.jpg")

        CTkLabel(self, text="Welcome to Ezplore Booking Page").pack(pady=20)

        CTkButton(self, text="Back to Dashboard", command=lambda: app.show_frame(DashboardPage)).pack(pady=10)
        CTkButton(self, text="Selanjutnya", command=lambda: app.show_frame(HotelPage)).pack(pady=10)


class HotelPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page6.jpg")

        CTkLabel(self, text="Welcome to Ezplore Hotel Page").pack(pady=20)

        CTkButton(self, text="Back to Dashboard", command=lambda: app.show_frame(DashboardPage)).pack(pady=10)
        CTkButton(self, text="Booking", command=lambda: app.show_frame(BookingKamar)).pack(pady=10)

class BookingKamar(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page7.jpg")

        CTkLabel(self, text="Welcome to Ezplore Booking Kamar").pack(pady=20)

        CTkButton(self, text="Back to Dashboard", command=lambda: app.show_frame(DashboardPage)).pack(pady=10)
        CTkButton(self, text="Logout", command=lambda: app.show_frame(LoginPage)).pack(pady=10)

if __name__ == "__main__":
    root = ctk.CTk()
    app = EzploreApp(root)
    ctk.set_appearance_mode('white')
    root.mainloop()
