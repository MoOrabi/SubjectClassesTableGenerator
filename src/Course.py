

class Course:
    def __init__(self, course_name, course_code, number_of_lectures, number_of_sections, number_of_labs
                 , preferred_professors=None, preferred_assistants=None):
        if preferred_assistants is None:
            preferred_assistants = []
        if preferred_professors is None:
            preferred_professors = []
        self.course_name = course_name
        self.course_code = course_code
        self.number_of_lectures = number_of_lectures
        self.number_of_sections = number_of_sections
        self.number_of_labs = number_of_labs
        self.preferred_professors = preferred_professors
        self.preferred_assistants = preferred_assistants
