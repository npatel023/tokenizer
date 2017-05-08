"Neil Patel"
"Texas Tech Computer Science"
"Parts of this code were taken from Nelson Rushton and were adapted to the Tokenizer program"

def whiteChar(c): return (c in " \r\n\t")

specialtoken = ["*", "+", "-", "^",
                "|", "~", ".", ",", "{", "}", "(",
                ")", "]", "[", "/", "\\"]

def tokenize(s):
    i=0
    token = []

    while i < len(s):
        if whiteChar(s[i]):
            i=i+1
        elif i < len(s)-1 and s[i:i+2] == "//":
            i=i+2
            while(i<len(s) and s[i] not in "\r\n"):
                i = i+1
        else:
            tok = munch(s,i)
            token.append(tok)
            i=i+len(tok)
    return token

def munch(s,i):
    A,j = 'em',i
    count = 0
    while True:
        if j == len(s): break
        count = count + 1
        
        A = StateChange(A,j, s, i,count)
        
        #print("A:" ,A)
        
        if A == 'err': break
        j = j+1                     #increment to next spot in string

    #print("s[i:j]", s[i:j])
    return s[i:j]

specialToken = ["<",">","="]
less_equal = ["<="]
greater_equal = [">="]
spaceship = ["<=>"]
Period = [".."]

def StateChange(A,i,s,j,count):
    a = []
    if A == 'em':
       
        if s[i].isalpha(): return 'identifier'
        if s[i].isdigit(): return 'numeral'
        if (s[i] == "'"): return 'quote'
        if (s[i:i+3] in spaceship):  return 'spaceship'
        if (s[i:i+2] in less_equal): return 'lessequal'
        if (s[i:i+2] in greater_equal): return 'greaterequal'
        if (s[i] in specialToken): return 'special'
        if (s[i] == "."): return 'periods'
        if (s[i] in specialtoken): return 'spec'
        if(c == "("): return 'block'

    
    elif A == 'identifier':                             #Identifier
        if(s[i].isalpha()): return 'identifier'
    elif A == 'numeral':                                 #Numeral
        if(s[i].isdigit()): return 'numeral'
        if(s[i] == "."): return 'decfraction'
    elif A == 'quote':                                          #QuotedString
        if(s[i] == "\\"): return 'slash'
        if(s[i] == "'"): return 'endquote'
        return 'quote'
    elif A == 'slash':
        if(s[i] == "\\"): return 'backslash_quote'
        return 'quote'
    elif A == 'backslash_quote':
        if(s[i] == "'"): return 'quote'
        return 'slash'
    elif A == 'block':                                          #RepeatingBlock
        while(i<len(s)):
            if(s[i] == "("): return 'block'
            if(s[i].isdigit()): return 'block'
            if(s[i] in "."): return 'block'
            if(s[i] == ")"): return 'endblock'
    elif A == 'decfraction':                                    #Decimal fraction
        if(s[i].isdigit()): return 'decfraction'
        while(i<len(s)):
            if(s[i] == "("): return 'decfraction'
            if(s[i].isdigit()): return 'decfraction'
            if(s[i] in "."): return 'decfraction'
            if(s[i] == ")"): return 'enddecfraction'
            else: break
        return 'err'
    elif A == 'spaceship':                                      #<=>
        if(count == 4):
            return 'err'
        if(s[i] == '='): return 'spaceship'
        if(s[i] == '>'): return 'spaceship'
    elif A == 'lessequal':                                      #<=
        if(s[i-1:i+1] == '<='): return 'lessequal'
    elif A == 'greaterequal':                                   #>=
        if(s[i-1:i+1] == '>='): return 'greaterequal'
    elif A == 'periods':                                        #..
        if(s[i-1:i+1] == ".."): return 'end'
        else: return 'decfraction'
    return 'err'


                  
