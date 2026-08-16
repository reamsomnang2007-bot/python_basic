# Math-case statement (switch): an alternative to using many 'elif' statements
#                               execute some code if a value matches a 'case'
#                               benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Monday!"
#         case 2:
#             return "It is Tuesday!"
#         case 3:
#             return "It is Wednesday!"
#         case 4:
#             return "It is Thursday!"
#         case 5:
#             return "It is Friday!"
#         case 6:
#             return "It is Saturday!"
#         case 7:
#             return "It is Sunday!"
#         case _:
#             return "Not a valid day"
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tueseday" | "Wednesday"  | "Thursday" | "Friday":
#             return False
#         case _:
#             return False

# print(is_weekend("Somnang"))

def month_of_years(month):
    match month:
        case 1:
            return "It is Janurary!"
        case 2:
            return "It is Februry!"
        case 3:
            return "It is March!"
        case 4:
            return "It is April!"
        case 5:
            return "It is May!"
        case 6:
            return "It is June!"
        case 7:
            return "It is July!"
        case 8:
            return "It is August!"
        case 9:
            return "It is September!"
        case 10:
            return "It is October!"
        case 11:
            return "It is November!"
        case 12:
            return "It is December!"
        case _:
            return "Not a valid Month...!"
print(month_of_years(10))


        