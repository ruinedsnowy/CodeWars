'''
def to_jaden_case(string):
    string = string.split(' ')
    ans = ''
    for i in range(len(string)):
        string[i] = string[i][0].upper() + string[i][1:]

        ans = ans + ' ' + string[i]
    print(ans[1:])
    return ans
'''



def to_jaden_case(string):
    if len(string) == 0:
        return None
    else:
        string = string.split(' ')
        ans = ''
        for i in range(len(string)):
            word = ''
            for x in string[i]:
                word = word + x.lower()
            string[i] = word[0].upper() + word[1:]
            ans = ans + string[i] + ' '
        ans = ans[:-1]
        return ans

to_jaden_case('bx ngRh jkVps fBm aBn GqB Vy YVgMPpo dPP wWzg YLOfrEHiqO F SuXelngeSt z kQSzDiP nNQG FE guo lw LtMGVsvn dOU C IoHHFuUmN TGESsKe aLKRVHGuf Cuf sqUZ vhdqllkhx MEYRHpJiyC Y GORIk RIF Sk DOpIhw AoFauG Z IPS HKjuBxaNQs CFOdyxXGv ZQwFHCBEC tQSxIu IMnpI CPqnFb HsIOTIa ql oJkihDWByi pKwsd ARGXDaMZZ X xkddN IItAUeeFh KU G lcjTWg XuXhQ PfhSg gy eIgjVzmL JuckMIdm NCvk eVu yAZqPmh S IyCC x rDaRnV t QXtUSygqMW NirLx wzZXCnR RrX IAnEV CHs xqxPRCsw daq HjJBpFVJd B xg WBseFsHncp N TSE')


'''
def to_jaden_case(string):
    string = string.split(' ')
    ans = ''
    print(string)
    for i in range(len(string)):
        k = 1
        word = ''
        print(string[i])
        for x in range(len(string[i:+1])):
            print(string(i[x]))
            #word = word + .lower()
            print(string(x[k]))
            k+=1
        string[i] = string[i][0].upper() + word
        print(k)
        #print(string[i])
    return ans

to_jaden_case('bx ngRh jkVps fBm aBn GqB Vy YVgMPpo dPP wWzg YLOfrEHiqO F SuXelngeSt z kQSzDiP nNQG FE guo lw LtMGVsvn dOU C IoHHFuUmN TGESsKe aLKRVHGuf Cuf sqUZ vhdqllkhx MEYRHpJiyC Y GORIk RIF Sk DOpIhw AoFauG Z IPS HKjuBxaNQs CFOdyxXGv ZQwFHCBEC tQSxIu IMnpI CPqnFb HsIOTIa ql oJkihDWByi pKwsd ARGXDaMZZ X xkddN IItAUeeFh KU G lcjTWg XuXhQ PfhSg gy eIgjVzmL JuckMIdm NCvk eVu yAZqPmh S IyCC x rDaRnV t QXtUSygqMW NirLx wzZXCnR RrX IAnEV CHs xqxPRCsw daq HjJBpFVJd B xg WBseFsHncp N TSE')
'''