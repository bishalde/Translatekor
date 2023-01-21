from flask import Flask,render_template,request,redirect
from googletrans import Translator , LANGUAGES

language = list(LANGUAGES.values())
app=Flask(__name__)
def transalate(lang_from,lang_text,lang_to):
    translator = Translator()
    if(lang_from=='Detecting Language..'):
        translated=translator.translate(text= lang_text,dest = lang_to)
        return translated
    else:
        translated=translator.translate(text= lang_text, src =lang_from ,dest = lang_to)
        return translated


@app.route('/homepage',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        src=request.form.get('from_language')
        src_txt=request.form.get('from_textarea')
        dest=request.form.get('to_language')
        try:
            dest_txt=transalate(src,src_txt,dest).text
            pronun=transalate(src,src_txt,dest).pronunciation
            data=[src,src_txt,dest,dest_txt,pronun]
            return render_template('index.html',language=language,data=data)
        except :
            return redirect("/")
    else:
        data=["Detecting Language..","","hindi","",""]
        return render_template('index.html',language=language,data=data)

app.run(debug=True,host='0.0.0.0')