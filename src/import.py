import pandas as pd
import csv,sys,os

# read csv file to dataframe
raw_data = pd.read_csv('list_of_cfi_awards_for_web.csv', encoding="ISO-8859-1")
df_raw = pd.DataFrame(raw_data)
columns_list = []
for i in df_raw.loc[0]:
    i_split = i.split('/')
    columns_list.append(i_split[0])
df_raw.columns = columns_list
df_raw = pd.DataFrame(df_raw[1:-2])
df_raw = df_raw.drop(['Sector (Area of Application)', 'Area of Application', 'Fund ',
                      'Project Title '], axis=1)


# convert string data to integer to represent money
df_money = df_raw
clean_int = [w.replace('$', '').replace(',', '') for w in df_money['Maximum CFI contribution ']]
df_raw['Maximum CFI contribution '] = pd.DataFrame(clean_int)
df_raw['Maximum CFI contribution '] = pd.to_numeric(df_money['Maximum CFI contribution '], downcast='integer')


# add new column with year of project implemented
df_raw['Final Decision '] = pd.to_datetime(df_raw['Final Decision '])
date_str_full = df_raw['Final Decision ']
full_year_list = ['']
for i, v in date_str_full.items():
    full_year_list.append(str(date_str_full.values[i-1])[:4])
del full_year_list[0]
df_raw['Year '] = full_year_list


# arrange setup for data importing

# Set the path to settings.py
project_dir = "F:/azamat/dev/trydjango/src/projector/"

# Add the path to sys.path variable
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# setup django settings
import django
django.setup()


from projects.models import Institution, Leader, Project, Province


# for index, row in df_raw.iterrows():
#     print(index)
#     project = Project()
#     project.province    = row[0]
#     project.institution = row[1]
#     project.leader      = row[2]
#     project.fund        = row[3]
#     project.date        = row[4]
#     project.keywords    = row[5]
#     project.sector      = row[6]
#     project.discipline  = row[7]
#     project.year        = row[8]
#     if index == 10387:
#         break
#     project.save()




for index, row in df_raw.iterrows():
    print(index)
    project = Institution()
    project.name    = row[0]

    if index == 10387:
        break
    project.save()

for index, row in df_raw.iterrows():
    print(index)
    project = Leader()
    project.name    = row[0]

    if index == 10387:
        break
    project.save()

for index, row in df_raw.iterrows():
    print(index)
    project = Province()
    project.name    = row[0]

    if index == 10387:
        break
    project.save()