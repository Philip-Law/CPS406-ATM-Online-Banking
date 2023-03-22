import tkinter as tk
import time

current_balance = 1000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (InsertCard, AccountMenu, EnterPIN, ServiceMenu, Withdraw, Deposit, Balance):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("InsertCard")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


#Insert Card Screen
class InsertCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#f0f0f0')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo.png")
    
        mazebank_label = tk.Label(self, image=img)
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        CClabel = tk.Label(text="Click the Card to Insert", bg='#f0f0f0', font=('Calibri', 25))
        CClabel.place(relx=0.5, rely=0.35, anchor="center")

        CC = tk.PhotoImage(file="CC.png")
        CCButton = tk.Button(self, image=CC, borderwidth=0, command=lambda: [CClabel.destroy(), self.controller.show_frame('EnterPIN')])
        CCButton.image = CC
        CCButton.pack(pady=130)


#Enter PIN Screen
class EnterPIN(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#f0f0f0')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo.png")
    
        mazebank_label = tk.Label(self,image=img)
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=4,bg='#f0f0f0')
        spacer.pack()

        PIN_label = tk.Label(self,text='Enter Your PIN',font=('calibri',20),bg='#f0f0f0',fg='black')
        PIN_label.pack(pady=10)

        PIN = tk.StringVar()
        enter_PIN = tk.Entry(self,textvariable=PIN,font=('calibri',20),width=22)
        enter_PIN.focus_set()
        enter_PIN.pack(ipady=7)

        def handle_focus_in(_):
            enter_PIN.configure(fg='black',show='*')
            
        enter_PIN.bind('<FocusIn>',handle_focus_in)

        def check_password():
           if PIN.get() == '123':
               PIN.set('')
               PIN_wrong['text']=''
               controller.show_frame('AccountMenu')
           else:
               PIN_wrong['text']='Incorrect Password'
                
        enter = tk.Button(self,text='Enter',command=check_password,relief='raised',borderwidth=1,width=30,height=3, bg='#da0000', fg='white')
        enter.pack(pady=10)

        PIN_wrong = tk.Label(self,font=('calibri',20),fg='black',bg='#f0f0f0',anchor='n')

        PIN_wrong.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()
        

#Choose Account Screen
class AccountMenu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,bg='#e8e8e8')
        self.controller = controller

        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        canvas.create_text(700, 25, text="Choose an account.", justify="center", fill='white', font=('calibri',18))
        canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        button_frame = tk.Frame(self,bg='#e8e8e8')
        button_frame.pack(fill='both',expand=True)
            
        chequing_account_button = tk.Button(button_frame,text='Chequing',command=lambda: controller.show_frame('ServiceMenu'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        chequing_account_button.grid(row=0, column=0, padx=730, pady=5, sticky="nsew")

        savings_account_button = tk.Button(button_frame,text='Savings',command=lambda: controller.show_frame('ServiceMenu'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        savings_account_button.grid(row=1,column=0,pady=5)
    
        exit_button = tk.Button(button_frame,text='Exit',command=lambda: controller.show_frame('InsertCard'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        exit_button.grid(row=3,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()


#Choose Service Screen
class ServiceMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#e8e8e8')
        self.controller = controller
   
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        canvas.create_text(700, 25, text="Choose a service.", justify="center", fill='white', font=('calibri',18))
        canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        button_frame = tk.Frame(self,bg='#e8e8e8')
        button_frame.pack(fill='both',expand=True)

        withdraw_button = tk.Button(button_frame,text='Withdraw',command=lambda: controller.show_frame('Withdraw'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        withdraw_button.grid(row=0, column=0, padx=730, pady=5, sticky="nsew")

        deposit_button = tk.Button(button_frame,text='Deposit',command=lambda: controller.show_frame('Deposit'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        deposit_button.grid(row=1,column=0,pady=5)

        transaction_log_button = tk.Button(button_frame,text='Transaction Log',command=lambda: controller.show_frame('Balance'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        transaction_log_button.grid(row=2,column=0,pady=5)

        exit_button = tk.Button(button_frame,text='Back',command=lambda: controller.show_frame('AccountMenu'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        exit_button.grid(row=3,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()


#Withdraw Screen
class Withdraw(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#e8e8e8')
        self.controller = controller
   
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        canvas.create_text(700, 25, text="Select the amount you wish to withdraw from this account.", justify="center", fill='white', font=('calibri',18))
        canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        button_frame = tk.Frame(self,bg='#e8e8e8')
        button_frame.pack(fill='both',expand=True)
            
        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame, textvariable=cash,width=59,justify='center')
        other_amount_entry.grid(row=0, column=0, padx=730, pady=5, sticky="nsew")
    
        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('ServiceMenu')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()
   

#Deposit Screen
class Deposit(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#e8e8e8')
        self.controller = controller
   
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        canvas.create_text(700, 25, text="Select the amount you wish to deposit to this account.", justify="center", fill='white', font=('calibri',18))
        canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,textvariable=cash,font=('calibri',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('ServiceMenu')
            cash.set('')
        enter = tk.Button(self,text='Enter',command=deposit_cash,relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        enter.pack(pady=10)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()


#View Balance Screen
class Balance(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#e8e8e8')
        self.controller = controller
   
        self.controller.title('Maze Bank')
        self.controller.state('zoomed')

        img = tk.PhotoImage(file="Logo2.png")
    
        mazebank_label = tk.Label(self,image=img,bg='#e8e8e8')
        mazebank_label.image = img
        mazebank_label.pack(pady=25)
        
        spacer = tk.Label(self,height=2,bg='#e8e8e8')
        spacer.pack()

        canvas = tk.Canvas(self, width=1400, height=50, bg='#da0000',highlightbackground='#e8e8e8')
        canvas.create_text(700, 25, text="Your balance in dollars (CAD).", justify="center", fill='white', font=('calibri',18))
        canvas.pack()

        spacer = tk.Label(self,height=3,bg='#e8e8e8')
        spacer.pack()

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,textvariable=controller.shared_data['Balance'],font=('calibri',25),fg='black',bg='#e8e8e8',anchor='center')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#e8e8e8')
        button_frame.pack(fill='both',expand=True)
    
        menu_button = tk.Button(button_frame,command=lambda:controller.show_frame('AccountMenu'),text='Menu',relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        menu_button.grid(row=0, column=0, padx=730, pady=5, sticky="nsew")
    
        exit_button = tk.Button(button_frame,text='Exit',command=lambda: controller.show_frame('InsertCard'),relief='raised',borderwidth=1,width=60,height=3, bg='#da0000', fg='white')
        exit_button.grid(row=1,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('calibri',12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
