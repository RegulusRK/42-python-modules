def ft_harvest_informations(current_day, total_days):
    if (current_day > total_days):
        return
    print(f'Day {current_day}')
    ft_harvest_informations(current_day + 1, total_days)


def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))
    ft_harvest_informations(1, days)
    print('Harvest time!')
