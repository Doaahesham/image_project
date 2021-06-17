from concentration import total_concentration_percentage, attendance_percentage
import os



PATH = os.path.join(os.path.dirname(__file__) +'\\test\\')


percentages,res = total_concentration_percentage(PATH)

attendance = attendance_percentage(2, PATH)

print(percentages)
print(res)
print('attendance', attendance)