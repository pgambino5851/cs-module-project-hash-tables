
import string
import re

def word_count(s):
    # Your code here
    cache = {}
    s = s.lower()
    transMap = (str.maketrans('', '', '[:;,."-+=/\\|[]{}()*^&]'))
    s = s.translate(transMap)

    

    print(s)
    strings = s.split()
    for i in range(0, len(strings)):
        
        if strings[i] not in cache and strings[i] is not None:
            
            cache[strings[i]] = 1
        else:
            cache[strings[i]] = cache[strings[i]] + 1

    return cache
#


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))