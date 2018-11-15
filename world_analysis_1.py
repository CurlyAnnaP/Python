#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:02:02 2018

@author: annap, olak, percyf, elliott, hemants, philipp
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'world_data_hult_regions_2(2).xlsx'
regions = pd.read_excel(file)
pd.set_option('max_columns',200)

#check the whole data info
regions 


regions.describe().round(2)

regions.count()

latam = regions.iloc[115:136, :]

latam.count()

latam.info()

latam.describe().round(2)

#missing values test (if complete then False)

latam.isnull().any()

#number of missing values

latam.isnull().sum()

# % of missing values

(latam.isnull().sum()/len(latam)).round(2).sort_values(ascending = False)


# Flagging missing values in respective columns ('m'+col name)

for col in latam :
    if latam[col].isnull().any():
        latam['m'+col] = latam[col].isnull().astype(int)

        
# Creating three DataFrames with different fill in method of missing values

la_mean  = pd.DataFrame.copy(latam)


la_median = pd.DataFrame.copy(la_mean)


la_dropped = pd.DataFrame.copy(la_median)

# Next step is to impurte missing values to data frame (latam_clean)
# firstly with mean values:

for col in la_mean:
    if la_mean[col].isnull().any():
        col_mean = la_mean[col].mean()
        la_mean[col] = la_mean[col].fillna(col_mean).round(2)
        

# Filling in with median in la_median file
        
for col in la_median:
    if la_median[col].isnull().any():
        col_median = la_median[col].median()
        la_median[col] = la_median[col].fillna(col_median).round(2)

        
# Drop missinf values
        
la_dropped = la_dropped.dropna().round(2)


# Checking the means between the 4 files for col pct_female_employment 

print(latam['pct_female_employment'].mean())

print(la_mean['pct_female_employment'].mean())

print(la_median['pct_female_employment'].mean())

print(la_dropped['pct_female_employment'].mean())

# Checking if there is no missing values in the new 3 files

print(la_mean.isnull().any().any())

print(la_median.isnull().any().any())

print(la_dropped.isnull().any().any())


# create histograms for all columns to check skeweness (will we use mean or median?)
# using a loop to enumerat e over columns and creaste sns.distplot


for i, col in enumerate(la_mean.iloc[:, 5    :30]):
    plt.figure(i)
    sns.distplot(la_mean[col],
                 color='red')


for i, col in enumerate(la_median.iloc[:, 5:30]):
    plt.figure(i)
    sns.distplot(la_median[col],
                 color='blue')

for i, col in enumerate(la_dropped.iloc[:, 5:30]):
    plt.figure(i)
    sns.distplot(la_dropped[col],
                  color='green')

#find outlier from latam_mediam
    
for i, col in enumerate(la_median.iloc[:,5:30]):
    plt.figure(i)
    la_median.boxplot(column = [col],
                 vert = False,
                 manage_xticks = True,
                 patch_artist = True,
                 meanline = True,
                 showmeans = True)
    plt.title(col)
    plt.show()

    
# Outliers detection and elimination & Setting limits 
    
# 1 access_to_electricity_pop
access_to_electricity_pop_lo = 80
 
# 2 access_to_electricity_rural
access_to_electricity_rural_lo = 40

# access_to_electricity_urban
access_to_electricity_urban_lo = 85
 
# CO2_emissions_per_capita
CO2_emissions_per_capita_hi = 10
 
# exports_pct_gdp 
exports_pct_gdp_hi = 100

# fdi_pct_gdp
fdi_pct_gdp_hi = 20

# gdp_usd
gdp_usd_hi = 0.2e+12

# incidence_hiv
incidence_hiv_hi = 0.2

# adult literacy
adult_literacy_low = 80

# homicides_per_100k
homicides_per_100k_hi = 60

# avg_air_pollution
avg_air_pollution_hi = 40 

# child_mortality_per_1k
child_mortality_per_1k_hi = 40

# female_employment
pct_female_employment_hi = 5

# male employment
pct_male_employment_hi = 5

# industry employment
pct_industry_employment_hi = 25


# Outlier flagging:
####################################

