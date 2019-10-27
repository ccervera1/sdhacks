import inputs
import timer
import mongotime  # would use it to connect information to a database for further implementation
import employee

if __name__ == "__main__":
    person_tuple = inputs.setup()
    person = employee.Employee(
        person_tuple[0],  # first name
        person_tuple[1],  # last name
        person_tuple[2],  # employee name
        person_tuple[3],  # hourly
        person_tuple[4]  # overtime
    )
    mps = person.hourly / 60 ** 2
    ops = person.overtime / 60 ** 2
    start = timer.clock_in()
    break_seconds = 0
    while True:
        choice = input(
            '''
                   You're clocked in!
                    Choose an option
(t)ime lapsed | (m)oney earned | (c)lock out | (l)unch break
            '''
        )
        if choice == 't':
            timer.clock_run(start, break_seconds)
        elif choice == 'm':
            timer.money_run(start, break_seconds, mps, ops)
        elif choice == 'c':
            break
        elif choice == 'l':
            #  break_seconds += timer.diff(start).total_seconds()
            ntt = timer.lunch(start)  # new_time_tuple (time seconds passed, new time)
            break_seconds += ntt
        else:
            'Invalid entry!'
    end_time = timer.datetime.now()
    print(f'Clocked out at {end_time.time()}!\n'
          f'Total Time lapsed: {timer.diff(start, end_time).total_seconds()}\n'
          f'Total money earned: ${timer.money_run(start, break_seconds, mps, ops):.2f}')

    person.update_mood(timer.datetime.now().date(),
                       input('How was work today on a scale of 1-5?\n'))

    print('Thank you for your update! Good job at work today, now enjoy the rest of your day :)')

    print(
        '''
        ------------- back-end stuff --------------
        '''
    )

    for k, v in person.moods.items():
        print(f'On {k}, {person.name()} (ID: {person.employid}) rated their work day a {v} out of 5')
