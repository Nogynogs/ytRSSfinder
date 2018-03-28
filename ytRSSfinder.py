#!encoding: utf-8

import os
from subprocess import call
import requests
from bs4 import BeautifulSoup

try:
    approot = os.path.dirname(os.path.abspath(__file__))
except NameError:
    import sys
    approot = os.path.dirname(os.path.abspath(sys.argv[0]))
finally:
    os.chdir(approot)





import random
import tkinter as tk
path_bin=os.path.abspath('bytecode/you-get')



def get_url(link):
    call([path_bin, '{}'.format(link)])

class FirstStepGui(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.frame0 = tk.Frame(self)
        self.frame0.pack(side="bottom")
        self.to_walk_directory = []
        self.pack()
        self.wello()
        self.id_entry = None
        self.well = None
        self.err = None
        self.current_color = "yellow"
        self.msgggg = tk.Label(self)

    def wello(self):
        """First Windows launch in application initialaisation a fast présentation  """
        # well message
        self.well1 = tk.Label(self)
        self.well1["text"] = "Entre l'adresse de la chaine:"
        self.well1.pack(side="top")
        self.entry = tk.Entry(self,width=70)
        self.entry.bind("<Button-3>", self.popup)
        self.entry.bind("<Button-1>", self.delete_entry)
        self.entry.pack(side='top')
        # Parcourir Button use self.display_dir
        self.valid = tk.Button(self,
                                     text="Lancer",
                                     fg="black",
                                     command=self.download)
        self.valid.pack(side="bottom")

    def delete_entry(self,arg):
        self.entry.delete(0, 'end')

    def popup(self, arg):
        if self.entry.get():
            self.entry.delete(0, 'end')
        self.entry.insert(0, root.clipboard_get())
        print('id', root.clipboard_get())

    def download(self):
        self.msgggg.destroy()
        finded = False
        if self.id_entry:
            self.id_entry.delete(0, 'end')
            self.id_entry.destroy()
        if self.err:
            self.err.destroy()
        if self.well:
            self.well.destroy()

        self.id_entry = tk.Entry(self, width=70)
        self.id_entry.bind("<Button-3>", self.pop2)

        try:
            r = requests.get(self.entry.get())
            chunk = r.text[r.text.find("ucid")::]
            first = chunk
        except Exception as e:
            print(e)
            self.err = tk.Label(self)
            self.err["text"] = "Erreur pendant la requête :("
            self.err.pack(side='bottom')

        try:
            soup = BeautifulSoup(r.text)
            lk = soup.find_all('link')
            for i in lk:
                if i.get("type")== 'application/rss+xml':
                    ucid = i.get('href')
                    self.rss_url = ucid

                    self.well = tk.Label(self)
                    self.well["text"] = "Voici l'identifiant de la chaine  :)"
                    self.well.pack(side='bottom')
                    finded = True
        except:
            pass
        if not finded:

            try:

                while '&quot;' in first:
                    first = first.replace('&quot;', '' )
                first = first.split(',')[0]
                ucid = first.split(':')[1].replace(' ','')

                print(ucid)
                ucid = ucid[1:]
                ucid = ucid[:-1]
                print(ucid)
                self.rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id={}".format(ucid)
                self.well = tk.Label(self)
                self.well["text"] = "Voici l'identifiant de la chaine :)"
                self.well.pack(side='bottom')
            except Exception as e:
                print(e)
                self.err = tk.Label(self)
                self.err["text"] = "Erreur pendant le parse de la requête :("
                self.err.pack(side='bottom')
        self.id_entry.insert(0,self.rss_url)
        self.id_entry.pack(side='bottom')

    def pop2(self, arg):
        self.msgggg.destroy()
        color = ["red", "orange", "yellow", "green", "cyan", "violet"]
        color.remove(self.current_color)
        self.current_color = random.choice(color)
        root.clipboard_append(self.rss_url)
        self.msgggg = tk.Label(self.frame0,  bg=self.current_color)
        self.msgggg["text"] = "L'url a été ajoutée à votre presse papier."
        self.msgggg.pack(side='left')

def first_config_gui():
    global root
    root = tk.Tk()
    root.title("Youtube Channel Id Finder")
    root.minsize(width=80, height=50)

    app = FirstStepGui(master=root)
    app.mainloop()
first_config_gui()
