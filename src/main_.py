import data_ as d
import course_ as c
from random import randint


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


def get_level_courses(courses_list, level_num):
    courses_level = [course for course in courses_list if course.get_code()[0] == str(level_num)]
    return courses_level


def add_class(course_code, day, slot, class_type):
    # day, slot should be numbers
    d.full_table[int(course_code[0])][days[day]][slots[slot]] = [course_code, class_type]

def check_table_free(level, day, slot):
    if d.full_table[level][days[day]][slots[slot]] == None:
        return True
    else:
        return False

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

# assign courses of level_1 to its table
level_1_courses = get_level_courses(d.courses, 1)
for course in level_1_courses:
    day = randint(1, 6)
    slot = randint(1, 5)
    # while()







for course in d.courses:
    print(course)
print("*" * 40)

