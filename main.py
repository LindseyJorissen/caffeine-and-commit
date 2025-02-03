from kivy.app import App

class CalculatorApp(App):
    def build(self):
        return self.root

    def on_button_press(self, instance):
        result = self.root.ids.result  #input
        text = instance.text

        if text == "C":
            result.text = ""  #clear if c is pressed
        elif text == "=":
            try:
                result.text = str(eval(result.text))  # calculate
            except:
                result.text = "Error"
        else:
            result.text += text

if __name__ == "__main__":
    CalculatorApp().run()
