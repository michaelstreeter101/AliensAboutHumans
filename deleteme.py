def shift4( w ):
    return w[3]+w[2]+w[0]+w[1]

def shift3( w ):
    return w[1]+w[2]+w[0]

def shift2( w ):
    return w[1]+w[0]

print( 'Type a sentence' )
string = input()  #string = 'This is a sentence.'
word=''
for char in string:
    word += char
    #print( char, end='' )
    if ord( char ) in (32, 46):
        terminator = char
        word = word[0:-1]
        if len( word ) <= 3:
            print( word, end='' )
            print( terminator, end='' )
            word = ''
            
        else: # len( word ) > 3
            first = word[0]
            mid = word[1:-1]
            last = word[-1:]

            print( first, end='' )
            # Scramble mid
            #print( mid, end='' )
            t = len( mid )
            #print( f'{t} = ', end='' )
            while t > 0:
                if t >=4:
                    dim = mid[t-4:t]
                    print( shift4( dim ), end='' )
                    t -= 4
                if t >=3:
                    dim = mid[t-3:t]
                    print( shift3( dim ), end='' )
                    t -= 3
                elif t >= 2:
                    dim = mid[t-2:t]
                    print( shift2( dim ), end='' )
                    t -= 2
                elif t >= 1:
                    print( mid[t-1:t], end='' )
                    t -= 1

            print( last, end='' )
            print(terminator, end='')
            word = ''
        
