from lib.connection import connection
from lib.auth import auth
from lib.find_user import Finduser
from lib.changepass import Changepass
from lib.find_soal import Findsoal
from lib.add_user import Adduser
from lib.del_user import Deluser
from lib.add_soal import Addsoal
from lib.del_soal import Delsoal
from lib.level_user import Leveluser
from lib.add_result import Addresult
from lib.check_kode import Checkkode

import tkinter.font as font
import random
import string
import pandas
import json

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from tkextrafont import Font

# window.iconbitmap("assets/mylogo.ico")


class Ujian:
    def __init__(self, master, fullname, kodeujian):
        self.fullname = fullname
        self.username = master
        self.kodeujian = kodeujian
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/background_ujian.png')
        self.sebelumnya = PhotoImage(file='assets/btn-sebelumnya.png')
        self.selanjutnya = PhotoImage(file='assets/btn-selanjutnya.png')
        self.pilihan = PhotoImage(file='assets/btn-abcd.png')
        self.btnimg_clicked = PhotoImage(file='assets/btn-abcd-clicked.png')
        self.positition = ""
        self.jumlah_soal = 0
        self.nomor_soal = 1
        self.index_soal = 0
        self.soal_dijawab = 0
        self.soal_belumdijawab = 0

        self.jawabansementara = []
        self.posisi_jawabansementara = 1

        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Keluar", "Apakah kamu ingin keluar? Data yang sudah disimpan tidak dapat dirubah kembali."):
            self.window.destroy()

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.window.destroy()
            messagebox.showinfo("Selesai!", "Soal sudah selesai!")
        else:
            mins, secs = divmod(self.remaining, 60)

            self.menit.configure(text="{0:2d}".format(mins))
            self.detik.configure(text="{0:2d}".format(secs))

            self.remaining = self.remaining - 1
            self.window.after(1000, self.countdown)

    def bersih(self):
        self.pilihan_a.config(image=self.pilihan)
        self.pilihan_b.config(image=self.pilihan)
        self.pilihan_c.config(image=self.pilihan)
        self.pilihan_d.config(image=self.pilihan)
        self.pilihan_e.config(image=self.pilihan)
        self.positition = ""

    def btn_clicked_a(self):
        self.bersih()
        self.pilihan_a.config(image=self.btnimg_clicked)
        self.positition = "A"
        if self.posisi_jawabansementara <= self.nomor_soal:
            self.posisi_jawabansementara += 1
            self.jawabansementara.append(self.positition)

        if self.posisi_jawabansementara > self.nomor_soal:
            self.jawabansementara[self.index_soal] = "A"

    def btn_clicked_b(self):
        self.bersih()
        self.pilihan_b.config(image=self.btnimg_clicked)
        self.positition = "B"
        if self.posisi_jawabansementara <= self.nomor_soal:
            self.posisi_jawabansementara += 1
            self.jawabansementara.append(self.positition)

        if self.posisi_jawabansementara > self.nomor_soal:
            self.jawabansementara[self.index_soal] = "B"

    def btn_clicked_c(self):
        self.bersih()
        self.pilihan_c.config(image=self.btnimg_clicked)
        self.positition = "C"
        if self.posisi_jawabansementara <= self.nomor_soal:
            self.posisi_jawabansementara += 1
            self.jawabansementara.append(self.positition)

        if self.posisi_jawabansementara > self.nomor_soal:
            self.jawabansementara[self.index_soal] = "C"

    def btn_clicked_d(self):
        self.bersih()
        self.pilihan_d.config(image=self.btnimg_clicked)
        self.positition = "D"
        if self.posisi_jawabansementara <= self.nomor_soal:
            self.posisi_jawabansementara += 1
            self.jawabansementara.append(self.positition)

        if self.posisi_jawabansementara > self.nomor_soal:
            self.jawabansementara[self.index_soal] = "D"

    def btn_clicked_e(self):
        self.bersih()
        self.pilihan_e.config(image=self.btnimg_clicked)
        self.positition = "E"
        if self.posisi_jawabansementara <= self.nomor_soal:
            self.posisi_jawabansementara += 1
            self.jawabansementara.append(self.positition)

        if self.posisi_jawabansementara > self.nomor_soal:
            self.jawabansementara[self.index_soal] = "E"

    def simpan_jawaban(self):
        print(self.jawabansementara)
        print(self.index_soal)
        if self.jawabansementara[self.index_soal] == "A":
            self.btn_clicked_a()
            print("A")
        elif self.jawabansementara[self.index_soal] == "B":
            self.btn_clicked_b()
            print("B")
        elif self.jawabansementara[self.index_soal] == "C":
            self.btn_clicked_c()
            print("C")
        elif self.jawabansementara[self.index_soal] == "D":
            self.btn_clicked_d()
            print("D")
        elif self.jawabansementara[self.index_soal] == "E":
            self.btn_clicked_e()
            print("E")

    def refresh(self):
        getsoal = Findsoal(self.kodeujian).kode()
        if getsoal["status"] == 200:
            self.terjawab.config(text=str(self.soal_dijawab))
            self.belumdijawab.config(text=str(self.soal_belumdijawab))
            self.pertanyaan.config(text="Soal " + str(self.nomor_soal))
            self.soal.config(text=getsoal["msg"][self.index_soal]["soal"])
            self.jawaban_a.config(text=getsoal["msg"][self.index_soal]["opsi_a"])
            self.jawaban_b.config(text=getsoal["msg"][self.index_soal]["opsi_b"])
            self.jawaban_c.config(text=getsoal["msg"][self.index_soal]["opsi_c"])
            self.jawaban_d.config(text=getsoal["msg"][self.index_soal]["opsi_d"])
            self.jawaban_e.config(text=getsoal["msg"][self.index_soal]["opsi_e"])
        else:
            messagebox.showwarning(
            "Peringatan!", "Kode soal tidak ditemukan!")

    def next_jawaban(self):
        if self.positition == "":
            messagebox.showwarning(
            "Peringatan!", "Jawaban tidak boleh kosong!")
        else:
            if self.nomor_soal >= self.jumlah_soal:
                if messagebox.askokcancel("Peringatan", "Jawaban yang telah dikirim tidak dapat diubah!"):
                    Addresult(self.kodeujian, self.jawabansementara, self.username).add()
                    self.window.destroy()
            else:   
                self.soal_belumdijawab -= 1
                self.soal_dijawab += 1
                self.nomor_soal += 1
                self.index_soal += 1
                if self.posisi_jawabansementara > self.nomor_soal:
                    self.simpan_jawaban()
                else:
                    self.bersih()
                self.refresh()

    def previous_jawaban(self):
        if self.soal_dijawab < 1:
            if messagebox.askokcancel("Keluar", "Apakah kamu ingin keluar? Data yang sudah disimpan tidak dapat dirubah kembali."):
                self.window.destroy()
        else:
            self.soal_belumdijawab += 1
            self.soal_dijawab -= 1
            self.nomor_soal -= 1
            self.index_soal -= 1
            if self.posisi_jawabansementara <= self.nomor_soal:
                self.bersih()
            self.simpan_jawaban()
            self.refresh()


    def main(self):

        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=14)

        font_jawaban = Font(file="assets/font/Manrope-Regular.ttf",
                            family="Manrope Regular", size=15)

        font_matkul = Font(file="assets/font/Quattrocento-Bold.ttf", family="Quattrocento Bold", size=18)

        self.menit = Label(self.window, text="", font=font, fg='#068EDA',
                           bg="#E4F5FF", width=3, borderwidth=0, anchor="w")  # bg='#969696'
        self.menit.place(x=1095, y=37)

        self.titik = Label(self.window, text=":", font=font, fg='#068EDA',
                           bg="#E4F5FF", width=2, borderwidth=0, anchor="w")  # bg='#969696'
        self.titik.place(x=1137, y=37)

        self.detik = Label(self.window, text="", font=font, fg='#068EDA',
                           bg="#E4F5FF", width=3, borderwidth=0, anchor="w")  # bg='#969696'
        self.detik.place(x=1150, y=37)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=15, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=750, y=70)  # 380

        self.remaining = 0

        countsoal = Findsoal(self.kodeujian).kode()
        self.jumlah_soal = countsoal["jumlah"]
        
        self.soal_belumdijawab = countsoal["jumlah"]


        self.temp = int(00)*3600 + int(countsoal["durasi"])*60 + int(10)
        self.countdown(self.temp)


        self.matkul = Label(self.window, text = countsoal["matkul"], font=font_matkul, fg='#000000', bg = "#E4F5FF", width=40,borderwidth=0, anchor="w") #bg='#969696'
        self.matkul.place(x=365, y=114)

        self.pertanyaan = Label(self.window, text="Soal 1", font=font, fg='#068EDA',
                                bg="#E4F5FF", width=5, borderwidth=0, anchor="w")  # bg='#969696'
        self.pertanyaan.place(x=70, y=168)



        self.soal = Label(self.window, text="\n", font=font, fg='#000000',
                          bg="#ffffff", width=500, borderwidth=0, anchor="w")  # bg='#969696'
        self.soal.place(x=70, y=195)
        self.terjawab = Label(self.window, text="17", font=font, fg='#000000',
                              bg="#E4F5FF", width=5, borderwidth=0, anchor="w")  # bg='#969696'
        self.terjawab.place(x=1060, y=105)
        self.belumdijawab = Label(self.window, text="17", font=font, fg='#000000',
                                  bg="#E4F5FF", width=5, borderwidth=0, anchor="w")  # bg='#969696'
        self.belumdijawab.place(x=1185, y=105)

        self.pilihan_a = Button(self.window, image=self.pilihan, borderwidth=0, height=40,
                                width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.btn_clicked_a)
        self.pilihan_a.place(x=50, y=260)

        self.pilihan_b = Button(self.window, image=self.pilihan, borderwidth=0, height=40,
                                width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.btn_clicked_b)
        self.pilihan_b.place(x=50, y=310)

        self.pilihan_c = Button(self.window, image=self.pilihan, borderwidth=0, height=40,
                                width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.btn_clicked_c)
        self.pilihan_c.place(x=50, y=360)

        self.pilihan_d = Button(self.window, image=self.pilihan, borderwidth=0, height=40,
                                width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.btn_clicked_d)
        self.pilihan_d.place(x=50, y=410)

        self.pilihan_e = Button(self.window, image=self.pilihan, borderwidth=0, height=40,
                                width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.btn_clicked_e)
        self.pilihan_e.place(x=50, y=460)

        self.jawaban_a = Label(self.window, text="jawaban 1", font=font_jawaban, fg='#000000',
                               bg="#ffffff", width=20, borderwidth=0, anchor="w")  # bg='#969696'
        self.jawaban_a.place(x=200, y=260)

        self.jawaban_b = Label(self.window, text="jawaban 2", font=font, fg='#000000',
                               bg="#ffffff", width=20, borderwidth=0, anchor="w")  # bg='#969696'
        self.jawaban_b.place(x=200, y=310)

        self.jawaban_c = Label(self.window, text="jawaban 3", font=font, fg='#000000',
                               bg="#ffffff", width=20, borderwidth=0, anchor="w")  # bg='#969696'
        self.jawaban_c.place(x=200, y=360)

        self.jawaban_d = Label(self.window, text="jawaban 4", font=font, fg='#000000',
                               bg="#ffffff", width=20, borderwidth=0, anchor="w")  # bg='#969696'
        self.jawaban_d.place(x=200, y=410)

        self.jawaban_e = Label(self.window, text="jawaban 5", font=font, fg='#000000',
                               bg="#ffffff", width=20, borderwidth=0, anchor="w")  # bg='#969696'
        self.jawaban_e.place(x=200, y=460)

        '''self.jawaban = Label(self.window, text = "jawaban 1", font=font, fg='#000000', bg = "#ffffff", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.jawaban.place(x=200, y=260)
        #pilihan = Button(self.window, image=self.pilihan, borderwidth=0, height=40, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        #pilihan.place(x=50,y=310)
        self.jawaban = Label(self.window, text = "jawaban 2", font=font, fg='#000000', bg = "#ffffff", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.jawaban.place(x=200, y=310)
        #pilihan = Button(self.window, image=self.pilihan, borderwidth=0, height=40, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        #pilihan.place(x=50,y=360)
        self.jawaban = Label(self.window, text = "jawaban 3", font=font, fg='#000000', bg = "#ffffff", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.jawaban.place(x=200, y=360)
        #pilihan = Button(self.window, image=self.pilihan, borderwidth=0, height=40, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        #pilihan.place(x=50,y=410)
        self.jawaban = Label(self.window, text = "jawaban 4", font=font, fg='#000000', bg = "#ffffff", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.jawaban.place(x=200, y=410)
        pilihan = Button(self.window, image=self.pilihan, borderwidth=0, height=40, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        pilihan.place(x=50,y=460)
        self.jawaban = Label(self.window, text = "jawaban 5", font=font, fg='#000000', bg = "#ffffff", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.jawaban.place(x=200, y=460)'''

        sebelumnya = Button(self.window, image=self.sebelumnya, borderwidth=0,
                            height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.previous_jawaban)
        sebelumnya.place(x=67, y=612)

        selanjutnya = Button(self.window, image=self.selanjutnya, borderwidth=0, height=40,
                             width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.next_jawaban)
        selanjutnya.place(x=1070, y=612)

        self.refresh()


