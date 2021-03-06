from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
# import face_recognition
# import cv2
# import numpy as np
# import pickle
from django.utils import timezone
# import datetime
# import time


# Create your views here.

# def detect(request):
#     employees = Employee.objects.all()
#     context={
#         'employees':employees    
#     }
    
#         # Get a reference to webcam #0 (the default one)
#     video_capture = cv2.VideoCapture(0)
#     with open('dataset_faces.xml', 'rb') as f:
#         data_encoding = pickle.load(f)
#     with open('dataset_label.xml', 'rb') as f:
#         data_known=pickle.load(f)
   
#     # print(data)

#     # Initialize some variables
#     face_locations = []
#     face_encodings = []
#     face_names = []
#     process_this_frame = True

#     while True:
#         # Grab a single frame of video
#         ret, frame = video_capture.read()

#         # Resize frame of video to 1/4 size for faster face recognition processing
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         rgb_small_frame = small_frame[:, :, ::-1]

#         # Only process every other frame of video to save time
#         if process_this_frame:
#             # Find all the faces and face encodings in the current frame of video
#             face_locations = face_recognition.face_locations(rgb_small_frame)
#             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#             face_names = []
#             for face_encoding in face_encodings:
#                 # See if the face is a match for the known face(s)
#                 matches = face_recognition.compare_faces(data_encoding, face_encoding)
#                 name = "Unknown"

#                 # # If a match was found in known_face_encodings, just use the first one.
#                 if True in matches:
#                     first_match_index = matches.index(True)
#                     name = data_known[first_match_index]
#                     for employee in employees:
#                         store_corporate = Employee.objects.get(id=name)
#                         if store_corporate.in_out == False:
#                             store_corporate.in_out = True
#                             store_corporate.in_time = datetime.datetime.now()
#                             store_corporate.how_many_times += 1
#                             diff1 = float(store_corporate.out_time.strftime('%S.%f'))-float(store_corporate.in_time.strftime('%S.%f'))
#                             # diff2 = float(store_corporate.out_time.strftime('%M'))-float(store_corporate.out_time.strtime('%M'))
#                             store_corporate.time_outside_office += datetime.timedelta( seconds=diff1)
#                             store_corporate.save()
#                             cv2.destroyAllWindows()
#                             return render(request,'employees/index.html')    
#                         elif store_corporate.in_out == True:
#                             store_corporate.in_out = False
#                             store_corporate.out_time = datetime.datetime.now()
#                             store_corporate.save()
#                             cv2.destroyAllWindows()
#                             return render(request,'employees/index.html')
#                 else:
#                     return render(request,'employees/index.html')


#                 # # Or instead, use the known face with the smallest distance to the new face
#                 # face_distances = face_recognition.face_distance(data_encoding, face_encoding)
#                 # best_match_index = np.argmin(face_distances)
#                 # if matches[best_match_index] and name not "Unknown":
#                 #     name = data_known[best_match_index]
#                 #     for employee in employees:
#                 #         if employee.id==name:
#                 #             store_corporate = Employee.objects.get(id=name)
#                 #         if store_corporate.in_out == False:
#                 #             store_corporate.in_out = True
#                 #             store_corporate.in_time = timezone.now()
#                 #             store_corporate.save()
#                 #             return render(request,'employees/EmployeeList.html',context)    
#                 #         elif store_corporate.in_out == True:
#                 #             store_corporate.in_out = False
#                 #             store_corporate.out_time = timezone.now()
#                 #             store_corporate.save()
#                 #             return render(request,'employees/EmployeeList.html',context)

#                 name = store_corporate.name

#                 face_names.append(name)

#         process_this_frame = not process_this_frame


#         # Display the results
#         # for (top, right, bottom, left), name in zip(face_locations, face_names):
#         #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#         #     top *= 4
#         #     right *= 4
#         #     bottom *= 4
#         #     left *= 4

#         #     # Draw a box around the face
#         #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         #     # Draw a label with a name below the face
#         #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         #     font = cv2.FONT_HERSHEY_DUPLEX
#         #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            


#         # Display the resulting image
#         cv2.imshow('Video', frame)

#         # Hit 'q' on the keyboard to quit!
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#             # Release handle to the webcam
#             video_capture.release()
#             cv2.destroyAllWindows()

def detect(request):
    return render(request,'pages/contacts.html')


def index(request):
    employees = Employee.objects.all()
    for employee in employees:
        store_corporate = Employee.objects.get(id=1)
        store_corporate.name = 'Not sure about this name'
        store_corporate.save()
    return render(request,'employees/index.html')

def contacts(request):
    return render(request,'pages/contacts.html')
