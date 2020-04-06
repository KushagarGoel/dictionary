"""
Created on Thu Apr  6 21:19:48 2020

@author: kushagar
"""

# using wordnet as set of words
from nltk.corpus import wordnet 

from tkinter import *

def finder():
    try:
        global e
        global string
        global he
        global root
        global antonyms
        
        string = e.get() 
        syns = wordnet.synsets(string)
        he = [wd.lemmas()[0].name() for wd in syns]
        he = list(set(he))
        
        antonyms = [] 
        for syn in wordnet.synsets(string): 
            for l in syn.lemmas(): 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name()) 
        antonyms = list(set(antonyms))
    
        #pane for synonyms
        pane2a = Frame(root) 
        pane2a.pack(fill = BOTH, expand = True)
        pane2a.configure(bg='#A3E4D7')
        
        #pane for antonyms
        pane2b = Frame(root) 
        pane2b.pack(fill = BOTH, expand = True)
        pane2b.configure(bg='#A3E4D7')

        #pane for output lables
        pane3 = Frame(root) 
        pane3.pack(fill = BOTH, expand = True)
        pane3.configure(bg='#A3E4D7')
        
        #Synonyms
        Label(pane2a, text="Synonyms",bg='#A3E4D7').pack()
        for i in range(len(he)):
            i = Button(pane2a,text=he[i],command=lambda j=i: printtext(j,pane2a,pane2b))
            i.pack(side='left',pady=10,padx=2)
            i.configure(bg='#76D7C4')
            
        #Antonyms
        Label(pane2b, text="Antonyms",bg = '#A3E4D7').pack()
        for p in range(len(antonyms)):
            p = Button(pane2b,text=antonyms[p],command=lambda q=p: printtextt(q,pane2b,pane2a))
            p.pack(side='left',pady=10,padx=2)
            p.configure(bg='#76D7C4')
            
        #Output lables
        Label(pane3, text="Word: "+string.upper(),bg='#A3E4D7',font='helvetica').pack()
        Label(pane3, text="Definition:  "+syns[0].definition(),bg='#A3E4D7').pack()
        Label(pane3, text="Examples:   "+syns[0].examples()[0],bg='#A3E4D7').pack()
        Label(pane3, text="            "+syns[0].examples()[0],bg='#A3E4D7').pack()
        Label(pane3,text="------------------------------------------------------------------------------------------------------",bg='#A3E4D7').pack()
        
    except:
         Label(pane3, text="No result Found",bg='#A3E4D7').pack()
         Label(pane3,text="-----------------------------------------------------------------------------------------------------",bg='#A3E4D7').pack()

#Called by Synonyms   
def printtext(i,pane,panee):
    global e
    e.delete(0,END)
    e.insert(0,he[i])
    pane.destroy()
    panee.destroy()
    finder()

#called by antonyms
def printtextt(i,pane,panee):
    global e
    e.delete(0,END)
    e.insert(0,antonyms[i])
    pane.destroy()
    panee.destroy()
    finder()

#To clear the window  
def clear():
    global root
    root.destroy()
    root = Tk()
    root.title('Dictionary')
    pane = Frame(root) 
    
    pane.configure(bg='#A3E4D7')
    pane.pack(fill = BOTH, expand = True) 
    
    
    pane1 = Frame(root) 
    pane1.pack(fill = BOTH, expand = True) 
     
    pane1.configure(bg='#A3E4D7')
    Label(pane, text='Enter the word',bg='#A3E4D7',font='helvetica').pack(side='left')
    
    e = Entry(pane)
    e.pack(side='left',padx=20,pady=10)
    e.configure(bg='#E8F8F5')
    m1 = Button(pane,text='Clear',command=clear)
    m1.pack(side='right')
    m1.configure(bg='#76D7C4')
    m2 = Button(pane,text='New',command=new)
    m2.pack(side='right',padx=10)
    m2.configure(bg='#76D7C4')
    
    m = Button(pane1,text='Search',command=finder)
    m.pack(side='left',padx=10)
    m.configure(bg='#76D7C4')

    root.mainloop()

#To open another fresh window
def new():
    global root
    root = Tk()
    root.title('Dictionary')
    pane = Frame(root) 
    
    pane.configure(bg='#A3E4D7')
    pane.pack(fill = BOTH, expand = True) 
    
    
    pane1 = Frame(root) 
    pane1.pack(fill = BOTH, expand = True) 
     
    pane1.configure(bg='#A3E4D7')
    Label(pane, text='Enter the word',bg='#A3E4D7',font='helvetica').pack(side='left')
    
    e = Entry(pane)
    e.pack(side='left',padx=20,pady=10)
    e.configure(bg='#E8F8F5')
    m1 = Button(pane,text='Clear',command=clear)
    m1.pack(side='right')
    m1.configure(bg='#76D7C4')
    m2 = Button(pane,text='New',command=new)
    m2.pack(side='right',padx=10)
    m2.configure(bg='#76D7C4')
    
    m = Button(pane1,text='Search',command=finder)
    m.pack(side='left',padx=10)
    m.configure(bg='#76D7C4')
    
    root.mainloop()
    
    
root = Tk()  #starting 
root.title('Dictionary')

pane = Frame(root) 
pane.configure(bg='#A3E4D7')
pane.pack(fill = BOTH, expand = True) 

pane1 = Frame(root) 
pane1.pack(fill = BOTH, expand = True) 
 
pane1.configure(bg='#A3E4D7')
Label(pane, text='Enter the word',bg='#A3E4D7',font='helvetica').pack(side='left')

e = Entry(pane)
e.pack(side='left',padx=20,pady=10)
e.configure(bg='#E8F8F5')
m1 = Button(pane,text='Clear',command=clear)
m1.pack(side='right')
m1.configure(bg='#76D7C4')
m2 = Button(pane,text='New',command=new)
m2.pack(side='right',padx=10)
m2.configure(bg='#76D7C4')

m = Button(pane1,text='Search',command=finder)
m.pack(side='left',padx=10)
m.configure(bg='#76D7C4')

root.mainloop()


