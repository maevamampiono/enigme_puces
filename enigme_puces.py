import PySimpleGUI as sg


# CONSTANTES

GAME_TITLE = "Jeu des puces"
SUCCESS_TITLE = "Bravo !"
FAIL_TITLE = "Oups..."


# CLASSES

class View:
    def __init__(self, positionA, positionB):
        layout = [
            [sg.Text(f"La puce A se situe à la case {positionA} et la puce B à la case {positionB}. À chaque seconde, la puce A se \ndéplace de 3 cases dans le sens des aiguilles d'une montre et la puce B se déplace de 2 \ncases dans le sens contraire. Au bout de combien de secondes les deux puces se \nposeront-elles en en même temps sur la même case ?", auto_size_text=True)],
            [sg.Image('enigme1img.png',expand_x=True, expand_y=True)],
            [sg.Text('Réponse : ', auto_size_text=True), sg.Input(size=(30, 1),key='_ANSWER_')],
            [sg.HorizontalSeparator()],
            [sg.Button('Valider', key = '_OK_'), sg.Button('Quitter', key= '_QUIT_')]
        ]
        self.window = sg.Window(GAME_TITLE, layout)

    def read(self):
        return self.window.read()
    
    def close(self):
        self.window.close()

    def update(self, key, value):
        self.window[key].update(value)
        

class Game:
    def __init__(self, positionA, positionB):
        self.view = View(positionA, positionB)
        self.positionA = positionA
        self.positionB = positionB
        self.time = 0
        self.end = False

    def start(self):
        pass

    def stop(self):
        self.end = True

    def quit(self):
        self.view.close()

    def say(self, title, msg):
        sg.popup(msg, title=title)

    def clear_answer(self):
        self.view.update('_ANSWER_', "")

    def correction(self):
        while self.positionA != self.positionB :
            self.positionA=(self.positionA+3)%17 #Sens de l'aiguille d'une montre
            self.positionB=self.positionB-2 #Sens inverse de l'aiguille d'une montre
            if self.positionB <= 0:
                self.positionB=17+self.positionB
            self.time+=1
        
        return self.time


    def loop(self):
        while not self.end:
            event, values = self.view.read()
            if event == '_QUIT_' or event == sg.WIN_CLOSED:
                self.stop()
            if event == '_OK_':
                answer = int(values['_ANSWER_'])
                if self.correction() == answer:
                    self.say(SUCCESS_TITLE, "T'as trouvé la bonne réponse")
                    self.stop()
                else:
                    self.say(FAIL_TITLE, "Désolé ce n'est pas ça")
                    self.clear_answer()
        self.quit()

test = Game(1,15)
test.loop()