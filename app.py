import customtkinter as ctk
import requests

api_key="your_api_key"


app=ctk.CTk()
app.title("News App")
app.geometry("1000x600")
app.resizable("false","false")

frame=ctk.CTkFrame(master=app, fg_color="#242424")
frame.pack(pady=2, fill="x")

AppName=ctk.CTkLabel(master=frame, text="Latest News", font=ctk.CTkFont(family="SF Pro", size=32, weight="bold"))
AppName.pack(side='left',padx=20, pady=20)

options=["India", "Spain", "Australia"]
dropdown=ctk.CTkOptionMenu(master=frame, values=options, width=150, height=30, font=("SF PRO", 14) )
dropdown.pack(side="right", padx=20, pady=20)

#Trial news
url=f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
response=requests.get(url)
data=response.json()


title = data["articles"][0]["title"]

TitleLbl=ctk.CTkLabel(app, text=title,  font=ctk.CTkFont(family="SF Pro", size=18), wraplength=800, justify="left")
TitleLbl.pack(anchor='w',padx=20, pady=20)

app.mainloop()