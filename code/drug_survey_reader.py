from __future__ import print_function, division
import statsmodels.formula.api as smf

import numpy as np
import pandas
import nsfg
import first
import thinkstats2
import thinkplot


def GoMining(df):
    variables = []
    for name in df.columns:
        try:
            if df[name].var() < 1e-7:
                continue
            formula='depressed_ever_dummy ~ ' + name
            model = smf.logit(formula, data=df)
            nobs = len(model.endog)
            if nobs < len(df)/2:
                continue
            results = model.fit()  
        except:
            continue
        variables.append((results.prsquared, name))
    return variables


# source: http://www.icpsr.umich.edu/icpsrweb/ICPSR/studies/36361
# consult 36361-00001-Codebook.pdf for information on spreadsheet
drug_data = pandas.read_table('ICPSR_36361/DS0001/36361-0001-Data.tsv')
cigs_ever = drug_data['CIGEVER']

alc_try = drug_data['ALCTRY']
#depression_ever = drug_data['DEPRSLIF']
drug_data = drug_data[drug_data['DEPRSLIF'] > -1]
#hist = thinkstats2.Hist(depression_ever)
#thinkplot.Hist(hist)
#thinkplot.Show()



# OLS Fit
"""
inter, slope = thinkstats2.LeastSquares(alc_try, depression_ever)
fit_xs, fit_ys = thinkstats2.FitLine(alc_try, inter, slope)

alc_try_jittered = thinkstats2.Jitter(alc_try, 0.5)
depression_ever_jittered = thinkstats2.Jitter(depression_ever, 0.05)
thinkplot.Scatter(alc_try_jittered, depression_ever_jittered, color='blue', alpha=0.1, s=10)
thinkplot.Plot(fit_xs, fit_ys, color='red', linewidth=2)
thinkplot.Config(xlabel="First drink)",
                 ylabel='Depressed',
                 axis=[10, 70, -0.3, 1.3],
                 legend=False)
print(inter, slope)"""

# Logistic Regression

drug_data['depressed_ever_dummy'] = (drug_data['DEPRSLIF']).astype(int)

model = smf.logit('depressed_ever_dummy ~ ALCTRY', data=drug_data)
results = model.fit()
results.summary()


#Now trying other variables...
print("Trying other variables...")
variables = GoMining(drug_data)
print(variables)

#print(alc_try)
#print(depression_ever)
#print(type(drug_data['CIGEVER']))
#pmf = thinkstats2.Pmf(days_drank, label="Midwest")
#hist = thinkstats2.Hist(days_drank)