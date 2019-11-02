# import os
# import csv
#
# dir_path = os.getcwd()
# file_path = os.path.join(dir_path, "bigcsv.csv")
#
#
# bigdict = {'column_1': 1, 'column_2': 2, 'column_3': 3}
#
# with open(file_path, 'a+') as csv_file:
#     fieldnames = ['column_1', 'column_2', 'column_3']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
#     if '\n' not in csv_file.readlines()[-1]:
#         csv_file.write("\n")
#     writer.writerow(bigdict)

import csv

with open('./testerExportCSVFile.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])