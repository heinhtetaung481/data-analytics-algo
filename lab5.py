import pandas as pd

offences = [145, 64, 434, 233, 5, 32]
index = ['speeding', 'drinking', 'running_redlights', 'reckless_driving', 'road_rage', 'passing_not_allowed']

# a(i)
cases = pd.Series(offences, index=index)
print('offences series\n', cases)

# a(ii)
print('no. of drinking offences\n', cases.drinking)

# a(iii)
cases.speeding = 20
print('updated speeding cases\n', cases)

# a(iv)
print('total number of traffic offences\n', cases.sum())

# b
num_cases = [100, 40, 5, 30, 34, 0, 404, 19, 11, 201, 31, 1]

# b(i)
traffic_offences_cases_dict = {
    'offence_type': ['speeding','speeding','speeding', 'drinking','drinking','drinking', 'running_redlights', 'running_redlights', 'running_redlights', 'reckless_driving', 'reckless_driving', 'reckless_driving'],
    'seriousness': ['low', 'middle', 'high'] * 4,
    'num_cases': num_cases
}

traffic_offences_cases = pd.DataFrame(traffic_offences_cases_dict)
print(traffic_offences_cases)

# b(ii)
print('cases more than 10\n', traffic_offences_cases[traffic_offences_cases.num_cases > 10])

# b(iii)
print('middle seriousness\n', traffic_offences_cases[traffic_offences_cases.seriousness == 'middle'])

# b(iv)
offence_types = traffic_offences_cases.offence_type.unique()
for type in offence_types:
    num_cases = traffic_offences_cases[traffic_offences_cases.offence_type == type].num_cases
    print(f'std for {type}', num_cases.std())

# b(v)
print('number of cases less than 10\n', traffic_offences_cases[traffic_offences_cases.num_cases < 10])