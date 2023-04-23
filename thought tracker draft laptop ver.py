import tkinter as tk
import time

class App:
    def __init__(self, master):
        self.master = master
        master.title("Thought Usage Tracker")
        master.attributes('-alpha', 1) # set opacity to 70%
        master.configure(background='black') # set background to black
        
        self.label = tk.Label(master, text="What is your thought usage?", font=("Arial", 20), pady=10, fg='red', bg='black') # set foreground to red and background to black
        self.label.pack()
        
        self.button_frame = tk.Frame(master, pady=10, bg='black') # set background to black
        self.button_frame.pack()
        
        self.button1 = tk.Button(self.button_frame, text="1", width=5, height=3, font=("Arial", 20), fg='red', bg='grey', command=lambda: self.submit_answer(1)) # set foreground to red
        self.button1.pack(side=tk.LEFT, padx=10)
        
        self.button2 = tk.Button(self.button_frame, text="2", width=5, height=3, font=("Arial", 20), fg='red', bg='grey', command=lambda: self.submit_answer(2)) # set foreground to red
        self.button2.pack(side=tk.LEFT, padx=10)
        
        self.button3 = tk.Button(self.button_frame, text="3", width=5, height=3, font=("Arial", 20), fg='red', bg='grey', command=lambda: self.submit_answer(3)) # set foreground to red
        self.button3.pack(side=tk.LEFT, padx=10)
        
        self.result_label = tk.Label(master, text="", font=("Arial", 20), fg='red', bg='black') # set foreground to red and background to black
        self.result_label.pack()
        
        self.log_frame = tk.Frame(master, bg='black', padx=10, pady=10) # set background to black
        self.log_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.log_label = tk.Label(self.log_frame, text="", font=("Arial", 12), justify=tk.LEFT, bg='black', fg='red') # set foreground to red and background to black
        self.log_label.pack()
        
        self.log = []
        
        current_time = time.localtime()
        self.last_sec = current_time.tm_sec

        self.schedule_popup()
    
    
    def submit_answer(self, answer):
        if answer == 1:
            thought_usage = "low"
            self.result_label.configure(text="Your thought usage is low.")
        elif answer == 2:
            thought_usage = "moderate"
            self.result_label.configure(text="Your thought usage is moderate.")
        elif answer == 3:
            thought_usage = "high"
            self.result_label.configure(text="Your thought usage is high.")

        timestamp = time.strftime("%I:%M %p")

        self.log.append((answer, thought_usage, timestamp))

        log_text = "\n".join(f"Pressed {entry[0]}, {entry[1]} thought usage at {entry[2]}" for entry in self.log)
        self.log_label.configure(text=log_text)
        
    def schedule_popup(self):
        # create a popup window
        popup = tk.Toplevel(self.master)
        popup.title("Time's up!")
        popup.geometry("300x100")
        popup.attributes('-alpha', 0.9) # set opacity to 90%

        # add a message to the popup window
        message = f"It's {time.strftime('%I:%M %p')}!"
        label = tk.Label(popup, text=message, font=("Arial", 20))
        label.pack(pady=10)

        # add a button to close the popup window
        close_button = tk.Button(popup, text="Close", font=("Arial", 14), command=lambda: self.reset_timer(popup))
        close_button.pack()

        # schedule the next popup in 30 seconds
        self.master.after(1800000, self.schedule_popup)
            
    def reset_timer(self, popup):
        # destroy the popup window
        popup.destroy()

        # reset the timer
        current_time = time.localtime()
        self.last_sec = current_time.tm_sec

# create the GUI
root = tk.Tk()
app = App(root)

# run the GUI
root.mainloop()


