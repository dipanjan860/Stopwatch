import tkinter as tk
class stopwatch(tk.Frame):
    def __init__(self,window=None):
        super().__init__(window)
        self.window = window
        self.new_time = ''
        self.running = False
        self.total_hours = 0
        self.total_minutes = 0
        self.total_seconds = 0
        self.pack(anchor='center',pady=200)
        self.features()

    def features(self):
        self.stopwatch_label = tk.Label(self,text='00:00:00',background="white",foreground="black",font=('agency fb',131,"bold"))
        self.stopwatch_label.pack()

        self.start_time_button=tk.Button(self,text="START",height=2,width=11,font=('arial',19,"bold"),background="#00FF7F",command=self.start_time)
        self.start_time_button.pack(side=tk.LEFT)

        self.stop_time_button=tk.Button(self,text="STOP",height=2,width=11,font=('arial',19,"bold"),background="#FF4040",command=self.pause_time)
        self.stop_time_button.pack(side=tk.LEFT)

        self.reset_time_button=tk.Button(self,text="RESET",height=2,width=11,font=('arial',19,"bold"),background="#66CDAA",command = self.reset_time)
        self.reset_time_button.pack(side=tk.LEFT)

        self.quit_button=tk.Button(self,text="QUIT",height=2,width=11,font=('arial',19,"bold"),background="#FFD700",command=self.window.quit)
        self.quit_button.pack(side=tk.LEFT)

        self.window.title('Stopwatch')

    def start_time(self):
        if not self.running:
            self.stopwatch_label.after(1000)
            self.change()
            self.running = True

    def pause_time(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.new_time)
            self.running = False

    def reset_time(self):
        if self.running:
            self.stop_time_button.after_cancel(self.new_time)
            self.running = False
        self.total_hours,self.total_minutes,self.total_seconds = 0,0,0
        self.stopwatch_label.config(text='00:00:00')

    def change(self):
        self.total_seconds += 1
        if self.total_seconds ==60:
            self.total_minutes +=1
            self.total_seconds = 0
        if self.total_minutes == 60:
            self.total_hours += 1
            self.total_minutes = 0
        total_hours_string = f'{self.total_hours}' if self.total_hours >9 else f'0{self.total_hours}'
        total_minutes_string = f'{self.total_minutes}' if self.total_minutes >9 else f'0{self.total_minutes}'
        total_seconds_string = f'{self.total_seconds}' if self.total_seconds >9 else f'0{self.total_seconds}'
        self.stopwatch_label.config(text=total_hours_string + ':' + total_minutes_string + ':' +  total_seconds_string)
        self.new_time = self.stopwatch_label.after(1000,self.change)

root = tk.Tk()
obj = stopwatch(window=root)
obj.mainloop()

        