# 3 : a class in a school have 40 students. write a java program to find the mean and max score in eng
import statistics

eng=[43,54,65,76,78,98,90,24,23,56,87,89,90,76,56,45,45,34,65,89]

print(min(eng))
def avg(marks): 
    return sum(marks)/len(marks)


def maxScore(marks):
    return max(eng)


print(maxScore(eng))


