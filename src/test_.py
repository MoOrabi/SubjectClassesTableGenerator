full_table = {1: {"sat": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "sun": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "mon": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "tue": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "wed": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "thu": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None}},
              2: {"sat": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "sun": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "mon": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "tue": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "wed": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "thu": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None}},
              3: {"sat": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "sun": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "mon": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "tue": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "wed": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "thu": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None}},
              4: {"sat": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "sun": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "mon": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "tue": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "wed": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None},
                  "thu": {"slot_1": None,
                          "slot_2": None,
                          "slot_3": None,
                          "slot_4": None,
                          "slot_5": None}}}

# print(full_table[1]["sat"]["slot_1"])

slots = {1: "slot_1",
         2: "slot_2",
         3: "slot_3",
         4: "slot_4",
         5: "slot_5"}

days = {1: "sat",
        2: "sun",
        3: "mon",
        4: "tue",
        5: "wed",
        6: "thu"}

# day, slot should be numbers
def add_class(course_code, day, slot, class_type):
    full_table[int(course_code[0])][days[day]][slots[slot]] = [course_code, class_type]

def check_table_free(level, day, slot):
    if full_table[level][days[day]][slots[slot]] == None:
        return True
    else:
        return False

print(check_table_free(1, 1, 1))
add_class("101", 1, 1, "lecture")
print(check_table_free(1, 1, 1))
print(full_table[1]["sat"]["slot_1"])
