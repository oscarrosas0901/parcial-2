from tkinter import Tk, Label, Frame, BOTH, Canvas, Button, Entry, messagebox

BASE = 480
ALTURA = 400

def mostrar_posicion():
    (x, y) = frame_graficacion.winfo_pointerxy()
    root_x = frame_graficacion.winfo_rootx()
    root_y = frame_graficacion.winfo_rooty()
    ancho_pantalla = frame_graficacion.winfo_width()
    alto_pantalla = frame_graficacion.winfo_height()
    mouse_x = x - root_x
    mouse_y = y - root_y
    if mouse_x < 0 or mouse_x > ancho_pantalla or mouse_y < 0 or mouse_y > alto_pantalla:
        mouse_x = -1
        mouse_y = -1 
    
    etiqueta.configure(text=str(mouse_x) + ", " + str(mouse_y))
    frame_graficacion.after(10, mostrar_posicion)

def calcular_pendiente():
    valor_x1 = int(datos_x1.get())
    valor_x2 = int(datos_x2.get())
    valor_y1 = int(datos_y1.get())
    valor_y2 = int(datos_y2.get())
    pendiente = (valor_y2 - valor_y1) / (valor_x2 - valor_x1)
    messagebox.showinfo("Pendiente de la recta", pendiente)

def graficas():
    C.create_line(datos_x1.get(), datos_y1.get(), datos_x2.get(), datos_y2.get(), fill = "blue", width = 5)

# ----------------------
# VENTANA PRINCIPAL
# ----------------------
ventana_principal = Tk()
ventana_principal.title("Plano cartesiano")
ventana_principal.resizable(False, False)
ventana_principal.config(bg = "red")
ventana_principal.geometry("600x600")

# ----------------------
# FRAME GRAFICACIÓN
# ----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "white", width = 480, height = 400)
frame_graficacion.pack(fill=BOTH, padx = 10, pady = 10)

# ----------------------
# CREACCIÓN CANVA
# ----------------------
C = Canvas(frame_graficacion, width = BASE, height = ALTURA)
C.place(x = 10, y = 10)

# ----------------------
# BOTÓN
# ----------------------
boton = Button(text="Calcular pendiente", padx=10,  fg="white", bg="grey", command=calcular_pendiente)
boton.pack(side="left", padx=10, pady=10)
graficar = Button(text="Graficar", padx=10,  fg="white", bg="grey", command=graficas)
graficar.pack(side="right", padx=10, pady=10)

# ----------------------
# LINEAS
# ----------------------
linea3 = C.create_line(BASE/2, 0, BASE/2, ALTURA/2, BASE/2, ALTURA, BASE/2, ALTURA/2, fill = "blue", width = 5)
linea4 = C.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, 0, ALTURA/2, BASE/2, ALTURA/2, fill = "green", width = 5)

# ----------------------
# COORDENADAS
# ----------------------
etiqueta = Label(text="-1, -1", font=("Arial", 20, "bold"))
etiqueta.pack(expand=True)
mostrar_posicion()

# ----------------------
# RECOLECTAR DATOS
# ----------------------
x1 = Label(text="X1")
x1.config(bg="white")
x1.place(x=200, y=440)
datos_x1 = Entry(ventana_principal)
datos_x1.place(x=230, y=440)

y1 = Label(text="Y1")
y1.config(bg="white")
y1.place(x=200, y=470)
datos_y1 = Entry(ventana_principal)
datos_y1.place(x=230, y=470)

x2 = Label(text="X2")
x2.config(bg="white")
x2.place(x=200, y=540)
datos_x2 = Entry(ventana_principal)
datos_x2.place(x=230, y=540)

y2 = Label(text="Y2")
y2.config(bg="white")
y2.place(x=200, y=570)
datos_y2 = Entry(ventana_principal)
datos_y2.place(x=230, y=570)


ventana_principal.mainloop()