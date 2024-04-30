from queue import Queue
import time

# Створення черги 
queue = Queue()

# Генерація заявок
def generate_request():
    # Унікальний номер заявки
    request = "Request-" + str(time.time())
    queue.put(request)
    print(f"Заявка {request} додана до черги")

# Обробка заявок
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request} оброблена")
    else:
        print("Черга порожня")

# Цикл програми
while True:
    choice = input("Додати нову заявку (1) або обробити заявку (2)? Вихід (exit): ")
    if choice.lower() == "exit":
        break
    elif choice == "1":
        generate_request()
    elif choice == "2":
        process_request()
    else:
        print("Невірний ввід. Спробуйте ще раз.")