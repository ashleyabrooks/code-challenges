"""Parse an unbroken sentence into possible words.

Example:

    >>> sentences = parse('iatenoodlesfordinnertonight', vocab)

    >>> for s in sorted(sentences):
    ...    print s
    i a ten oodles for dinner to night
    i a ten oodles for dinner tonight
    i a ten oodles ford inner to night
    i a ten oodles ford inner tonight
    i ate noodles for dinner to night
    i ate noodles for dinner tonight
    i ate noodles ford inner to night
    i ate noodles ford inner tonight

"""

vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night',
         'ate', 'noodles', 'for', 'dinner', 'tonight'}


def parse(phrase, vocab=vocab):
    """Break a string into words.

    Input:
        - string of words without space breaks
        - vocabulary (set of allowed words)

    Output:
        set of all possible ways to break this down, given a vocab    
    """

    results = set()

    # base case: entire phrase is a word
    if phrase in vocab:
        results.add(phrase)

    # general case: look at substrings starting at first letter
    for i in range(len(phrase)):
        word = phrase[:i]
        if word in vocab:
            sub_results = parse(phrase[i:])
            for sub_result in sub_results:
                results.add(word + ' ' + sub_result)

    return results

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED ***\n"
