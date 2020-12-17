import tkinter

def create_new_window():
    new_window = tkinter.Toplevel(main)

main = tkinter.Tk()

# window title
main.title('カルシウム')

# window size (width x height)
main.geometry('400x300')

#
# main frame
#
# grid
#     column -> 配置する列 row -> 配置する行 sticky -> どこに配置するか padx -> 横の隙間
#     pady -> 縦の隙間
#
main_frame = tkinter.Frame(main)
main_frame.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=5)

# title
title_label = tkinter.Label(main_frame, text='カルシウム', foreground='#0000ff', font=('', 20))
#title.pack()

button1 = tkinter.Button(main_frame, text='ボタン1', command=create_new_window)
button2 = tkinter.Button(main_frame, text='ボタン2')
button3 = tkinter.Button(main_frame, text='ボタン3')

# 配置
title_label.grid(column=1, row=0)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)

main.mainloop()
