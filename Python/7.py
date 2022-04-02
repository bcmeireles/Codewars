"""
Categorize New Member
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
"""
def open_or_senior(data):
    list = []
    for member in data:
        list.append("Senior") if (member[0] > 54 and member[1] > 7) else list.append("Open")
    return list

"""
Complementary DNA
https://www.codewars.com/kata/554e4a2f232cdd87d9000038
"""
def DNA_strand(dna):
    final = ""
    for letter in dna:
        if letter == "A":
            final += "T"
        elif letter == "T":
            final += "A"
        elif letter == "C":
            final += "G"
        elif letter == "G":
            final += "C"
        else:
            final += letter
    return final
