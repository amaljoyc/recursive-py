def get_character_list(word):
    anagrams = list()
    for e in word:
        anagrams = get_anagrams(e, anagrams)
    print anagrams

def get_anagrams(e,old_anagrams):
    if len(old_anagrams) == 0:
        new_anagrams = [e]
    else:
        new_anagrams = list()
    for anagram in old_anagrams:
        temp_list = yet_another_fn(e,anagram)
        for element in temp_list:
            new_anagrams.append(element)
    return new_anagrams

def yet_another_fn(e,anagram):
    length = len(anagram)
    anagram = list(anagram)
    new_list = list()
    for x in range(length+1):
        x_list = list(anagram) 
        x_list.insert(x,e)
        new_list.append(''.join(x_list))
    return new_list


# The function bellow uses recursion to find the anagrams...
def recursive_fn(x,string,length):
    if len(x) == length:
        print x
        return
    else:    
        for y in string:
            s = ''.join(string.replace(y,''))
            recursive_fn(x+y,s,length)

if __name__ == '__main__':
    print 'Not Using Recursion....'
    get_character_list('abcd')


    print 'Using Recursion....'
    string = 'abcd'
    length = len(string)
    for x in string:
        s = ''.join(string.replace(x,''))
        recursive_fn(x,s,length)