.ipynb_checkpoints/Linear Algebra with Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
%matplotlib inline
person = pd.DataFrame({'Name':['Asif' , 'Basit' , 'John', 'Hary'],
                       'DOB': ['3/20/1960', '3/19/1981', '9/12/1999' , '7/12/1967'],
                       'EmpID': ['E453', 'E983', 'E675','E120']})
person
person.dtypes
# Change the datatype of the column to Datetime
person['DOB']=pd.to_datetime(person['DOB']) 
person.dtypes
person
# Extract Month , Day , Year , 'Day of Week' and 'Week of Year' from the Date field 
person['Month'] = person.DOB.dt.month
person['Day'] = person.DOB.dt.day
person['Year'] = person.DOB.dt.year
person['Week Number'] =person.DOB.dt.isocalendar().week
person['Day Of Week'] = person.DOB.dt.dayofweek
person['Day Name']=pd.to_datetime(person['DOB']).dt.day_name()
person['Month Name']=pd.to_datetime(person['DOB']).dt.month_name()
person 
# Changing Datetime format to '%d/%m/%Y' using strftime()
person['DOB']=pd.to_datetime(person['DOB']).dt.strftime('%d/%m/%Y') # Note : This will change the datatype back to object
person
person.dtypes
# Changing Datetime format to ''%m-%d-%Y' using strftime()
person['DOB']=pd.to_datetime(person['DOB']).dt.strftime('%m-%d-%Y') # Note : This will change the datatype back to object
person
person.dtypes
# Find employees who are born after 12-20-1980
from datetime import date
person[pd.to_datetime(person['DOB']) > pd.Timestamp(date(1980,12,20))]
# Find employees who are born after 12-20-1980
from datetime import date
person[pd.to_datetime(person['DOB']) > pd.Timestamp('1980/12/20')]
# Find all records where DOB is between "12-20-1980" - "12-20-2000"
from datetime import date
person[(pd.to_datetime(person['DOB']) > pd.Timestamp(date(1980,12,20))) & 
       (pd.to_datetime(person['DOB']) < pd.Timestamp(date(2000,12,20)))]
# Min Date in a dataframe column
pd.to_datetime(person['DOB']).min()
# Max Date in a dataframe column
pd.to_datetime(person['DOB']).max()
# Current timestamp
timestamp = pd.to_datetime('now')
print('Timestamp :{}'.format(timestamp))

# Current Date (Today)
current_date=pd.to_datetime('now').date()
print('Current Date : {}'.format(current_date))

# Yesterday
yesterday = pd.to_datetime('now').date()- pd.Timedelta('1 day')
print('Yesterday: {}'.format(yesterday))

# tomorrow
tomorrow = pd.to_datetime('now').date() + pd.Timedelta('1 day')
print('Tomorrow: {}'.format(tomorrow))
#OR 
tomorrow = pd.to_datetime('now').date() + pd.DateOffset(days=1)
print('Tomorrow: {}'.format(tomorrow))

#Add Business Day to current date
add_buss_day=pd.to_datetime('now').date()+pd.offsets.BDay(1)
print('Date after adding Business Day: {}'.format(add_buss_day)) # Saturday & Sunday will be excluded

#Add 1 month to current date
add_month=pd.to_datetime('now').date()+pd.DateOffset(months=1)
print('Date after adding 1 month to current date: {}'.format(add_month)) 

# Date Difference in hours
diff_hrs= (pd.to_datetime('2021-03-26 21:11:13') - pd.to_datetime('2021-03-01 11:11:13')).total_seconds()//3600
print('Date Difference in hours: {}'.format(diff_hrs))
# Age of the person (Extract year from current time and subtract from Year column)
person['Age'] = pd.to_datetime('now').year - person['Year']
person

# OR 
person['Age'] = pd.to_datetime('now').year - pd.to_datetime(person['DOB']).dt.year
person 
# Lets work on simple dataset (Female birth Dataset)
# The source of the dataset is credited to Newton (1988).
female = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-total-female-births.csv')
female.head(10)
# Find min & max date to get the date range
pd.to_datetime(female['Date']).max()-pd.to_datetime(female['Date']).min()  # This is one year of dataset that we need to anlyse.
# Change datatype of Date column to Datetime
female['Date'] = pd.to_datetime(female['Date'])
# Create helper columns
female['Month'] = female.Date.dt.month
female['Day'] = female.Date.dt.day
female['Year'] = female.Date.dt.year
female['Week Number'] =female.Date.dt.isocalendar().week
female['Day Of Week'] = female.Date.dt.dayofweek
female['Day Name']=pd.to_datetime(female['Date']).dt.day_name()
female['Month Name']=pd.to_datetime(female['Date']).dt.month_name()

# OR We can use below lines of code as well
female['Month'] = female.Date.apply(lambda x:x.month)
female['Day'] = female.Date.apply(lambda x:x.day)
female['Year'] = female.Date.apply(lambda x:x.year)
female['Week Number'] =female.Date.apply(lambda x:x.week)
female['Day Of Week'] = female.Date.apply(lambda x:x.dayofweek)
female['Day Name']=pd.to_datetime(female['Date']).apply(lambda x:x.day_name())
female['Month Name']=pd.to_datetime(female['Date']).apply(lambda x:x.month_name())

female.head()
# Total female births in the month of January
female[female['Month Name'] =='January']['Births'].sum()
# Total female births in each month using for loop
for i in female['Month Name'].unique():
    print('Female births in {0} : {1}'.format(i,female[female['Month Name'] ==i]['Births'].sum()))
