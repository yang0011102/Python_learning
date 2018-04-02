#读写示范，保存在本文件根目录
newfile='\nLine third.\nline forth.'

test=open('test.txt','a')
test.write(newfile)
test.close()
