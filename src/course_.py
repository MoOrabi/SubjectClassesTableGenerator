# from data_ import courses

class Course:
    def __init__(self, course_code, course_name, number_of_lectures, number_of_sections, number_of_labs,
                 preferred_professor=None, preferred_assistant=None):
        self.course_name = course_name
        self.course_code = course_code
        self.number_of_lectures = number_of_lectures
        self.number_of_sections = number_of_sections
        self.number_of_labs = number_of_labs
        self.preferred_professor = preferred_professor
        self.preferred_assistant = preferred_assistant

    def get_code(self):
        return self.course_code

    def get_name(self):
        return self.course_name

    def get_no_lectures(self):
        return self.number_of_lectures

    def get_no_sections(self):
        return self.number_of_sections

    def get_no_labs(self):
        return self.number_of_labs

    def get_preferred_professor(self):
        return self.preferred_professor

    def get_preferred_assistant(self):
        return self.preferred_assistant

    def set_preferred_professor(self, prefferred_professor_id):
        self.preferred_professor = prefferred_professor_id

    def set_preferred_assistant(self, preferred_assistant_id):
        self.preferred_assistant = preferred_assistant_id

    def __str__(self):
        return self.course_code + ", " + self.course_name + ", " + str(self.preferred_professor) + ", " + str(
            self.preferred_assistant)

    # def get_course(self, courses, course_code):
    #     for c in courses:
    #         if c.course_code == course_code:
    #             return c
