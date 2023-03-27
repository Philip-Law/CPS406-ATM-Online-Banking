import tkinter as tk
import time
from tkinter import *
from tkinter import ttk
from ATMSystemController import ATMSystemController
from ATMCard import ATMCard
from User import User

sys_controller = ATMSystemController()

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Card': None, 'Account': tk.StringVar(value='None'), 'Balance':tk.IntVar()}
        self.sys_controller = ATMSystemController()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Selection, InsertCard, EnterPIN, AccountMenu, ServiceMenu, Withdraw, Deposit, Approval, Balance):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Selection")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name in ['AccountMenu', 'ServiceMenu', 'Withdraw', 'Deposit', 'Approval', 'Balance']:
            frame.update()
    
    def set_card(self, card):
        self.shared_data['Card'] = card



#Choose User Screen
class Selection(tk.Frame):
    def __init__(self, parent, controller ):
        
        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        self.controller = controller
        
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo.png")
    
        mazebank_label = tk.Label(self, image=img)
        mazebank_label.image = img
        mazebank_label.pack(pady=25)

        #Creating frame to display all cards (emulating different customers/users) (only used for demo and not within real program)
        frame = Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        cards = self.controller.sys_controller.get_cards()

        tv = ttk.Treeview(frame, columns=(1,2,3), show="headings", height=len(cards), selectmode="browse")
        tv.pack()

        # Depending on the card that is selected, use that ATMCards information and move to next screen
        def on_treeview_select(event):
            literal_list = tv.item(tv.focus())["values"]
            card = self.controller.sys_controller.find_card(literal_list[0], literal_list[1], str(literal_list[2]))
            self.controller.set_card(card)
            self.controller.show_frame('InsertCard')

        tv.bind("<<TreeviewSelect>>", on_treeview_select)

        tv.heading(1, text="NAME")
        tv.heading(2, text="CARD NUMBER")
        tv.heading(3, text="PIN")        

        for card in cards:
            tv.insert("", "end", values=(card.get_user().get_name(), card.get_card_number(), card.get_PIN()))



#Insert Card Screen
class InsertCard(tk.Frame):
    def __init__(self, parent, controller ):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo.png")

        mazebank_label = tk.Label(self, image=img)  
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        #Creating label to prompt user to click on card to insert (enter the ATM program)
        CClabel = tk.Label(self, text="Click the Card to Insert", bg='#f0f0f0', font=('Calibri', 25))
        CClabel.place(relx=0.5, rely=0.35, anchor="center")
        
        self.controller.set_card(self.controller.shared_data['Card'])

        CC = tk.PhotoImage(file="images/CC.png")
        CC = CC.subsample(2)
        CCButton = tk.Button(self, image=CC, borderwidth=0, command=lambda: [self.controller.show_frame('EnterPIN')])
        CCButton.image = CC
        CCButton.pack(pady=130)


