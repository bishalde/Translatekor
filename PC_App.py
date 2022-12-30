from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator , LANGUAGES


class Translator(Tk):

    def __init__(self):
        def move_app(e):
            self.geometry(f'+{e.x_root}+{e.y_root}')
        def on_enter(e):
            self.exitbtn.config(background='OrangeRed3')
        def on_leave(e):
            self.exitbtn.config(background='navy')

        super().__init__()
        self.geometry('500x700+800+100')
        #self.attributes('-toolwindow', True)
        #self.attributes('-alpha',0.5)
        self.overrideredirect(True)
        self.attributes('-topmost', 1)
        self.iconbitmap('')
        self["bg"]="bisque"

        title_bar=Frame(self,bg='navy',relief='raised',bd=0,height=45,width=500)
        title_bar.place(relx=0,rely=0)
        title_bar.bind("<B1-Motion>",move_app)

        self.exit_image = PhotoImage(file='Resources/exit1.png')
        self.exitbtn=Button(self, text=">>>", bd=0,command=exit,cursor="hand2",bg='navy',fg='bisque',font=("Cascadia Code",14,"bold"))
        self.exitbtn.place(relx=.888,rely=0)
        self.exitbtn.bind('<Enter>',on_enter)
        self.exitbtn.bind('<Leave>',on_leave)

        self.title=Label(self,text="Translator",font=("Centaur",20,"bold"),fg='Yellow',bg='navy')
        self.title.place(relx=.01,rely=0.005)




        self.from_heading=Label(self, text = "From", font = ("Microsoft YaHei", 20,'bold' ), bg='bisque',fg='blue')
        self.from_heading.place(relx=.02,rely=0.1)

        ##################
        language = list(LANGUAGES.values())

        self.src_lang = ttk.Combobox(self, values= language,font = ("OCR A Extended", 15,'bold' ), width =20)
        self.src_lang.place(relx=.02,rely=0.16)
        self.src_lang.set('Language..')

        self.from_Input_text = Text(self,font = ('Cascadia Code',15,'bold'), height = 7, wrap = WORD, padx=5, pady=5, width = 39,bd=2,relief='groove',)
        self.from_Input_text.place(relx=.02,rely=.22)
        self.from_Input_text.focus_set()
        


        self.to_heading=Label(self, text = "To", font = ("Microsoft YaHei", 20,'bold' ), bg='bisque',fg='blue')
        self.to_heading.place(relx=.02,rely=0.51)

        self.dest_lang = ttk.Combobox(self, values= language,font = ("OCR A Extended", 15,'bold' ), width =20)
        self.dest_lang.place(relx=0.02,rely=0.57)
        self.dest_lang.set('Language..')

        self.to_Input_text = Text(self,font = ('Cascadia Code',15,'bold'), height = 7, wrap = WORD, padx=5, pady=5, width = 39,bd=2,relief='groove',)
        self.to_Input_text.place(relx=.02,rely=.63)

        #rest btn----------------
        self.reset=Button(self,cursor="hand2",bg="red4",fg="ivory",text="Reset",font=("Bahnschrift SemiBold",15,"bold"),height=1,width=10,command=exit,bd=0)
        self.reset.place(relx=0.27, rely=0.935)

        #proceed btn----------------
        self.proceed=Button(self,cursor="hand2",bg="green4",fg="ivory",text="Transalate",font=("Bahnschrift SemiBold",15,"bold"),height=1,width=10,bd=0)
        self.proceed.place(relx=0.55, rely=0.935)



if __name__=='__main__':
    root=Translator()
    root.mainloop()