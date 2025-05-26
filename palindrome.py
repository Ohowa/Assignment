from collections import deque
import re

def is_palindrome(s):
    # Normalize: remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    stack = []
    queue = deque()

    for char in s:
        stack.append(char)
        queue.append(char)

    for _ in range(len(s) // 2):
        if stack.pop() != queue.popleft():
            return False

    return True
