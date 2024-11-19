from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import math


class MainApp(App):
    def build(self):
        self.title = "Обчислення площі трикутника"

        # Основний контейнер
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Поля для вводу сторін
        self.side_a = TextInput(
            hint_text="Введіть сторону A",
            multiline=False,
            font_size=18,
            size_hint=(1, 0.15)
        )
        self.side_b = TextInput(
            hint_text="Введіть сторону B",
            multiline=False,
            font_size=18,
            size_hint=(1, 0.15)
        )
        self.side_c = TextInput(
            hint_text="Введіть сторону C",
            multiline=False,
            font_size=18,
            size_hint=(1, 0.15)
        )

        # Додавання полів до макету
        layout.add_widget(self.side_a)
        layout.add_widget(self.side_b)
        layout.add_widget(self.side_c)

        # Кнопка для обчислення площі
        calculate_btn = Button(
            text="Обчислити площу",
            font_size=18,
            size_hint=(1, 0.2)
        )
        calculate_btn.bind(on_press=self.calculate_triangle_area)
        layout.add_widget(calculate_btn)

        # Поле для відображення результату
        self.result_label = Label(
            text="",
            font_size=20,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.result_label)

        return layout

    def calculate_triangle_area(self, instance):
        try:
            # Зчитуємо значення сторін
            a = float(self.side_a.text.strip())
            b = float(self.side_b.text.strip())
            c = float(self.side_c.text.strip())

            # Перевіряємо умови існування трикутника
            if a + b > c and a + c > b and b + c > a:
                # Формула Герона
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                self.result_label.text = f"Площа трикутника: {area:.2f} кв. одиниць"
            else:
                self.result_label.text = "Трикутник не існує!"
        except ValueError:
            self.result_label.text = "Некоректний ввід. Введіть числові значення."


if __name__ == "__main__":
    app = MainApp()
    app.run()