# access_to_electricity_pop
la_median['out_access_to_electricity_pop'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'access_to_electricity_pop']):
    
    if val[1] < access_to_electricity_pop_lo:
        la_median.loc[val[0], 'out_access_to_electricity_pop'] = 1

la_median['out_access_to_electricity_pop'].abs().sum()


# access_to_electricity_rural
la_median['out_access_to_electricity_rural'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'access_to_electricity_rural']):
    
    if val[1] < access_to_electricity_rural_lo:
        la_median.loc[val[0], 'out_access_to_electricity_rural'] = 1

la_median['out_access_to_electricity_rural'].abs().sum()


# access_to_electricity_urban
la_median['out_access_to_electricity_urban'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'access_to_electricity_urban']):
    
    if val[1] < access_to_electricity_urban_lo:
        la_median.loc[val[0], 'out_access_to_electricity_urban'] = 1

la_median['out_access_to_electricity_urban'].abs().sum()


# CO2_emissions_per_capita
la_median['out_CO2_emissions_per_capita'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'CO2_emissions_per_capita']):
    
    if val[1] > CO2_emissions_per_capita_hi:
        la_median.loc[val[0], 'out_CO2_emissions_per_capita'] = 1

la_median['out_CO2_emissions_per_capita'].abs().sum()


# exports_pct_gdp_hi
la_median['out_exports_pct_gdp'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'exports_pct_gdp']):
    
    if val[1] > exports_pct_gdp_hi:
        la_median.loc[val[0], 'out_exports_pct_gdp'] = 1

la_median['out_exports_pct_gdp'].abs().sum()


# incidence_hiv
la_median['out_incidence_hiv'] = 0
la_median.index = range(21)

for val in enumerate(la_median.loc[ : , 'incidence_hiv']):
    
    if val[1] > incidence_hiv_hi:
        la_median.loc[val[0], 'out_incidence_hiv'] = 1

la_median['out_incidence_hiv'].abs().sum()


# adult_literacy_pct
la_median['out_adult_literacy_pct'] = 0

for val in enumerate(la_median.loc[ : , 'adult_literacy_pct']):
    
    if val[1] < adult_literacy_low:
        la_median.loc[val[0], 'out_adult_literacy_pct'] = 1

la_median['adult_literacy_pct'].abs().sum()    


# homicides_per_100k
la_median['out_homicides_per_100k'] = 0

for val in enumerate(la_median.loc[ : , 'homicides_per_100k']):
    
    if val[1] > homicides_per_100k_hi:
        la_median.loc[val[0], 'out_homicides_per_100k'] = 1

la_median['out_homicides_per_100k'].abs().sum()       
     

# avg_air_pollution
la_median['out_avg_air_pollution'] = 0

for val in enumerate(la_median.loc[ : , 'avg_air_pollution']):
    
    if val[1] > avg_air_pollution_hi:
        la_median.loc[val[0], 'out_avg_air_pollution'] = 1

la_median['out_avg_air_pollution'].abs().sum()       


# child_mortality_per_1k
la_median['out_child_mortality_per_1k'] = 0

for val in enumerate(la_median.loc[ : , 'child_mortality_per_1k']):
    
    if val[1] > child_mortality_per_1k_hi:
        la_median.loc[val[0], 'out_child_mortality_per_1k'] = 1   

la_median['out_child_mortality_per_1k'].abs().sum()


# pct_female_employment
la_median['out_pct_female_employment'] = 0

for val in enumerate(la_median.loc[ : , 'pct_female_employment']):
    
    if val[1] > pct_female_employment_hi:
        la_median.loc[val[0], 'out_pct_female_employment'] = 1

la_median['out_pct_female_employment'].abs().sum()


# pct_male_employment
la_median['out_pct_male_employment'] = 0

for val in enumerate(la_median.loc[ : , 'pct_male_employment']):
    
    if val[1] > pct_male_employment_hi:
        la_median.loc[val[0], 'out_pct_male_employment'] = 1

la_median['out_pct_male_employment'].abs().sum()


# pct_industry_employment
la_median['out_pct_industry_employment'] = 0

