from collections import deque

def is_palindrome(s):
    stack = []
    queue = deque()

    for char in s:
        stack.append(char)
        queue.append(char)

    for _ in range(len(s) // 2):
        if stack.pop() != queue.popleft():
            return False

    return True


s = input("Enter a word: ")

if is_palindrome(s):
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
