from tkinter import *
textvariable=Tk()
textvariable.option_add("*Font","consolas 20")

Label(textvariable,text="Lab1",bg="green").pack(fill=X)
Label(textvariable,text="Software Lab",bg="deep sky blue").pack(fill=X)
Label(textvariable,text="Just be yourself, because life's too shot to be anybody else.",bg="gold").pack(fill=X)
Label(textvariable,text="Just be yourself, because life's too shot to be anybody else.",bg="orange",wraplength=700,justify=RIGHT).pack(fill=X)
Label(textvariable,text="Just be yourself, because life's too shot to be anybody else.",bg="#21C4F8").pack(fill=X)
Label(textvariable,text="Just be yourself, because life's too shot to be anybody else.",bg="hot pink",justify=CENTER).pack(fill=X)
Label(textvariable,text="",bg="hot pink",justify=CENTER).pack(fill=X)
Label(textvariable,text="Step Up 2: The Streets",bg="hot pink",justify=CENTER).pack(fill=X)

textvariable.mainloop()