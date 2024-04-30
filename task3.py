from queue import LifoQueue

def is_balanced(expression):
    stack = LifoQueue()
    pairs = {')': '(', '}': '{', ']': '['}
    opening = pairs.values()
    closing = pairs.keys()
    for char in expression:
        if char in opening:
            stack.put(char)
        elif char in closing:
            if stack.empty():
                return False
            if pairs[char] != stack.get():
                return False
    return stack.empty()

print(is_balanced("( ) { [ ] ( ) ( ) { } }"))  # True
print(is_balanced("( ( ( ) )"))  # False
print(is_balanced("( { [ ) ] }"))  # False