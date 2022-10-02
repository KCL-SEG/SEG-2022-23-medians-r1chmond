"""Median calculator."""
def getMedian(list):
    list.sort()
    index = len(list)
    if(index == 1):
        return list[0]
    elif(index % 2 == 0):
        return (list[int(index/2)] + list[int(index/2) - 1]) / 2
    else:
        return list[int(index/2)]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("Median of " + str(numbers) + " is : " + str(getMedian(numbers)))