# Using "group by" to get female births in each month
female.groupby('Month Name').sum()[['Births']] # Month Name column data is not in ascending order.
# Use Pivot table to get female births in each month
pd.pivot_table(female,values=['Births'],index=['Month Name'],aggfunc=np.sum) # Month Name data is not in proper order.
pd.pivot_table(female,values=['Births'],index=['Month Name'],aggfunc=np.sum).plot.bar()
# We will convert "Month Name" column into Categorical variable and specify the ordering
order = ['January','February','March','April','May','June',
         'July','August','September','October','November','December']
 
female['Month Name']=pd.Categorical(female['Month Name'],order)
female.groupby('Month Name').sum()[['Births']] # Now the output is much better after custom ordering
# Bar plot to get monthly female births using matplotlib library
plt.figure(figsize=(14,6))
plt.bar(female.groupby('Month Name').sum().index,female.groupby('Month Name').sum()['Births'])
plt.show()
# Bar plot to get monthly female births using Pandas
pd.pivot_table(female,values=['Births'],index=['Month Name'],aggfunc=np.sum).plot.bar()
# Same way we can implement custom ordering for Day Name field
order=[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
female['Day Name']=pd.Categorical(female['Day Name'],order)
female.groupby('Day Name').sum()[['Births']] 
# Plot Bar Graph to show female births on day basis.
plt.figure(figsize=(14,6))
plt.bar(female.groupby('Day Name').sum().index,female.groupby('Day Name').sum()['Births'])
plt.show()
# Daily female births
plt.figure(figsize=(15,5))
plt.plot(female['Date'],female['Births'])
# Get all records for the month of Janaury(1959-01-01 - 1959-01-31). 
# Using boolean is not good method when we are dealing with large datasets.
female[(pd.to_datetime(female['Date']) > pd.Timestamp(date(1959,1,1))) & 
       (pd.to_datetime(female['Date']) < pd.Timestamp(date(1959,1,31)))]
# Convert date column into Datetime index for faster selection.
female = female.set_index(['Date'])
female
female.index # DatetimeIndex
# Now lets select the data
female.loc['1959'] # Get all data for year 1959
emale.loc['1960'] # There is no data for 1960. 
# Get all rows for the month of Janaury(1959-01-01 - 1959-01-31).
female.loc['1959-01-01':'1959-01-31'][['Births']]
# Get all rows for the month of Janaury(1959-01-01 - 1959-01-31).
female.loc['1959-01-01':'1959-01-31'][['Births']]
# plot line chart for January data using Pandas visualization
female.loc['1959-01-01':'1959-01-31'][['Births']].plot(figsize=(13,5))
# plot line chart for January data using Matplotlib library
plt.figure(figsize=(13,5))
plt.plot(female.loc['1959-01-01':'1959-01-31'][['Births']])
#Generate Test Dataset using date_range() and random.randint()
df = pd.DataFrame({'Date':pd.date_range('1/19/1920', periods = 1200, freq ='M') ,'SampleData':np.random.randint(0,200,size=1200)})
df=df.set_index(['Date']) # Set Date column as index
df
df.loc['2010':'2012'].plot(figsize=(16,5)) # Plot line chart for data between 2010-2012













import numpy as np
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
Merging Dataframes
emp1= pd.DataFrame({'empid':['E90','E87'],
                   'Name':['Asif','Basit']})
emp1


emp2= pd.DataFrame({'empid':['E22','E74','E90'],
                   'Name':['Minil','Akash','Asif']})
emp2


address= pd.DataFrame({'empid':['E87','E22','E49'], 
                   'City':['Mumbai','Banglore','Pune'] , 
                   'State':['Maharashtra','Karnataka','Maharashtra']})
address
#Concat Dataframes
# Method-1
employees = pd.concat([emp1,emp2])
employees
employees=employees.reset_index(drop=True)
employees
#Concat Dataframe
# Method-2
employees1 = emp1.append(emp2)
employees1
employees1=employees1.reset_index(drop=True)
employees1
employees2= pd.concat([emp1,emp2],ignore_index=True)
employees2
# Check for duplicates after concatenation
duplicates = employees[employees.duplicated()]
duplicates
# Remove duplicates
employees.drop_duplicates(keep='last',inplace=True)
employees
employees.reset_index(drop=True,inplace=True)
employees
employees
address
# Inner Join
inner = pd.merge(employees,address,on='empid')
inner
# Inner Join
inner = pd.merge(employees,address,on='empid',how='inner')
inner
# Left Outer Join
left = pd.merge(employees,address,on='empid',how='left')
left
# Right Outer Join
right = pd.merge(employees,address,on='empid',how='right')
right
employees
address
#Full outer join
full = pd.merge(employees,address,how='outer',on='empid')
full
# Salary Data
sal = pd.DataFrame({'empid':['E87','E22','E74','E90','E49'],
                    'salary':['$10,000','$30,000','$20,000','$60,000','$90,000']})
sal
# Add Salary details ( Merge sal & full dataframes)
employee_details = pd.merge(full,sal,how='inner',on='empid')
employee_details
# Employee experience
exp = pd.DataFrame({'employee_id':['E87','E22','E74','E90','E49'],
                    'experience':['5 years','3 years','7 years','2 years','10 years']})
exp 
# Add employee experinece using merge()
# As column names are different (empid , employee_id) we have to use left_on & right_on parameter
pd.merge(employee_details,exp,left_on=['empid'],right_on=['employee_id'],how='inner')
# Add employee experinece using merge() and drop the duplicate column (employee_id)
pd.merge(employee_details,exp,left_on=['empid'],right_on=['employee_id'],how='inner').drop('employee_id',axis=1)
#Save the dataframe
employee_details=pd.merge(employee_details,exp,
                          left_on=['empid'],
                          right_on=['employee_id'],
                          how='inner').drop('employee_id',axis=1)
employee_details
