from pytube import *
from tkinter.messagebox import *
from tkinter import *
from tkinter.filedialog import *
from threading import *
file_size=0
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    file_downloaded=file_size-remaining
    per=float((file_downloaded/file_size)*100)
    btn.config(text=f"{per}% downloaded")
def downloadvideo():
    global file_size
    try:
        url=urlField.get()
        print(url)
        btn=Button()
        btn.config(text='Please wait...')
        path_to_save_video=askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        ob=YouTube(url,on_progress_callback=progress)
        # stream=ob.streams.all()
        # for s in stream:
        #     print(s)
        stream=ob.streams.first()
        # print(stream)
        file_size=stream.filesize
        # print(stream.filesize)
        # print(stream.title)
        # print(ob.description)
        stream.download(path_to_save_video)
        print("done...")
        btn.config(text="done")
        showinfo("Downloaded Finished","Downloaded successfully")
    except Exception as e:
        print(e)
        print("error")
def downloadvideothread():
    thread=Thread(target=downloadvideo)
    thread.start()

    
main=Tk()
main.title("Shivam Youtube downloader")
main.geometry("500x600")
urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
btn=Button(main,text="Start download",command=downloadvideothread)
btn.pack(side=TOP,pady=10)

main.mainloop()

