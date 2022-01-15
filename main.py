from tkinter import*  #Tkinter is Python's default GUI module                                =>>pratik
import qrcode
from PIL import Image,ImageTk # pillow library used to deal with jpj or png imageimport resizeimage
from resizeimage import resizeimage  # (pip install python-resize-image)  python-resize-image library used for resizing the image
class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        # 900=width,500=height,space from left side=200,space from top=50
        self.root.title(" QR code Generator| Developed by p4")
        # title
        self.root.resizable(False, False)
        # to avoid to adjust size of tk window(optional)

        title = Label(self.root, text="   QR Code Generator", font=(
            "times new roman", 40), bg='brown', fg='white', anchor='w').place(x=0,y=0,relwidth='1')#place is to show that title
        
        # ***********  Student Details Window *********                                       =>yogesh
        # ********** variables *****
        self.var_name_code = StringVar()
        self.var_email_code = StringVar()
        self.var_phone_number_code = StringVar()

        # bd=border;relief=border style
        std_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')#.place(x=20, y=80, width=500, height=380)

        std_Frame.place(x=20, y=80, width=500, height=380)

        std_title = Label(std_Frame, text="Students Details", font=(
            "times new roman", 30), bg='purple', fg='white').place(x=0, y=0, relwidth=1)

        lbl_name_code = Label(std_Frame, text="Student's Name", font=(
            "times new roman", 15, 'bold'), bg='white', anchor='w').place(x=20, y=90)
        lbl_email_code = Label(std_Frame, text="Email Id", font=(
            "times new roman", 15, 'bold'), bg='white', anchor='w').place(x=20, y=130)
        lbl_phone_number_code = Label(std_Frame, text="Phone Number", font=(
            "times new roman", 15, 'bold'), bg='white', anchor='w').place(x=20, y=170)

# ******  the Label is given by the progrmmer but the Entry is taken from user  ********
#     Label and Entry , Button are  just classes ...

        txt_name_code = Entry(std_Frame, font=("times new roman", 15),
                              textvariable=self.var_name_code, bg='lightyellow').place(x=180, y=90)
        txt_email_code = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_email_code, bg='lightyellow').place(x=180, y=130)
        txt_phone_number_code = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_phone_number_code, bg='lightyellow').place(x=180, y=170)

        # to call generate function                                                      #=>> kaustubh
        btn_generator = Button(std_Frame, text="Generate QR Code", command=self.generate, font=(
            "times new roman", 17, 'bold'), bg='skyblue').place(x=30, y=250, width=210, height=50)
        btn_generator = Button(std_Frame, text="Clear", font=(
            "times new roman", 17, 'bold'),command=self.clear, bg='grey').place(x=280, y=250, width=100, height=50)

        self.msg = ''
        self.lbl_msg = Label(std_Frame, text=self.msg, font=("times new roman", 18, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=320, relwidth=1)  # relwidth for allingning text at centre
         #to make 'self' as object of whole class we defined it two times(in two different lines)    

# ***********  Student QR Code Window *********                                      =>>jay
        # bd=border;relief=border style
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=570, y=80, width=290, height=380)

        qr_title = Label(qr_Frame, text="Students QR Code ", font=(
            "times new roman", 25), bg='purple', fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text="No QR available", font=(
            "times new roman", 20), bg='black', fg='white')
        self.qr_code.place(x=45, y=100, width=200, height=180)

    def clear(self):                                              # => prasad
        self.var_name_code.set('')
        self.var_email_code.set('')
        self.var_phone_number_code.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):                                          #=> omkar
         if self.var_name_code.get() == '' or self.var_phone_number_code.get() == '' or self.var_email_code.get() == '':
                
             self.msg='All fields are Required!!!'
             self.lbl_msg.config(text=self.msg,fg='red')   
         else:
             qr_data=(f"student name :{self.var_name_code.get()}\nStudent email :{self.var_email_code.get()}\nStudent Phone no. :{self.var_phone_number_code.get()}")
             qr_code=qrcode.make(qr_data)
             #******to resize the image of qr code image**********
             qr_code=resizeimage.resize_cover(qr_code,[180,180])
             qr_code.save("Student_QR/Std_"+str(self.var_name_code.get())+'.png')
             #**********qr code image update********/**
             self.im=ImageTk.PhotoImage(file="Student_QR/Std_"+str(self.var_name_code.get())+'.png')
             self.qr_code.config(image=self.im)
             #************* updating notification ***********

             self.msg='QR Code Generated Successfully!!!!'
             self.lbl_msg.config(text=self.msg,fg='green')

#   =>>>  yogesh
# object(root) for Tk (used to bind certain default behaviors to widgets, and is executed once at the point where the Python tkinter package is imported.)
root = Tk()
obj = Qr_Generator(root)  # object(obj) for class
root.mainloop()
#when we want to run our application ,this method will loop forever ,waiting for events from user ,until the user exits the program