class Setting:
    def __init__(self, master, fullname):
        self.fullname = fullname
        self.username = master
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/background_setting.png')
        self.closewin = PhotoImage(file='assets/btn-logout.png')
        self.upcomingtest = PhotoImage(file='assets/btn-upcoming.png')
        self.setting_bold = PhotoImage(file='assets/btn-settings-bold.png')
        self.startbu = PhotoImage(file='assets/btn-change_pass.png')
        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def setmenu_dashboard(self):
        self.window.destroy()
        Dashboard(self.username, self.fullname)

    def close_windows(self):
        self.window.destroy()

    def verify_pass(self, event):
        if self.before_pass.get():
            if self.password.get():
                if self.password_verify.get():
                    if self.password.get() == self.password_verify.get():
                        check_log = auth(
                            self.username, self.before_pass.get()).acc_login()
                        if check_log["status"] == 200:
                            Changepass(self.username,
                                       self.password.get()).change()
                            messagebox.showinfo(
                                "Sukses!", "Password sukses diubah!")
                        elif check_log["status"] == 400:
                            messagebox.showerror("Invalid", check_log["msg"])
                        else:
                            messagebox.showerror("Invalid", check_log["msg"])
                    else:
                        messagebox.showerror(
                            "Invalid", "Password Verify Harus Sama!")
                else:
                    messagebox.showerror(
                        "Invalid", "Password Verify Tidak Boleh Kosong!")
            else:
                messagebox.showerror("Invalid", "Password Tidak Boleh Kosong!")
        else:
            messagebox.showerror(
                "Invalid", "Password Sebelumnya Tidak Boleh Kosong!")

    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=17)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=28, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=445, y=124)  # 380

        self.before_pass = Entry(self.window, font=(
            'Manrope', 14), fg='#000000', width=25, borderwidth=0)
        self.before_pass.place(x=380, y=235)
        self.password = Entry(self.window, font=(
            'Manrope', 14), fg='#000000', show="*", width=25, borderwidth=0)  # bg='#969696'
        self.password.place(x=380, y=292)
        self.password_verify = Entry(self.window, font=(
            'Manrope', 14), fg='#000000', show="*", width=25, borderwidth=0)  # bg='#969696'
        self.password_verify.place(x=380, y=345)

        start = Button(self.window, image=self.startbu, borderwidth=0, height=50,
                       width=110, bg="#E4F5FF", activebackground="#E4F5FF", command=self.verify_pass)
        start.place(x=463, y=390)

        self.window.bind('<Return>', self.verify_pass)

        upcomingtest = Button(self.window, image=self.upcomingtest, bg="#FFFFFF", activebackground="#DDDDDD",
                              borderwidth=0, height=20, width=170, command=self.setmenu_dashboard)
        upcomingtest.place(x=66, y=172)

        setting_bold = Button(self.window, image=self.setting_bold,
                              bg="#FFFFFF", borderwidth=0, height=20, width=110)
        setting_bold.place(x=73, y=214)

        logout = Button(self.window, image=self.closewin, bg="#FFFFFF", activebackground="#DDDDDD",
                        borderwidth=0, height=20, width=110, command=self.close_windows)
        logout.place(x=68, y=255)


