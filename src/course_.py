

class Course:
    def __init__(self, course_code, course_name, number_of_lectures, number_of_sections, number_of_labs
                 , preferred_professor=None, preferred_assistant=None):
        self.course_name = course_name
        self.course_code = course_code
        self.number_of_lectures = number_of_lectures
        self.number_of_sections = number_of_sections
        self.number_of_labs = number_of_labs
        self.preferred_professor = preferred_professor
        self.preferred_assistant = preferred_assistant
