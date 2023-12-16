class Faculty_member:
    def __init__(self, id, name, first_course_code, second_course_code, third_course_code):
        self.id = id
        self.name = name
        self.first_course_code = first_course_code
        self.second_course_code = second_course_code
        self.third_course_code = third_course_code

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_first_well_code(self):
        return self.first_course_code

    def get_second_well_code(self):
        return self.second_course_code

    def get_third_well_code(self):
        return self.third_course_code

    def __str__(self):
        return self.id + self.name