class Dashboard:
    def __init__(self, master, fullname):
        self.fullname = fullname
        self.username = master
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/input_token.png')
        self.upcoming = PhotoImage(file='assets/btn-upcoming-bold.png')
        self.settingmenu = PhotoImage(file='assets/btn-settings.png')
        self.closewin = PhotoImage(file='assets/btn-logout.png')
        self.btntoken = PhotoImage(file='assets/btn-token.png')
        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def setmenu_setting(self):
        self.window.destroy()
        Setting(self.username, self.fullname)

    def close_windows(self):
        self.window.destroy()

    def submit_ujian(self):
        token = self.token.get()
        if token:
            findsoalku =  Findsoal(token).kode()
            if findsoalku['status'] == 200:
                self.window.destroy()
                Ujian(self.username, self.fullname, token) 
            else:
                messagebox.showerror("Invalid", "Kode Token Tidak Ditemukan!")
        else:
            messagebox.showerror("Invalid", "Harap Masukkan Kode Token!")

    def submit_ujian_btn(self, event):
        token = self.token.get()
        if token:
            findsoalku =  Findsoal(token).kode()
            if findsoalku['status'] == 200:
                self.window.destroy()
                Ujian(self.username, self.fullname, token) 
            else:
                messagebox.showerror("Invalid", "Kode Token Tidak Ditemukan!")
        else:
            messagebox.showerror("Invalid", "Harap Masukkan Kode Token!")

    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        self.token = Entry(self.window, font=('Manrope', 14),
                           fg='#000000', width=20, borderwidth=0)  # bg='#969696'
        self.token.place(x=380, y=248)  # 380

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=17)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=28, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=445, y=124)  # 380

        btntoken = Button(self.window, image=self.btntoken, bg="#068EDA", activebackground="#DDDDDD",
                          borderwidth=0, height=38, width=110, command=self.submit_ujian)
        btntoken.place(x=710, y=240)

        self.window.bind('<Return>', self.submit_ujian_btn)

        upcomingtest = Button(self.window, image=self.upcoming, bg="#FFFFFF",
                              activebackground="#DDDDDD", borderwidth=0, height=20, width=170)
        upcomingtest.place(x=66, y=172)

        setting_menu = Button(self.window, image=self.settingmenu, bg="#FFFFFF",
                              borderwidth=0, height=20, width=110, command=self.setmenu_setting)
        setting_menu.place(x=73, y=214)

        logout = Button(self.window, image=self.closewin, bg="#FFFFFF", activebackground="#DDDDDD",
                        borderwidth=0, height=20, width=110, command=self.close_windows)
        logout.place(x=68, y=255)


