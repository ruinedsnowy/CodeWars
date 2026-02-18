'''
def is_valid_walk(walk):
    if len(walk) == 10:
        k = n = s = e = w = 0
        if walk[-1] == 'n':
            n += 1
        elif walk[-1] == 's':
            s += 1
        elif walk[-1] == 'e':
            e += 1
        else:
            w += 1
        for i in range(len(walk)-1):
            if walk[i] != walk[i+1]:
                print(walk[i], walk[i+1])
                if walk[i] == 'n':
                    n+=1
                elif walk[i] == 's':
                    s+=1
                elif walk[i] == 'e':
                    e+=1
                elif walk[i] == 'w':
                    w+=1
            else:
                k = 1
        if (k == 0) and (n == s) and (e == w):
            print(n, s, e, w)
            return True
        else:
            print(n,s,e,w)
            return False
    else:
        return False

print(is_valid_walk( ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
'''

def is_valid_walk(walk):
    if len(walk) == 10:
        n = s = e = w = 0
        if walk[-1] == 'n':
            n += 1
        elif walk[-1] == 's':
            s += 1
        elif walk[-1] == 'e':
            e += 1
        else:
            w += 1
        for i in range(len(walk)-1):
            if walk[i] == 'n':
                n+=1
            elif walk[i] == 's':
                s+=1
            elif walk[i] == 'e':
                e+=1
            elif walk[i] == 'w':
                w+=1
        if (n == s) and (e == w):
            return True
        else:
            return False
    else:
        return False

print(is_valid_walk( ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))