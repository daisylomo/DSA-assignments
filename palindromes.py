import re

def Palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    stack = []
    queue = []

    # Push/enqueue each character in cleaned string
    for ch in cleaned:
        stack.append(ch)
        queue.append(ch)

    # Compare characters from stack and queue
    while len(stack) > 0:
        if stack.pop() != queue.pop(0):
            return False
    return True


s = input("Enter a word:").strip()
if Palindrome(s):
        print(f"The word, {s}, is a palindrome.")
else:
        print(f"The word, {s}, is not a palindrome.")
