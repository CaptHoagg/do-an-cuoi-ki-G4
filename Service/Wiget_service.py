from enum import auto
from tkinter import * 
import re 
import Api.Main_Api as main_api

class AutofillEntry(Entry): #input window field, autocompletelist, width, height 
    def __init__(self,autocompleteList, *args, **kwargs): 

        def matches(fieldValue, acListEntry):
            pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
            return re.match(pattern, acListEntry)
        api =  main_api.Api()

        Entry.__init__(self, *args, **kwargs)
        self.focus()
        self.autocompleteList = autocompleteList
        self.matchesFunction = matches
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>" , self.selection)
        self.bind("<Return>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self["height"])
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.bind("<Return>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
        
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]