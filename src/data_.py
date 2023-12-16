import professor_ as p
import course_ as c

full_table = {}

professors = [p.Professor("1", "Ahmed Mohamed",   "101", "301", "301"),
              p.Professor("2", "Hassan Ali",      "102", "302", "301"),
              p.Professor("3", "Mohamed Ibrahim", "103", "303", "301"),
              p.Professor("4", "Omar Samir",      "104", "304", "301"),
              p.Professor("5", "Khaled Ahmed",    "105", "305", "301"),
              p.Professor("6", "Amr Hossam",      "106", "306", "301"),
              p.Professor("7", "Ali Mahmoud",     "207", "401", "301"),
              p.Professor("8", "Tarek Hassan",    "208", "402", "301"),
              p.Professor("9", "Mahmoud Sami",    "209", "403", "301"),
              p.Professor("10", "Youssef Ahmed",  "210", "404", "301"),
              p.Professor("11", "Karim Mohamed",  "211", "405", "301"),
              p.Professor("12", "Mamdouh Adel",   "212", "406", "301")]

assistants = [p.Professor("13", "Ahmed Mohamed",   "101", "301", "301"),
              p.Professor("14", "Hassan Ali",      "102", "302", "301"),
              p.Professor("15", "Mohamed Ibrahim", "103", "303", "301"),
              p.Professor("16", "Omar Samir",      "104", "304", "301"),
              p.Professor("17", "Khaled Ahmed",    "105", "305", "301"),
              p.Professor("18", "Amr Hossam",      "106", "306", "301"),
              p.Professor("19", "Ali Mahmoud",     "207", "401", "301"),
              p.Professor("20", "Tarek Hassan",    "208", "402", "301"),
              p.Professor("21", "Mahmoud Sami",    "209", "403", "301"),
              p.Professor("22", "Youssef Ahmed",  "210", "404", "301"),
              p.Professor("23", "Karim Mohamed",  "211", "405", "301"),
              p.Professor("24", "Mamdouh Adel",   "212", "406", "301")]

courses = {"level_1": [c.Course("101", "Introduction to Programming",    2, 2, 1),
                       c.Course("102", "Data Structures and Algorithms", 2, 2, 1),
                       c.Course("103", "Database Management Systems",    2, 2, 1),
                       c.Course("104", "Computer Networks",              2, 2, 1),
                       c.Course("105", "Operating Systems",              2, 2, 1),
                       c.Course("106", "Software Engineering",           2, 2, 1)],
           "level_2": [c.Course("207", "Cybersecurity Basics",           2, 2, 1),
                       c.Course("208", "Web Development Fundamentals",   2, 2, 1),
                       c.Course("209", "Artificial Intelligence Concepts", 2, 2, 1),
                       c.Course("210", "Machine Learning Applications",  2, 2, 1),
                       c.Course("211", "Data Science Essentials",        2, 2, 1),
                       c.Course("212", "Network Security Protocols",     2, 2, 1)],
           "level_3": [c.Course("301", "Introduction to Cryptography",   2, 2, 1),
                       c.Course("302", "Web Development Advanced",       2, 2, 1),
                       c.Course("303", "Advanced AI Concepts",           2, 2, 1),
                       c.Course("304", "Advanced Machine Learning",      2, 2, 1),
                       c.Course("305", "Advanced Data Science",          2, 2, 1),
                       c.Course("306", "Advanced Network Security",      2, 2, 1)],
           "level_4": [c.Course("401", "Advanced Cryptography",          2, 2, 1),
                       c.Course("402", "Cloud Computing",                2, 2, 1),
                       c.Course("403", "Computer Vision",                2, 2, 1),
                       c.Course("404", "Advanced Robotics",              2, 2, 1),
                       c.Course("405", "Natural Language Processing",    2, 2, 1),
                       c.Course("406", "Cyber-Physical Systems",         2, 2, 1)]}


