# Python writing to a files (.txt, .json, .csv)

import json
import csv


employee = ["Ream Somnang", "Sokha Chhun", "Sopheap Chea", "Sokun Ngin", "Sophal Chum"]
txt_data = "I like Python programming."

employee1 = {
    "name": "Ream Somnang", 
    "Age": 18,
    "Job": "Collect Student in RUPP"
}

employees = [["Name", "Age", "Position"], 
             ["Ream Somnang", 18, "Software development"], 
             ["Meas Chandara", 18, "Computer science"],
             ["Tal Davith", 18, "Accounting"]]

# file_path = "C:\\Users\\TUF\\Desktop\\ITE_year_1\\output.txt"
# file_path = "C:\\Users\\TUF\\Desktop\\ITE_year_1\\output.json"
file_path = "C:\\Users\\TUF\\Desktop\\ITE_year_1\\output.csv"
try:
    with open(file_path, "w") as file:
        # file.write(txt_data)
        # for emp in employee:
        #     file.write(emp + "\n")
        # print(f"txt file '{file_path}' was created.")

        # json.dump(employee1, file)
        # print(f"json file '{file_path}' was created.")

        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created.")

except FileExistsError:
    print("That file already exists.")
