from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо у нижній регістр
    s = s.replace(" ", "").lower()
    # Створюємо двосторонню чергу
    queue = deque(s)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False