from tkinter import *
# ---------------------------
# ventana principal
# se crea una pantalla llamada venta principal que adquiere las caracteristicas de un objeto tk
ventana_principal = Tk()

#titulo de la venta
ventana_principal.title("Sistemas UIS")

#tamaño de la ventana
ventana_principal.geometry("1000x500")

#deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

#color del fondo
ventana_principal.config(bg="white")

#----------------------------------
# frame entrada de datos
#----------------------------------
frame_c1 = Frame(ventana_principal)
frame_c1.config(bg="maroon", width=200, height=200)
frame_c1.place(x=0, y=300)

#----------------------------------
frame_c2 = Frame(ventana_principal)
frame_c2.config(bg="maroon", width=200, height=200)
frame_c2.place(x=0, y=0)

#----------------------------------
frame_c3 = Frame(ventana_principal)
frame_c3.config(bg="maroon", width=700, height=200)
frame_c3.place(x=300, y=300)

#--------------------------------------------------------
frame_c4 = Frame(ventana_principal)
frame_c4.config(bg="maroon", width=700, height=200)
frame_c4.place(x=300, y=0)
#--------------------------------------------------------
frame_l1 = Frame(ventana_principal)
frame_l1.config(bg="blue4", width=50, height=500)
frame_l1.place(x=225, y=0)

#----------------------------------
frame_l2 = Frame(ventana_principal)
frame_l2.config(bg="blue4", width=1000, height=50)
frame_l2.place(x=0, y=225)

ventana_principal.mainloop()
