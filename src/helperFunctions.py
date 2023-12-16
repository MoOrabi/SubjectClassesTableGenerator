from src.data import level1_times, level_1_courses, level1_classes, \
                     level2_times, level_2_courses, level2_classes, \
                     level3_times, level_3_courses, level3_classes, \
                     level4_times, level_4_courses, level4_classes


def choose_time_for_class(level_times):
    return {"day": "", "time": ""}


def get_least_busy_prof(preferred_professors):
    return ""


def put_lectures_classes(course_name, course_code, number_of_lectures, preferred_professors, level_classes, level_times):
    for i in range(number_of_lectures):
        chooses_day_and_time = choose_time_for_class(level_times)
        professor = get_least_busy_prof(preferred_professors)
        subject_class = {"course_name": course_name, "course_code": course_code,
                         "type_of_class": "Lecture", "faculty_member": professor,
                         "day": chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")}
        level_times.append({"day":chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")})
        level_classes.append(subject_class)


def put_sections_classes(course_name, course_code, number_of_sections, preferred_assistants, level_classes, level_times):
    for i in range(number_of_sections):
        chooses_day_and_time = choose_time_for_class(level_times)
        assistant = get_least_busy_prof(preferred_assistants)
        subject_class = {"course_name": course_name, "course_code": course_code,
                         "type_of_class": "Section", "faculty_member": assistant,
                         "day": chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")}
        level_times.append({"day": chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")})
        level_classes.append(subject_class)


def put_labs_classes(course_name, course_code, number_of_labs, preferred_assistants, level_classes, level_times):
    for i in range(number_of_labs):
        chooses_day_and_time = choose_time_for_class(level_times)
        assistant = get_least_busy_prof(preferred_assistants)
        subject_class = {"course_name": course_name, "course_code": course_code,
                         "type_of_class": "Lab", "faculty_member": assistant,
                         "day": chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")}
        level_times.append({"day": chooses_day_and_time.get("day"), "time": chooses_day_and_time.get("time")})
        level_classes.append(subject_class)


def assign_classes_to_course(level_times, level_classes, course):
    put_lectures_classes(course.course_name, course.course_code,
                         course.number_of_lectures, course.preferred_professors, level_classes, level_times)
    put_sections_classes(course.course_name, course.course_code,
                         course.number_of_sections, course.preferred_assistants,level_classes, level_times)
    put_labs_classes(course.course_name, course.course_code,
                     course.number_of_labs, course.preferred_assistants,level_classes, level_times)


def add_classes_to_level(level_times, level_classes, level_courses):
    for course in level_courses:
        assign_classes_to_course(level_times, level_classes, course)


def add_classes_to_levels():
    add_classes_to_level(level1_times, level1_classes, level_1_courses)
    add_classes_to_level(level2_times, level2_classes, level_2_courses)
    add_classes_to_level(level3_times, level3_classes, level_3_courses)
    add_classes_to_level(level4_times, level4_classes, level_4_courses)
