f = open("sample.txt", "r")

text = f.read()

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)

f.close()