class Menulogin:
    def __init__(self):
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)

        self.bg = PhotoImage(file='assets/bg/background.png')
        self.startbu = PhotoImage(file='assets/button_login.png')
        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def login(self):
        username = self.username.get()
        password = self.password.get()
        check_log = auth(username, password).acc_login()
        if check_log["status"] == 200:
            self.window.destroy()
            self.fullname = Finduser(username).fullname()
            hakakses = Leveluser(username).fullname()

            if hakakses == "admin":
                AdminTambahSiswa(username, self.fullname)
            else:
                Dashboard(username, self.fullname)
        elif check_log["status"] == 400:
            messagebox.showerror("Invalid", check_log["msg"])
        else:
            messagebox.showerror("Invalid", check_log["msg"])

    def check_empty(self):
        user = self.username.get()
        passw = self.password.get()
        if user == "" or passw == "":
            messagebox.showerror(
                "Invalid", 'Harap masukkan username / password!')
        else:
            self.login()

    def check_empty_enter(self, event):
        user = self.username.get()
        passw = self.password.get()
        if user == "" or passw == "":
            messagebox.showerror(
                "Invalid", 'Harap masukkan username / password!')
        else:
            self.login()

    def _add_username_placeholder(self, tipe):
        if not self.username.get():
            self.username.insert("0", "username")

    def _clear_username_placeholder(self, tipe):
        if self.username.get() == "username":
            self.username.delete("0", "end")

    def _add_password_placeholder(self, tipe):
        if not self.password.get():
            self.password.insert("0", "password")

    def _clear_password_placeholder(self, tipe):
        if self.password.get() == "password":
            self.password.delete("0", "end")

    def main(self):
        connect = connection().check_database()
        if connect == True:
            self.bgg = Label(self.window, image=self.bg, borderwidth=0)
            self.bgg.place(x=0, y=0)
            self.username = Entry(self.window, font=(
                'Manrope', 17), fg='#000000', width=28, borderwidth=0)
            self.username.insert("0", "username")
            self.username.bind("<FocusIn>", self._clear_username_placeholder)
            self.username.bind("<FocusOut>", self._add_username_placeholder)
            self.username.place(x=715, y=305)

            self.password = Entry(self.window, font=(
                'Manrope', 17), fg='#000000', show="*", width=28, borderwidth=0)  # bg='#969696'
            self.password.insert("0", "password")
            self.password.bind("<FocusIn>", self._clear_password_placeholder)
            self.password.bind("<FocusOut>", self._add_password_placeholder)
            self.password.place(x=715, y=385)  # 380
            self.window.bind('<Return>', self.check_empty_enter)
            start = Button(self.window, image=self.startbu, borderwidth=0, height=55,
                           width=180, activebackground="#E4F5FF", command=self.check_empty)
            start.place(x=810, y=450)

        else:
            messagebox.showerror(
                "Error", 'Harap aktifkan internet anda. Koneksi database error!')


