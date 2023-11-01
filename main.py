import keyword
import tkinter as tk
from tkinter import messagebox
import random



class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")
        self.master.configure(bg="lightblue")
        self.master.geometry('700x800')
        self.master.resizable(width=False, height=False)
        self.target_number = None
        self.max_number = 20  # Максимальное значение по умолчанию
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Выберите уровень сложности:",bg="lightblue")
        self.label.pack(pady=10)

        # Создаем кнопки для выбора уровня сложности
        self.easy_button = tk.Button(self.master, text="Легкий", command=lambda: self.set_difficulty(4),bg="#e1f1fd")
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self.master, text="Средний", command=lambda: self.set_difficulty(6),bg="#e1f1fd")
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self.master, text="Сложный", command=lambda: self.set_difficulty(7),bg="#e1f1fd")
        self.hard_button.pack(pady=10)

        self.quit_button = tk.Button(self.master, text="Выйти", command=self.master.quit, bg="#e1f1fd")
        self.quit_button.pack(pady=10)

    def set_difficulty(self, attempts):
        self.attempts = attempts
        if attempts == 7:
            self.max_number = 100
        elif attempts == 6:
            self.max_number = 50
        elif attempts == 5:
            self.max_number = 20
        #self.max_number = attempts * 10
        self.target_number = random.randint(1, self.max_number)
        messagebox.showinfo("Новая игра", f"Выбран уровень сложности: {attempts} попыток. Начнем игру!")
        # После выбора уровня сложности, запускаем игру
        self.play_game()

    def play_game(self):
        self.master.focus_force()
        #self.reset_game()  # Сбросить игру при начале новой игры
        self.label.config(text="Угадайте число от 1 до " + str(self.max_number))

        # Создаем новые кнопки для выбора числа
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.quit_button.pack_forget()
        self.buttons = []
        button_size = 50  # Размер кнопки
        rows = 5  # Количество строк
        cols = self.max_number // rows  # Количество столбцов

        # Рассчитываем размер матрицы кнопок
        matrix_width = cols * button_size
        matrix_height = rows * button_size

        # Рассчитываем смещение для центрирования
        x_offset = (700 - matrix_width) // 2
        y_offset = (700 - matrix_height) // 2

        for i in range(rows):
            for j in range(cols):
                x = x_offset + j * button_size
                y = y_offset + i * button_size
                num = i * cols + j + 1
                if num <= self.max_number:
                    button = tk.Button(self.master, text=str(num), width=4, height=2,
                                       command=lambda num=num: self.check_number(num), bg="#e1f1fd")
                    button.place(x=x, y=y)
                    self.buttons.append(button)

        #self.quit_button['state'] = 'active'

    def remove_buttons(self):
        for button in self.buttons:
            button.destroy()

    def remove_main_buttons(self):
        for button in self.easy_button:
            button.destroy()
        for button in self.medium_button:
            button.destroy()
        for button in self.hard_button:
            button.destroy()

    def check_number(self, guessed_number):
        if self.target_number is None:
            messagebox.showinfo("Ошибка", "Выберите уровень сложности перед началом игры.")
            return

        self.attempts -= 1

        if self.attempts == 0:
            messagebox.showinfo("Результат", "Игра окончена. Попытки исчерпаны.")
            self.remove_buttons()
            self.remove_buttons2()
            self.reset_game()
            return

       # self.attempts -= 1

        if guessed_number < self.target_number:
            messagebox.showinfo("Результат", "Больше! Осталось попыток: " + str(self.attempts))
            self.disable_buttons(guessed_number, "less")
        elif guessed_number > self.target_number:
            messagebox.showinfo("Результат", "Меньше! Осталось попыток: " + str(self.attempts))
            self.disable_buttons(guessed_number, "greater")
        else:
            messagebox.showinfo("Результат", "Вы угадали число!")
            #self.disable_buttons()
            self.remove_buttons()
            self.remove_buttons2()
            self.reset_game()

    def disable_buttons(self, guessed_number=None, direction=None):
        self.master.focus_force()
        for i in range(1, self.max_number + 1):
            if guessed_number:
                if direction == "less" and i <= guessed_number:
                    self.buttons[i - 1]['state'] = 'disabled'
                elif direction == "greater" and i >= guessed_number:
                    self.buttons[i - 1]['state'] = 'disabled'
            else:
                self.buttons[i - 1]['state'] = 'disabled'


    def reset_game(self):
        self.target_number = None
        self.easy_button.pack(pady=5)
        self.medium_button.pack(pady=5)
        self.hard_button.pack(pady=5)
        self.quit_button.pack(pady=5)
        self.master.update()
        self.label.config(text="Выберите уровень сложности:")
        #simulate_click()

    def remove_buttons2(self):
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.quit_button.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

