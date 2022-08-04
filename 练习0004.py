file = open("01.txt","rt")

text= file.read()

words = text.split()

print(words)

print("单词个数:",len(words))