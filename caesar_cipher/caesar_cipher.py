import nltk
nltk.download('words')
original_words_list = nltk.corpus.words.words()
words_list = [word.lower() for word in original_words_list]


def encrypt(string, key):
    
    output = ''
    for letter in string:
        
        if ord(letter)>64 and ord(letter)<91:
            x = ord(letter) - 65
            new = x+key
            new = new%26 + 65
            output+=chr(new)            
        
        elif ord(letter)>96 and ord(letter)<123:
            x = ord(letter) - 97
            new = x+key
            new = new%26 + 97
            output+=chr(new)

        elif letter == ' ':
            output += letter


    return output



def decrypt(string, key):
    return encrypt(string, -key)

def crack(string):
    pass

if __name__=="__main__":
    # string= "Whvw hqfubsw"
    # key= 3
    # print(encrypt(string, key))
    # print(decrypt(string, key))

    print(encrypt('  #$@#$@#$ TT !@#!@#%^^&%^&',2))
    # print(decrypt("   VV ", 2))
