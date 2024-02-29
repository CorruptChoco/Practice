# didn't work because it didn't work when there were multiple spaces

# def reverse_words(text):
#     sText = text.split()
#     listText = [list(string)[::-1] for string in sText]
#     for item in listText[:-1]:
#         item.append(' ')
#     flatList = [item for sublist in listText for item in sublist]
#     return ''.join(flatList)


# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    tempText = []
    fullText = []
    for char in text:
        if char != ' ':
            tempText.append(char)
        elif char == ' ':
            tempText = tempText[::-1]
            fullText.extend(tempText)
            fullText.append(char)
            tempText = []
    tempText = tempText[::-1]
    fullText.extend(tempText)
    return ''.join(fullText)

text = ''
print(reverse_words(text))


# better version for the solutions page

# def reverse_words(text):
#   return ' '.join([ word[::-1] for word in text.split(' ')])