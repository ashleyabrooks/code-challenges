"""Codefights challenge against Asana's bot."""

from datetime import date

def recurringTask(firstDate, k, daysOfTheWeek, n):
    """Return first n dates for a recurring task.

    For example:

    >>> firstDate = "31/12/2999"
    >>> k = 4
    >>> n = 4
    >>> daysOfTheWeek = ["Tuesday"]
    >>> recurringTask(firstDate, k, daysOfTheWeek, n)
    ['31/12/2999', '28/01/3000', '25/01/3000', '22/01/3000']

    >>> firstDate = "01/02/2100"
    >>> k = 14
    >>> n = 4
    >>> daysOfTheWeek = ["Sunday", "Monday"]
    >>> recurringTask(firstDate, k, daysOfTheWeek, n)
    ['01/02/2100', '07/02/2100', '15/05/2100', '21/05/2100']

    """

    fday, fmonth, fyear = firstDate.split('/')

    # first, determine if year is leap
    feb = 28
    if (int(fyear) % 4 == 0 and int(fyear) % 100 != 0) or (int(fyear) % 400 == 0):
        feb = 29

    month_lengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_to_nums = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    
    days_of_the_week = []
    
    # converting names of days of the week to numbers to compare to date.isoweekday() output
    for day in daysOfTheWeek:
        days_of_the_week.append(days_to_nums[day])
    
    # with date.isoweekday(), Monday is 1 and Sunday is 7
    start_day = date(int(fyear), int(fmonth), int(fday)).isoweekday()
    
    deltas = []
        
    for day in days_of_the_week:
        delta = day - start_day
        if delta < 0:
            delta = (delta * -1) + 1
        deltas.append(delta)

    # now we have the deltas for the first week



    while len(deltas) < n:
        new_deltas = []
        for delta in deltas[-1 * len(days_of_the_week):]:
            new_deltas.append(delta + (k * 7))

        deltas.extend(new_deltas)

    deltas = deltas[:n]

    # now we have n number of deltas, so we can add those deltas to firstDate
    
    first_n_dates = []
    month_length = month_lengths[int(fmonth) - 1]
    
    deltas.sort()

    for delta in deltas: # TODO: simplify logic in this for loop
        next_day = '00' + str(delta + int(fday))

        if int(next_day) <= month_length: 
            next_date = str(next_day[-2:]) + '/' + str(fmonth) + '/' + fyear
        
        elif int(next_day) > month_length:
            add_month = 0

            while next_day > month_length:
                next_day = int(next_day) - month_length
                add_month += 1
            
            next_day = '00' + str(next_day)

            if int(fmonth) + add_month > 12:
                next_date = str(next_day[-2:]) + '/' + '01' + '/' + str(int(fyear) + 1)
            else:
                next_date = str(next_day[-2:]) + '/' + ('00' + str(int(fmonth) + add_month))[-2:] + '/' + fyear
        
        first_n_dates.append(next_date)
    
    return first_n_dates


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. *** \n"
    