class AdminTambahSiswa:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file = 'assets/bg/bg_admin_tambahsiswa.png')
        self.tambahsiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsiswa-bold.png') 
        self.hapussiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussiswa.png') 
        self.tambahsoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsoal.png') 
        self.hapussoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussoal.png') 
        self.logoutimg = PhotoImage(file = 'assets/btn-menuadmin/btn-logout.png') 
        self.tambahklikimg = PhotoImage(file = 'assets/btn_tambahsiswa.png')



        w = 1280
        h = 720
        

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def close_windows(self):
        self.window.destroy()

    def tambah_soal(self):
        self.window.destroy()
        AdminTambahSoal(self.username, self.fullname)
    
    def hapus_soal(self):
        self.window.destroy()
        AdminHapusSoal(self.username, self.fullname)

    def tambah_siswa(self):
        self.window.destroy()
        AdminTambahSiswa(self.username, self.fullname)

    def hapus_siswa(self):
        self.window.destroy()
        AdminHapusSiswa(self.username, self.fullname)

    def btn_verify(self):
        if self.username_verify.get() == "" and self.password_verify.get() == "" and self.fullname_verify.get() == "":
            messagebox.showwarning("PERINGATAN","Data Tidak Boleh Kosong")
        else:
            if self.username_verify.get() == "":
                messagebox.showwarning("PERINGATAN","Masukkan Username")
            else:
                if self.password_verify.get() == "":
                    messagebox.showwarning("PERINGATAN","Masukan password")
                else:
                    if self.fullname_verify.get() == "":
                        messagebox.showwarning("PERINGATAN","Masukan Fullname")
                    else:
                        checkuser = Finduser(self.username_verify.get()).fullname()
                        if checkuser == False:
                            responseadd = Adduser(self.username_verify.get(), self.password_verify.get(), self.fullname_verify.get(), self.cb1.get()).add()
                            if responseadd:
                                messagebox.showinfo("SUKSES","Sukses menambahkan user ke dalam Database!")
                            else:
                                messagebox.showwarning("PERINGATAN","Tidak dapat menambahkan users!")
                        else:
                            messagebox.showwarning("PERINGATAN","Tidak dapat menambahkan user, karena Username sudah ada di dalam Database!")
        
    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        font = Font(file="assets/font/Manrope-SemiBold.ttf", family="Manrope SemiBold", size=19)
        font1 = Font(file="assets/font/Manrope-Regular.ttf", family="Manrope Regular", size=12)
        font2 = Font(file="assets/font/Manrope-Medium.ttf", family="Manrope Regular", size=17)


        '''self.txtusername = Label(self.window, text = "Username", font=font, fg='#068EDA', bg = "#E4F5FF", width=9,borderwidth=0, anchor="w") #bg='#969696'
        self.txtpassword = Label(self.window, text = "Password", font=font, fg='#068EDA', bg = "#E4F5FF", width=9,borderwidth=0, anchor="w") #bg='#969696'
        self.txtfullname = Label(self.window, text = "Fullname", font=font, fg='#068EDA', bg = "#E4F5FF", width=9,borderwidth=0, anchor="w") #bg='#969696'
        self.txthakakses = Label(self.window, text = "Hak Akses", font=font, fg='#068EDA', bg = "#E4F5FF", width=9,borderwidth=0, anchor="w") #bg='#969696'''

        pilihan=['siswa','admin']
        self.cb1 = ttk.Combobox(self.window, values=pilihan,width=20,font=font2) # Combobox
        self.cb1.grid(row=1,column=1,padx=476,pady=383) # adding to grid
        self.cb1.set('siswa') # default selected option

        self.user = Label(self.window, text = self.fullname, font=font,fg='#068EDA', bg = "#E4F5FF", width=20,borderwidth=0, anchor="w") #bg='#969696'
        self.user.place(x=520, y=122) #380

        self.password_verify = Entry(self.window,font=font1, fg='#000000', show="*", width=23,borderwidth=0) #bg='#969696'
        self.password_verify.place(x=490, y=285)

        self.username_verify = Entry(self.window,font=font1, fg='#000000',width=23,borderwidth=0) #bg='#969696'
        self.username_verify.place(x=490, y=232)
        
        self.fullname_verify = Entry(self.window,font=font1, fg='#000000',width=23,borderwidth=0) #bg='#969696'
        self.fullname_verify.place(x=490, y=337)
        
        #self.hakakses_verify = Entry(self.window,font=font1, fg='#000000',width=23,borderwidth=0) #bg='#969696'
        #self.hakakses_verify.place(x=490, y=388)

        self.tambah= Button(self.window, image=self.tambahklikimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.btn_verify)
        self.tambah.place(x=544,y=440)

        # Menu Samping
        
        self.tambahsiswa= Button(self.window, image=self.tambahsiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        self.tambahsiswa.place(x=70,y=190)

        self.hapussiswa= Button(self.window, image=self.hapussiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_siswa)
        self.hapussiswa.place(x=65,y=230)

        self.tambahsoal = Button(self.window, image=self.tambahsoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_soal)
        self.tambahsoal.place(x=65,y=270)

        self.hapussoal = Button(self.window, image=self.hapussoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_soal)
        self.hapussoal.place(x=60,y=310)

        self.logout= Button(self.window, image=self.logoutimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command=self.close_windows)
        self.logout.place(x=45,y=350)

        # End Menu Samping


class AdminTambahSoal:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/bg_admin_tambahsoal.png')
        self.imggenerate = PhotoImage(file='assets/btn_generate.png')
        self.imgimport = PhotoImage(file='assets/btn_import.png')
        self.imgtambah = PhotoImage(file='assets/btn_tambahsoal.png')
        self.tambahsiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsiswa.png') 
        self.hapussiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussiswa.png') 
        self.tambahsoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsoal-bold.png') 
        self.hapussoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussoal.png') 
        self.logoutimg = PhotoImage(file = 'assets/btn-menuadmin/btn-logout.png')
        self.randomint = 5
        self.json_str = []

        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def close_windows(self):
        self.window.destroy()

    def tambah_siswa(self):
        self.window.destroy()
        AdminTambahSiswa(self.username, self.fullname)
    
    def hapus_soal(self):
        self.window.destroy()
        AdminHapusSoal(self.username, self.fullname)

    def hapus_siswa(self):
        self.window.destroy()
        AdminHapusSiswa(self.username, self.fullname)

    def random_char(self):
       self.randomint =  ''.join(random.choice(string.ascii_letters) for x in range(5))

    def generate_kode(self):
        self.kodesoal.delete(0, 'end')
        self.random_char()
        self.kodesoal.insert(0, self.randomint)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        excel_data_df = pandas.read_excel(filepath)
        self.json_str = excel_data_df.to_dict(orient='records')
        self.soal.config(state= "normal")
        self.soal.delete("0", "end")
        self.soal.insert("0", filepath)
        self.soal.config(state= "disabled")

    def submit_verify(self):
        if self.kodesoal.get() == "":
            messagebox.showwarning("PERINGATAN","Kode Soal Tidak boleh kosong!")
        else:
            if self.matkul.get() == "":
                messagebox.showwarning("PERINGATAN","Matkul Tidak boleh kosong!")
            else:
                if self.durasi.get() == "":
                    messagebox.showwarning("PERINGATAN","Durasi Tidak boleh kosong!")
                else:
                    if self.json_str == []:
                        messagebox.showwarning("PERINGATAN","Silahkan pilih soal!")
                    else:
                        findsoalku =  Findsoal(self.kodesoal.get()).kode()
                        if findsoalku['status'] == 200:
                            messagebox.showwarning("PERINGATAN","Kode soal sudah ada di dalam database, silahkan inputkan kode lain!")
                        else:
                            Addsoal(self.kodesoal.get(), self.matkul.get(), self.durasi.get(), self.json_str).add()
                            messagebox.showinfo("SUKSES","Sukses menambah soal ke dalam database!")

    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=17)
        font1 = Font(file="assets/font/Manrope-Regular.ttf",
                     family="Manrope Regular", size=12)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=28, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=520, y=124)  # 380

        self.kodesoal = Entry(self.window, font=font1,
                              fg='#000000', width=25, borderwidth=0)
        self.kodesoal.place(x=483, y=232)

        self.matkul = Entry(self.window, font=font1,
                            fg='#000000', width=25, borderwidth=0)
        self.matkul.place(x=483, y=293)

        self.durasi = Entry(self.window, font=font1,
                            fg='#000000', width=25, borderwidth=0)
        self.durasi.place(x=483, y=358)

        self.soal = Entry(self.window, font=font1,
                          fg='#000000', width=25, borderwidth=0)
        self.soal.config(state= "disabled")
        self.soal.place(x=483, y=420)

        self.generate = Button(self.window, image=self.imggenerate, borderwidth=0,
                               height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command = self.generate_kode)
        self.generate.place(x=780, y=222)

        self.importt = Button(self.window, image=self.imgimport, borderwidth=0,
                              height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command = self.open_file)
        self.importt.place(x=780, y=414)

        self.tambah = Button(self.window, image=self.imgtambah, borderwidth=0,
                             height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command=self.submit_verify)
        self.tambah.place(x=540, y=480)

        # Menu Samping
        
        self.tambahsiswa= Button(self.window, image=self.tambahsiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_siswa)
        self.tambahsiswa.place(x=70,y=190)

        self.hapussiswa= Button(self.window, image=self.hapussiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_siswa)
        self.hapussiswa.place(x=65,y=230)

        self.tambahsoal = Button(self.window, image=self.tambahsoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        self.tambahsoal.place(x=65,y=270)

        self.hapussoal = Button(self.window, image=self.hapussoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_soal)
        self.hapussoal.place(x=60,y=310)

        self.logout= Button(self.window, image=self.logoutimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command=self.close_windows)
        self.logout.place(x=45,y=350)

        # End Menu Samping
        

class AdminHapusSoal:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/bg_admin_hapussoal.png')
        self.imghapus = PhotoImage(file='assets/btn_admin_hapus.png')
        self.tambahsiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsiswa.png') 
        self.hapussiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussiswa.png') 
        self.tambahsoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsoal.png') 
        self.hapussoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussoal-bold.png') 
        self.logoutimg = PhotoImage(file = 'assets/btn-menuadmin/btn-logout.png')
        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def close_windows(self):
        self.window.destroy()

    def tambah_siswa(self):
        self.window.destroy()
        AdminTambahSiswa(self.username, self.fullname)

    def tambah_soal(self):
        self.window.destroy()
        AdminTambahSoal(self.username, self.fullname)

    def hapus_siswa(self):
        self.window.destroy()
        AdminHapusSiswa(self.username, self.fullname)

    def submit_verify(self):
        if self.kodesoal.get() == "":
            messagebox.showwarning("PERINGATAN","Kode Soal Tidak boleh kosong!")
        else:
            findsoalku =  Findsoal(self.kodesoal.get()).kode()
            if findsoalku['status'] == 404:
                messagebox.showwarning("PERINGATAN","Kode soal tidak ditemukan!")
            else:
                Delsoal(self.kodesoal.get()).delete()
                messagebox.showinfo("SUKSES","Soal sukses dihapus!")

    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=17)
        font1 = Font(file="assets/font/Manrope-Regular.ttf",
                     family="Manrope Regular", size=12)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=28, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=520, y=124)  # 380

        self.kodesoal = Entry(self.window, font=font1,
                              fg='#000000', width=25, borderwidth=0)
        self.kodesoal.place(x=483, y=232)

        self.tambah = Button(self.window, image=self.imghapus, borderwidth=0,
                             height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command = self.submit_verify)
        self.tambah.place(x=780, y=222)

        # Menu Samping
        
        self.tambahsiswa= Button(self.window, image=self.tambahsiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_siswa)
        self.tambahsiswa.place(x=70,y=190)

        self.hapussiswa= Button(self.window, image=self.hapussiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_siswa)
        self.hapussiswa.place(x=65,y=230)

        self.tambahsoal = Button(self.window, image=self.tambahsoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_soal)
        self.tambahsoal.place(x=65,y=270)

        self.hapussoal = Button(self.window, image=self.hapussoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        self.hapussoal.place(x=60,y=310)

        self.logout= Button(self.window, image=self.logoutimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command=self.close_windows)
        self.logout.place(x=45,y=350)

        # End Menu Samping


class AdminHapusSiswa:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.window = Tk()
        self.window.title("Aplikasi Ujian Berbasis Desktop")
        self.window.resizable(False, False)
        self.window.maxsize(1280, 720)
        self.window.minsize(1280, 720)
        self.bg = PhotoImage(file='assets/bg/bg_admin_hapussiswa.png')
        self.imghapus = PhotoImage(file='assets/btn_admin_hapus.png')
        self.tambahsiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsiswa.png') 
        self.hapussiswaimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussiswa-bold.png') 
        self.tambahsoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-tambahsoal.png') 
        self.hapussoalimg = PhotoImage(file = 'assets/btn-menuadmin/btn-hapussoal.png') 
        self.logoutimg = PhotoImage(file = 'assets/btn-menuadmin/btn-logout.png')
        w = 1280
        h = 720

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)

        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.main()
        self.window.mainloop()

    def close_windows(self):
        self.window.destroy()

    def tambah_siswa(self):
        self.window.destroy()
        AdminTambahSiswa(self.username, self.fullname)
    
    def hapus_soal(self):
        self.window.destroy()
        AdminHapusSoal(self.username, self.fullname)

    def tambah_soal(self):
        self.window.destroy()
        AdminTambahSoal(self.username, self.fullname)

    def verify_btn(self):
        if self.delusername.get() == "":
            messagebox.showwarning("PERINGATAN","Username Tidak boleh kosong!")
        else:
            checkuser = Finduser(self.delusername.get()).fullname()
            if checkuser == False:
                messagebox.showwarning("PERINGATAN","Tidak dapat menghapus user, karena tidak ada Username di dalam Database!")
            else:
                responsedel = Deluser(self.delusername.get()).delete()
                if responsedel:
                    messagebox.showinfo("SUKSES","Sukses menghapus user!")
                else:
                    messagebox.showwarning("PERINGATAN","Tidak dapat menambahkan users!")
            

    def main(self):
        self.bgg = Label(self.window, image=self.bg, borderwidth=0)
        self.bgg.place(x=0, y=0)

        font = Font(file="assets/font/Manrope-SemiBold.ttf",
                    family="Manrope SemiBold", size=17)
        font1 = Font(file="assets/font/Manrope-Regular.ttf",
                     family="Manrope Regular", size=12)

        self.txtuser = Label(self.window, text=self.fullname, font=font, fg='#068EDA',
                             bg="#E4F5FF", width=28, borderwidth=0, anchor="w")  # bg='#969696'
        self.txtuser.place(x=520, y=124)  # 380

        self.delusername = Entry(self.window, font=font1,
                              fg='#000000', width=25, borderwidth=0)
        self.delusername.place(x=483, y=232)

        self.tambah = Button(self.window, image=self.imghapus, borderwidth=0,
                             height=40, width=170, bg="#FFFFFF", activebackground="#E4F5FF", command = self.verify_btn)
        self.tambah.place(x=780, y=222)

        # Menu Samping
        
        self.tambahsiswa= Button(self.window, image=self.tambahsiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_siswa)
        self.tambahsiswa.place(x=70,y=190)

        self.hapussiswa= Button(self.window, image=self.hapussiswaimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF")
        self.hapussiswa.place(x=65,y=230)

        self.tambahsoal = Button(self.window, image=self.tambahsoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.tambah_soal)
        self.tambahsoal.place(x=65,y=270)

        self.hapussoal = Button(self.window, image=self.hapussoalimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command = self.hapus_soal)
        self.hapussoal.place(x=60,y=310)

        self.logout= Button(self.window, image=self.logoutimg, borderwidth=0, height=39, width=170, bg = "#FFFFFF", activebackground="#E4F5FF", command=self.close_windows)
        self.logout.place(x=45,y=350)

        # End Menu Samping


def start():
    Menulogin()

if __name__ == "__main__":
    start()