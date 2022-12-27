import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout



class Comp(BoxLayout):
    def __init__(self):
        super().__init__()
        self.result = None
        self.load_result()
    def mostrar_resultado(self):
        dr_Andre = "d1"
        dr_Adriano = "d2"
        dr_Edgar = "d3"
        valor = (self.ids.valor.text)
        if valor == "d1":
            self.result = "Dr Adriano"
            print("Dr Adriano")
            nome = "Dr Adriano"
        elif valor == "d2":
            self.result = "Dr Edgar"
            print("Dr Edgar")
            nome = "Dr Edgar"
        elif valor == "d3":
            self.result = "Dr Andre"
            print("Dr Andre")
            nome = "Dr Andre"
        else:
            self.result = "Você digitou errado"
        self.clear_input()
        self.save_result()
        
    def clear_input(self):
        self.ids.valor.text = self.result

    def save_result(self):
        with open("result.json", "w") as f:
            json.dump(self.result, f)

    def load_result(self):
        try:
            with open("result.json", "r") as f:
                self.result = json.load(f)
        except FileNotFoundError:
            self.result = None


class tela(App):
    def build(self):
        return Comp()


tela().run()



