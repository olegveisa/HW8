from datetime import datetime

users = [
        {"name": "Harry",
        'birthday': datetime(year=2002, month=1, day=15)},
        {'name': 'Ron',
        'birthday': datetime(year=2000, month=1, day=2)},
        {'name': 'Hermione',
        'birthday': datetime(year=2000, month=1, day=8)},
        {'name': 'Tom',
        'birthday': datetime(year=2000, month=1, day=7)}
        ]

list_of_birthdays = {"day_0": "Monday", "name_0": [],
                    "day_1": "Tuesday", "name_1": [],
                    "day_2": "Wednesday", "name_2": [],
                    "day_3": "Thursday", "name_3": [],
                    "day_4": "Friday", "name_4": []
                    }


def get_birthdays_per_week(users, n_days):

    current_date = datetime.now()

    for user in users:

        user_name = user.get('name')
        user_date = user.get('birthday')
        user_date = user_date.replace(year=current_date.year)
        weekday = user_date.weekday()
        delta_days = user_date - current_date
        
        if delta_days.days <= n_days:
            if weekday in [5, 6]:
                list_of_birthdays["name_0"].append(user_name)
            else:
                list_of_birthdays[f"name_{weekday}"].append(user_name)

        else:
            user_date = user_date.replace(year=user_date.year + 1)
            delta_days = user_date - current_date
            if delta_days.days <= n_days:
                if weekday in [5, 6]:
                    list_of_birthdays["name_0"].append(user_name)
                else:
                    list_of_birthdays[f"name_{weekday}"].append(user_name)
    
    for i in range(6):
        if not list_of_birthdays[f"name_{i}"]:
            continue
        else:
            print(list_of_birthdays[f"day_{i}"]+":", ", ".join(list_of_birthdays[f"name_{i}"]))


def main():
    get_birthdays_per_week(users, 7)


if __name__ == '__main__':
    main()