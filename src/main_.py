import data_ as d
from random import randint
from src.faculty_member_ import Faculty_member
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




def get_professor_by_id(prof_id):
    for professor in d.professors:
        if professor.get_id() == prof_id:
            return professor


def get_assistant_by_id(assis_id):
    for assis in d.assistants:
        if assis.get_id() == assis_id:
            return assis


def get_course_by_code(course_code):
    for course in d.courses:
        if course.get_code() == course_code:
            return course


# print courses data to verify that all courses have professors and assisstants
# for course in d.courses:
#     print(course)
#
# print("*" * 40)
#
# # print the full table to check if table is ok
# pprint(d.full_table)

def get_table_by_faculty_member(faculty_member_name):
    list_of_classes = []
    full_table_classes = get_full_table()
    for subject_class in full_table_classes:
        if subject_class[5] == faculty_member_name:
            list_of_classes.append(subject_class)
    return list_of_classes


def get_table_by_level(level):
    list_of_classes = []
    full_table_classes = get_full_table()
    for subject_class in full_table_classes:
        if subject_class[2] == level:
            list_of_classes.append(subject_class)
    return list_of_classes


def get_full_table():
    list_of_classes = []
    for level in d.full_table:
        for day in d.full_table[level]:
            day_slots = d.full_table[level][day]
            for slot in day_slots:
                course_code = d.full_table[level][day][slot][0]
                course = get_course_by_code(course_code)
                chosen_prof = get_professor_by_id(course.get_preferred_professor())
                chosen_assis = get_assistant_by_id(course.get_preferred_assistant())
                member = ""
                if d.full_table[level][day][slot][1] == "lecture":
                    member = "Dr." + chosen_prof.get_name()
                else:
                    member = "Eng." + chosen_assis.get_name()
                subject_class = [day, slot, level, course.course_name, d.full_table[level][day][slot][1], member]
                list_of_classes.append(subject_class)
    return list_of_classes

pprint(get_full_table())


# pprint(get_table_by_faculty_member("Dr.Amr Hossam"))
# pprint(get_table_by_level(2))


