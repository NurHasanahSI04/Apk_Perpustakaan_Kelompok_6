import tkinter 
from tkinter import ttk
import tkinter as tk
import customtkinter
from tkinter import messagebox



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")



def halaman():
    l.destroy()
    w=customtkinter.CTk()
    w.geometry('1500x900')
    w.title('Home')
    l1= customtkinter.CTkLabel(master=w, text="SELAMAT DATANG \n SILAHKAN PILIH MENU", font=('Impact', 60))
    l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    button1 = customtkinter.CTkButton(master= w, text="Daftar Buku", command= tombol)
    button1.place(relx=0.39, rely=0.7, anchor=tkinter.CENTER)

    
    button2 = customtkinter.CTkButton(master= w, text="Peminjaman Buku", command= tombol2)
    button2.place(relx=0.60, rely=0.7, anchor=tkinter.CENTER)

    w.mainloop()
   

def tombol():
    

    c=customtkinter.CTk()
    c.title('Daftar Koleksi Buku')
    c.geometry('1200x1000')
    label_daftar_buku = customtkinter.CTkLabel(c, text="DAFTAR KOLEKSI BUKU", font=("impact", 60))
    label_daftar_buku.place(relx=0.5,rely=0.18,anchor=tkinter.CENTER)
    
    bingkai = customtkinter.CTkFrame(master=c,
                               width=500,
                               height=300,
                               corner_radius=20)
    bingkai.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    c.listbox_daftar_buku = tk.Listbox(master=c, width=30, height=10)
    c.listbox_daftar_buku.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    daftar_buku = ["Layangan Putus - Mommy ASF", "Laskar Pelangi - Andrea Hirata", "Hujan - Tere Liye", "Bumi Manusia - Pramoedya Ananta Toer", "Cantik Itu Luka - Eka Kurniawan"]
    for buku in daftar_buku:
        c.listbox_daftar_buku.insert(tk.END, buku)
        
    button1 = customtkinter.CTkButton(master= c, text="Kembali", command=page)
    button1.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)  

    c.mainloop()
    
def page():
    w=customtkinter.CTk()
    w.geometry('1500x900')
    w.title('Home')
    l1= customtkinter.CTkLabel(master=w, text="SELAMAT DATANG \n SILAHKAN PILIH MENU", font=('Impact', 60))
    l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    button1 = customtkinter.CTkButton(master= w, text="Daftar Buku", command= tombol)
    button1.place(relx=0.39, rely=0.7, anchor=tkinter.CENTER)

    
    button2 = customtkinter.CTkButton(master= w, text="Peminjaman Buku", command= tombol2)
    button2.place(relx=0.60, rely=0.7, anchor=tkinter.CENTER)

    w.mainloop()


def tombol2():
    b=customtkinter.CTk()
    b.title('welcome')
    b.geometry('900x900')
    t=customtkinter.CTkLabel(master=b, text="SYARAT PEMINJAMAN BUKU",font=('impact', 30))
    t.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    l1= customtkinter.CTkLabel(master=b, text=" 1.Terdaftar sebagai anggota.\n 2. Hanya bisa meminjam maksimal 1 buku\n 3. Masa peminjaman berlaku selama 14 hari. \n 4. Perpanjangan masa pinjam dapat dilakukan sebanyak satu kali \ndan berlaku selama 14 hari dari tanggal jatuh tempo peminjaman pertama.", 
                               font=('arial', 17))
    l1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    
    button4 = customtkinter.CTkButton(master=b, text="Pinjam Buku",command=pinjam)
    button4.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    b.mainloop()
    
def pinjam():
    b = tk.Toplevel()
    b.title('Form Peminjaman')
    b.geometry('900x900')

    bingkai = customtkinter.CTkFrame(master=b,
                                     width=500,
                                     height=350,
                                     corner_radius=20,)
    
    bingkai.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    judul = customtkinter.CTkLabel(master=b, text="Nama Peminjam  :", font=('Century Ghotic', 15))
    judul.place(relx=0.38, rely=0.4, anchor=tk.CENTER)

    label_nama = customtkinter.CTkLabel(master=b, text="FORM PEMINJAMAN BUKU :", font=('impact', 30))
    label_nama.place(relx=0.5, rely=0.17, anchor=tk.CENTER)

    nama_lengkap = customtkinter.CTkEntry(b,width=220, placeholder_text="Nama Lengkap")
    nama_lengkap.place(relx=0.58, rely=0.4, anchor=tk.CENTER)

    label_judul = customtkinter.CTkLabel(master=b, text="Judul Buku  :", font=('Century Ghotic', 15))
    label_judul.place(relx=0.39, rely=0.5, anchor=tk.CENTER)

    daftar_buku = ["Layangan Putus - Mommy ASF", "Laskar Pelangi - Andrea Hirata", "Hujan - Tere Liye", "Bumi Manusia - Pramoedya Ananta Toer", "Cantik Itu Luka - Eka Kurniawan"]

   
    selected_book = tk.StringVar()
    b.dropdown_daftar_buku = ttk.Combobox(b,width=28, textvariable=selected_book, values=daftar_buku, state="readonly")
    b.dropdown_daftar_buku.place(relx=0.58, rely=0.5, anchor=tk.CENTER)

    submit_button = customtkinter.CTkButton(master=b, text="submit", command=lambda: submit_form(b, nama_lengkap, selected_book))
    submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    b.mainloop()

def submit_form(window, nama_entry, selected_book):
    nama_peminjam = nama_entry.get()
    judul_buku = selected_book.get()

    
    print(f"Nama Peminjam: {nama_peminjam}")
    print(f"Judul Buku: {judul_buku}")

    

    window.destroy()


def submit_form(b, nama_lengkap, judul_buku):
    peminjam = nama_lengkap.get()
    judul = judul_buku.get()

    if judul and peminjam:
        messagebox.showinfo("Sukses", f"{judul} telah berhasil dipinjam oleh {peminjam}")
        
        
    else:
        messagebox.showerror("Error", "Mohon isi semua kolom")
    

    b.mainloop()

def on_login():
        if entry1.get() == "user" and entry2.get() == "password":
            halaman()
        else:
            messagebox.showerror("Error", "Username atau password salah!")  

l = customtkinter.CTk()
l.title("Perpustakaan Nurul Fikri")
l.geometry("1200x1200")


label_selamat_datang = customtkinter.CTkLabel( master=l, text="APLIKASI PERPUSTAKAAN DIGITAL \n STT TERPADU NURUL FIKRI", font=("impact", 55))
label_selamat_datang.place(relx=0.5, rely=0.19, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=l,
                               width=310,
                               height=296,
                               corner_radius=20,)

frame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y=155)

button1 = customtkinter.CTkButton(master= frame, text="Login", command= halaman)
button1.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)


l.mainloop()

