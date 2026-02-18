def first_non_repeating_letter(s):
    if len(s) > 1:
        s1 = list(s)
        s = list(s)
        d = {}
        a = []
        for i in range(len(s1)):
            s1[i] = s1[i].lower()
        for i in range(len(s1)):
            if s1[i] in d:
                d[s1[i]] += 1
            else:
                d[s1[i]] = 1
        su = 0
        for i in range(len(d)):
            if list(d.items())[i][1] > 1:
                pass
            else:
                su = 1
        if su == 0:
            return ''
        for i in range(len(s)):
            for l in range(len(d)):
                if ((list(d.items())[l][0] == s[i].lower()) and list(d.items())[l][1] == 1) or ((list(d.items())[l][0] == s[i].upper()) and list(d.items())[l][1] == 1):
                    a.append(list(d.items())[l][0])
        x = f"'{a[0]}'"
        print(a)
        if len(a) > 0:
            for i in range(len(s)):
                if (x.upper() == f"'{s[i]}'") or (x.lower == f"'{s[i]}'"):
                    return s[i]
                    break
            return a[0]
    elif len(s) == 1:
        return s
    else:
        return ''