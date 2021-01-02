#x = 'enter'
#print(type(x))
#print(dir(x))

text = 'X-DSPAM-Confidence:     0.8475'
#find the number place of 0.8475
ftext = text.find(':')
#print(ftext)
#converting to float and string slicing 0.8475
print(float(text[ftext+1:]))

