#!/usr/bin/env python
# coding: utf-8

# # <p style="font-family: Arial; font-size:2em;color:darkorange;"> Semestrální práce </p>
# ### <p style="font-family: Arial; font-size:1.4em;color:midnightblue;"> Analýza dat: Požáry Brazilských lesů </p>
# <p style="font-family: Arial; 1em; color:c;"> V semestrální práci se zabývám analýzou dat, která sleduje požáry v Brazilských pralesech. Data sledují situaci od roku 1998 až do roku 2016 skrz celý rok. </p>

# In[5]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[36]:


df = pd.read_csv('amazon.csv',encoding="ISO-8859-1")
df


# In[37]:


months_portugese=list(pd.unique(df['month']))
months_english=['January','February','March','April','May','June','July','August','September','October','November','December']
dict_month=dict(zip(months_portugese,months_english))
dict_month


# In[38]:


df.month=df['month'].map(dict_month)
df


# In[39]:


df.head(19)


# #### <p style="font-family: Arial; font-size:2em;color:olivedrab;"> Vypíšeme data, která máme v jednotlivých sloupcích.  </p>

# In[44]:


years = df["year"].unique()
years


# In[48]:


states = year_info['state'].unique()
states


# In[14]:


print("month : ", df['month'].unique())


# In[18]:


for col in df[['year', 'state', 'month']]:
    print('Unikátní hodnoty ve sloupci: %s' %col)
    print(df[col].unique())
    print('\n')

print('Počet unikátních hodnot: ')
print(df[['year', 'state', 'month']].nunique())


# #### <p style="font-family: Arial; font-size:2em;color:goldenrod;"> Vizualizace dat  </p>
# Nejprve jsou vypsány součty požárů za jednotlivé roky a v jednotlivých státech.
# Grafy ukazují počty požárů v jednotlivých státech.

# In[38]:


# Kolik požárů bylo za 19 let nahlášeno
print('Počet nahlášených požárů za 19 let:',df['number'].sum())


# In[39]:


# Tabulka požárů pro každý rok
table = pd.pivot_table(df,values="number",index=["year"],aggfunc=np.sum)
table


# In[69]:


# Vizualizace počty požárů za rok
data2 = pd.DataFrame(df.groupby('year')['number'].sum().reset_index())

plt.figure(figsize=(15,8))
sns.lineplot(x='year', y='number', data=data2, color='darkmagenta', lw=2)
plt.xlabel('Rok')
plt.ylabel('Počet požárů')
plt.title('Počet požárů v Brazílii za rok', fontsize=12)
plt.xlim(1998,2017)
plt.xticks(np.arange(1998, 2018, 1),fontsize=10)
plt.yticks(fontsize=10)


# In[91]:


# Tabulka požárů pro každý stát
table = pd.pivot_table(df,values="number",index=["state"],aggfunc=np.sum)
table


# In[57]:


# Druhá vizualizace požáry podle států

plt.figure(figsize = (15,10))
df[['state','number']].groupby(['state']).number.sum().sort_values(ascending=True).plot.barh(width=0.9,color=sns.color_palette('autumn',15))
plt.title('Počet požárů')
plt.show()


# In[40]:


data_98 = df.query("year == 1998")
print(data_98)


# In[42]:


df.loc[df.year == 2003]


# In[45]:


year_info = df[df["year"] == years[5]]
year_info.head(10)


# In[50]:


single_year_state = []

for state in states:
  state_name = state
  count_fire = year_info[year_info['state'] == state].number.sum()
  obj = {"state":state_name, "count_fire":count_fire}
  single_year_state.append(obj)
single_year_state


# In[51]:


year_state_df = pd.DataFrame(single_year_state)
year_state_df


# In[62]:


plt.figure(figsize=(15,8))
sns.set(style="whitegrid")
ax = sns.barplot(x="state",y="count_fire",data=year_state_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=35 )
plt.xlabel("Státy")
plt.ylabel("Součet požárů za rok 2003")
plt.title("Graf požárů za rok 2003")
plt.show()


# In[67]:


for year in years:
  year_info = df[df["year"] == year]
  states = year_info['state'].unique()

  single_year_state = []

  for state in states:
    state_name = state
    count_fire = year_info[year_info['state'] == state].number.sum()
    obj = {"state":state_name, "count_fire":count_fire}
    single_year_state.append(obj)

  year_state_df = pd.DataFrame(single_year_state)

  plt.figure(figsize=(15,9))
  sns.set(style="whitegrid")
  ax = sns.barplot(x="state",y="count_fire",data=year_state_df)
  ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
  plt.xlabel("Státy")
  plt.ylabel("Počet požárů v roce {0}".format(year))
  plt.title("Četnost požárů v roce {0}".format(year))
  plt.show()


# In[ ]:




