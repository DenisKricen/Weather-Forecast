from customtkinter import *
import pyowm
from PIL import Image

owm=pyowm.OWM('fdee5261ebb1e35776e945b079b99ce9')
mgr=owm.weather_manager()

class window(CTk):
    def __init__(self):
            super().__init__()

            self.geometry('450x500+700+200')
            self.title('Weather Checker')
            self.resizable(False,False)

            self.logo=CTkImage(dark_image=Image.open('GUI_prog\images\weather_forecast_logo.png'),size=(460,150))
            self.logo_label=CTkLabel(master=self,text='',image=self.logo)
            self.logo_label.grid(row=4,column=0)

            self.top_frame=CTkFrame(master=self,bg_color='green')
            self.top_frame.grid(row=0,column=0,pady=(20,20),padx=(20,20))

            self.entr_sity=CTkEntry(master=self.top_frame,placeholder_text='Sity,Country')
            self.entr_sity.grid(row=0,column=0)

            self.weather=CTkLabel(master=self,text='',width=350,height=250)
            self.weather.grid(row=2,column=0)

            self.check_weather=CTkButton(master=self.top_frame,text='Search',command=self.search_wether)
            self.check_weather.grid(row=0,column=1)

            self.mainloop()

    def search_wether(self):
        observ=mgr.weather_at_place(self.entr_sity.get())
        w=observ.weather
        self.weather.configure(text=f'''
THE WEATHER
        status    - {w.detailed_status.center(15)}
        humidity  - {w.humidity}
        avrg temp - {w.temperature('celsius')['temp']}
        min temp  - {w.temperature('celsius')['temp_min']}
        max temp  - {w.temperature('celsius')['temp_max']}
        fells like- {w.temperature('celsius')['feels_like']}''')
        
 
          

app=window()
