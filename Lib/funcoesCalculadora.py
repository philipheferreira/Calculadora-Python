import tkinter as tk

def make_root() -> tk.Tk: #criar um root, retorna tk.Tk
    root = tk.Tk() # Tk é o modulo, e tk é a classe
    root.title("Calculadora")
    root.config(padx=10, pady=10, background ='#fff') #definir o tamanho da janela e a cor de fundo
    root.resizable(False, False) # não é redimensionada
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text = "Operações aqui",
        archor = 'e', justify = 'right', background="#fff" #archor para alinahr no canto difeito -> o label, o justify é para justificar o texto a direita
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify = 'right', bd= 1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'