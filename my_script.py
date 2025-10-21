# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed:", reverse_string(text))
