import customtkinter as ctk
import requests
import webbrowser
from tkinter import messagebox


def load_news():
    # Clear previous news widgets
    for widget in newsContainerFrame.winfo_children():
        widget.destroy() 
    search=SearchBar.get("1.0", "end-1c").strip()
    print("search1:",search)
    api_key = "Your_Api_Key" 
    if search=="":
        url= url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    else: 
        url=f"https://newsapi.org/v2/everything?q={search}&from=2025-07-02&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if search=='apple':
        print(data)
    for i in range(10):
        title = data["articles"][i]["title"]
        author = data["articles"][i]["author"]
        description = data["articles"][i]["description"]
        articleUrl=data["articles"][i]["url"]

        News1Frame = ctk.CTkFrame(master=newsContainerFrame, fg_color="#F8F8F8", corner_radius=12,border_width=1, border_color="black")
        News1Frame.pack(anchor="w", fill="x", padx=10, pady=10)

        TitleLbl = ctk.CTkLabel(
        News1Frame,
        text=title,
        font=ctk.CTkFont(family="SF Pro", size=20, weight="bold"),
        justify="left",
        text_color="black"
        )
        TitleLbl.pack(anchor="w", padx=20, pady=(12, 4))

        AuthorLbl = ctk.CTkLabel(
        master=News1Frame,
        text=f"Author: {author}",
        font=ctk.CTkFont(family="SF Pro", size=12),
        text_color="blue",
        justify="left"
        )
        AuthorLbl.pack(anchor="w", padx=20, pady=(0, 4))

        bottomframe=ctk.CTkFrame(master=News1Frame, fg_color="transparent")
        bottomframe.pack(fill='x',padx=20, pady=10)


        DescriptionLbl = ctk.CTkLabel(
        master=bottomframe,
        text=description,
        font=ctk.CTkFont(family="SF Pro", size=16),
        text_color="black",
        justify="left",
        wraplength=900,
        anchor='nw'
        )
        DescriptionLbl.pack(side="left", fill="both", expand=True, padx=(0, 10))

        ViewBtn=ctk.CTkButton(master=bottomframe,
                          text="View",
                          fg_color="black",
                          text_color="white",
                          command=lambda link=articleUrl: webbrowser.open(link)
                          )
        ViewBtn.pack(side="right", padx=20, pady=20)



###################### Main App #####################################
app = ctk.CTk()
app.title("News App")
app.geometry("1000x600")
app._set_appearance_mode("light")
app.configure(fg_color="#D9D9D9")
# app.resizable(False, False)

mainFrame=ctk.CTkScrollableFrame(app,fg_color="transparent")
mainFrame.pack(fill='both',expand='True', pady=20)

headerframe = ctk.CTkFrame(master=mainFrame, fg_color="transparent", height=100)
headerframe.pack( fill="both")

# Left frame for Breaking News label
left_frame = ctk.CTkFrame(master=headerframe, fg_color="transparent")
left_frame.pack(side="left", padx=20, pady=20)

AppName = ctk.CTkLabel(
    master=left_frame,
    text="Newsberg",
    font=ctk.CTkFont(family="Georgia", size=42),
    text_color="Black"
)
AppName.pack(pady=(4,4))

# Right frame for dropdown menu (if any)
right_frame = ctk.CTkFrame(master=headerframe, fg_color="transparent")
right_frame.pack(side="right", padx=20, pady=20)

# Place SearchBar and SearchBtn inside center_frame instead of right_frame
SearchBar = ctk.CTkTextbox(master=right_frame, height=30, width=250, fg_color="white", text_color="black", border_width=1, border_color="black")
SearchBar.pack(side="left", padx=(0, 10), pady=10)

SearchBtn = ctk.CTkButton(master=right_frame, text="Search", fg_color="black", text_color="white", width=80, command=load_news, hover_color="#282828")
SearchBtn.pack(side="right", pady=10)

newsContainerFrame = ctk.CTkFrame(master=mainFrame, fg_color="transparent")
newsContainerFrame.pack(fill='both', expand=True)


load_news()
app.mainloop()