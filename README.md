# Understanding Child Mortality
## Studying Outliers


#### Project Proposal for cs169
#### by Ruchir Patel

GitLab on CS server: https://gitlab.cs.dartmouth.edu/ruchir/international-aid-and-health

### Hypothesis

1. Countries that receive more aid, must do better at Child Mortality rate.
2. Urbanization, Women Employment, GDP and Child Mortality must be inversely correlated
3. Adolescence fertility and Child Mortality must be correlated

### Goals

Goal 1. Visualize Aid, Visualize Child Mortality rates by Country


Goal 2. Study the outliers


Goal 3. Understanding factors of Child Mortalirty rate

### Datasets

1. World Bank official Aid Received: http://data.un.org/Data.aspx?q=Official+Development+Assistance&d=WDI&f=Indicator_Code%3aDT.ODA.ALLD.CD
2. Child Mortality Rate Dataset: https://ourworldindata.org/child-mortality
3. World Bank Economic Data: http://databank.worldbank.org/data/reports.aspx?source=jobs#

### Questions

1. Which countries are outliers when it comes to Child Mortality?
i.e. which coutnries that are suppose to do good aren't doing as well (US, India), and which countries despite being tiny countries with history of war are doing pretty well.
2. Why is Sri Lanka doing so good? Is there data significantly different from other countries?
3. Study United States, India, Rwanda

### Lessons Learned

Pros

1. High level perspective
2. Shows where a government’s priorities are
3. Which countries are serious about healthcare
4. GDP is NOT an excuse

Cons

1. Data -> Analysis -> Results -> Actions?
2. Impact?


### Future Steps

#### qualitative

Do qualitative analysis of outliers, geo-political and economical

Understand why outliers exist in the first place?

#### Quantitative

Detailed data about Child Mortality. Study the Causes, why are these kids dying.


Bridge the gap between
Data / Analysis / Results -> Actionable Items


Would like to look at GDP per capita by Purchasing Power Parity, rather than over GDP in percentage.

### Conclusion

I am shocked by some of the results I got.

1. GDP of a (most) country is not statistically significantly correlated to Child Mortality rates.
2. In Sri Lanka, which is doing a fantastic job at keeping childing mortality rate low, Urban Population is directly correlated with Child mortality rates. i.e. child mortality rate icnreases as more people move to urban areas.



Finland     3
US         44
Sri Lanka     61
Rwanda     133
India         135

Total        188



## References

[1] https://en.wikipedia.org/wiki/Multidimensional_scaling

[2] http://www.who.int/news-room/fact-sheets/detail/children-reducing-mortality

[3] https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.pearsonr.html

[4] http://www.projecthope.org/assets/documents/Child-Mortality-in-the-US-and-19-OECD.pdf

[5] https://www.indexmundi.com/facts/indicators/SH.DYN.MORT/rankings

[6] https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

[7] http://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html

### Base Code from

MDS: http://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html

Plot: https://pythonspot.com/matplotlib-bar-chart/

Graph: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html



# --------------------------------------------
This project has evolved over dicusssions with Professor Campbell and my older description and pitch is as below as we narrow down the scope


Because International Aid data is segregated by class, i.e. data specific to health aid is not recorded by UN. However, some countries independently publish that data.
# --- Older Description


# Understanding International Aid
# and It's Impact on Health

#### Project Proposal for cs169
#### by Ruchir Patel

GitLab on CS server: https://gitlab.cs.dartmouth.edu/ruchir/international-aid-and-health

### Goals

Goal 1. I want to primarily look at International Aid data to analyse where is the money coming from, and where it is going.


For example,

India receives a few billion dollars a year in Aid. India also gives a few Billion Dollar in Aids to neighbouring countries. I want to analyse & visualize where the flow originates.

Goal 2. Furthermore, I would like to find Aid data intended specifically for Health and measure the impact.

Goal 3. If time permits, I would also like to study the impact of aid by looking at correlation between trade & aid, to child mortality rates, poverty rates, and malaria rates in India and African Countries.

### Datasets

I want to start with UN Dataset, and US Aid datasets. Build a network, where each node is a country, and visualize the quantified world.

1. https://www.foreignassistance.gov/explore
2. https://comtrade.un.org
3. World Bank official Aid Received: http://data.un.org/Data.aspx?q=Official+Development+Assistance&d=WDI&f=Indicator_Code%3aDT.ODA.ALLD.CD
4. Bill & Melinda Gates Foundation dataset and results
5. Child Mortality Rate Dataset: https://ourworldindata.org/child-mortality

### Questions

1. Where the money is coming from and where is it going?
2. Does spending more money actually decrease the disease rates, decrease poverty?
3. Can effects of independent foundations like Bill & Melinda Gates Foundation be measured?
4. Are the rates of Malaria, Polio, and Child Mortality related to Trade, or Aid money?

### Related work

1. Official Stastical Report: http://www.oecd.org/dac/financing-sustainable-development/development-finance-data/ODA-2016-detailed-summary.pdf

2. http://aiddata.org/publications/apples-and-dragon-fruits-the-determinants-of-aid-and-other-forms-of-state-financing-from-china-to-africa-2

Non Western Countries have wide veriety of economic activities, and above paper looks into China's Official Development Assistence, and more commercially oriented sources of financing like debt financing for infrastructure and commerce. I would like to do similar analysis for India and Aid data.

### Webpage

https://ruchir594.github.io/cs169/


### Dataset Used

1. World Bank official Aid Received: http://data.un.org/Data.aspx?q=Official+Development+Assistance&d=WDI&f=Indicator_Code%3aDT.ODA.ALLD.CD
2. Child Mortality Rate Dataset: https://ourworldindata.org/child-mortality
3. World Bank Data: http://databank.worldbank.org/data/reports.aspx?source=jobs#

### Intriguing questions

1. Why is Sri Lanka doing so good?




