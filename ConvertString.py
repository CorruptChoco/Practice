def to_camel_case(text):
    string = '_'
    string2 = '-'
    delimiterLoc = []
    startIndex = 0
    for i in range(len(text)):
        a = text.find(string,startIndex)
        # print(a)
        if(a!=-1):
            startIndex = a + 1
            delimiterLoc.append(a)
    startIndex = 0
    for i in range(len(text)):
        b = text.find(string2,startIndex)
        # print(b)
        if(b!=-1):
            startIndex = b + 1
            delimiterLoc.append(b)
    delimiterLoc.sort()
    clearText = text.translate({ord(i): None for i in '_-'})
    # print(delimiterLoc)
    # print(clearText)
    count = 0
    clearList = list(clearText)
    # print(clearList)
    for loc in delimiterLoc:
        loc = loc - count
        clearList[loc] = clearList[loc].upper()
        count += 1
    finalText = ''.join(clearList)
    return finalText
    
#  Much better version
# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

print(to_camel_case('The-pippi_Was-kawaii'))