# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon"]
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95]
        self.lista_tipo_pokemones = ["eléctrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psíquico", "agua"]


    def btn_cargar_pokedex_on_click(self):
        alert("carga","carga")
        
        for _ in range(10):

            nombre = prompt("pokemon", "Ingrese nombre del pokemon")
            while nombre == None or not nombre.isalpha():
                nombre = ("pokemon", "Error! Ingrese nuevamente el nombre de su pokemon")
            else: 
                self.lista_nombre_pokemones.append(nombre)    

            elemento = prompt("elemento", "Ingrese el elemento de su pokemon")
            while elemento == None or not elemento.isalpha() or elemento != "Electrico" and elemento != "Agua" and elemento != "Psiquio":
                elemento = prompt("elemento", "Error!, Ingrese el elemento nuevamente")
            else:
                self.lista_poder_pokemones.append(elemento)

            poder = prompt("poder", "Ingrese la cantidad de poder de su pokemon (50/200)")
            while poder == None or not elemento.isdigit() or int(poder) < 50 or int(poder) > 200:
                poder = prompt ("poder", "Error! Ingrese nuevamente el poder")
            else:
                poder = int(poder)
                self.lista_poder_pokemones.append(poder)       

    def btn_mostrar_informe_1(self):
        alert("1","1")
        #5
        contador_pokemones = 0
        contador_psiquio = 0
        elemento = self.lista_nombre_pokemones
        poder = self.lista_poder_pokemones

        for pokemones in self.lista_nombre_pokemones:
                print(f"pokemon: {pokemones}")
                print(f"posicion:{contador_pokemones}")
                contador_pokemones += 1

        if elemento == "Psiquio":
            if poder <=150:
                contador_psiquio += 1
        porcentaje_psiquio =  (contador_psiquio * 100) / contador_pokemones      

        print("Simulacro", porcentaje_psiquio)

    def btn_mostrar_informe_2(self):
        alert("2","2")
        #4
        contador_agua = 0
        elemento = self.lista_nombre_pokemones
        poder = self.lista_poder_pokemones
        contador_pokemones = 0

        for pokemones in self.lista_nombre_pokemones:
                print(f"pokemon: {pokemones}")
                print(f"posicion:{contador_pokemones}")
                contador_pokemones += 1

        if elemento == "Agua":
            if poder >= 100:
                contador_agua += 1
        porcentaje_agua = (contador_agua * 100) / contador_pokemones

        print("Simulacro", porcentaje_agua)

    def btn_mostrar_informe_3(self):
        alert("3","3")
        #6        
        contador_electrico = 0
        contador_agua = 0
        contador_psiquio = 0
        elemento = self.lista_nombre_pokemones
        mayor_pokemones = 0

        if elemento == "electrico":
            contador_electrico += 1
        if elemento == "agua":
            contador_agua += 1
        if elemento == "psiquio":
            contador_psiquio += 1  

        if contador_electrico > contador_agua and contador_electrico > contador_psiquio:
            mayor_pokemones = "El tipo de pokemones que mas hay es electrico"
        if contador_agua > contador_electrico and contador_agua > contador_psiquio:
            mayor_pokemones = "El tipo de pokemones que mas hay son de agua" 
        else:
            mayor_pokemones = "El tipo de pokemones que mas hay son de psiquio"  

        print("Simulacro", mayor_pokemones)         



if __name__ == "__main__":
    app = App()
    app.mainloop()