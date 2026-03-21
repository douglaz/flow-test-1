try:
    line = input()
except EOFError:
    line = ""
print(line[::-1])
