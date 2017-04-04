from datetime import date 

def recurringTask(firstDate, k, daysOfTheWeek, n):
    """Return first n dates for a recurring task."""

    def get_deltas(days_of_the_week, start_day):
        """Return list of deltas - numbers that will be added to firstDate 
        to get recurring task dates."""

        deltas = []

        for day in days_of_the_week:
            delta = day - start_day
            if delta < 0:
                delta = (delta * -1) + 1
            deltas.append(delta)

        # now we have the deltas for the first week

        new_deltas = []

        while len(deltas) < n:

            for delta in deltas:
                new_deltas.append(delta + (k * 7))

            deltas.extend(new_deltas)

        return deltas

    fday, fmonth, fyear = firstDate.split('/')

    # first, determine if year is leap
    feb = 28
    if (int(fyear) % 4 == 0 and int(fyear) % 100 != 0) or (int(fyear) % 400 == 0):
        feb = 29

    month_lengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_to_nums = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 
                    'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    

    # then, convert names of daysOfTheWeek to numbers so we can more easily get the deltas

    days_of_the_week = []

    for day in daysOfTheWeek:
        days_of_the_week.append(days_to_nums[day])
    
    # with date.isoweekday(), Monday is 1 and Sunday is 7

    start_day = date(int(fyear), int(fmonth), int(fday)).isoweekday()

    deltas = get_deltas(days_of_the_week, start_day)

    # now we have n number of deltas, so we can add those deltas to firstDate
    
    first_n_dates = []
    month_length = month_lengths[int(fmonth) - 1]
    
    deltas.sort() # ensure deltas are sorted so output is in chronological order

    print deltas
    



firstDate = "31/12/2999"
k = 1
n = 2
daysOfTheWeek = ["Tuesday"]

# firstDate = "01/02/2100"
# k = 4
# n = 4
# daysOfTheWeek = ["Sunday", "Monday"]

recurringTask(firstDate, k, daysOfTheWeek, n)
    
    
        
    

