#读写示范，保存在本文件根目录
file='Line first.\nline second.'

test=open('test.txt','w')
test.write(file)
test.close()
