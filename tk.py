from pytube import YouTube
from tkinter import*
from tkinter.filedialog import *
from threading import*
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk
filesize=0
def completedownload(stream=None,filepath=None):
    print("Download completed")
    showinfo("Message","File has been downloaded..")
    dwnbtn['text']='Download Video'
    dwnbtn['state']='active'
    urlField.delete(0,END)
def progressdownload(stream=None,chunk=None,bytesremaining=None):
    percent = (100 * ((filesize - bytesremaining) / filesize))
    dwnbtn['text'] = "{:00.0f}% downloaded ".format(percent)
    
def startdownload(url):
    global file_size
    pathtosave=askdirectory()
    if pathtosave is None:
        return
    try:
        yt=YouTube(url)
        #for i in yt.streams:    
        #st=yt.streams.first()
        #yt.register_on_complete_callback(completedownload)
        #yt.register_on_progress_callback(progressdownload)
        #filesize=st.filesize
        #st.download(output_path=pathtosave)
    except Exception as e:
        print(e)

def btnclicked():
    dwnbtn['text']='Please wait...'
    dwnbtn['state']='disabled'
    url=urlField.get()
    if url=='':
        return
    yt=YouTube(url)
    yt=yt.streams
    #print(yt)
    res144=[]
    res240=[]
    res360=[]
    res480=[]
    res720=[]
    res1080=[]
    for i in range(len(yt)):
        if yt[i].resolution == "144p":
            res144.append(yt[i])
        elif yt[i].resolution=="240p":
            res240.append(yt[i])
        elif yt[i].resolution=="360p":
            res360.append(yt[i])
        elif yt[i].resolution=="480p":
            res480.append(yt[i])
        elif yt[i].resolution=="720p":
            res720.append(yt[i])
        elif yt[i].resolution=="1080p":
            res1080.append(yt[i])
    res=list([res144[-1],res240[-1],res360[-1],res480[-1],res720[-1],res1080[-1]])
    print(res)
    def monthchanged(event):
        global msg
        msg=month.get()
        print(msg)
        showinfo(title='result',message=msg)
    
    #root=tk.Tk()
    #root.geometry('300x200')
    #root.resizable(0,0)
    pixels=('144','240','360','480','720','1020')
    select=StringVar()
    month=ttk.Combobox(root,textvariable=select)
    month['values']=pixels
    month['state']='readonly'
    month.place(x=700,y=300,width=40)
    month.bind("<<ComboboxSelected>>",monthchanged)
    
    #thread=Thread(target=startdownload,args=(url,))
    #thread.start()
global root
root=Tk()
root.config(bg="black")
root.resizable(width=True, height=True)
w = str(root.winfo_screenwidth())
h = str(root.winfo_screenheight())
res=w+"x"+h
root.title("YOUTUBE-RIPPER")
root.geometry(res)
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
image=Image.open(r'C:\Users\saraswathi\Downloads\yyt.png')
image=image.resize((350,150))
file=ImageTk.PhotoImage(image)#=r"C:\Users\saraswathi\Downloads\yt.gif")
headingIcon=Label(root,image=file).place(x=600,y=20)
#headingIcon.grid(row=1,column=1,sticky="NSEW")
l1=Label(root,text="Enter Video URL").place(x=600,y=200)
#l1.grid(row=600,column=200,sticky="NSEW")

urlField = Entry(root, width=40, justify=CENTER)
urlField.place(x=700,y=200)
urlField.focus()
while True:
    dwnbtn=Button(root,text="Download Video",relief='ridge',command=btnclicked)
    dwnbtn.place(x=1000,y=200)
    root.mainloop()
