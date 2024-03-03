# The cheese gifts project, an example of using the Hadoop ecosystem

## First part of the project
The reducer_lot2_exo1.py is used to create an excel file of lines red from the original csv file with clients zip code starting with 53, 28, 61 and 50 and for gifts send between 2010 and 2020.
To filter the csv file on your localhost and create the xlsx file, use the following command :
dataw_fro3.csv | python3 mapper_lot2_exo1.py | pyhton3 reducer_lot2_exo1.py