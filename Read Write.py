# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:44:20 2021

@author: kulkarni Gaurav
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021
@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('E:/Skill Edge/Data Analytics Python/Data/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('E:/Skill Edge/Data Analytics Python/Data/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('E:/Skill Edge/Data Analytics Python/Data/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
