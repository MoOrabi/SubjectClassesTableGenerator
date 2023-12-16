import data_ as d
import course_ as c
from random import randint
from pprint import pprint


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
    d.full_table[int(course_code[0])][d.days[day]][d.slots[slot]] = [course_code, class_type]


def check_table_free(level, day, slot):
    if d.full_table[level][d.days[day]][d.slots[slot]] == None:
        return True
    else:
        return False


def assign_classes_to_courses(level, class_type):
    level_courses = get_level_courses(d.courses, level)
    for course in level_courses:
        if class_type == "lecture":
            ctr = course.get_no_lectures()
        elif class_type == "section":
            ctr = course.get_no_sections()
        elif class_type == "lab":
            ctr = course.get_no_labs()
        while ctr != 0:
            day = randint(1, 6)
            slot = randint(1, 5)
            if check_table_free(level, day, slot):
                add_class(course.get_code(), day, slot, class_type)
                ctr -= 1


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

# assign lectures to all levels
assign_classes_to_courses(1, "lecture")
assign_classes_to_courses(2, "lecture")
assign_classes_to_courses(3, "lecture")
assign_classes_to_courses(4, "lecture")

# assign sections to all levels
assign_classes_to_courses(1, "section")
assign_classes_to_courses(2, "section")
assign_classes_to_courses(3, "section")
assign_classes_to_courses(4, "section")

# assign labs to all levels
assign_classes_to_courses(1, "lab")
assign_classes_to_courses(2, "lab")
assign_classes_to_courses(3, "lab")
assign_classes_to_courses(4, "lab")






for course in d.courses:
    print(course)
print("*" * 40)
pprint(d.full_table)
