import os

def calculator():
    expression = ""
    while True:
        os.system('clear')
        print("=== JARVIS CALCULATOR ===")
        print(f" Дисплей: [ {expression if expression else '0'} ]")
        print("=========================")
        print("Введите число/операцию (+, -, *, /), '=' для расчета, 'C' для сброса, 'q' для выхода:")
        
        user_input = input("> ").strip()
        
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'c':
            expression = ""
        elif user_input == '=':
            try:
                expression = str(eval(expression))
            except Exception:
                expression = "Ошибка"
        else:
        
            expression += user_input

if __name__ == "__main__":
    calculator()