#Enter PIN Screen
class EnterPIN(tk.Frame):
    def __init__(self, parent, controller ):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo.png")
    
        mazebank_label = tk.Label(self,image=img)
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=4,bg='#f0f0f0')
        spacer.pack()

        #Creating label to prompt user to enter their PIN below
        PIN_label = tk.Label(self,text='Enter Your PIN',font=('calibri',20),bg='#f0f0f0',fg='black')
        PIN_label.pack(pady=10)

        PIN = tk.StringVar()
        enter_PIN = tk.Entry(self,textvariable=PIN,font=('calibri',20),width=22)
        enter_PIN.focus_set()
        enter_PIN.pack(ipady=7)

        # Hides PIN from other individuals by displaying *'s instead of the PIN itself
        def handle_focus_in(_):
            enter_PIN.configure(fg='black',show='*')
            
        enter_PIN.bind('<FocusIn>',handle_focus_in)

        # Depending on the card that was inserted, the PIN will be different, if PIN is correct go to Account Menu, otherwise display incorrect password
        def check_password():
            if PIN.get() == self.controller.shared_data['Card'].get_PIN():
                PIN.set('')
                PIN_wrong['text']=''
                self.controller.show_frame('AccountMenu')
            else:
                PIN_wrong['text']='Incorrect Password'
        
        enter = tk.Button(self,text='Enter',command=check_password,relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        enter.pack(pady=10)

        PIN_wrong = tk.Label(self,font=('calibri',20),fg='black',bg='#f0f0f0',anchor='n')
        PIN_wrong.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



#Choose Account Screen
class AccountMenu(tk.Frame):
    def __init__(self, parent, controller):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#e8e8e8')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        #Creates label that prompts users to choose an account (chequing/savings)
        self.canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.canvas.create_text(700, 25, text="Select an account.", justify="center", fill='white', font=('calibri',18))
        self.canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        #Methods direct user to the respective account depending on what option is selected
        def do_chequing():
            controller.shared_data['Account'].set('Chequing')
            controller.show_frame('ServiceMenu')

        def do_savings():
            controller.shared_data['Account'].set('Savings')
            controller.show_frame('ServiceMenu')

        #If user selects chequing button, redirect to service menu of chequing account
        chequing_account_button = tk.Button(self,text='Chequing',command=do_chequing,relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        chequing_account_button.pack(pady=10)

        #If user selects savings button, redirect to service menu of savings account
        savings_account_button = tk.Button(self,text='Savings',command=do_savings,relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        savings_account_button.pack(pady=10)
    
        exit_button = tk.Button(self,text='Exit',command=lambda: controller.show_frame('Selection'),relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        exit_button.pack(pady=10)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



#Choose Service Screen
class ServiceMenu(tk.Frame):
    def __init__(self, parent, controller):
        
        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#e8e8e8')
        self.controller = controller
        
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        #Creates label that prompts users to choose a service (withdraw,deposit,transaction log)
        self.canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.canvas.create_text(700, 25, text="Select a service.", justify="center", fill='white', font=('calibri',18))
        self.left_text = self.canvas.create_text(100, 25, text="", justify="left", fill='white', font=('calibri',18))
        self.right_text = self.canvas.create_text(1300, 25, text="", justify="right", fill='white', font=('calibri',18))
        self.canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        #If user selects withdraw then show user the withdraw screen
        withdraw_button = tk.Button(self,text='Withdraw',command=lambda: controller.show_frame('Withdraw'),relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        withdraw_button.pack(pady=10)

        #If user selects deposit then show user the deposit screen
        deposit_button = tk.Button(self,text='Deposit',command=lambda: controller.show_frame('Deposit'),relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        deposit_button.pack(pady=10)

        #If user selects transaction log then show user the transaction log screen
        transaction_log_button = tk.Button(self,text='Transaction Log',command=lambda: controller.show_frame('Balance'),relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        transaction_log_button.pack(pady=10)

        exit_button = tk.Button(self,text='Back',command=lambda: controller.show_frame('AccountMenu'),relief='raised',borderwidth=1,width=35,height=1, bg='#da0000', fg='white', font=('calibri', 18))
        exit_button.pack(pady=10)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

    def update(self):
        card = self.controller.shared_data['Card']
        account = self.controller.shared_data['Account'].get()
        if card is not None and account in ['Chequing', 'Savings']:
            # Update the text of the left and right canvas text widgets
            self.canvas.itemconfigure(self.left_text, text=card.get_user().get_name())
            self.canvas.itemconfigure(self.right_text, text=f"\t${card.get_user().get_account(account).get_balance()}")


#Withdraw Screen
class Withdraw(tk.Frame):
    def __init__(self, parent, controller):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#e8e8e8')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo2.png")

        mazebank_label = tk.Label(self, image=img, bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)

        spacer = tk.Label(self, height=2, bg='#e8e8e8')
        spacer.pack()

        #Prompts the user to enter a withdraw amount
        self.canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000', highlightbackground='#e8e8e8')
        self.middle_text = self.canvas.create_text(700, 25, text="Enter the amount you wish to withdraw from this account.", justify="center", fill='white', font=('calibri', 18))
        self.left_text = self.canvas.create_text(100, 25, text="NAME HERE", justify="left", fill='white', font=('calibri', 18))
        self.right_text = self.canvas.create_text(1300, 25, text="BALANCE HERE", justify="right", fill='white', font=('calibri', 18))
        self.canvas.pack()

        spacer = tk.Label(self, height=3, bg='#e8e8e8')
        spacer.pack()

        cash = tk.StringVar()
        amount_entry = tk.Entry(self, textvariable=cash, width=50, justify='center', font=('calibri', 15))
        amount_entry.pack(ipady=7)


        def amount():
            card = self.controller.shared_data['Card']
            account = self.controller.shared_data['Account'].get()
            check = True
            #If card and account is valid, then withdraw the appropriate amount, else display invalid amount to the screen
            if card is not None and account in ['Chequing', 'Savings']:
                try:
                    amount = int(cash.get())
                    self.controller.sys_controller.withdraw_amount(account, card, amount)
                except ValueError:
                    check = False
                    canvas = tk.Canvas(self, width=200, height=100, bg='#da0000', highlightbackground='#e8e8e8')
                    canvas.create_text(100, 50, text="Invalid Amount", justify="center", fill='white', font=('calibri', 18))
                    canvas.pack(side='bottom')
                    self.after(2000, canvas.pack_forget)
            if(check):
                cash.set('')
                self.controller.show_frame('Approval')

        enter = tk.Button(self, text='Enter', command=amount, relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18))
        enter.pack(pady=10)

        back_button = tk.Button(self, text='Back', command=lambda: controller.show_frame('ServiceMenu'), relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18))
        back_button.pack(pady=10)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

    def update(self):
        card = self.controller.shared_data['Card']
        account = self.controller.shared_data['Account'].get()
        if card is not None and account in ['Chequing', 'Savings']:
            self.canvas.itemconfigure(self.left_text, text=card.get_user().get_name())
            self.canvas.itemconfigure(self.middle_text, text=f"Enter the amount you wish to withdraw from {account} account.")
            self.canvas.itemconfigure(self.right_text, text=f"\t${card.get_user().get_account(account).get_balance()}")

# Deposit Screen
class Deposit(tk.Frame):
    def __init__(self, parent, controller):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent, bg='#e8e8e8')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo2.png")

        mazebank_label = tk.Label(self, image=img, bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)

        spacer = tk.Label(self, height=2, bg='#e8e8e8')
        spacer.pack()

        #Prompts the user to enter a deposit amount
        self.canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000', highlightbackground='#e8e8e8')
        self.middle_text = self.canvas.create_text(700, 25, text="Enter the amount you wish to deposit to this account.", justify="center", fill='white', font=('calibri', 18))
        self.left_text = self.canvas.create_text(100, 25, text="NAME HERE", justify="left", fill='white', font=('calibri', 18))
        self.right_text = self.canvas.create_text(1300, 25, text="BALANCE HERE", justify="right", fill='white', font=('calibri', 18))
        self.canvas.pack()

        spacer = tk.Label(self, height=3, bg='#e8e8e8')
        spacer.pack()

        cash = tk.StringVar()
        amount_entry = tk.Entry(self, textvariable=cash, width=50, justify='center', font=('calibri', 15))
        amount_entry.pack(ipady=10)


        def amount():
            card = self.controller.shared_data['Card']
            account = self.controller.shared_data['Account'].get()
            check = True
            #If card and account is valid, then deposit the appropriate amount, else display invalid amount to the screen
            if card is not None and account in ['Chequing', 'Savings']:
                try:
                    amount = int(cash.get())
                    self.controller.sys_controller.deposit_amount(account, card, amount)
                except ValueError:
                    check = False
                    canvas = tk.Canvas(self, width=200, height=100, bg='#da0000', highlightbackground='#e8e8e8')
                    canvas.create_text(100, 50, text="Invalid Amount", justify="center", fill='white', font=('calibri', 18))
                    canvas.pack(side='bottom')
                    self.after(2000, canvas.pack_forget)
            if(check):
                cash.set('')
                self.controller.show_frame('Approval')

        enter = tk.Button(self, text='Enter', command=amount, relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18))
        enter.pack(pady=10)

        back_button = tk.Button(self, text='Back', command=lambda: controller.show_frame('ServiceMenu'), relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18))
        back_button.pack(pady=10)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

    def update(self):
        card = self.controller.shared_data['Card']
        account = self.controller.shared_data['Account'].get()
        if card is not None and account in ['Chequing', 'Savings']:
            self.canvas.itemconfigure(self.left_text, text=card.get_user().get_name())
            self.canvas.itemconfigure(self.middle_text, text=f"Enter the amount you wish to deposit to {account} account.")
            self.canvas.itemconfigure(self.right_text, text=f"\t${card.get_user().get_account(account).get_balance()}")

# Approval Screen
class Approval(tk.Frame):
    def __init__(self, parent, controller):

        #Header/Screen Setup
        tk.Frame.__init__(self, parent,bg='#e8e8e8')        
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="images/Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

    #Removes canvas when neccesary 
    def destroy_widgets(self, cont_button):
        self.canvas.destroy()
        self.canvas2.destroy()
        self.canvas3.destroy()
        cont_button.destroy()

    def update(self):
        card = self.controller.shared_data['Card']
        account = self.controller.shared_data['Account'].get()
        transaction_amount = card.get_user().get_account(account).get_transaction_history()[-1].get_amount()
        transaction_type = card.get_user().get_account(account).get_transaction_history()[-1].get_action_type()
        transaction_id = card.get_user().get_account(account).get_transaction_history()[-1].get_id()

        #Shows customer the transaction they just completed (displays Transaction ID, Transaction Type, and New Balance)
        self.canvas = tk.Canvas(self, width=300, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.transaction_id = self.canvas.create_text(150, 25, text=f"Transaction ID: {transaction_id}", justify="center", fill='white', font=('calibri',18), anchor="center")
        self.transaction_id = self.canvas.pack(side='top', pady=10, anchor='center')
        
        self.canvas2 = tk.Canvas(self, width=200, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.transction_type = self.canvas2.create_text(100, 25, text=transaction_type, justify="center", fill='white', font=('calibri',18))
        self.transction_type = self.canvas2.pack(side='top', pady=10)

        self.canvas3 = tk.Canvas(self, width=200, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.transction_type = self.canvas3.create_text(100, 25, text=f"${transaction_amount}", justify="center", fill='white', font=('calibri',18))
        self.transction_type = self.canvas3.pack(side='top', pady=10)

        #customer can continue to make changes on their account if needed, when continue is clicked all widgets are destroyed and user gets redirected to servicemenu
        cont_button = tk.Button(self, text='Continue', command=lambda: [self.controller.show_frame('ServiceMenu'), self.destroy_widgets(cont_button)], relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18))
        cont_button.pack(pady=7)

# View Balance Screen
class Balance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#e8e8e8')
        self.controller = controller
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        # Create header widgets
        img = tk.PhotoImage(file="images/Logo2.png")
        mazebank_label = tk.Label(self, image=img, bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        tk.Label(self, height=2, bg='#e8e8e8').pack()
        
        # Create balance canvas
        self.canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        self.balance_text = self.canvas.create_text(700, 25, text="Your balance in dollars (CAD).", justify="center", fill='white', font=('calibri',18))
        self.canvas.pack()
        tk.Label(self, height=3, bg='#e8e8e8').pack()

        # Create transaction history treeview
        self.transaction_frame = tk.Frame(self)
        self.transaction_frame.pack(side='top', pady=50)
        self.transaction_tv = ttk.Treeview(self.transaction_frame, columns=(1, 2, 3, 4), show="headings", height="5")
        self.transaction_tv.pack()
        self.transaction_tv.heading(1, text="TRANSACTION TYPE")
        self.transaction_tv.heading(2, text="TRANSACTION ID")
        self.transaction_tv.heading(3, text="AMOUNT")
        self.transaction_tv.heading(4, text="DATE")

        # Create exit back buttons
        tk.Button(self, text='Exit', command=lambda: self.controller.show_frame('Selection'), relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18)).pack(pady=7, side='bottom')
        tk.Button(self, command=lambda: self.controller.show_frame('AccountMenu'), text='Back', relief='raised', borderwidth=1, width=35, height=1, bg='#da0000', fg='white', font=('calibri', 18)).pack(pady=7, side='bottom')

    def update(self):
        # Update balance label
        card = self.controller.shared_data['Card']
        account_type = self.controller.shared_data['Account'].get()
        balance = card.get_user().get_account(account_type).get_balance()

        # Clear existing data from treeview
        for item in self.transaction_tv.get_children():
            self.transaction_tv.delete(item)

        # Populate treeview with new transaction history
        transaction_history = card.get_user().get_account(account_type).get_transaction_history()
        for transaction in transaction_history:
            self.transaction_tv.insert("", "end", values=(transaction.get_action_type(), transaction.get_id(), f"${transaction.get_amount()}", transaction.get_date()))

        # Update balance text in canvas
        balance_text = f"Your balance is {balance} dollars (CAD)."
        self.canvas.itemconfigure(self.balance_text, text=balance_text)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
