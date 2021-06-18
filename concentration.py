import os
from video import video_concentration
from camera import camera_concentration


# from main import Ui_MainWindow




def total_concentration_percentage(path, gui):
    '''
     fucntion take path return list of each student percentage, total percentage of all students
    '''

    #my_window = Ui_MainWindow(window)


    percentages = []
    percentage = 0
    files = os.listdir( path )
    num_of_files = float(len(files))

    counter = 0
    gui.progressBar.setValue(0 )
    for video in files:
        current = video_concentration(path + video)
        percentages.append( [video,current])
        percentage += current
        counter += 1
        gui.progressBar.setValue ( (counter / num_of_files)* 100.00 )
    
    res = round(percentage/counter , 2) 
    return percentages,res




def attendance_percentage (num_students, path):
    '''
    takes total number of students, path . returns attendance percentage
    '''
    files = os.listdir( path )
    return round((len(files)/ num_students) * 100 ,2)



def live_camera_concentration():
    return camera_concentration()