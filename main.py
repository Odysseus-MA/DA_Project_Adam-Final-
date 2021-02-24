#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse and display data.
#Name: <Mihran Adam>
#Group Name: <Attack on Python>
#Class: <PN2004J>
#Date: <11/02/2021>
#Version: <1>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import matplotlib for pie chart
import matplotlib.pyplot as pit
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #display countries in asia-pacific
  asia_pacific = df.iloc[84:216, 9:14]
  df1 = df.iloc[84:216, 0:2]
  asiapacific_region = df1.join(asia_pacific) 

  #Display region and date selected + printing total country in region
  print("\n\n" + "Asia-Pacific Region was selected.")
  print("Total number of countries:", str(len(asiapacific_region.columns) - 2) + "\n")
  print("\n", asiapacific_region)
 

  #display top 3 countries with most amount of visitor in asia-pacific region between 1985-1995
  visitors = df.iloc[84:216, 9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
  print(visitors.to_string())

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #Initialize variables
  region = []
  new_year = []
  regional = ""
  yyyy_mm = ""
  z_year = ""
  regions = ['S.E.A', 'Asia-Pacific', 'South-Asia Pacific', 'Middle East', 'Europe', 'North America', 'Australia', 'Africa']
  x_range = ['1978-1987', '1988-1997', '1998-2007', '2008-2017']
  y_range = [1978, 1988, 1998, 2008]
  token = 0

  #Intialise "MonthlyVistiors.csv" for reading as df
  df = pd.read_csv('MonthyVisitors.csv')

  #convert string in list to integer
  #for i in range(0, len(y_range)):
    #y_range[i] = int(y_range[i])

  #User Input region
  print("\n\n" , regions)
  region = input('Enter a Region:')

  #Error Checking for region
  while True:
    #Ensure input is String before continuing
    region = str(region)
    #If input is not in Regions's list, print then break
    if not region in regions:
      print("Region is Invalid!!!")
      break
    #If input is in Regions's list it will continue
    elif region in regions:
      #If region = user input do this, if not skip
      if region == "S.E.A":
        #Parse data from csv to variable "regional"
        regional = df.iloc[: ,2:9]
        #token +1 to continue the program
        token += 1
        #Stop the program
        break
      elif region == "Asia-Pacific":
        regional = df.iloc[: ,9:14]
        token += 1
        break
      elif region == "South-Asia Pacific":
        regional = df.iloc[: ,14:17]
        token += 1
        break
      elif region == "Middle East":
        regional = df.iloc[: ,17:20]
        token += 1
        break
      elif region == "Europe":
        regional = df.iloc[: ,20:31]
        token += 1
        break
      elif region == "North America":
        regional = df.iloc[: ,31:33]
        token += 1
        break
      elif region == "Australia":
        regional = df.iloc[: ,33:35]
        token += 1
        break
      elif region == "Africa":
        regional = df.iloc[: ,35:36]
        token += 1
        break

  #token is needed to continue the program
  if token >= 1:
    #Display year range
    print('\n\n', x_range)
    while True:
      #User input year
      new_year = input("Enter a Starting Year: ")

      #Error checking for year
      try:
        new_year = int(new_year)
      except:
        print("Invalid format!!!")
      else:
        if new_year in y_range:
          if new_year == 1978:
            #Parse data from csv to variable "yyyy_mm"
            yyyy_mm = df.iloc[0:120, 0:2]
            #Set z_year as date range
            z_year = ["1978 - 1987"]
            token += 1
            break
          elif new_year == 1988:
            yyyy_mm = df.iloc[120:240, 0:2]
            z_year = ["1988 - 1997"]
            token += 1
            break
          elif new_year == 1998:
            yyyy_mm = df.iloc[240:360, 0:2]
            z_year = ["1998 - 2007"]
            token += 1
            break
          elif new_year == 2008:
            yyyy_mm = df.iloc[360:478, 0:2]
            z_year = ["2008 - 2017"]
            token += 1
            break
        else:
          print("Year is invalid")
          break

  if token >= 2:
    #Display region and date selected + printing total country in region
    print('\n\n' , "You have selected" , region , "region between the dates" , z_year)
    print("Total number of countries:", str(len(regional.columns)) + "\n")

    #Merge the "yyyy_mm" with "regional"
    result = yyyy_mm.join(regional)
    print("\n\n", result)

    #Pie Chart to display fixed data
    #Note: If given more time I might be able to display different region pie chart based on user input

    #Country names
    countries = ['Japan', 'Hong Kong', 'China', 'Taiwan', 'Korea']\
    #Amount of total visitors
    slices = [8979753, 2042240, 839684,3106422,1440946]
    #Pie chart color
    colours = ['r', 'g', 'b', 'o', 'p']

    #Pie chart customization
    pit.pie(slices,
            labels=countries,
            startangle=90,
            shadow=True,
            explode=(0.2, 0, 0, 0, 0),
            autopct='%1.2f%%')

    pit.legend()

    pit.show()

#########################################################################
#Main Branch: End of Code`
#########################################################################