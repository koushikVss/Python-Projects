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
    percent = (100 *((filesize - bytesremaining) / filesize))
    dwnbtn['text'] = "{:00.0f}% downloaded ".format(percent)
    
'''def startdownload(url):
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
        print(e)'''
#strating download thread
def start():
    global file_size
    pathtosave=askdirectory()
    if pathtosave is None:
        return
    #gt.register_on_complete_callback(completedownload)
    #gt.register_on_progress_callback(progressdownload)
    #filesize=res[choice].filesize
    res[choice].download(output_path=pathtosave)
    
    
def btnclicked():
    dwnbtn['text']='Please wait...'
    dwnbtn['state']='disabled'
    url=urlField.get()
    if url=='':
        return
    try:
        dwnbtn['text']='search'
        dwnbtn['state']='enabled'
        global gt
        gt=YouTube(url)
        yt=gt.streams
    except Exception as e:
        error=Label(root,text="Error, Invalid link or its a live streams",fg="white",bg="black").place(x=50,y=210)
        print(e)
    gt=YouTube(url)
    yt=gt.streams
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
    global res
    res=list([res144[-1],res240[-1],res360[-1],res480[-1],res720[-1],res1080[-1]])
    chek=[]
    for i in res:
        if i.resolution=="144p":
            chek.append("144")
        elif i.resolution=="240p":
            chek.append("240")
        elif i.resolution=="360p":
            chek.append("360")
        elif i.resolution=="480p":
            chek.append("480")
        elif i.resolution=="720p":
            chek.append("720")
        elif i.resolution=="1080p":
            chek.append("1080")
    click=StringVar()
    drop=ttk.Combobox(root)
    vidchoose=Label(root,text="Video resolution",fg="white",bg="black").place(x=65,y=210)
    drop['values']=chek
    drop.current(0)
    drop.place(x=110,y=210)
    global choice
    choice=chek.index(drop.get())
    if len(chek)!=0:
        downbut=Button(root,text="download",command=start).place(x=180,y=270)
    else:
        return
    
    
'''    try:
        #for i in yt.streams:    
        #st=yt.streams.first()
        #yt.register_on_complete_callback(completedownload)
        #yt.register_on_progress_callback(progressdownload)
        #filesize=st.filesize
        #st.download(output_path=pathtosave)
    except Exception as e:
        print(e)
    def monthchanged(event):
        global msg
        msg=month.get()
        print(msg)
        showinfo(title='result',message=msg)'''
    #root=tk.Tk()
    #root.geometry('300x200')
    #root.resizable(0,0)
'''pixels=('144','240','360','480','720','1080')
    select=StringVar()
    month=ttk.Combobox(root,textvariable=select)
    month['values']=pixels
    month['state']='readonly'
    month.place(x=700,y=300,width=40)
    month.bind("<<ComboboxSelected>>",monthchanged)'''
    #thread=Thread(target=startdownload,args=(url,))
    #thread.start()

global root
root=Tk()
root.config(bg="black")
root.resizable(width=False, height=False)
#w = str(root.winfo_screenwidth())
#h = str(root.winfo_screenheight())
#res=w+"x"+h
root.title("YOUTUBE-RIPPER")
#root.geometry(res)
root.geometry("350x550")
#Grid.rowconfigure(root,0,weight=1)
# Grid.columnconfigure(root,0,weight=1)
#Grid.rowconfigure(root,1,weight=1)
image=Image.open(r'C:\Users\saraswathi\Downloads\yyt.png')
image=image.resize((250,100))
file=ImageTk.PhotoImage(image)
headingIcon=Label(root,image=file).place(x=50,y=50)
l1=Label(root,text="Enter URL",pady=10,fg="white",bg="black").place(x=50,y=160)
urlField = Entry(root, width=20, justify=CENTER,borderwidth=1,bg="white",fg="grey")
urlField.place(x=110,y=170)
def rest():
    dwnbtn['state']='enabled'
    root.mainloop()
while True:
    urlField.delete(0,END)
    dwnbtn=Button(root,text="search",relief='ridge',command=btnclicked,bg="grey")
    urlField.focus()
    reset=Button(root,text="Reset",command=rest)
    reset.place(x=250,y=250)
    dwnbtn.place(x=250,y=170)
    root.mainloop()
