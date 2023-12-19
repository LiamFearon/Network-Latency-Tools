with open('ping_results.txt', 'r') as file:
   lines = file.readlines()

ping_times = []

for line in lines:
   ping_time_index = line.find("time=")
   if ping_time_index != -1:
       ping_time_str = line[ping_time_index + 5:].split()[0]
       # Remove the "ms" unit from the ping time string
       ping_time_str = ping_time_str.replace('ms', '')
       try:
           ping_time = float(ping_time_str)
           ping_times.append(ping_time)
       except ValueError:
           print(f"Error converting to float: {ping_time_str}")
   else:
       print(f"Line did not match pattern: {line}")

if not ping_times:
   print("No ping times found in the file.")
else:
   # Store the ping times in a CSV file
   with open('ping_times.csv', 'w') as csv_file:
       csv_file.write('PingTime\n')
       for ping_time in ping_times:
           csv_file.write(f'{ping_time}\n')
