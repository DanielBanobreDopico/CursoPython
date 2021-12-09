from uuid import uuid4

class Character:
    '''
    Clase general para la construcción de los personajes del juego.

        Atributos:
            id - UUID4 para la identificación de las diferentes instancias.

        Métodos:
            move - Hace una llamada al método mode de playground indicándole un desplazamiento para este personaje.
            up, down, left, right - Métodos de conveniencia para asociar a los callback. Llaman a move con los parámetros adecuados. 
    '''
    def __init__(self, playground, keyboard, callbacks):
        '''
        Instancia un personaje proporcionandole un tablero e insertando sus callbacks en el controlador de teclado.

            Parametros:
                playground - Instancia de Playground
                keyboard - Instancia de Keyboard
                callbacks - Lista de tuplas con dos strings indicando el keycode segun pynput y el método de la instancia.
            
            Ejemplo:
                callbacks = [
                    ("up","up"),
                    ("right","right"),
                    ("down","down"),
                    ("left","left"),
                ]
                character = Character(playground, keyboard, callbacks)
        '''
        self.id = str(uuid4())
        self.playground = playground
        self.playground.addCharacter(self)
        true_callbacks = [ (keymap, getattr(self, callback)) for keymap, callback in callbacks ]
        keyboard.add_callbacks(true_callbacks)
    def __repr__(self):
        return " 🚶 "
    def __str__(self):
        return self.__repr__()
    def move(self,x,y):
        '''
        Llama al método move de playground indicando un desplazamiento en los ejes x e y.

            Parámetros:
                x, y - Entero positivo o negativo representando desplazamiento en uno y otro eje.
        '''
        self.playground.move(self,x,y)
    def up(self, key, event):
        '''Facilita un callback para llamar a self.move para el desplazamiento arriba.'''
        if event == "press": self.move(0,1)
    def right(self, key, event):
        '''Facilita un callback para llamar a self.move para el desplazamiento a la derecha.'''
        if event == "press": self.move(1,0)
    def down(self, key, event):
        '''Facilita un callback para llamar a self.move para el desplazamiento abajo.'''
        if event == "press": self.move(0,-1)
    def left(self, key, event):
        '''Facilita un callback para llamar a self.move para el desplazamiento a la izquierda.'''
        if event == "press": self.move(-1,0)