import data_ as d
import course_ as c
from random import shuffle


def get_course(courses_list, course_code):
    for course in courses_list:
        if course.get_code() == course_code:
            return course


def check_all_courses_assigned_prof(courses_list):
    for course in courses_list:
        if course.get_preferred_professor() == None:
            return False
    return True


def check_all_courses_assigned_assis(courses_list):
    for course in courses_list:
        if course.get_preferred_assistant() == None:
            return False
    return True


# ************************* Start main *************************


# assign professors to courses
while not check_all_courses_assigned_prof(d.courses):
    for prof in d.professors:
        course = get_course(d.courses, prof.get_first_well_code())
        if course.get_preferred_professor() == None:
            course.set_preferred_professor(prof.get_id())
        else:
            course = get_course(d.courses, prof.get_second_well_code())
            if course.get_preferred_professor() == None:
                course.set_preferred_professor(prof.get_id())
            else:
                course = get_course(d.courses, prof.get_third_well_code())
                if course.get_preferred_professor() == None:
                    course.set_preferred_professor(prof.get_id())
                else:
                    print("Can't find courses for prof", prof)

# assign assistants to courses
while not check_all_courses_assigned_assis(d.courses):
    for assistant in d.assistants:
        course = get_course(d.courses, assistant.get_first_well_code())
        if course.get_preferred_assistant() == None:
            course.set_preferred_assistant(assistant.get_id())
        else:
            course = get_course(d.courses, assistant.get_second_well_code())
            if course.get_preferred_assistant() == None:
                course.set_preferred_assistant(assistant.get_id())
            else:
                course = get_course(d.courses, assistant.get_third_well_code())
                if course.get_preferred_assistant() == None:
                    course.set_preferred_assistant(assistant.get_id())
                else:
                    print("Can't find courses for assistant", assistant)

for course in d.courses:
    print(course)
