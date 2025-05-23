import tkinter as tk
from director import Director
from point import Point
from personaje import Personaje

class MazeGUI:
    def __init__(self, master, laberinto_file):
        self.master = master
        self.laberinto_file = laberinto_file
        self.juego = None
        self.canvas = None
        self.ancho = 0
        self.alto = 0

        #carga de imagenes
        self.bicho_agresivo=tk.PhotoImage(file="images/agresivo.png")
        self.bicho_perezoso=tk.PhotoImage(file="images/perezoso.png")
        self.bomba_img = tk.PhotoImage(file="images/bomba.png")  
        self.bicho_caotico=tk.PhotoImage(file="images/caotico.png").subsample(2, 2)  # Reduce el tamaño de la imagen a la mitad
        self.personaje_img=tk.PhotoImage(file="images/personaje.png").subsample(3, 3)  


        self.load_laberinto()
        personaje=Personaje(self.juego,"Pepe",5)
        habitacion=self.juego.obtenerHabitacion(1)
        habitacion.entrar(personaje)
        self.juego.personaje=personaje
        self.init_ui()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        if not hasattr(self.juego, "personaje") or self.juego.personaje is None:
            personaje = Personaje(self.juego,"Pepe",5)
            habitacion = self.juego.laberinto.obtenerHabitacion(1)
            habitacion.entrar(personaje)
            self.juego.personaje = personaje

    def init_ui(self):
        self.master.title("Maze Game")
        self.canvas = tk.Canvas(self.master, width=1150, height=700, bg="white")
        self.canvas.pack(side=tk.BOTTOM)

        #botones de movimiento
        frame = tk.Frame(self.master)
        frame.pack(side=tk.TOP)
        tk.Button(frame, text="Norte", command=self.mover_norte).grid(row=0, column=1)
        tk.Button(frame, text="Oeste", command=self.mover_oeste).grid(row=1, column=0)
        tk.Button(frame, text="Este", command=self.mover_este).grid(row=1, column=2)
        tk.Button(frame, text="Sur", command=self.mover_sur).grid(row=2, column=1)

        self.calcularLaberinto()
        for habitacion in self.juego.laberinto.hijos:
            print("num-punto",habitacion.num,habitacion.forma.punto.x,habitacion.forma.punto.y)
        self.dibujarLaberinto()
       #self.draw_maze()
        self.draw_person()
        self.draw_bichos()

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()
    
    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self)

    def visitarHabitacion(self, hab):
        self.dibujarRectangulo(hab.forma)
    
    def mover_norte(self):
        self.mover_personaje("Norte")

    def mover_sur(self):
        self.mover_personaje("Sur") 

    def mover_oeste(self):
        self.mover_personaje("Oeste")

    def mover_este(self):
        self.mover_personaje("Este")  

    def mover_personaje(self, direccion):   
        personaje = self.juego.personaje
        habitacion_actual = personaje.posicion
        # Busca la puerta en la dirección dada
        elemento = habitacion_actual.obtenerElementoEnOrientacion(direccion)
        if elemento and hasattr(elemento, "habitaion_destino"):
            nueva_hab=elemento.habitaion_destino
            habitacion_actual.personaje=None
            nueva_hab.entrar(personaje)
            self.juego.personaje=personaje
        self.canvas.delete("all")
        self.dibujarLaberinto()
        self.draw_person()
        self.draw_bichos()
        

    def visitarPared(self, pared):
        pass
    def visitarPuerta(self, puerta):
        hab=puerta.lado1
        x = hab.forma.punto.x
        y = hab.forma.punto.y
        w = hab.forma.extent.x
        h = hab.forma.extent.y

        dx = puerta.lado2.forma.punto.x - x
        dy = puerta.lado2.forma.punto.y - y

        px, py = x + w // 2, y + h // 2
        if dx > 0:  # lado2 está a la derecha: puerta Este
            px, py = x + w, y + h // 2
        elif dx < 0:  # lado2 está a la izquierda: puerta Oeste
            px, py = x, y + h // 2
        elif dy > 0:  # lado2 está abajo: puerta Sur
            px, py = x + w // 2, y + h
        elif dy < 0:  # lado2 está arriba: puerta Norte
            px, py = x + w // 2, y
        from estado_puerta import Abierta
        color = "green" if isinstance(puerta.estadoPuerta, Abierta) else "red"
        self.canvas.create_rectangle(px-5, py-5, px+5, py+5, fill=color)



    def visitarBomba(self, bomba):
        # Suponiendo que bomba tiene un atributo 'forma' con punto y extent
        x = bomba.forma.punto.x + bomba.forma.extent.x // 2
        y = bomba.forma.punto.y + bomba.forma.extent.y // 2
        self.canvas.create_image(x, y, image=self.bomba_img)
        print("Imagen bomba cargada:")

    def visitarTunel(self, tunel):
        pass

    def dibujarRectangulo(self,forma):
        self.canvas.create_rectangle(forma.punto.x, forma.punto.y, forma.punto.x+forma.extent.x, forma.punto.y+forma.extent.y, fill="lightgray")
    
    def draw_person(self):
        for habitacion in self.juego.laberinto.hijos:
            if habitacion.personaje:
                x = habitacion.forma.punto.x + habitacion.forma.extent.x // 2 - 50
                y = habitacion.forma.punto.y + habitacion.forma.extent.y // 2 
                self.canvas.create_image(x, y, image=self.personaje_img)
                print("Imagen personaje cargada:", self.personaje_img)

   
    def draw_bichos(self):

        for habitacion in self.juego.laberinto.hijos:
         print("Habitacion:", habitacion.num);
         x = habitacion.forma.punto.x + habitacion.forma.extent.x // 2 + 50
         y = habitacion.forma.punto.y + habitacion.forma.extent.y // 2    
         for bicho in habitacion.bichos:
             modo = type(bicho.modo).__name__.lower()
             print(f"Dibujando bicho {bicho.modo} en ({x}, {y})")
             if "agresivo"  in modo:
                    self.canvas.create_image(x, y, image=self.bicho_agresivo)
                    print("Imagen agresivo cargada:", self.bicho_agresivo)
             elif  "perezoso" in modo:
                 self.canvas.create_image(x, y, image=self.bicho_perezoso)
             elif "caotico" in modo:
                 self.canvas.create_image(x, y, image=self.bicho_caotico)
             else:
                print("Tipo de bicho desconocido:", bicho.modo)
        pass

    def calcularPosicion(self):
        habitacion1 = self.juego.obtenerHabitacion(1)
        habitacion1.forma.punto = Point(0, 0)
        for habitacion in self.juego.laberinto.hijos:
            habitacion.calcularPosicion()
    
    def normalizar(self):
        min_x = 0
        min_y = 0

        # Buscar min_x y min_y
        for each in self.juego.laberinto.hijos:
            min_x = min(min_x, each.forma.punto.x)
            min_y = min(min_y, each.forma.punto.y)

        # Ajustar puntos
        for each in self.juego.laberinto.hijos:
            un_punto = each.forma.punto
            nuevo_x = un_punto.x + abs(min_x)
            nuevo_y = un_punto.y + abs(min_y)
            each.forma.punto = Point(nuevo_x, nuevo_y)  
    def calcularTamContenedor(self):
        max_x = 0
        max_y = 0

        for each in self.juego.laberinto.hijos:
            max_x = max(max_x, each.forma.punto.x)
            max_y = max(max_y, each.forma.punto.y)

        max_x += 1
        max_y += 1

        self.ancho = round(1050 / max_x)
        self.alto = round(600 / max_y)

    def asignarPuntosReales(self):
        origen_x, origen_y = 70, 10

        for each in self.juego.laberinto.hijos:
            x = origen_x + (each.forma.punto.x * self.ancho)
            y = origen_y + (each.forma.punto.y * self.alto)
            
            each.forma.punto = Point(x, y)  # Asumo que Punto(x, y) es una clase
            each.forma.extent = Point(self.ancho, self.alto)

            # Si quisieras incluir la recursión comentada:
            # for hijo in each.hijos:
            #     hijo.asignar_puntos_reales(each)

if __name__ == '__main__':
    root = tk.Tk()
    gui = MazeGUI(root, "./laberintos/lab4HabIzd4Bichos.json")  # Use a default laberinto file
    root.mainloop()