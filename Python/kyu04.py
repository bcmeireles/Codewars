"""
Human readable duration format
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""
def format_duration(seconds):
    if seconds == 0:
        return "now"

    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    days = hours // 24
    hours = hours - (24 * days)
    years = days // 365
    days = days - (365 * years)
    
    sec_str = " second" if seconds == 1 else " seconds"
    min_str = " minute" if minutes == 1 else " minutes"
    hr_str = " hour" if hours == 1 else " hours"
    day_str = " day" if days == 1 else " days"
    year_str = " year" if years == 1 else " years"

    duration = ""
    indendation_aux = [years, days, hours, minutes, seconds]
    diff0 = 0
    for n in indendation_aux:
        if n != 0:
            diff0 += 1

    if years != 0:
        if diff0 == 1:
            duration += str(years) + year_str
            return duration
        elif diff0 == 2:
            duration += str(years) + year_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(years) + year_str + ", "
            diff0 -= 1
    
    if days != 0:
        if diff0 == 1:
            duration += str(days) + day_str
            return duration
        elif diff0 == 2:
            duration += str(days) + day_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(days) + day_str + ", "
            diff0 -= 1
            
    if hours != 0:
        if diff0 == 1:
            duration += str(hours) + hr_str
            return duration
        elif diff0 == 2:
            duration += str(hours) + hr_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(hours) + hr_str + ", "
            diff0 -= 1
            
    if minutes != 0:
        if diff0 == 1:
            duration += str(minutes) + min_str
            return duration
        elif diff0 == 2:
            duration += str(minutes) + min_str + " and "
            diff0 -= 1
        elif diff0 > 2:
            duration += str(minutes) + min_str + ", "
            diff0 -= 1
        
    if seconds != 0:
        duration += str(seconds) + sec_str
        return duration
