from tkinter import *
from tkinter import ttk

class Admin_Inventory_create:

    @staticmethod
    def generate_inventory(obj):

        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.formframe = Frame(obj.window, bg='#fccde0')
        obj.formframe.place(x=30, y=265, width=400, height=335)

        obj.tableframe = Frame(obj.window, bg='#fccde0')
        obj.tableframe.place(x=455, y=320, width=605, height=360)

        obj.searchframe = Frame(obj.window, bg='#ffffff')
        obj.searchframe.place(x=455, y=265, width=605, height=45)

        obj.buttonframe = Frame(obj.window, bg='#ffffff')
        obj.buttonframe.place(x=30, y=620, width=400, height=60)

        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.tableframe)
        obj.allframes.append(obj.buttonframe)

    @staticmethod
    def generate_inventory_form(obj):
        # create form in form frame
        obj.product_name = StringVar()
        obj.description = StringVar()
        obj.category = StringVar()
        obj.price = StringVar()
        obj.current_stock = StringVar()
        obj.add_stock = StringVar()

        obj.product_name_label = Label(obj.formframe, text="Product name:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.product_name_label.place(x=50, y=290, width=170, height=25)
        obj.product_name_entry = Entry(obj.formframe, textvariable=obj.product_name, font=("Arial", 12))
        obj.product_name_entry.place(x=220, y=285, width=200, height=35)

        obj.description_label = Label(obj.formframe, text="Description:", font=('Arial', 12, 'bold'), bg='#ffffff')
        obj.description_label.place(x=50, y=340, width=140, height=25)
        obj.description_entry = Entry(obj.formframe, textvariable=obj.description, font=("Arial", 12))
        obj.description_entry.place(x=220, y=335, width=200, height=35)

        obj.category_label = Label(obj.formframe, text="Category:", font=('Arial', 12, 'bold'), bg='#ffffff')
        obj.category_label.place(x=50, y=390, width=110, height=25)
        obj.category_entry = Label(obj.formframe, textvariable=obj.category, font=('Arial', 12))
        obj.category_entry.place(x=220, y=385, width=200, height=35)

        obj.price_label = Label(obj.formframe, text="Price:", font=('Arial', 12, 'bold'), bg='#ffffff')
        obj.price_label.place(x=50, y=440, width=70, height=25)
        obj.price_entry = Entry(obj.formframe, textvariable=obj.price, font=("Arial", 12))
        obj.price_entry.place(x=220, y=435, width=200, height=35)

        obj.current_stock_label = Label(obj.formframe, text="Current stock:", font=('Arial', 12, 'bold'), bg='#ffffff')
        obj.current_stock_label.place(x=50, y=490, width=155, height=25)
        obj.current_stock_entry = Entry(obj.formframe, textvariable=obj.current_stock, font=("Arial", 12))
        obj.current_stock_entry.place(x=240, y=490, width=200, height=35)

        obj.add_stock_label = Label(obj.formframe, text="Add stock:", font=('Arial', 12, 'bold'), bg='#ffffff')
        obj.add_stock_label.place(x=40, y=540, width=130, height=25)
        obj.add_stock_entry = Entry(obj.formframe, textvariable=obj.add_stock, font=("Arial", 12))
        obj.add_stock_entry.place(x=220, y=535, width=200, height=35)

    @staticmethod
    def generate_inventory_button(obj):
        # create buttons in button frame
        obj.update_button = Button(obj.buttonframe, text='Update', font=('Arial', 12, 'bold'), bg='#ccccfe')
        obj.update_button.place(x=50, y=625, width=150, height=50)

        obj.remove_button = Button(obj.buttonframe, text="Remove", font=('Arial', 12, 'bold'), bg='#ccccfe')
        obj.remove_button.place(x=260, y=625, width=150, height=50)

    @staticmethod
    def generate_inventory_search(obj):
        # create entry in search frame
        obj.search_entry = Entry(obj.searchframe, font=('Arial', 12), width=20)
        obj.search_entry.place(x=470, y=270, width=335, height=35)

        #create button in search frame
        obj.search_button = Button(obj.searchframe, text="Search",font=('Arial', 12, 'bold'), bg='#ccccfe')
        obj.search_button.place(x=835, y=275,width=80, height=25)

        obj.reset_button = Label(obj.searchframe, text='Search', font=('Arial', 12, 'bold'), bg='#ccccfe')
        obj.reset_button.place(x=950, y=275, width=80, height=25)

    @staticmethod
    def generate_inventory_table(obj):
        def clickprodtable(event):
            # get selected product
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_product = cur['values']
                obj.product_name.set(cur['values'][0])
                obj.description.set(cur['values'][1])
                obj.category.set(cur['values'][2])
                obj.price.set(cur['values'][3])
                obj.current_stock.set(cur['values'][4])
                obj.add_stock.set(cur['values'][5])
            except:
                pass

        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns=('ID', 'Name', 'Description',
                                                         'Category', 'Price', 'Stocks'))
        obj.tree.heading('#0', text="ID")
        obj.tree.heading('#1', text='Name')
        obj.tree.heading('#2', text='Description')
        obj.tree.heading('#3', text='Category')
        obj.tree.heading('#4', text='Price')
        obj.tree.heading('#5', text='Stocks')

        obj.tree.column('#0', width=40)
        obj.tree.column('#1', width=105)
        obj.tree.column('#2', width=165)
        obj.tree.column('#3', width=110)
        obj.tree.column('#4', width=110)
        obj.tree.column('#5', width=75)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row=1, column=0, columnspan=6)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.tableframe, orient=VERTICAL, command=obj.tree.yview)
        obj.scrollbary.grid(row=1, column=6)

