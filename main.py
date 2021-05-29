# compute CGPA for university and college students
print('Please Input your Name')
Name = input()
print('You are Welcome ' + str(Name) + ' to the CGPA Compiler')
print(str(Name) + ' Kindly input your Current Level: 1, 2, 3, 4, 5, or 6 for spill')
print('NOTE: Use 1 for Direct Entry')
Level = int(input())
if Level > 1:
    print('kindly input  your previous Total Points')
    print('Use 0 where value cannot be ascertained')
    PrevTP = int(input())  # system reject PrevT.P
    print('kindly input your previous Total Number of Units')
    print('Use 0 where value cannot be ascertained')
    PrevTNU = int(input())
else:
    print('kindly Input Current Semester: 1 or 2')
    Sem = int(input())
    if Sem == 2:
        print('kindly input  your previous Total Points')
        print('Use 0 where value cannot be ascertained')
        PrevTP = int(input())  # system reject PrevT.P
        print('kindly input your previous Total Number of Units')
        print('Use 0 where value cannot be ascertained')
        PrevTNU = int(input())
    else:
        print('kindly insert Course Codes, Units, and Grades obtained for the current semester')


def CompRes1():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

        if Sem == 1:
            CurrTP = points1a
            CurrTU = units1a
            GPA = CurrTP / CurrTU
            print('Course Code   Units   Grade   points')
            print(course1a + str(units1a) + Grade1a + str(points1a))
            print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
        else:
            CurrTP = points1a
            CurrTU = units1a
            CummTP = CurrTP + PrevTP
            CummTU = CurrTU + PrevTNU
            GPA = CurrTP / CurrTU
            CGPA = CummTP / CummTU
            # Class of Degree (Check)

            print('Course Code   Units   Grade   points')
            print(course1a + str(units1a) + Grade1a + str(points1a))

            print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
            print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes2():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    CurrTP = points1a + points2a
    CurrTU = units1a + units2a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes3():  ########3
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    CurrTP = points1a + points2a + points3a
    CurrTU = units1a + units2a + units3a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes4():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    CurrTP = points1a + points2a + points3a + points4a
    CurrTU = units1a + units2a + units3a + units4a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))

    if Level == 1 and Sem == 1:
        print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    else:
        print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
        print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes5():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    CurrTP = points1a + points2a + points3a + points4a + points5a
    CurrTU = units1a + units2a + units3a + units4a + units5a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes6():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    print('Input Current Semester 6th Course Code, eg ACC111')
    course6a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course6a + ' Units')
    units6a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course6a + ': A, B, C, D, or F')
    Grade6a = input('')

    if Grade6a == 'A':
        points6a = 5 * units6a

    elif Grade6a == 'B':
        points6a = 4 * units6a

    elif Grade6a == 'C':
        points6a = 3 * units6a


    elif Grade6a == 'D':
        points6a = 2 * units6a

    else:
        points6a = 0 * units6a

    CurrTP = points1a + points2a + points3a + points4a + points5a + points6a
    CurrTU = units1a + units2a + units3a + units4a + units5a + units6a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))
    print(course6a + str(units6a) + Grade6a + str(points6a))

    if Level == 1 and Sem == 1:
        print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    else:
        print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
        print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes7():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    print('Input Current Semester 6th Course Code, eg ACC111')
    course6a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course6a + ' Units')
    units6a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course6a + ': A, B, C, D, or F')
    Grade6a = input('')

    if Grade6a == 'A':
        points6a = 5 * units6a

    elif Grade6a == 'B':
        points6a = 4 * units6a

    elif Grade6a == 'C':
        points6a = 3 * units6a


    elif Grade6a == 'D':
        points6a = 2 * units6a

    else:
        points6a = 0 * units6a

    print('Input Current Semester 7th Course Code, eg ACC113')
    course7a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course7a + ' Units')
    units7a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course7a + ': A, B, C, D, or F')
    Grade7a = input('')

    if Grade7a == 'A':
        points7a = 5 * units7a

    elif Grade7a == 'B':
        points7a = 4 * units7a

    elif Grade7a == 'C':
        points7a = 3 * units7a

    elif Grade7a == 'D':
        points7a = 2 * units7a

    else:
        points7a = 0 * units7a

    CurrTP = points1a + points2a + points3a + points4a + points5a + points6a + points7a
    CurrTU = units1a + units2a + units3a + units4a + units5a + units6a + units7a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))
    print(course6a + str(units6a) + Grade6a + str(points6a))
    print(course7a + str(units7a) + Grade7a + str(points7a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes8():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    print('Input Current Semester 6th Course Code, eg ACC111')
    course6a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course6a + ' Units')
    units6a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course6a + ': A, B, C, D, or F')
    Grade6a = input('')

    if Grade6a == 'A':
        points6a = 5 * units6a

    elif Grade6a == 'B':
        points6a = 4 * units6a

    elif Grade6a == 'C':
        points6a = 3 * units6a


    elif Grade6a == 'D':
        points6a = 2 * units6a

    else:
        points6a = 0 * units6a

    print('Input Current Semester 7th Course Code, eg ACC113')
    course7a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course7a + ' Units')
    units7a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course7a + ': A, B, C, D, or F')
    Grade7a = input('')

    if Grade7a == 'A':
        points7a = 5 * units7a

    elif Grade7a == 'B':
        points7a = 4 * units7a

    elif Grade7a == 'C':
        points7a = 3 * units7a

    elif Grade7a == 'D':
        points7a = 2 * units7a

    else:
        points7a = 0 * units7a

    print('Input Current Semester 8th Course Code, eg ACC115')
    course8a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course8a + ' Units')
    units8a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course8a + ': A, B, C, D, or F')
    Grade8a = input('')

    if Grade8a == 'A':
        points8a = 5 * units8a

    elif Grade8a == 'B':
        points8a = 4 * units8a

    elif Grade8a == 'C':
        points8a = 3 * units8a

    elif Grade8a == 'D':
        points8a = 2 * units8a

    else:
        points8a = 0 * units8a

    CurrTP = points1a + points2a + points3a + points4a + points5a + points6a + points7a + points8a
    CurrTU = units1a + units2a + units3a + units4a + units5a + units6a + units7a + units8a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))
    print(course6a + str(units6a) + Grade6a + str(points6a))
    print(course7a + str(units7a) + Grade7a + str(points7a))
    print(course8a + str(units8a) + Grade8a + str(points8a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes9():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    print('Input Current Semester 6th Course Code, eg ACC111')
    course6a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course6a + ' Units')
    units6a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course6a + ': A, B, C, D, or F')
    Grade6a = input('')

    if Grade6a == 'A':
        points6a = 5 * units6a

    elif Grade6a == 'B':
        points6a = 4 * units6a

    elif Grade6a == 'C':
        points6a = 3 * units6a


    elif Grade6a == 'D':
        points6a = 2 * units6a

    else:
        points6a = 0 * units6a

    print('Input Current Semester 7th Course Code, eg ACC113')
    course7a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course7a + ' Units')
    units7a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course7a + ': A, B, C, D, or F')
    Grade7a = input('')

    if Grade7a == 'A':
        points7a = 5 * units7a

    elif Grade7a == 'B':
        points7a = 4 * units7a

    elif Grade7a == 'C':
        points7a = 3 * units7a

    elif Grade7a == 'D':
        points7a = 2 * units7a

    else:
        points7a = 0 * units7a

    print('Input Current Semester 8th Course Code, eg ACC115')
    course8a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course8a + ' Units')
    units8a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course8a + ': A, B, C, D, or F')
    Grade8a = input('')

    if Grade8a == 'A':
        points8a = 5 * units8a

    elif Grade8a == 'B':
        points8a = 4 * units8a

    elif Grade8a == 'C':
        points8a = 3 * units8a

    elif Grade8a == 'D':
        points8a = 2 * units8a

    else:
        points8a = 0 * units8a

    print('Input Current Semester 9th Course Code, eg ACC117')
    course9a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course9a + ' Units')
    units9a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course9a + ': A, B, C, D, or F')
    Grade9a = input('')

    if Grade9a == 'A':
        points9a = 5 * units9a

    elif Grade9a == 'B':
        points9a = 4 * units9a

    elif Grade9a == 'C':
        points9a = 3 * units9a

    elif Grade9a == 'D':
        points9a = 2 * units9a

    else:
        points9a = 0 * units9a

    CurrTP = points1a + points2a + points3a + points4a + points5a + points6a + points7a + points8a + points9a
    CurrTU = units1a + units2a + units3a + units4a + units5a + units6a + units7a + units8a + units9a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))
    print(course6a + str(units6a) + Grade6a + str(points6a))
    print(course7a + str(units7a) + Grade7a + str(points7a))
    print(course8a + str(units8a) + Grade8a + str(points8a))
    print(course9a + str(units9a) + Grade9a + str(points9a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


def CompRes10():
    print('Input Current Semester 1st Course Code, eg ACC101')
    course1a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course1a + ' Units')
    units1a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course1a + ': A, B, C, D, or F')
    Grade1a = input('')

    if Grade1a == 'A':
        points1a = 5 * units1a

    elif Grade1a == 'B':
        points1a = 4 * units1a

    elif Grade1a == 'C':
        points1a = 3 * units1a

    elif Grade1a == 'D':
        points1a = 2 * units1a

    else:
        points1a = 0 * units1a  #

    print('Input Current Semester 2nd Course Code, eg ACC103')
    course2a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course2a + ' Units')
    units2a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course2a + ': A, B, C, D, or F')
    Grade2a = input('')

    if Grade2a == 'A':
        points2a = 5 * units2a

    elif Grade2a == 'B':
        points2a = 4 * units2a

    elif Grade2a == 'C':
        points2a = 3 * units2a

    elif Grade2a == 'D':
        points2a = 2 * units2a

    else:
        points2a = 0 * units2a

    print('Input Current Semester 3rd Course Code, eg ACC105')
    course3a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course3a + ' Units')
    units3a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course3a + ': A, B, C, D, or F')
    Grade3a = input('')

    if Grade3a == 'A':
        points3a = 5 * units3a

    elif Grade3a == 'B':
        points3a = 4 * units3a

    elif Grade3a == 'C':
        points3a = 3 * units3a

    elif Grade3a == 'D':
        points3a = 2 * units3a

    else:
        points3a = 0 * units3a

    print('Input Current Semester 4th Course Code, eg ACC107')
    course4a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course4a + ' Units')
    units4a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course4a + ': A, B, C, D, or F')
    Grade4a = input('')

    if Grade4a == 'A':
        points4a = 5 * units4a

    elif Grade4a == 'B':
        points4a = 4 * units4a

    elif Grade4a == 'C':
        points4a = 3 * units4a

    elif Grade4a == 'D':
        points4a = 2 * units4a

    else:
        points4a = 0 * units4a

    print('Input Current Semester 5th Course Code, eg ACC109')
    course5a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course5a + ' Units')
    units5a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course5a + ': A, B, C, D, or F')
    Grade5a = input('')

    if Grade5a == 'A':
        points5a = 5 * units5a

    elif Grade5a == 'B':
        points5a = 4 * units5a

    elif Grade5a == 'C':
        points5a = 3 * units5a

    elif Grade5a == 'D':
        points5a = 2 * units5a

    else:
        points5a = 0 * units5a

    print('Input Current Semester 6th Course Code, eg ACC111')
    course6a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course6a + ' Units')
    units6a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course6a + ': A, B, C, D, or F')
    Grade6a = input('')

    if Grade6a == 'A':
        points6a = 5 * units6a

    elif Grade6a == 'B':
        points6a = 4 * units6a

    elif Grade6a == 'C':
        points6a = 3 * units6a


    elif Grade6a == 'D':
        points6a = 2 * units6a

    else:
        points6a = 0 * units6a

    print('Input Current Semester 7th Course Code, eg ACC113')
    course7a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course7a + ' Units')
    units7a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course7a + ': A, B, C, D, or F')
    Grade7a = input('')

    if Grade7a == 'A':
        points7a = 5 * units7a

    elif Grade7a == 'B':
        points7a = 4 * units7a

    elif Grade7a == 'C':
        points7a = 3 * units7a

    elif Grade7a == 'D':
        points7a = 2 * units7a

    else:
        points7a = 0 * units7a

    print('Input Current Semester 8th Course Code, eg ACC115')
    course8a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course8a + ' Units')
    units8a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course8a + ': A, B, C, D, or F')
    Grade8a = input('')

    if Grade8a == 'A':
        points8a = 5 * units8a

    elif Grade8a == 'B':
        points8a = 4 * units8a

    elif Grade8a == 'C':
        points8a = 3 * units8a

    elif Grade8a == 'D':
        points8a = 2 * units8a

    else:
        points8a = 0 * units8a

    print('Input Current Semester 9th Course Code, eg ACC117')
    course9a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course9a + ' Units')
    units9a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course9a + ': A, B, C, D, or F')
    Grade9a = input('')

    if Grade9a == 'A':
        points9a = 5 * units9a

    elif Grade9a == 'B':
        points9a = 4 * units9a

    elif Grade9a == 'C':
        points9a = 3 * units9a

    elif Grade9a == 'D':
        points9a = 2 * units9a

    else:
        points9a = 0 * units9a

    print('Input Current Semester 10th Course Code, eg ACC119')
    course10a = input()  # course code 1a (a = 1st semester)
    print('Input ' + course10a + ' Units')
    units10a = int(input())  # the units allocated to that course
    print('Input Grade Obtained in ' + course10a + ': A, B, C, D, or F')
    Grade10a = input('')

    if Grade10a == 'A':
        points10a = 5 * units10a

    elif Grade10a == 'B':
        points10a = 4 * units10a

    elif Grade10a == 'C':
        points10a = 3 * units10a

    elif Grade10a == 'D':
        points10a = 2 * units10a

    else:
        points10a = 0 * units10a

    CurrTP = points1a + points2a + points3a + points4a + points5a + points6a + points7a + points8a + points9a + points10a
    CurrTU = units1a + units2a + units3a + units4a + units5a + units6a + units7a + units8a + units9a + units10a
    CummTP = CurrTP + PrevTP
    CummTU = CurrTU + PrevTNU
    GPA = CurrTP / CurrTU
    CGPA = CummTP / CummTU
    # Class of Degree (Check)

    print('Course Code   Units   Grade   points')
    print(course1a + str(units1a) + Grade1a + str(points1a))
    print(course2a + str(units2a) + Grade2a + str(points2a))
    print(course3a + str(units3a) + Grade3a + str(points3a))
    print(course4a + str(units4a) + Grade4a + str(points4a))
    print(course5a + str(units5a) + Grade5a + str(points5a))
    print(course6a + str(units6a) + Grade6a + str(points6a))
    print(course7a + str(units7a) + Grade7a + str(points7a))
    print(course8a + str(units8a) + Grade8a + str(points8a))
    print(course9a + str(units9a) + Grade9a + str(points9a))
    print(course10a + str(units10a) + Grade10a + str(points10a))

    print('TP: ' + str(CurrTP) + 'TU: ' + str(CurrTU) + 'GPA: = ' + str(GPA))
    print('CTU: ' + str(CummTP) + 'CTU: ' + str(CummTU) + 'CGPA = ' + str(CGPA))


print('plis insert number of courses offered in the current semester')

x = int(input())
if x == 1:  # 2nd sem
    CompRes1()
elif x == 2:
    CompRes2()
elif x == 3:
    CompRes3()
elif x == 4:
    CompRes4()
elif x == 5:
    CompRes5()
elif x == 6:
    CompRes6()
elif x == 7:
    CompRes7()
elif x == 8:
    CompRes8()
elif x == 9:
    CompRes9()
else:
    CompRes10()
