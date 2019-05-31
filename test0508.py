import time;
def rf(url):
    webinfo={}
    file_webinfo = open(url, 'r', encoding='utf-8');
    for line in file_webinfo:
        result = line.split('=')
        print(result)
        # print(type(dict(result)))
        # webinfo.update(dict([result]))
        webinfo[result[0]] = result[1]
    return webinfo;

def getUserInfo(url):
    userinfo = []
    file_userinfo = open(url, 'r' ,encoding='utf-8')
    for line in file_userinfo:
        res = [ele.split('=')  for ele in line.split('  ')]
        result = dict(res);
        userinfo.append(result)
    return userinfo



if __name__ == '__main__':
    # webinfo = rf('./webinfo.txt');
    # print(webinfo)
    # print(type(webinfo))

    userinfo = getUserInfo('./userinfo.txt')
    print(userinfo)

