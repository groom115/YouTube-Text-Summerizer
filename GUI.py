def summarizer(text, option, fraction):
    
    frac=fraction
    if option == "Extractive":
        return freq_summary(text, frac)
    if option == "abstractive":
        return abs(text)
      
   
  def browse():
    global folder
    folder = filedialog.askdirectory(initialdir='/')
    get_folder.insert(0, folder)


browse = Button(root, text="Browse", command=browse)
browse.place(height=30, x=475, y=290)


# Button Clear --> Reset all settings to default
def on_clear():
    default_option.set(options[0])
    get_url.delete(0, END)
    get_folder.delete(0, END)
    get_fraction.delete(0, END)


clear = Button(root, text="Clear", command=on_clear)
clear.place(width=50, x=240, y=350)
# Function on Submit


def on_submit():
    global url, choice, frac, current, folder
    url = get_url.get()
    choice = default_option.get()
    frac = float(get_fraction.get())
    current = os.getcwd()
    folder = get_folder.get()
    os.chdir(folder)
    print(url,choice,frac,folder)
    corpus = get_caption(url)
    with open("corpus.txt",'w+') as c:
        print(corpus,file=c)
    # Calling the main summarizer function
    summary = summarizer(corpus, choice, frac)
    filename = video_title+" "+choice+'.txt'
    filename = re.sub(r'[\/:*?<>|]', ' ', filename)
    with open(filename, 'w+') as f:
        print(summary, file=f)
    os.remove(os.getcwd()+'\\test.en.vtt')
    os.chdir(current)
    openpath = Button(root, text="Open Folder",
                      command=lambda: os.startfile(get_folder.get()))
    openpath.place(x=360, y=350)


# Button -->Submit
submit = Button(root, text="Submit", command=on_submit)
submit.place(width=50, x=300, y=350)

# Button Open Folder to view Saved files

root.mainloop()
