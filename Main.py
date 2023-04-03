#creates an histogram of a string
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
            
    #change value to probability
    for c in d:
        d[c] = str(d[c]) + '/' + str(len(d))
        
    return d

if __name__ == '__main__':
    d = []; k=0
    d.append('nigeria')
    d += ['absolutely']
    d += ['diamond']
    d += ['atmosphere']

    r = random.randint(0, 3)
    for t in d:
        if k == r:
            print('\n')
            print(t)
            ans = histogram(t)
        k += 1
        
    for a in ans:
        print(a, ans[a])
