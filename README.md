# HR Attendance Over Zoom
I joined a new company. My HR has to download the zoom report for participants to mark attendance. Some people join from personal ID , some don't use middle name, some don't use employee code etc. She has to then map every name against the official list of employees. She does it by matching names and considering the duration. I made her life simple by making a script that takes in zoom csv file (1) and officialEmployeeList.txt(2) as input and spits out the list of people who attended or didn't attend the session. She also considers the duration attended and only then marks the attendance. The script takes duration as an command line argument.

The list of employees in .txt file is like follows:

<employee1_code> \
<employee1_name> \
<employee2_code> \
<employee2_name> \
...

The CSV file is in the following format

Name (Original Name), User Email, Join Time, Leave Time, Duration (Minutes) \
<employee1_name>, <emp1_email>, <date time>, <date time>, <time in minutes> \
...





