print('Input numbers. If you want to stop, input \'done\'')
total = 0
value = None
count = 0

while value != 'done':
    value = input('Enter a number: ')
    try:
        num = int(value)
    except:
        print('Invalid input')
        num = 0
    total = total + num
    if num != 0:
        count = count+1

print(total, count, total/count)