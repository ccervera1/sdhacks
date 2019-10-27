from datetime import datetime


def clock_in():
    start = datetime.now()
    print(f"Time start at {start.time()}")
    return start


def diff(start, end=None):
    if end == None:
        current = datetime.now()
        difference = current - start
        return difference
    else:
        current = end
        difference = current - start
        return difference



def clock_run(start: datetime, break_seconds) -> None:
    difference = diff(start)
    time_lapsed = difference.total_seconds() - break_seconds
    hours = divmod(time_lapsed, 60 ** 2)  # (hours, min remainder)
    min_sec = divmod(time_lapsed, 60)  # (min, sec remainder)
    print(f'{int(hours[0])} hours, {int(min_sec[0])} minutes, {int(min_sec[1])} seconds')


def money_run(start, break_seconds, mps, otp) -> None:
    seconds_passed = diff(start).total_seconds() - break_seconds
    money = seconds_passed * mps
    if seconds_passed // 60 ** 2 < 8:
        print(f'You\'ve earned ${money:.2f} so far!')
        return money
    else:  # overtime
        money = (60 ** 2) * mps
        overtime = money + (seconds_passed - 60 ** 2) * otp
        print(f'You\'ve earned ${overtime:.2f} so far! \n You\'re in overtime!')
        return overtime



def lunch(start):
    lunch_start = datetime.now()
    while True:
        choice = input(f'You\'re on break now {lunch_start}! Press enter to clock in again')
        if choice == '':
            break
        else:
            pass
    lunch_end = datetime.now()
    print(f'You\'re clocked back in! Time: {lunch_end.time()}')
    break_seconds = (lunch_end - lunch_start).total_seconds()
    print(break_seconds)
    return break_seconds


'''
def menu(start, mps) -> None:
    difference = datetime.now() - start
    option = input("You are clocked in select an option:\n \
                    Money (e)arned | Clock (o)ut | Resume (c)ountdown")
    if option == 'e':
        money = difference.total_seconds() * mps
        print(f'You\'ve earned ${money:.3} so far!\n (Without tax)')
    elif option == 'o':
        confirm = input('Are you sure you want to clock out? (y/n)')
        if confirm == 'y':
            end = datetime.now().time()
            print(f"Clocked out at {end}.")
        else:
            pass
    elif option == 'c':
        pass
    else:
        pass
'''

'''
    user_input = None
    print(type(start))
    while user_input != 'Out':
    user_input = input("You are clocked in select an option:\n"
                           "Time (passed) | Money (earned) | Clock (out)")
        if user_input.lower() == 'time':
            current = datetime.now()
            difference = current - start
            time_lapsed = difference.total_seconds()
            hours = divmod(time_lapsed, 120) # (hours, min remainder)
            min_sec = divmod(time_lapsed, 60) # (min, sec remainder)
            print(f'{hours[0]} hours, {min_sec[0]} minutes, {min_sec[1]:.3} seconds')
        elif user_input == '':
            break
        time.sleep(1)
        current = datetime.now()
        difference = current - start
        money_run(difference, mps)
    end = datetime.now().time()
    print(f"Clocked out at {end}.")
'''

if __name__ == '__main__':
    money_run(3000, 12 / 60 ** 2, 14 / 60 ** 2)
