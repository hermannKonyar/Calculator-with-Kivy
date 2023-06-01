from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1, 0.5, 0, 1)  # sets the background color of the app to orange

class RoundButton(Button):
    pass

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        root_widget = BoxLayout(orientation="vertical")

        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        root_widget.add_widget(self.solution)

        main_layout = GridLayout(cols=4, rows=5, padding=20, spacing=5)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "C", "+",
        ]

        for button in buttons:
            btn = RoundButton(text=button)
            btn.bind(on_release=self.on_button_press)
            main_layout.add_widget(btn)

        equals_button = RoundButton(text="=")
        equals_button.bind(on_release=self.on_solution)
        main_layout.add_widget(equals_button)

        root_widget.add_widget(main_layout)

        return root_widget

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
