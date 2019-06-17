# A crime scene has been discovered, and among the evidence is a list of agents, with no apparent connection.
# Your job in the records department is to match this list with police records to find an exact match.
# Your function will receive a list as the first parameter, the stolen record,
# followed by a list of lists, the database.
# A match is found only if it contains the same names in the same order, no more, no less.
# Your code should return None if the first parameter is an empty list.
# The database will always contain more than one list.
# A match should return "Match found". If no matches are found, your code should return "No matches".
# Example: agents(["John", "Sarah"], [["John", "Sarah"], ["Mary", "David"]]) == "Match found"

def agents(list_found, list_records):
    if list_found == []:
        print("None")
        return None
    else:
        for i in range(len(list_records)):
            z = list_records[i]     # We are considering length of "list_found" & "z" is same #
            if len(list_found) == len(list_records[i]):
                for j in range(len(z)):
                    if z[j] == list_found[j] and j != (len(z) - 1):
                        continue
                    elif z[j] == list_found[j] and j == (len(z) - 1):
                        print("Match found")
                        return "Match found"
                    else:
                        break
            else:
                break
    print("No matches")
    return "No matches"

list_found = []
list_records = [[], []]
agents(list_found,list_records)