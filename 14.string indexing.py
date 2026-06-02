# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
credit_num = "123-456-789-321"
# print(credit_num[0:3])
# print(credit_num[4:7])
# print(credit_num[4:])
# print(credit_num[-1])
# print(credit_num[-4])
# print(credit_num[::3])
# print(credit_num[0:10:2])
# last_digits = credit_num[-4:]
credit_num = credit_num[::-1]
# print(f"XXX-XXX-XXX{last_digits}")
print(f"The number after reverse: {credit_num}")

