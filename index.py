from clearJSON import *
from readJSON import *
from writeJSON import *
from tkinter import *

# Instancia de Tkinter
window = Tk()

# Titulo de mi programa
window.title("Base de datos")

# Dimension de mi programana
window.geometry("900x500")


Label(window, text="¡Vamos a guardar tus datos!",
      font=("Helvetica", 20)).place(x=30, y=10)

# Creamos el input del nombre de usuario
Label(window, text='Ingrese su nombre:', font=(
    "Helvetica", 14)).place(x=60, y=70)
username = Entry(window, width=30, font=(
    "Helvetica", 12))
username.place(x=60, y=100)

# Creamos el input que pida nombre de la ciudad
Label(window, text='Ingrese su ciudad:', font=(
    "Helvetica", 14)).place(x=60, y=140)
userCity = Entry(window, width=30, font=(
    "Helvetica", 12))
userCity.place(x=60, y=170)

# Creamos el input que pida la edad al usuario
Label(window, text='Ingrese su edad:', font=(
    "Helvetica", 14)).place(x=60, y=210)
userAge = Entry(window, width=30, font=(
    "Helvetica", 12))
userAge.place(x=60, y=240)

# Creamos un boton para agregar los datos
add_data_button = Button(window, text="Agregar datos",
                         command=lambda: add_user()).place(x=150, y=280)
delete_input_content = Button(window, text="Eliminar contenido de los inputs",
                              command=lambda: clear_inputs()).place(x=120, y=310)
delete_database_content = Button(window, text="Eliminar información de la base de datos",
                                 command=lambda: clear_data_base()).place(x=100, y=340)


# Funciones para del usuario
def add_user():
    dataList = readJSON('data')
    dataList.append({
        "name": username.get(),
        "age": userAge.get(),
        "city": userCity.get(),
    })
    writeJSON('data', dataList)
    printData()

# Funcion para elimar la info de la base de datos


def clear_data_base():
    clearJSON('data')
    printData()

# Función para borrar el contenido de los inputs


def clear_inputs():
    username.delete(0, END)
    userAge.delete(0, END)
    userCity.delete(0, END)


Label(window, text='Su info es:', font=(
    "Helvetica", 14)).place(x=500, y=30)


def printData():
    dataList = readJSON('data')
    i = 30

    for data in dataList:
        Label(window, text=f"Nombre: {data['name']}", font=(
            "Helvetica", 12)).place(x=500, y=40+i)
        Label(window, text=f"Edad: {data['age']}", font=(
            "Helvetica", 12)).place(x=500, y=70+i)
        Label(window, text=f"Ciudad: {data['city']}", font=(
            "Helvetica", 12)).place(x=500, y=100+i)
        i += 110


printData()


window.mainloop()
