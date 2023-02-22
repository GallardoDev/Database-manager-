from tkinter import *
from tkinter import messagebox
import sqlite3

#----------------Funciones---------------------

def conexionBBDD():
    miConexion=sqlite3.connect("Clientes")
    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute('''
            CREATE TABLE DATOSCLIENTES (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDOS VARCHAR(50),
            EDAD INTEGER,
            EMAIL VARCHAR(50),
            TELEFONO VARCHAR(10),
            PASSWORD VARCHAR(50),
            OBSERVACIONES VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "Base de Datos creada con éxito")    
    except:
        messagebox.showwarning("¡ATENCION!", "La BBDD ya existe")


        
def salirAplicacion():
        valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
        if valor == "yes":
           root.destroy()
        
def nuevo():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miEdad.set("")
    miEmail.set("")
    miTelef.set("")
    miPass.set("")
    cuadroComentario.delete(1.0, END)
    
def crear():
    miConexion=sqlite3.connect("Clientes")
    miCursor=miConexion.cursor()
    
    miCursor.execute("INSERT INTO DATOSCLIENTES VALUES(NULL, ' "+miNombre.get() +
     " ',' "+ miApellido.get() +
      " ',' "+ miEdad.get() + 
      " ',' "+ miEmail.get() +
      " ',' "+ miTelef.get() +
      " ',' "+miPass.get() + 
      " ',' "+ cuadroComentario.get("1.0", END) + " ')")
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    
def leer():
     miConexion=sqlite3.connect("Clientes")
     miCursor=miConexion.cursor()
     miCursor.execute("SELECT * FROM DATOSCLIENTES WHERE ID="+ miID.get())
     elUsuario=miCursor.fetchall()
     for usuario in elUsuario:
         miID.set(usuario[0])
         miNombre.set(usuario[1])
         miApellido.set(usuario[2])
         miEdad.set(usuario[3])
         miEmail.set(usuario[4])
         miTelef.set(usuario[5])
         miPass.set(usuario[6])
         cuadroComentario.insert(1.0, usuario[7])
         
     miConexion.commit()
     
def actualizar():
    miConexion=sqlite3.connect("Clientes")
    miCursor=miConexion.cursor()
    
    miCursor.execute("UPDATE DATOSCLIENTES SET NOMBRE_USUARIO= ' " + miNombre.get() +
    " ' , APELLIDOS= ' " + miApellido.get()+
    " ' , EDAD= ' " + miEdad.get()+
    " ' , EMAIL= ' " + miEmail.get()+
    " ' , TELEFONO= ' " + miTelef.get()+
    " ' , PASSWORD= ' " + miPass.get()+
    " ' , OBSERVACIONES= ' " + cuadroComentario.get(1.0, END)+
    " ' WHERE ID=" + miID.get())
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def delete():
    miConexion=sqlite3.connect("Clientes")
    miCursor=miConexion.cursor()

    borrar=messagebox.askquestion("Borrar", "¿Desea eliminar el campo seleccionado?")
    if borrar == "yes":
         miCursor.execute("DELETE FROM DATOSCLIENTES WHERE ID="+ miID.get())
         miConexion.commit()

         messagebox.showinfo("BBDD", "Registro borrado con éxito.")

def acerca_de():
    messagebox.showinfo("Gestor de Bases de Datos", "GBD_EASY\nDesarrollada por Adriel Gallardo García\nVersión 1.1\nPython 3.0")

def licencia():
    messagebox.showinfo("Licencia", "Derechos Reservados\nGallardo\'s app\n© Copyright")



#------------------------------------------------------------------------------------------------


root=Tk()
root.title("GBD_EASY")
root.iconbitmap('foto.ico')
root.resizable(0,0)


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
BDmenu=Menu(barraMenu, tearoff=0)
BDmenu.add_command(label="Conectar", command=conexionBBDD)
BDmenu.add_command(label="Salir", command=salirAplicacion)


BorrarMenu=Menu(barraMenu, tearoff=0)
BorrarMenu.add_command(label="Limpiar", command=nuevo)


CrudMenu=Menu(barraMenu, tearoff=0)
CrudMenu.add_command(label="Crear", command=crear)
CrudMenu.add_command(label="Leer", command=leer)
CrudMenu.add_command(label="Actualizar", command=actualizar)
CrudMenu.add_command(label="Borrar Registro", command=delete)


AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia", command=licencia)
AyudaMenu.add_command(label="Acerca de..." , command=acerca_de)

barraMenu.add_cascade(label="BBDD", menu=BDmenu)
barraMenu.add_cascade(label="Nuevo", menu=BorrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CrudMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

#----------------Comienzo de Campos-----------

miFrame=Frame(root)
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="#E1C699")

miID=StringVar()
miNombre=StringVar()
miNombre2=StringVar()
miApellido=StringVar()
miEdad=StringVar()
miEmail=StringVar()
miTelef=StringVar()
miPass=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="green")


cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="green")

cuadroEdad=Entry(miFrame, textvariable=miEdad)
cuadroEdad.grid(row=3, column=1, padx=10, pady=10)
cuadroEdad.config(fg="green")

cuadroEmail=Entry(miFrame, textvariable=miEmail)
cuadroEmail.grid(row=4, column=1, padx=10, pady=10)
cuadroEmail.config(fg="green")

cuadroTelef=Entry(miFrame, textvariable=miTelef)
cuadroTelef.grid(row=5, column=1, padx=10, pady=10)
cuadroTelef.config(fg="green")

cuadroPassword=Entry(miFrame, textvariable=miPass)
cuadroPassword.grid(row=6, column=1, padx=10, pady=10)
cuadroPassword.config(fg="green")
cuadroPassword.config(show="x")

cuadroComentario=Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=7, column=1, padx=10, pady=10)
cuadroComentario.config(fg="green")
barraDesplaza=Scrollbar(miFrame, command=cuadroComentario.yview)
barraDesplaza.grid(row=7, column=2, sticky="nsew")

cuadroComentario.config(yscrollcommand=barraDesplaza.set)

#---------------Aqui comienzan los Label------

idLabel=Label(miFrame, text="Id :")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombres :")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellidos :")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

edadLabel=Label(miFrame, text="Edad :")
edadLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

emailLabel=Label(miFrame, text="Email :")
emailLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

telefLabel=Label(miFrame, text="Telefono :")
telefLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password :")
passLabel.grid(row=6, column=0, sticky="e",padx=10, pady=10)

comentLabel=Label(miFrame, text="Observaciones :")
comentLabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

#------------Aqui los botones inferiores----------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonUpdate=Button(miFrame2, text="Update", command=actualizar)
botonUpdate.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonDelete=Button(miFrame2, text="Delete", command=delete)
botonDelete.grid(row=0, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
