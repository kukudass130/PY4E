str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+1:]
# print(piece)
value = float(piece)    
#실수나 정수형으로 타입변환을 할 때 공백은 포함하지 않고 변환!
print(value+2.0)