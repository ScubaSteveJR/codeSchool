import numpy as np

job_titles = np.array(['Data Analyst', 'Data Scientist',
                      'Data Engineer', 'Macine Learning Engineer'])
base_salaries = np.array([60000, 80000, 75000, 90000])
bonus_rates = np.array([.05, .1, .08, .12])

total_salaries = base_salaries * (1 + bonus_rates)
print(total_salaries)
