# PyGame

������� � ������ ������� (����) ����������� ��������� (GUI).

���� ����� ��������� ��� �������� GUI �� python: PyQt (�������, ����� �����), PyGtk (���� ������������������), tkinter (�����).

��� �������� GUI ��� ���� ���� ����������� ����������, �������� PyGame � �� ��������� ��� ����� PyGame Zero

## ������

* [https://pygame-zero.readthedocs.io/en/stable/index.html] pygame-zero
  * [https://github.com/bennuttall/uno] - ���� UNO �� pygame-zero
* [https://www.pygame.org/wiki/tutorials] - pygame
   * [http://www.pygame.org/docs/ref/examples.html] - ������� ���
   * [http://openbookproject.net/thinkcs/python/english3e/pygame.html]
   * [http://pygametutorials.wikidot.com/tutorials-basic] - OOP pygame tutorial
* [https://www.python-course.eu/python_tkinter.php] - tkinter tutorial
   * [https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html] - OOP tkinter tutorial
   * ����������, ����� 13. �������� � ���������������� ������������ ����������
   * ���� ���������������� �� Python, ��� 89 � �����
   * Sammerfield, Pithon in Practice. Chapter 7 Graphical User Interface with Python and Tkinker

## �������� ��������� GUI �� ������� tkinter

[https://docs.python.org/3/library/tk.html] - ������������

* ������ � ����������� ��������.
* ��������� ������.
* ������������ ������ � IDLE

��������, � Windows ����� *.pyw ����������� ���������� pythonw.exe, � �� python.exe, ������� ��� ������� �� ����� �������. � Linux ������� � ����������� ���.

��������� ���� ���������� ��������� � ��������� � GUI. ��� 13.1 ����������

### Event-Listener

��� ������� ������������ GUI ����� ����� ������������ ������ Event (�������) - Listener (���������).

����� �������� � GUI ��������� ������� (event). ��������, ������� Shift �� ����������, �������� ���� ��� ������� �� ������. ��� �������� �� ����� GUI, ������� ����������� (�������) ��� �������. ����� ������ ������ ����� �������� 1 �������. ������ ����� ����� ��-������� ������������� �� ���� � �� �� �������.

### Hello, world!

����� �� ���������� https://www.python-course.eu/tkinter_labels.php

������� ���������� ��������� � GUI �� tkinter.

```python
import tkinter as tk

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk

root = tk.Tk()                              # ������ ����

w = tk.Label(root, text="Hello Tkinter!")   # � ��� ���� ��������� ������� (Label)
w.pack()                                    # ���� ���������� �� ������� ������������ �������

root.mainloop()                             # ���� ��������� �������
```
Linux, Gnome
[!img/hello_tkinker.png]

Windows:
[!img/hello_tkinker_windows.png]

���� ������������ (��������) �������� �������� ��������� ��� �����, ��������� � ������������ �������.

� Windows ��� �� Mac ��� ���� ����� ���������, ��� ������� ��������� ����� � Windows ��� �� Mac.

�������: *control*, *wiget* - ������� GUI.

### Label - ������� (�����������).

������� ������� �������������� ����������� � ���� �������� python ��� Label.

```python
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.gif")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
```

*justify* - ������������. LEFT, RIGHT, CENTER (�� ���������).

*padx* - �������������� �������������� ������ ������ w2. �� ��������� ������ 1. 

*pady* - ������������ ������.

������� 

[!img/label_with_image.png]

**���� ����� �������� ����� ������ ��������, ��������� � ��������, � ����� � ����� � ��� �� Label**

[!img/text_on_top_of_image.png]

```python
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.gif")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root, 
             compound = tk.CENTER,
             text=explanation, 
             image=logo).pack(side="right")

root.mainloop()
```

** ����� � ���� **

[!img/colored_labels.png]

```python
import tkinter as tk

root = tk.Tk()
tk.Label(root, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").pack()
tk.Label(root, 
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
tk.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()
```

** ������������ ��������� Label �� �������**

[!img/dynamic_label.png]

```python
import tkinter as tk

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
```

### ������ widget (�� ������)

* **Frame** - ������-���������, ������� ������������� ������ ���� �� ����� �������� � ������ ����. ������������ ��� ����������� ������ �������� � layout.
* **Toplevel** - ��������� ����.
* **Canvas** - �������� ���! ����� ������� �������������. ������ ��� �������� ����� ���������� ��������.
* **Text** - ����� � �������������� ���������������� ������, ����� ���� �������� �����������.
* **Button** - ������.
* **Label** - ������� ��� �����������, ������ �� �������������.
* **Message** - ������� �������, ������� ����� ���� wrapped. ������ �� Label.
* **Scrollbar**
* **Checkbutton**, **Radiobutton**, **Listbox**, **Entry** � **Scale** - ������ ���� �������� ��� ����� ����������.
* **Menu** � **Menubutton** - ������� ����

## ������������� tkinter � ��� �����

https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.htm

������� GUI � ��������, ��������� ���������� tkinter.

���� �� ����� ������������ ������������, ��������� �����������. ���� ������� �� ������� � ���� ������.

������� � Label (�������) ��� � Button (������). �� ������� �� ������ greet_button ���������� ����� self.greet, ������� �������� "Greetings!".

�������� ��� ������� ������ close_button � �������� ����� ����.

```python
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
```

## Layout Manager - ���������� ������������ �������� (pack, grid, place)

����� ���������� �� ����� **pack()**, ������� ������� ������� ���� �� ������ � ������������ ���������, ������ ����. ������ ��� ���������� ����.

����� ������� � pack �������� **side**. ���� ����� ������� ������������ ��������. �� ���� ��� �������.

```python
from tkinter import LEFT, RIGHT

# (...)

self.label.pack()
self.greet_button.pack(side=LEFT)
self.close_button.pack(side=RIGHT)
```

��� ������� ���� ����������� **grid()**.

```python
from tkinter import W

# (...)

self.label.grid(columnspan=2, sticky=W) # ������ 0, �������� 2 �������, ������������ W ( left-aligned)
self.greet_button.grid(row=1)           # ������ 1, ������� 0
self.close_button.grid(row=1, column=1) # ������ 1, ������� 1
```

������ �� ��������� - ������ ��������� ������. ������� �� ��������� 0.

������������ � ��������� **sticky** ���� �� �������� �����: N, S, W, E.

�� ��������� ������������ �� ������ (�� ����������� � �� ���������).

W+E �������� "��������� ����� �������".

����� ������� ���������� NE, SW � ��� �����.

����� columnspan ���� rowspan (�� �������� �������� ��� ������� ���������� ������).

*�� ���������� � ����� ���������� pack � grid! �������� ��������� �������� � ������ Frame � ���������� ������ ��� Frame ������ layout manager.*

**place()** - �������������� layout manager. ���� ����� ������� ����� ��������� ���.

https://www.tutorialspoint.com/python/tk_place.htm

## Custom Events

* **Event** - ������� (������)
* **event handler** - ���������� �������  (�������)

���������� ��������� �������, ��� Label ������ ���� ����� �� ����� ����.

```python
from tkinter import Tk, Label, Button, StringVar

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text) # ������ label � ����� cycle_label_text
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
```

����� �� ������ ��������� ������� ���������� ������� (greet) � ���������, ������� ��� ���������� � tkinter �� ���������. ����� Button (������) ��� ����� � ����� �� ������, ��� ��� ���� �� ������ - ��������� ����� ��������� ���� ������. 

������, �� �� ���������� ����� ������������� ��������� � ����� ��������� ������ ������� ������ ������� � ������� � ���� �������-�����������, ��������� ����� **bind()**, ������� ���� � ������ ������ ��������.

������� ���������� ���������������� �� ����� ������������������ � ���� ������ �� ����-�����, ������� �� �������� ����������� ��� python. ��� ��������� �������� ������� �������:

https://www.python-course.eu/tkinter_events_binds.php

* ������� "&lt;Button-1&gt;", "&lt;Button-2&gt;" � "&lt;Button-3&gt;" �������������, ��� ���� ������ ������������ ������ ����, ����� ������ ��� ��� ��������. 
   * Button-1 - ����� ������ ����;
   * Button-2 - ������� ������ ����; - �� ����� � �� ����!
   * Button-3 - ������ ������ ����;
* "&lt;ButtonRelease-1&gt;" - ����� ������ ���� ���� ��������.
* "&lt;B1-Motion&gt;" - ���� ������������ ��� ������� ����� ������ (��� ������ ������ ���������� B2 � B3).
* "&lt;Enter&gt;" � "&lt;Leave&gt;" - ������ ���� ����� ��� ������� ������.
* "&lt;Key&gt;" - ��������, ��� ���� ������ *�����* ������ �� ����������. ����� ����������� �� ������� ������������ ������, ��������, "&lt;Return&gt;" (the enter key) ��� ���������� ������, ��������,  "&lt;Shift-Up&gt;" (shift-up-arrow). ������� ������ ����������� ���������� �������� ������� ��� ������ ������, ��� ������; ��������, ������� ������ � ��� ������ "a".
* "&lt;Configure&gt;" - � ������� ��������� ������.

���������� ������ ����� ������� �������� - �� �� ����� ������ �������� �����, ��������� ������� ������ Python. ������ ����� �� ������ ������������ ����� ����������� ������ **StringVar** ��������� ���������� tkinter � ���������� ����� �������� ��� ������� ������ ���, ����� �� �����, ����� ����� � ����� ���������.

��������, ��� ����������� ������� cycle_label_text(self, event) ���������� ������ event, � ������� ������� �������������� ���������� � �������. 

����� �������� ���� � ��� �� ���������� �� ������ �������.

## �����������

������� �����������, ������� ����� ������ ���������� � �������� ��������� �����. ������ reset ������ �������� ���������.

���� ������� ������ ������, �� ����� ��������� ��������� ������ � ����������� �� ������ ����.

```python
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()
```
