"""
This script provides functionality to get information about students from a data dictionary.

Functions:
- print_attendance(data): Prints the name and attendance of each student.
- print_BusService(data): Prints the name and bus service status of each student based on user input.
- print_EnrolmentNumber(data): Prints the name and enrollment ID of each student.
- print_Mess(data): Prints the name and mess service status of each student based on user input.
- Score(data): Prints the name and scores of students for a selected semester based on user input.
- Status(data): Prints the name and pass/fail status of students for a selected semester based on user input.
"""

data = {
    'Student-1': {
        'name': ('Sambhav',),
        'Enrolment ID': ('AU23B1001',),
        'score': {
            'Semister-1': [('itd', 7.8), ('cct', 7.2), ('em', 7), ('jom', 8.9)],
            'Pass_Sem1': True,
            'Semister-2': [('DT', 7), ('PoE', 7.5), ('Fop', 8.9), ('ItC', 7)],
            'Pass_Sem2': True
        },
        'attendance': 98,
        'Bus Service': True,
        'Mess': False
    },

    'Student-2': {
        'name': ('Pavan',),
        'Enrolment ID': ('AU23B1002',),
        'score': {
            'Semister-1': [('itd', 3.5), ('cct', 2.8), ('em', 3.2), ('jom', 2.9)],
            'Pass_Sem1': False,
            'Semister-2': [('DT', 7), ('PoE', 7.5), ('Fop', 8.9), ('ItC', 7)],
            'Pass_Sem2': True
        },
        'attendance': 10,
        'Bus Service': False,
        'Mess': True
    },

    'Student-3': {
        'name': ('Arjun',),
        'Enrolment ID': ('AU23B1003',),
        'score': {
            'Semister-1': [('itd', 6.5), ('cct', 7.8), ('em', 8), ('jom', 9.2)],
            'Pass_Sem1': True,
            'Semister-2': [('DT', 6.9), ('PoE', 8), ('Fop', 8.5), ('ItC', 7.7)],
            'Pass_Sem2': True
        },
        'attendance': 92,
        'Bus Service': True,
        'Mess': True
    },

    'Student-4': {
        'name': ('Kunal',),
        'Enrolment ID': ('AU23B1004',),
        'score': {
            'Semister-1': [('itd', 3.2), ('cct', 3.5), ('em', 3.8), ('jom', 3.2)],
            'Pass_Sem1': False,
            'Semister-2': [('DT', 3.5), ('PoE', 7), ('Fop', 4.8), ('ItC', 2)],
            'Pass_Sem2': False
        },
        'attendance': 85,
        'Bus Service': True,
        'Mess': True
    },

    'Student-5': {
        'name': ('Siddharth',),
        'Enrolment ID': ('AU23B1005',),
        'score': {
            'Semister-1': [('itd', 7), ('cct', 7.5), ('em', 7.8), ('jom', 8.2)],
            'Pass_Sem1': True,
            'Semister-2': [('DT', 7.3), ('PoE', 7.8), ('Fop', 8.2), ('ItC', 7.6)],
            'Pass_Sem2': True
        },
        'attendance': 90,
        'Bus Service': True,
        'Mess': False
    },

    'Student-6': {
        'name': ('Aradhya',),
        'Enrolment ID': ('AU23B1006',),
        'score': {
            'Semister-1': [('itd', 3.8), ('cct', 3.2), ('em', 3.5), ('jom', 3.9)],
            'Pass_Sem1': False,
            'Semister-2': [('DT', 3.7), ('PoE', 4.1), ('Fop', 2.8), ('ItC', 6.2)],
            'Pass_Sem2': False
        },
        'attendance': 94,
        'Bus Service': True,
        'Mess': True
    },

    'Student-7': {
        'name': ('Ishita',),
        'Enrolment ID': ('AU23B1007',),
        'score': {
            'Semister-1': [('itd', 8), ('cct', 8.2), ('em', 8.5), ('jom', 9)],
            'Pass_Sem1': True,
            'Semister-2': [('DT', 7.8), ('PoE', 8.3), ('Fop', 8.7), ('ItC', 8)],
            'Pass_Sem2': True
        },
        'attendance': 96,
        'Bus Service': True,
        'Mess': True
    },

    'Student-8': {
        'name': ('Aman',),
        'Enrolment ID': ('AU23B1008',),
        'score': {
            'Semister-1': [('itd', 7.6), ('cct', 7.9), ('em', 6.9), ('jom', 8.2)],
            'Pass_Sem1': True,
            'Semister-2': [('DT', 3.5), ('PoE', 4.3), ('Fop', 2.1), ('ItC', 7)],
            'Pass_Sem2': False
        },
        'attendance': 91,
        'Bus Service': True,
        'Mess': True
    },

    'Student-9': {
        'name': ('Akash',),
        'Enrolment ID': ('AU23B1009',),
        'score': {
            'Semister-1': [('itd', 3.2), ('cct', 3.5), ('em', 3.7), ('jom', 3.1)],
            'Pass_Sem1': False,
            'Semister-2': [('DT', 7), ('PoE', 7.3), ('Fop', 7.8), ('ItC', 7.2)],
            'Pass_Sem2': True
        },
        'attendance': 88,
        'Bus Service': True,
        'Mess': True
    },

    'Student-10': {
        'name': ('Tanvi',),
        'Enrolment ID': ('AU23B1010',),
        'score': {
            'Semister-1': [('itd', 3.9), ('cct', 3.2), ('em', 3), ('jom', 3.8)],
            'Pass_Sem1': False,
            'Semister-2': [('DT', 7), ('PoE', 7.5), ('Fop', 8.9), ('ItC', 7)],
            'Pass_Sem2': True
        },
        'attendance': 10,
        'Bus Service': False,
        'Mess': True
    }
}


