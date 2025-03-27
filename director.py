import json

class Director:
    def __init__(self):
        self.builder = None
        self.dict = {}
    
    def get_builder(self):
        return self.builder
    
    def set_builder(self, builder):
        self.builder = builder
    
    def get_dict(self):
        return self.dict
    
    def set_dict(self, dictionary):
        self.dict = dictionary
    
    def fabricar_bichos(self):
        bichos = self.dict.get('bichos', None)
        if bichos is None:
            return
        for each in bichos:
            self.builder.fabricar_bicho_modo(each['modo'], each['posicion'])
    
    def fabricar_juego(self):
        self.builder.fabricar_juego()
    
    def fabricar_laberinto(self):
        self.builder.fabricar_laberinto()
        
        for each in self.dict.get('laberinto', []):
            self.fabricar_laberinto_recursivo(each, 'root')
        
        for each in self.dict.get('puertas', []):
            self.builder.fabricar_puerta(each[0], each[1], each[2], each[3])
    
    def fabricar_laberinto_recursivo(self, un_dic, padre):
        contenedor = None
        
        if un_dic['tipo'] == 'habitacion':
            contenedor = self.builder.fabricar_habitacion(un_dic['num'])
        elif un_dic['tipo'] == 'armario':
            contenedor = self.builder.fabricar_armario(un_dic['num'], padre)
        
        if un_dic['tipo'] == 'bomba':
            self.builder.fabricar_bomba_en(padre)
        elif un_dic['tipo'] == 'tunel':
            self.builder.fabricar_tunel_en(padre)
        
        for each in un_dic.get('hijos', []):
            self.fabricar_laberinto_recursivo(each, contenedor)
    
    def ini_builder(self):
        forma = self.dict.get('forma')
        if forma == 'cuadrado':
            self.builder = LaberintoBuilder()
        elif forma == 'rombo':
            self.builder = LaberintoBuilderRombo()
    
    def leer_archivo(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as file:
            self.dict = json.load(file)
    
    def obtener_juego(self):
        return self.builder.obtener_juego()
    
    def procesar(self, archivo):
        self.leer_archivo(archivo)
        self.ini_builder()
        self.fabricar_laberinto()
        self.fabricar_juego()
        self.fabricar_bichos()
