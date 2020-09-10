from os import getcwd;
from os import listdir;
from os.path import isfile, join, isdir;
from tkinter import Label,Frame,Button,Scrollbar,Listbox,Tk,BOTTOM,LEFT,END,MULTIPLE,ACTIVE;

prefix = '\t-';

def getFiles(path,arr):
    for f in listdir(path):
        dirpath = join(path,f);
        if isdir(dirpath):
            arr = arr + getFiles(dirpath,arr);
        elif isfile(dirpath):
            arr.append(dirpath);
    return arr;

def generateTodoFile(onlyfiles,root=None,mylistbox=None):
    if mylistbox:
        onlyfiles = [onlyfiles[int(item)] for item in  mylistbox.curselection()]
    if root:
        root.destroy();
    f= open("TODOS.txt","w+",encoding="utf8");
    for name in onlyfiles:
        counter = 0;
        if(name != 'getTodos.py' and name != 'TODOS.txt'):
            f1 = open(name, 'r',encoding = "ISO-8859-1");
            lines = f1.readlines();
            for line in lines:
                pos = line.find("TODO");
                if pos != -1:
                    if counter == 0:
                        f.write(name + ":\n");
                    f.write(prefix+line[pos:]+'\n');
                    counter+=1;

def ui(onlyfiles):
    root=Tk()
    # root.geometry("680x500")

    Label(root, text="Select the files you want to analyse:").pack()
    frame = Frame(root)
    frame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    # root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    def CurSelet(evt):
        value=str((mylistbox.get(ACTIVE)))
    mylistbox=Listbox(frame,width=60,height=10,font=('times',13),selectmode=MULTIPLE)
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=90)
    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=mylistbox.yview)
    scrollbar.pack(side="right", fill="y")

    mylistbox.config(yscrollcommand=scrollbar.set)
    for items in onlyfiles:
        mylistbox.insert(END,items[len(getcwd()):])
    mylistbox.pack();
    # frame = Frame(master=root).grid(row=1, column=1)
    b1 = Button(bottomFrame, text="Generate TODO File(select all)", command= lambda: generateTodoFile(onlyfiles,root))
    b1.pack(side=LEFT)
    b = Button(bottomFrame, text="Generate TODO File(selected)", command= lambda: generateTodoFile(onlyfiles,root,mylistbox))
    b.pack(side=LEFT);
    root.mainloop()

def main():
    arr = [];
    onlyfiles = list(dict.fromkeys(getFiles(getcwd(),arr)));
    ui(onlyfiles);
    # TODO: Make ui to choose dirs
    # generateTodoFile(onlyfiles);


main();
