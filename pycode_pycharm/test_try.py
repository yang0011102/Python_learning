try:
    file=open('test111','r+')
except Exception as new:
    print('There is no file called','test111')
    Re=input('Do you want to create a new file? (Y/N)')
    if Re=='Y':
        file=open('test111','w')
    else:
        pass
else:
    file.write('test')
    print('finish')
    file.close()