import tkinter as tk
from typing import List

class calculadora:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[List[tk.Buttons]]):
        self.root= root
        self.label = label
        self.display = display
        self.buttons = buttons

