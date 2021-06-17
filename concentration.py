import os
from video import video_concentration


def total_concentration_percentage(path):
    '''
     fucntion take path return list of each student percentage, total percentage of all students
    '''
    percentages = []
    percentage = 0
    files = os.listdir( path )
    counter = 0
    for video in files:
        current = video_concentration(path + video)
        percentages.append(current)
        percentage += current
        counter += 1
    
    res = round(percentage/counter , 2) 
    return percentages,res




def attendance_percentage (num_students, path):
    '''
    takes total number of students, path . returns attendance percentage
    '''
    files = os.listdir( path )
    return round((len(files)/ num_students) * 100 ,2)

