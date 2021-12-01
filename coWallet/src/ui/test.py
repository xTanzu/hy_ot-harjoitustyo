# class SuperThing:

#     def __init__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)

# class Thing(SuperThing):

#     def __init__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         self.purpose = kwargs["purpose"]
#         print(self.purpose)
#         del kwargs["purpose"]
#         super().__init__(*args, **kwargs)

# a = Thing(1,2,3,4,5, name="The Thing", purpose="Nothing", reason="None")









class JustRandom:
    pass

class Stuff:
    pass

class Here:
    pass

types = [Stuff, JustRandom, Here]
names = ["JustRandom", "Stuff", "Here"]

print([thing.__name__ for thing in types].index("pöö"))

# for typ in types:
#     print(typ.__name__)
#     print(isinstance(typ, (object, type)))









































# import tkinter as tk

# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#     def show(self):
#         self.lift()

# class Page1(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 1")
#        label.pack(side="top", fill="both", expand=True)

# class Page2(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 2")
#        label.pack(side="top", fill="both", expand=True)

# class Page3(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 3")
#        label.pack(side="top", fill="both", expand=True)

# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)

#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)

#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")

#         p1.show()

# if __name__ == "__main__":
#     root = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()










































































# # a = ['first','second', 'third']
# # b = {'a': 'first', 'b': 'second', 'c': 'third'}


# # def foo(*args, **kwargs):
# #     for item in args:
# #         print(item)
# #     keys = sorted(kwargs.keys())
# #     for key in keys:
# #         print(key + ": " + kwargs[key])

# # foo("just", "words", "after", "another", c="associated", b="some", d="words", a="and")

# import tkinter as tk #import Tkinter as tk #change to commented for python2

# root = tk.Tk()

# for i in range(4):
#     #make a window with a label
#     window = tk.Toplevel(root)
#     label = tk.Label(window,text="window {}".format(i))
#     label.pack()
#     #add a button to root to lift that window
#     button = tk.Button(root, text = "lift window {}".format(i), command=window.lift)
#     button.grid(row=i)

# root.mainloop()