for val in enumerate(la_median.loc[ : , 'pct_industry_employment']):
    
    if val[1] > pct_industry_employment_hi:
        la_median.loc[val[0], 'out_pct_industry_employment'] = 1

la_median['out_pct_industry_employment'].abs().sum()




# Visualization
#######################################################################

#### Correlation matricies


# Create clean la_median without flagged missing values and outliers
la_clean = la_median.iloc[:, 4:30]

la_clean["income_group"] = la_clean["income_group"].map(
        {"Low income": 1,
         "Lower middle income": 2,
         "Upper middle income": 3,
         "High income": 4})


la_corr = la_clean.corr().round(2)
print(la_corr)

# Heatmaps
########################

# Using palplot to view a color scheme
sns.palplot(sns.color_palette('coolwarm', 12))

fig, ax = plt.subplots(figsize=(15,15))

sns.heatmap(la_corr,
            cmap = 'coolwarm',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5)


plt.savefig('LATAM Heatmap 2.png')
plt.show()


plt.show()
plt.savefig('heatmap2.png')

### pct_female_employment

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["pct_female_employment"],
                 notch=False,
                 palette="Blues",
                
                 width = 0.6
                 )

plt.title('Percentage Female Employment')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))
ax = sns.swarmplot(x='pct_female_employment',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   edgecolor="black",
                   linewidth=1,
                   size=8)

plt.xlabel('Female Employment [%]')
plt.ylabel('')
plt.xlim(0, 2)

plt.savefig('pct_female_pct_big.png')


### GDP USD

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["gdp_usd"],
                 notch=False,
                 palette="Blues",
                 width = 0.6
                 )

plt.title('Gross Domestic Product')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))

ax = sns.swarmplot(x='gdp_usd',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   size=8,
                   edgecolor="black",
                   linewidth=1
                   )

plt.xlabel('GDP [USD]')
plt.ylabel('')
plt.xlim(0, 0.2e+12)

plt.savefig('gdp_usd_big_2.png')



####  lmplot for GDP vs Income Group withlabels 
my_plot = sns.lmplot(x = 'gdp_usd',
           y = 'income_group',
           data = la_clean,
           size=8,   
           scatter_kws= {"marker": "D", 
                        "s": 100},
            line_kws={'color': 'orange'},
            aspect=2 
           )
fake = pd.DataFrame({'cat': ['0','Low', 'Lower middle', 'Upper middle', 'High'], 'val': [0, 1, 2, 3, 4]})
fig = sns.barplot(x = 'val', y = 'cat', 
                  data = fake, 
                  color = 'black')
plt.ylim(0,5)
plt.xlim(0,0.2e+12)
plt.xlabel('GDP')
plt.ylabel('Income Group')
plt.savefig('GDP & Income correlation.png')
plt.show()

#### Child Mortality

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["child_mortality_per_1k"],
                 notch=False,
                 palette="Blues",
                 width = 0.6
                 )

plt.title('Child Mortality per 1K')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))

ax = sns.swarmplot(x='child_mortality_per_1k',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   size=8,
                   edgecolor="black",
                   linewidth=1
                   )

plt.xlabel('child mortality per 1k')
plt.ylabel('')
plt.xlim(0, 75)

plt.savefig('Chlid_mortality_per_1k.png')



##### Adult Literacy
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["adult_literacy_pct"],
                 notch=False,
                 palette="Blues",
                 width = 0.6
                 )

plt.title('Adult Literacy')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))

ax = sns.swarmplot(x='adult_literacy_pct',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   size=8,
                   edgecolor="black",
                   linewidth=1
                   )

plt.xlabel('Adult Literacy [%]')
plt.ylabel('')
plt.xlim(0.5, 1.05)

plt.savefig('Adult_Literacy_pct.png')


#### Access to Electricity
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["access_to_electricity_pop"],
                 notch=False,
                 palette="Blues",
                 width = 0.6
                 )

plt.title('Access to Electricity')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))

ax = sns.swarmplot(x='access_to_electricity_pop',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   size=8,
                   edgecolor="black",
                   linewidth=1
                   )

