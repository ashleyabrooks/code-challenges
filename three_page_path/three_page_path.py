def get_three_page_path():
    """Input file with user id, page id, and time stamp. 
    Return most common three page path pattern and count of 
    how many times the most common pattern occurred.

    >>> get_three_page_path()
    7 [('P5', 'P2', 'P4'), ('P12', 'P9', 'P6'), ('P4', 'P14', 'P10')]

    """
    
    f = open('input2.txt', 'r')

    users_and_pages = {}

    for line in f:
        time_stamp, user, page = line.rstrip().split(', ')
        
        if user in users_and_pages:
            users_and_pages[user].append(page)
        else:
            users_and_pages[user] = [page]

    patterns = {} # {[pages]: count}

    for user in users_and_pages:
        pages = users_and_pages[user]
        
        while len(pages) >= 3:
            pattern = tuple(pages[0:3])
            
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1

            pages.pop(0) # slows runtime down to O(n^2) because of pop(0)

    max_count = 0
    common_pattern = []

    for pattern in patterns:
        if patterns[pattern] > max_count:
            max_count = patterns[pattern]
            common_pattern = [pattern]
        elif patterns[pattern] == max_count:
            common_pattern.append(pattern)

    print max_count, common_pattern


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TEST PASSED. ***\n"