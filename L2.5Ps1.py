### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)

def nextDay(year, month, day):
    
    """Returns the year, month, day of the next day.
        Simple version: assume every month has 30 days."""
    
    while day < 30 and month < 13 :
        return (year, month, day+1)
    if month == 12 and day == 30:
        return (year+1, 1, 1)
    elif month < 13 and day == 30:
        return (year, month+1, 1)
    else: return (year, month+1, day)
