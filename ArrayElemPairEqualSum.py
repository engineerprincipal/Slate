#!/usr/bin/env python
def FindMatchedArrayPairs(L1):
    s = set()
    MatchPairs = []
    L1_len = len(L1)
    for x in range(L1_len):
            for n in range(x, L1_len):
                    if (n+1 < L1_len) and (n < L1_len) :
                            i = L1[n+1] + L1[x]
                            if i not in s:
                                    s.add(i)
                            elif i in s:
                                    match = []
                                    match.append(L1[x])
                                    match.append(L1[n+1])
                                    MatchPairs.append(match)
                                    '''print( "* Matching * i in s L1[x] L1[n+1]", i, s, L1[x],  L1[n+1] )
                            print("i=", i, ",  x=", x, ",  n=", n )
                    print("match ", match)
                    print("MatchPairs ", MatchPairs)
                    print("s ", s, "\n")'''
    print("MatchPairs =", MatchPairs)
    s = set()
    match_len = len(MatchPairs)
    for x in range(match_len):
        s.add(sum(MatchPairs[x]))
    print("set of summation =", s)

    MatchPairs = []
    for x in range(L1_len):
        for n in range(x, L1_len):
                if (n+1 < L1_len) and (n < L1_len) :
                        i = L1[n+1] + L1[x]
                        if i in s:
                                match = []
                                match.append(L1[x])
                                match.append(L1[n+1])
                                MatchPairs.append(match)
    print("MatchPairs ", MatchPairs)


if __name__ == "__main__":
        '''a = [35, 4, 7, 3, 32, 9, 73, 5]'''
        '''a = [1,3,2,7,4]'''
        a = [1,2,3,4,5]
        a = [int(x) for x in input().split()]
        print("a =", a)
        FindMatchedArrayPairs(a)
