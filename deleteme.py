# Author: MWS
# Date: 2020-12-09
# Purpose: takes text typed in and converts it according to rules
# "couldnt believe that I could actually understand what I was reading" becomes
# "cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg" (or similar!)
#
def shift4( w ):
    # takes 4 letters and returns 4 letters scrambled. e.g. nder begomes rend
    return w[3]+w[2]+w[0]+w[1]

def shift3( w ):
    # takes 3 letters and returns 3 letters scrambled. e.g. oul becomes ulo
    return w[1]+w[2]+w[0]

def shift2( w ):
    # takes 2 letters and returns 2 letters swapped. e.g. ha becomes ah
    return w[1]+w[0]

# Main function
print( 'Type a sentence' )
string = input()  #string = 'This is a sentence.'

# work through the sentence, character by character, 
# whenever you get to a word boundary (' ' or '.'),
# output the first letter, scrambled innards, last letter, boundary character.
# Rinse and repeat until you get to the end of the line.

word=''
for char in string:
    word += char # add the next character to the word

    if ord( char ) in (32, 46): # if it's ' ' or '.' print the word
        terminator = char
        word = word[0:-1] # strip the terminator character off the word
        if len( word ) <= 3:
            print( word, end='' ) # short words (I, am, the) go through unprocessed.
            print( terminator, end='' )
            word = ''
            
        else: # len( word ) > 3
            first = word[0] # first letter (has to remain in the same place)
            mid = word[1:-1] # middle part of the word (will get scrambled)
            last = word[-1:] # last letter (has to remain in the same place)

            print( first, end='' )
            # Scramble mid
            t = len( mid )
            #print( f'{t} = ', end='' )
            while t > 0:
                if t >=4:
                    dim = mid[t-4:t] # 'dim' is 'mid' rearranged
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
        
# Follow Aliens About Humans, @HumansExplained