plt.xlabel('Access to Electricity [% of population]')
plt.ylabel('')
plt.xlim(0.2, 1.05)

plt.savefig('Access_to_electricity_pop.png')

####  Chlild Mortality x Adult Literacy

sns.lmplot(x = 'adult_literacy_pct',
           y = 'child_mortality_per_1k',
           data = la_clean,
           size = 8,
           fit_reg = True,
           scatter_kws= {"marker": "D", 
                        "s": 100},
           palette = 'plasma',
           aspect = 2)

plt.title("Child Mortality & Adult Literacy")
plt.ylabel('Child Mortality per 1K')
plt.xlabel('Adult Literacy [%]')
plt.tight_layout()
plt.show()

plt.savefig('Chlid Mordtality x Adult Literacy.png')

#### Chlild Mortality x Access to Electricy

sns.lmplot(x = 'access_to_electricity_pop',
           y = 'child_mortality_per_1k',
           data = la_clean,
           size = 8,
           fit_reg = True,
           scatter_kws= {"marker": "D", 
                        "s": 100},
           palette = 'Blues',
           aspect = 2)

plt.title("Child Mortality & Access to Electricity")
plt.ylabel('Child Mortality per 1K')
plt.xlabel('Access to Electricity [%]')
plt.tight_layout()
plt.show()

plt.savefig('Chlid Mordtality x Access to Electricity.png')


#### Adult Literacy x Access to Electricy

sns.lmplot(x = 'access_to_electricity_pop',
           y = 'adult_literacy_pct',
           data = la_clean,
           size = 8,
           scatter_kws= {"marker": "D", 
                        "s": 100},
           aspect = 2)

plt.title("Adult Literacy & Access to Electricity")
plt.ylabel('Adult Literacy [%]')
plt.xlabel('Access to Electricity [%]')
plt.tight_layout()
plt.show()

plt.savefig('Adult Literacy x Access to Electricity.png')


#### Adult Literacy x Access to Electricity

sns.lmplot(x = 'access_to_electricity_pop',
           y = 'adult_literacy_pct',
           data = la_clean,
           size = 8,
           scatter_kws= {"marker": "D", 
                        "s": 100},
           aspect = 2)

plt.title("Adult Literacy & Access to Electricity")
plt.ylabel('Adult Literacy [%]')
plt.xlabel('Access to Electricity [%]')
plt.tight_layout()
plt.show()

plt.savefig('Adult Literacy x Access to Electricity.png')


#### Boxplot for HIV 
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,2))

ax = sns.boxplot(x=la_clean["incidence_hiv"],
                 notch=False,
                 palette="Blues",
                 width = 0.6
                 )

plt.title('incidence_hiv')


# Transparency
for patch in ax.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))

ax = sns.swarmplot(x='incidence_hiv',
                   data=la_clean,
                   color="red",
                   alpha=1,
                   size=8,
                   edgecolor="black",
                   linewidth=1
                   )

plt.xlabel('')
plt.ylabel('')
plt.xlim(0, 0.90)

plt.savefig('incidence_hiv.png')

#### correlation between Air pollution and HIV 
 
my_plot = sns.lmplot(x = 'incidence_hiv',
           y = 'avg_air_pollution',
           data = la_median,
           size=8,   
           scatter_kws= {"marker": "D", 
                        "s": 100},
             line_kws={'color': 'red'},
            aspect=2 
           )
#plt.ylim(0,5)
#plt.xlim(0,0.2e+12)
plt.xlabel('Incident HIV')
plt.ylabel('Air Pollution')
plt.savefig('HIV & Air Pollution.png')
plt.show()






#### correlation between CO2 emissions and HIV 
 
my_plot = sns.lmplot(x = 'incidence_hiv',
           y = 'CO2_emissions_per_capita',
           data = la_median,
           size=8,   
           scatter_kws= {"marker": "D", 
                        "s": 100},
             line_kws={'color': 'green'},
            aspect=2 
           )
#plt.ylim(0,5)
#plt.xlim(0,0.2e+12)
plt.xlabel('Incident HIV')
plt.ylabel('CO2 emissions')
plt.savefig('HIV & CO2 emissions.png')
plt.show()