def print_EnrolmentNumber(data):
    for name, details in data.items():
        print("Name: ",details['name'][0])
        print("Enrolment ID: " ,(details['Enrolment ID'][0]),"\n")

# print_EnrolmentNumber(data)


def print_attendance(data):
    for name, details in data.items():
        # print(details)
        # print(name)
        print("Name: ",details['name'][0])
        print("Attendance: " ,details['attendance'],"\n")

# print_attendance(data)


def Score(data):
    print('Score available for:\n1.Semister-1\n2.semister-2',)
    sem_score=int(input('Enter Semister: '))
    print()
    print('Score of all Students')

    if sem_score==1:
        for name, details in data.items():
            print("Name: ",details['name'][0])
            print("Score in: ")
            for subject, value in details['score']['Semister-1']:
                print(subject,'=',value)
            print()
            
    elif sem_score==2:
        for name, details in data.items():
            print("Name: ",details['name'][0])
            print("Score in: ")
            for subject, value in details['score']['Semister-2']:
                print(subject,'=',value)
            print()
    return 'End'
    
# Score(data)


def Status(data):
    print('Status available for:\n1.Semister-1\n2.semister-2',)
    sta_score=int(input('Enter Semister: '))
    print('Status (pass/fail):\n1.Pass\n2.Fail',)
    status_score=int(input('Select Option: '))
    print()
    print('Status of all Students')

    if sta_score==1:
        if status_score==1:
            for name, details in data.items():
                if details['score']['Pass_Sem1']==True:
                    print("Name: ",details['name'][0])
                    print("Status: " ,details['score']['Pass_Sem1'],"\n")
                    print()

        elif status_score==2:
            for name, details in data.items():
                if details['score']['Pass_Sem1']==False:
                    print("Name: ",details['name'][0])
                    print("Status: " ,details['score']['Pass_Sem1'],"\n")
                    print()


    elif sta_score==2:
        if status_score==1:
            for name, details in data.items():
                if details['score']['Pass_Sem2']==True:
                    print("Name: ",details['name'][0])
                    print("Status: " ,details['score']['Pass_Sem2'],"\n")
                    print()

        elif status_score==2:
            for name, details in data.items():
                if details['score']['Pass_Sem2']==False:
                    print("Name: ",details['name'][0])
                    print("Status: " ,details['score']['Pass_Sem2'],"\n")
                    print()

# Status(data)


def print_BusService(data):

    print('What you want to see: \n1.List of all student \n2.List of Student Using Bus Service \n3.Student Not using Bus Service')
    b_input=int(input('Select Opton:'))
    print()
    

    if b_input==1:
        for name, details in data.items():
               
            print("Name: " ,details['name'][0])
            print("Bus Service: " ,details['Bus Service'],"\n")

    elif b_input==2:
       for name, details in data.items():
            if details['Bus Service']==True:
               print("Name: " ,details['name'][0])
               print("Bus Service: " ,details['Bus Service'],"\n")

    elif b_input==3:
        for name, details in data.items():
            if details['Bus Service']==False:
                print("Name: " ,details['name'][0])
                print("Bus Service: " ,details['Bus Service'],"\n")



def print_Mess(data):
    print('What you want to see: \n1.List of all student \n2.List of Student Using Mess \n3.Student Not using Mess')
    m_input=int(input('Select Option: '))
    print()
    if m_input==1:
        for name, details in data.items():
           print("Name: ",details['name'][0])
           print("Mess: " ,details['Mess'],"\n")

    elif m_input==2:
        for name, details in data.items():
           if details['Mess']==True:
            print("Name: ",details['name'][0])
            print("Mess: " ,details['Mess'],"\n")

    elif m_input==3:
        for name, details in data.items():
           if details['Mess']==False:
            print("Name: ",details['name'][0])
            print("Mess: " ,details['Mess'],"\n")


# print_Mess(data)

print('Want you want to enquire:')
print('1.Enrolment id \n2.Attendance \n3.Score \n4.Statue (Pass/Fail)\n5.Bus \n6.Mess')
enq=int(input('Enter Option:'))
print()

if enq==1:
    print('Enrolment ID of all Students')
    print_EnrolmentNumber(data)

elif enq==2:
    print('Attendance of all Students')
    print_attendance(data)

elif enq==3:
    print(Score(data))

elif enq==4:
    Status(data)

elif enq==5:
    print_BusService(data)

elif enq==6:
    print_Mess(data)

