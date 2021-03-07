# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061207.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
data2 = list(filter(lambda item: item['PRES'] != '-99.000', data))
target_data = list(filter(lambda item: item['PRES'] != '-999.000', data2))
C0A880 = list(filter(lambda item: item['station_id'] == 'C0A880', target_data))
C0F9A0 = list(filter(lambda item: item['station_id'] == 'C0F9A0', target_data))
C0G640 = list(filter(lambda item: item['station_id'] == 'C0G640', target_data))
C0R190 = list(filter(lambda item: item['station_id'] == 'C0R190', target_data))
C0X260 = list(filter(lambda item: item['station_id'] == 'C0X260', target_data))
for i in C0A880: i = i['PRES']
for i in C0F9A0: i = i['PRES']
for i in C0G640: i = i['PRES']
for i in C0R190: i = i['PRES']
for i in C0X260: i = i['PRES']
result = [
   ['C0A880', sum(C0A880) / len(C0A880)]
   ['C0F9A0', sum(C0F9A0) / len(C0F9A0)]
   ['C0G640', sum(C0G640) / len(C0G640)]
   ['C0R190', sum(C0R190) / len(C0R190)]
   ['C0X260', sum(C0X260) / len(C0X260)]]

#=======================================

# Part. 4
#=======================================
# Print result
print(result)
#========================================

