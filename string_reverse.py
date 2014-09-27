def reverse(s, l):
    if l == 0:
        return s
    else:
        print s[l-1]
        return reverse(s, l-1)

if __name__ == '__main__':
    reverse('amal', len('amal'))