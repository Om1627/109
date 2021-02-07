import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
readingScore=[]
count=[]
df= pd.read_csv("StudentsPerformance.csv")

readingScore_list=df["reading score"].to_list()


mean=statistics.mean(readingScore_list)
median=statistics.median(readingScore_list)
mode=statistics.mode(readingScore_list)
print(mean,median,mode)

std_deviation=statistics.stdev(readingScore_list)
print(std_deviation)



f_std_start,f_std_end=mean-std_deviation,mean+std_deviation
list_1_std=[result for result in readingScore_list if result>f_std_start and result<f_std_end]
print("{}% of data lies within first standard deviation".format(len(list_1_std)*100.0/len(readingScore_list)))

s_std_start,s_std_end=mean-(2*std_deviation),mean+(2*std_deviation)
list_2_std=[result for result in readingScore_list if result>s_std_start and result<s_std_end]
print("{}% of data lies within second standard deviation".format(len(list_2_std)*100.0/len(readingScore_list)))

t_std_start,t_std_end=mean-(3*std_deviation),mean+(3*std_deviation)
list_3_std=[result for result in readingScore_list if result>t_std_start and result<t_std_end]
print("{}% of data lies within third standard deviation".format(len(list_3_std)*100.0/len(readingScore_list)))

fig=ff.create_distplot([df["reading score"].tolist()],["Reading score"],show_hist=False)
fig.show()


 
 

 
 

 
 

 
 

 
 

 
 

 
 

 
 

 
 

 
 

 
 

 

 
 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
