from src.Course import Course
from random import choices

levels_courses = []
professors = [{"name": "Ahmed Mohamed", "number_of_classes": 0},
              {"name": "Hassan Ali", "number_of_classes": 0},
              {"name": "Mohamed Ibrahim", "number_of_classes": 0},
              {"name": "Omar Samir", "number_of_classes": 0},
              {"name": "Khaled Ahmed", "number_of_classes": 0},
              {"name": "Amr Hossam", "number_of_classes": 0},
              {"name": "Ali Mahmoud", "number_of_classes": 0},
              {"name": "Tarek Hassan", "number_of_classes": 0},
              {"name": "Mahmoud Sami", "number_of_classes": 0},
              {"name": "Youssef Ahmed", "number_of_classes": 0},
              {"name": "Karim Mohamed", "number_of_classes": 0},
              {"name": "Mamdouh Adel", "number_of_classes": 0}]
assistants = [{"name": "Ahmad Salah", "number_of_classes": 0},
              {"name": "Adham Mostafa", "number_of_classes": 0},
              {"name": "Hisham Amr", "number_of_classes": 0},
              {"name": "Wael Mahmoud", "number_of_classes": 0},
              {"name": "Mazen Samy", "number_of_classes": 0},
              {"name": "Hamza Sherif", "number_of_classes": 0},
              {"name": "Nabil Tawfiq", "number_of_classes": 0},
              {"name": "Tamer Adel", "number_of_classes": 0},
              {"name": "Hany Youssef", "number_of_classes": 0},
              {"name": "Mohsen Ali", "number_of_classes": 0},
              {"name": "Sherif Ezzat", "number_of_classes": 0}]
professors_names_list = [
    "Ahmed Mohamed", "Hassan Ali", "Mohamed Ibrahim", "Omar Samir",
    "Khaled Ahmed", "Amr Hossam", "Ali Mahmoud", "Tarek Hassan",
    "Mahmoud Sami", "Youssef Ahmed", "Karim Mohamed", "Mamdouh Adel"
]

assistants_names_list = [
    "Ahmad Salah", "Adham Mostafa", "Hisham Amr", "Wael Mahmoud",
    "Mazen Samy", "Hamza Sherif", "Nabil Tawfiq", "Tamer Adel",
    "Hany Youssef", "Mohsen Ali", "Sherif Ezzat"
]


level1_courses_list = [
    ["Introduction to Programming", "101", 2, 2, 1,
     ["Ahmed Mohamed", "Hassan Ali", "Mohamed Ibrahim"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],
    ["Data Structures and Algorithms", "102", 2, 2, 1,
     ["Omar Samir", "Khaled Ahmed", "Amr Hossam"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],
    ["Database Management Systems", "103", 2, 2, 1,
     ["Hassan Ali", "Mohamed Ibrahim", "Omar Samir"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],
    ["Computer Networks", "104", 2, 2, 1,
     ["Khaled Ahmed", "Amr Hossam", "Ahmed Mohamed"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],
    ["Operating Systems", "105", 2, 2, 1,
     ["Amr Hossam", "Ahmed Mohamed", "Hassan Ali"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],
    ["Software Engineering", "106", 2, 2, 1,
     ["Omar Samir", "Khaled Ahmed", "Amr Hossam"],
     ["Ali Mahmoud", "Tarek Hassan", "Mahmoud Youssef"]],

]

level2_courses_list = [
    ["Cybersecurity Basics", "207", 1, 2, 2,
     ["Hassan Ali", "Mohamed Ibrahim", "Omar Samir"],
     ["Ali Mohammed", "Khaled Ahmed", "Osama Ismail"]],
    ["Web Development Fundamentals", "208", 1, 2, 2,
     ["Youssef Ahmed", "Karim Mohamed", "Mamdouh Adel"],
     ["Hany Youssef", "Mohsen Ali", "Sherif Ezzat"]],
    ["Artificial Intelligence Concepts", "209", 1, 2, 2,
     ["Amr Hossam", "Ali Mahmoud", "Tarek Hassan"],
     ["Adham Mostafa", "Hisham Amr", "Wael Mahmoud"]],
    ["Machine Learning Applications", "210", 1, 2, 2,
     ["Khaled Ahmed", "Amr Hossam", "Ali Mahmoud"],
     ["Ali Mahmoud", "Tarek Hassan", "Nabil Tawfiq"]],
    ["Data Science Essentials", "211", 1, 2, 2,
     ["Mahmoud Sami", "Youssef Ahmed", "Karim Mohamed"],
     ["Mamdouh Adel", "Ahmad Salah", "Adham Mostafa"]],
    ["Network Security Protocols", "212", 1, 2, 2,
     ["Ali Mahmoud", "Tarek Hassan","Mahmoud Sami"],
     ["Karim Mohamed", "Mamdouh Adel", "Ahmad Salah"]]
]

level3_courses_list = [
    ["Introduction to Cryptography", "301", 3, 1, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Web Development Advanced", "302", 4, 1, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Advanced AI Concepts", "303", 1, 2, 2,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Advanced Machine Learning", "304", 2, 2, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Advanced Data Science", "305", 1, 1, 3,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Advanced Network Security", "306", 1, 2, 2,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)]
]

level4_courses_list = [
    ["Advanced Cryptography", "401", 2, 2, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Cloud Computing", "402", 2, 2, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Computer Vision", "403", 2, 2, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Advanced Robotics", "404", 3, 1, 1,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Natural Language Processing", "405", 1, 2, 2,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)],
    ["Cyber-Physical Systems", "406", 2, 1, 2,
     choices(professors_names_list, k=3),
     choices(assistants_names_list, k=3)]
]

# Creating objects from the Course class based on the list
course1_1 = Course(*level1_courses_list[0])
course1_2 = Course(*level1_courses_list[1])
course1_3 = Course(*level1_courses_list[2])
course1_4 = Course(*level1_courses_list[3])
course1_5 = Course(*level1_courses_list[4])
course1_6 = Course(*level1_courses_list[5])

course2_1 = Course(*level2_courses_list[0])
course2_2 = Course(*level2_courses_list[1])
course2_3 = Course(*level2_courses_list[2])
course2_4 = Course(*level2_courses_list[3])
course2_5 = Course(*level2_courses_list[4])
course2_6 = Course(*level2_courses_list[5])

course3_1 = Course(*level3_courses_list[0])
course3_2 = Course(*level3_courses_list[1])
course3_3 = Course(*level3_courses_list[2])
course3_4 = Course(*level3_courses_list[3])
course3_5 = Course(*level3_courses_list[4])
course3_6 = Course(*level3_courses_list[5])

course4_1 = Course(*level4_courses_list[0])
course4_2 = Course(*level4_courses_list[1])
course4_3 = Course(*level4_courses_list[2])
course4_4 = Course(*level4_courses_list[3])
course4_5 = Course(*level4_courses_list[4])
course4_6 = Course(*level4_courses_list[5])

level_1_courses = [course1_1, course1_2, course1_3, course1_4, course1_5, course1_6]
levels_courses.append(level_1_courses)

level_2_courses = [course2_1, course2_2, course2_3, course2_4, course2_5, course2_6]
levels_courses.append(level_2_courses)

level_3_courses = [course3_1, course3_2, course3_3, course3_4, course3_5, course3_6]
levels_courses.append(level_3_courses)

level_4_courses = [course4_1, course4_2, course4_3, course4_4, course4_5, course4_6]
levels_courses.append(level_4_courses)

level1_classes = []
level2_classes = []
level3_classes = []
level4_classes = []

levels_classes = []

times = [{"day": "Saturday", "time": "09:00"}, {"day": "Saturday", "time": "10:30"},
         {"day": "Saturday", "time": "12:00"}, {"day": "Saturday", "time": "01:30"},
         {"day": "Saturday", "time": "03:00"},
         {"day": "Sunday", "time": "09:00"}, {"day": "Sunday", "time": "10:30"},
         {"day": "Sunday", "time": "12:00"}, {"day": "Sunday", "time": "01:30"},
         {"day": "Sunday", "time": "03:00"},
         {"day": "Monday", "time": "09:00"}, {"day": "Monday", "time": "10:30"},
         {"day": "Monday", "time": "12:00"}, {"day": "Monday", "time": "01:30"},
         {"day": "Monday", "time": "03:00"},
         {"day": "Tuesday", "time": "09:00"}, {"day": "Tuesday", "time": "10:30"},
         {"day": "Tuesday", "time": "12:00"}, {"day": "Tuesday", "time": "01:30"},
         {"day": "Tuesday", "time": "03:00"},
         {"day": "Wednesday", "time": "09:00"}, {"day": "Wednesday", "time": "10:30"},
         {"day": "Wednesday", "time": "12:00"}, {"day": "Wednesday", "time": "01:30"},
         {"day": "Wednesday", "time": "03:00"},
         {"day": "Thursday", "time": "09:00"}, {"day": "Thursday", "time": "10:30"},
         {"day": "Thursday", "time": "12:00"}, {"day": "Thursday", "time": "01:30"},
         {"day": "Thursday", "time": "03:00"}
         ]

level1_times = []
level2_times = []
level3_times = []
level4_times = []