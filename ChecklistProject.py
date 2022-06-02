import tkinter as tk
from PIL import ImageTk, Image
import requests, json
from io import BytesIO






root=tk.Tk()
root.title("Daily Organizer")
#urls for api data
#catURL= 'https://cataas.com/cat'
catURL= 'https://thiscatdoesnotexist.com/'
#jokeURL= 'https://v2.jokeapi.dev/joke/Any?format=txt&type=single'
jokeURL='https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single'
motivateURL= 'https://zenquotes.io/api/random'


hydrateFlag=tk.BooleanVar()
codeFlag=tk.IntVar()
stretchFlag=tk.IntVar()



motivateResponse= requests.get(motivateURL)
jokeResponse= requests.get(jokeURL)
response = requests.get(catURL)


img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
data=json.loads(motivateResponse.text)
quote = data[0]['q']+ ' -' + data[0]['a']

#make the grid
#root.columnconfigure([0],minsize=200,weight=0)
#root.columnconfigure([1],minsize=400,weight=1)
#root.rowconfigure([0],minsize=400,weight=0)
#root.rowconfigure([1],minsize=200,weight=0)


def printer():
    if hydrateFlag.get() == True and stretchFlag.get() == 1 and codeFlag.get() == 1:
        congratulations.pack(side=tk.BOTTOM)



#make the frames
checkList= tk.Frame(master=root, width=10, height=100, bg='gray',)
picture=tk.Frame(master=root,height=100,width=100)
quoteFrame= tk.Frame(master=root,height=100,width=5,)
jokeFrame= tk.Frame(master=root,height=10, width=10)

#create the actual widgets
motivate=tk.Label(master=quoteFrame, text="motivate")
label=tk.Label(master=picture)
joke= tk.Label(master=jokeFrame,text='joke')
hydrate= tk.Checkbutton(master=checkList,text='Hydrate!!!', command=printer, variable=hydrateFlag, onvalue=True, offvalue = False)
code= tk.Checkbutton(master=checkList, text='code(NO ZERO DAYS!)', command=printer, variable=codeFlag, onvalue= 1, offvalue= 0)
stretch= tk.Checkbutton(master=checkList, text='Stretch',  command=printer, variable=stretchFlag, onvalue = 1, offvalue= 0)
congratulations = tk.Label(master=checkList, text='Congrats!!! \nDont Forget to Relax! :)')

#assign the values from the api
label['image'] = img
joke['text']=jokeResponse.text
motivate['text']= quote


#place onto tkinter
#checkList.grid(row=0,column=0,fill=tk.X)
#picture.grid(row=0, column=1)
#jokeFrame.grid(row=1,column=1)
#quoteFrame.grid(row=1,column=0)
checkList.pack(side=tk.LEFT,expand=False,fill=tk.Y)
picture.pack(side=tk.TOP,expand=True)
quoteFrame.pack(side=tk.BOTTOM,expand=True)
jokeFrame.pack(side=tk.BOTTOM,expand=True)

#place widgets onto frames
label.pack()
joke.pack()
motivate.pack(side=tk.BOTTOM,)
hydrate.pack()
code.pack()
stretch.pack()



root.mainloop()