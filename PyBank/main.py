#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os,sys,csv


# In[21]:


#Sets Path for CSV file.
Budget = 'C:/Users/Thinh/Desktop/Data_Science_Assignment/python-challenge/PyBank/budget_data.csv'


# In[22]:


#Sets up Lists for calculating.

Total_Months=[];
Profit_Losses=[];


# In[23]:



#Opens budget_data.csv and appends the months and the Profits/Losses to the corresponding lists.
with open(Budget) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',');
    
    print(next(csvreader));
    
    for row in csvreader:
        Total_Months.append(row[0]);
        Profit_Losses.append(float(row[1]));
        


# In[26]:


Changes = [];
#Starting from the second month (Index of 1) the the change between Profit/Losses from month to month was calculated.
for i in range(1,len(Profit_Losses)):
        Changes.append(Profit_Losses[i]-Profit_Losses[i-1]);

#Gets the index of the max/min of the Changes list.
MaxCIndex=Changes.index(max(Changes));
MinCIndex=Changes.index(min(Changes));

    


# In[34]:




#Total Months is calculated by finding the size of the Total_Month list : len(Total_Months)
#Total is calculated by suming up the Profit_Losses list using sum(Profit_Losses)
#Average Change is calculated by calculating the sum of the Changes list sum(Profit_Losses) and dividing the by the size of the list len(Changes).

#Greatest Increase/Decrease month is calculating using the index of Max/Min of the Changes list. The + 1 to the index is to account for no change calculation present for the first month.

print(f"""
Total Months: {len(Total_Months)}
Total: ${sum(Profit_Losses)}
Average  Change: ${round(sum(Changes)/len(Changes),2)}
Greatest Increase in Profits: {Total_Months[MaxCIndex+1]} (${int(max(Changes))})
Greatest Decrease in Profits: {Total_Months[MinCIndex+1]} (${int(min(Changes))})
""")





# In[ ]:

# Opens a text file and writes the data summary to the file.
with open(os.path.join(sys.path[0],'BudgetSummary.txt'),'w') as TextFile:

    TextFile.write(f"""
Total Months: {len(Total_Months)}
Total: ${sum(Profit_Losses)}
Average  Change: ${round(sum(Changes)/len(Changes),2)}
Greatest Increase in Profits: {Total_Months[MaxCIndex+1]} $({int(max(Changes))})
Greatest Decrease in Profits: {Total_Months[MinCIndex+1]} $({int(min(Changes))})
""")


# In[ ]:




