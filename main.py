##################### Extra Hard Starting Project ######################


# import pandas
# import random
# import smtplib
# from datetime import date
#
#
# MY_EMAIL = "test@example.com"
# MY_PASSWORD = "abcd1234()"
#
# today = date.today()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdate_dict = data.to_dict(orient="records")

# MY SOLUTION (UNTESTED)

# Check if today matches a birthday in the birthdays.csv
# def return_current_birthdays():
#     current_birthdays = []
#     for birthdate in birthdate_dict:
#         if birthdate["month"] == today.month and birthdate["day"] == today.day:
#             current_birthdays.append({"name": birthdate["name"], "email": birthdate["email"]})
#     return current_birthdays
#
#
# def send_birthday_letters(current_birthdays):
#     birthday_letters = []
#     for name in current_birthdays:
#         random_letter_number = random.choice(range(1,4))
#         with open(f"letter_templates/letter_{random_letter_number}.txt", mode="r") as birthday_letter_template:
#             with open(f"{name["name"]}_{today.year}_birthday_letter.txt", mode="w") as birthday_letter:
#                 for line in birthday_letter_template.readlines():
#                     birthday_letter.write(line.replace("[NAME]", name["name"]))
                # with smtplib.SMTP("smt.gmail.com") as connection:
                #     connection.starttls()
                #     connection.login(MY_EMAIL, MY_PASSWORD)
                    # connection.sendmail(from_addr=MY_EMAIL,
                    #                     to_addrs=name["email"],
                    #                     msg=f"{name["name"]}_{today.year}_birthday_letter.txt")


# current_birthday_list = return_current_birthdays()
# send_birthday_letters(current_birthday_list)



# COURSE SOLUTION

import pandas
import random
import smtplib
from datetime import date


MY_EMAIL = "test@example.com"
MY_PASSWORD = "abcd1234()"

today = date.today()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




