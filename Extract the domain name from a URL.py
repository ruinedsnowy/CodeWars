
#url = "http://www.codewars.com/kata/" + 's'
url = "http://google.com"

def domain_name(url):
    ind = 0
    x = 0
    a = []
    if len(url) > 0:
        for i in range(len(url)-1, 0, -1):
            if url[i] == '/' and url[i+1] != '/':
                ind = i
        if ind != 0:
            url = url[:len(url)-ind]
            url = url[:-1]
        for i in range(len(url)-1, 0, -1):
            if url[i] != '.':
                x+=1
            else:
                break
        url = url[:len(url)-x-1]
        for i in range(len(url)-1, 0, -1):
            if url[i] != '.':
                a.append(url[i])
            else:
                break
        url = url[:len(url)-x-1]
        a.reverse()
        x = ''.join(a)

    return x
print(domain_name(url))
