from gtts import gTTS
import os

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator , LANGUAGES

from playsound import playsound  

class Translatorr(Tk):

    def __reset(self):
        self.from_Input_text.delete(1.0, END)
        self.to_Input_text.delete(1.0, END)
        self.pronunciation_Input_text.delete(1.0, END)
        self.dest_lang.set('Language..')
        self.src_lang.set('Detecting Language..')

    def __speech(self):
        text=self.pronunciation_Input_text.get(1.0, END)
        t1 = gTTS(text,lang=lang_to)
        t1.save("Resources/audio.mp3") 
        playsound("Resources/audio.mp3")

    def __translate(self):
        global lang_to
        lang_text=self.from_Input_text.get(1.0, END)
        lang_from=self.src_lang.get()
        lang_to=self.dest_lang.get()
        if(lang_to=="Language.."):
            messagebox.showinfo("No Language Selected","Select Destination Language")
        
        else:
            self.translator = Translator()
            try:
                if(lang_from=='Detecting Language..'):
                    self.translated=self.translator.translate(text= lang_text,dest = lang_to)
                else:
                    self.translated=self.translator.translate(text= lang_text, src =lang_from ,dest = lang_to)

                self.to_Input_text.delete(1.0, END)
                self.to_Input_text.insert(END, self.translated.text)
                self.pronunciation_Input_text.delete(1.0, END)
                if(self.translated.pronunciation==None):
                    self.pronunciation_Input_text.insert(END,"")
                else:
                    self.pronunciation_Input_text.insert(END, self.translated.pronunciation)
                lang_to=self.translated.dest
            except:
                messagebox.showerror("No Internet","Could not Connect to the server")


    def __init__(self):
        def move_app(e):
            self.geometry(f'+{e.x_root}+{e.y_root}')
        def on_enter(e):
            self.exitbtn.config(background='OrangeRed3')
        def on_leave(e):
            self.exitbtn.config(background='navy')

        super().__init__()
        self.geometry('500x800+800+50')
        #self.attributes('-toolwindow', True)
        #self.attributes('-alpha',0.5)
        self.overrideredirect(True)
        self.attributes('-topmost', 1)
        self.iconbitmap('')
        self["bg"]="bisque"

        title_bar=Frame(self,bg='navy',relief='raised',bd=0,height=45,width=500)
        title_bar.place(relx=0,rely=0)
        title_bar.bind("<B1-Motion>",move_app)

        
        self.exitbtn=Button(self, text=">>>", bd=0,command=exit,cursor="hand2",bg='navy',fg='bisque',font=("Cascadia Code",14,"bold"))
        self.exitbtn.place(relx=.888,rely=0)
        self.exitbtn.bind('<Enter>',on_enter)
        self.exitbtn.bind('<Leave>',on_leave)

        self.title=Label(self,text="Translator",font=("Centaur",20,"bold"),fg='Yellow',bg='navy')
        self.title.place(relx=.01,rely=0.005)


        self.from_heading=Label(self, text = "From", font = ("Microsoft YaHei", 20,'bold' ), bg='bisque',fg='blue')
        self.from_heading.place(relx=.02,rely=0.06)

        ##################
        language = list(LANGUAGES.values())

        self.src_lang = ttk.Combobox(self, values= language,font = ("OCR A Extended", 15,'bold' ), width =20)
        self.src_lang.place(relx=.022,rely=0.11)
        self.src_lang.set('Detecting Language..')
        # self.src_lang.set('English')

        self.from_Input_text = Text(self,font = ('Cascadia Code',15,'bold'), height = 7, wrap = WORD, padx=5, pady=5, width = 39,bd=2,relief='groove',)
        self.from_Input_text.place(relx=.022,rely=.155)
        self.from_Input_text.focus_set()
        


        self.to_heading=Label(self, text = "To", font = ("Microsoft YaHei", 20,'bold' ), bg='bisque',fg='blue')
        self.to_heading.place(relx=.022,rely=0.42)

        self.dest_lang = ttk.Combobox(self, values= language,font = ("OCR A Extended", 15,'bold' ), width =20)
        self.dest_lang.place(relx=0.022,rely=0.47)
        self.dest_lang.set('Language..')
        #self.dest_lang.set('Hindi')

        self.to_Input_text = Text(self,font = ('Cascadia Code',15,'bold'), height = 7, wrap = WORD, padx=5, pady=5, width = 39,bd=2,relief='groove',)
        self.to_Input_text.place(relx=.022,rely=.515)

        self.pronounciation_heading=Label(self, text = "Pronunciation : ", font = ("Microsoft YaHei", 15,'bold' ), bg='bisque',fg='blue')
        self.pronounciation_heading.place(relx=.022,rely=0.77)

        self.audio_image = PhotoImage(file='Resources/audio.png')
        self.audio_btn=Button(self,cursor="hand2",image=self.audio_image,bd=0,command=self.__speech)
        self.audio_btn.place(relx=.35,rely=0.77)

        self.pronunciation_Input_text = Text(self,font = ('Cascadia Code',15,'bold'), height = 3, wrap = WORD, padx=5, pady=5, width = 39,bd=2,relief='groove',)
        self.pronunciation_Input_text.place(relx=.022,rely=.81)

        #rest btn----------------
        self.reset=Button(self,cursor="hand2",bg="red4",fg="ivory",text="Reset",font=("Bahnschrift SemiBold",15,"bold"),height=1,width=10,command=self.__reset,bd=0)
        self.reset.place(relx=0.27, rely=0.935)

        #proceed btn----------------
        self.proceed=Button(self,cursor="hand2",bg="green4",fg="ivory",text="Translate",font=("Bahnschrift SemiBold",15,"bold"),height=1,width=10,bd=0,command=self.__translate)
        self.proceed.place(relx=0.55, rely=0.935)



if __name__=='__main__':
    root=Translatorr()
    root.mainloop()