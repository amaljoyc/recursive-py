def word_count():
    d = dict()
    with open('word_count.txt') as f:
        for line in f:
            for word in line.split():
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
    return d


if __name__ == '__main__':
    result = word_count()
    print result