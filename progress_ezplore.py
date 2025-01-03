from tkinter import messagebox
from tkinter import *
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

def image_to_button(master, image_path,fg_color, command):
    img = Image.open(image_path)  # Open the image
    img = ImageTk.PhotoImage(img)  # Convert the image to PhotoImage
    button = CTkButton(master, image=img, fg_color=fg_color,text=None,command=command)  # Create the button
    button.image = img  # Store a reference to the image to prevent garbage collection
    return button
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

        self.NAMA_PENGGUNA=StringVar()
        self.PASSWORD=StringVar()

        self.entry_nama_pengguna = CTkEntry(self,textvariable=self.NAMA_PENGGUNA, width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_nama_pengguna.place(x=613, y=287)
        self.entry_password = CTkEntry(self,textvariable=self.PASSWORD, show="*",width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_password.place(x=613, y=329)

        CTkButton(self, text="Masuk", width=50,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9,), command=self.login).place(relx=0.5, rely=0.67, anchor="center")
        image_button = image_to_button(self,"Belum memiliki akun_ Buat akun.png",'#FF8225', lambda: app.show_frame(ValidationAge))
        image_button.place(relx=0.5, rely=0.58, anchor="center")

    def login(self):
        nama_pengguna = self.entry_nama_pengguna.get()
        password = self.entry_password.get()
        if nama_pengguna == "admin" and password == "password":  # Placeholder validation
            self.app.show_frame(DashboardPage)
        else:
            messagebox.showerror("Error", "Invalid credentials")

class ValidationAge(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page2.jpg")

        self.UMUR=IntVar()

        self.entry_umur = CTkEntry(self,textvariable=self.UMUR, width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_umur.place(x=613, y=300)

        #CTkButton(self, text="Selanjutnya", width=50,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9,), command=self.cek_umur_pengguna).place(relx=0.545, rely=0.67, anchor="center")
        CTkButton(self, text="Selanjutnya", width=50,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9,), command=lambda: app.show_frame(DashboardPage)).place(relx=0.545, rely=0.67, anchor="center")

#BUKA UNTUK UJI SYNTAX
#    def cek_umur_pengguna(self):
#        umur_pengguna = int(self.entry_umur.get())
#        try:
#            if umur_pengguna < 18:
#                messagebox.showinfo("Info", "Usia minimal untuk mendaftar adalah 18 tahun!")
#            else:
#                self.app.show_frame(RegistrationPage)
#        except ValueError:
#            if self.entry_umur.get() == "":
#                messagebox.showinfo("Info", "Harap lengkapi biodata usia Anda!")
#            else:
#                messagebox.showinfo("Info", "Masukkan usia yang valid!")

class RegistrationPage(Frame):
    def __init__(self, app):
        super().__init__(app.master)
        self.app = app
        setup_background(self,"page3.jpg")

        self.NAMA_PENGGUNA=StringVar()
        self.NOMOR_TELEPON=IntVar()
        self.PASSWORD=StringVar()

        self.entry_nama_pengguna = CTkEntry(self,textvariable=self.NAMA_PENGGUNA, width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_nama_pengguna.place(x=613, y=287)
        self.entry_nomor_telepon = CTkEntry(self,textvariable=self.NOMOR_TELEPON, width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_nomor_telepon.place(x=613, y=329)
        self.entry_password = CTkEntry(self,textvariable=self.PASSWORD,width=120,height=12 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 9))
        self.entry_password.place(x=613, y=371)

        CTkButton(self, text="Selanjutnya", width=50,height=13 ,fg_color='#163B44', text_color='#F7EDEC', font=('Inter', 8,), command=lambda: app.show_frame(DashboardPage)).place(relx=0.545, rely=0.67, anchor="center")

#    def register(self):
#        # MENGECEK APAKAH SUDAH TERISI
#        try:
#            nama_pengguna = self.entry_nama_pengguna.get()
#            nomor_telepon = self.entry_nomor_telepon()
#            password = self.entry_password.get()
#            if nama_pengguna and password and nomor_telepon: #Seluruh field terisi
#          # Placeholder validation
#                self.app.show_frame(DashboardPage)
#            else:
#                messagebox.showerror("Error", "Harap lengkapi semua data!")
#        except Exception as e:
#            messagebox.showinfo("Info", f"Terjadi kesalahan: {e}")

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
