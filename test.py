def wfile():
    try:
        filename = './test.txt'
    except IOError:
        print('file create error')
    else:
        fp = open(filename,'wb')
        fp.write("test1\n".encode('utf-8'))
        fp.write('test2\n'.encode('utf-8'))
        fp.write('test3'.encode('utf-8'))
        fp.close()

def rfile():
    try:
        filename = './test.txt';
        fp = open(filename,'r')

    except IOError:
        print('file open error')
    else:
        for f in fp:
            print('file data is:'+f+"\n")
        fp.close()



if __name__ == '__main__':
    wfile()
    rfile()
    print('Done!')
