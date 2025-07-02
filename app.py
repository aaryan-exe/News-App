import customtkinter as ctk
import requests

app = ctk.CTk()
app.title("News App")
app.geometry("1000x600")
app._set_appearance_mode("dark")
# app.resizable(False, False)

headerframe = ctk.CTkFrame(master=app, fg_color="transparent", height=100)
headerframe.pack(pady=2, fill="both")

# Left frame for Breaking News label
left_frame = ctk.CTkFrame(master=headerframe, fg_color="transparent")
left_frame.pack(side="left", padx=20, pady=20)

AppName = ctk.CTkLabel(
    master=left_frame,
    text="Breaking News",
    font=ctk.CTkFont(family="SF Pro", size=32, weight="bold"),
)
AppName.pack()

# Right frame for dropdown menu (if any)
right_frame = ctk.CTkFrame(master=headerframe, fg_color="transparent")
right_frame.pack(side="right", padx=20, pady=20)

# Place SearchBar and SearchBtn inside center_frame instead of right_frame
SearchBar = ctk.CTkTextbox(master=right_frame, height=30, width=300)
SearchBar.pack(side="left", padx=(0, 10), pady=10)

SearchBtn = ctk.CTkButton(master=right_frame, text="Search")
SearchBtn.pack(side="right", pady=10)


mainFrame=ctk.CTkScrollableFrame(app,fg_color="transparent")
mainFrame.pack(fill='both',expand='True', pady=20)
# Trial news
api_key = "Your_Api_Key"  
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
response = requests.get(url)
data = response.json()



for i in range(10):
    title = data["articles"][i]["title"]
    author=data["articles"][i]["author"]
    News1Frame=ctk.CTkFrame(master=mainFrame,)
    News1Frame.pack(anchor="w",fill="x", padx=10, pady=10)

    TitleLbl = ctk.CTkLabel(
        News1Frame,
        text=title,
        font=ctk.CTkFont(family="SF Pro", size=20),
        justify="left",
        # wraplength=900,
    )
    TitleLbl.pack(anchor="w", padx=20, pady=(10,2))

    AuthorLbl=ctk.CTkLabel(master=News1Frame,
                      text=f"author: {author}",
                      font=ctk.CTkFont(family="SF Pro", size=12),
                      text_color="blue",
                      justify="left"
                      )
    AuthorLbl.pack(anchor="w", padx=20, pady=(4,10))
app.mainloop()
