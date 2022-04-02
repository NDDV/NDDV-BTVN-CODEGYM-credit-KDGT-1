#%%
import matplotlib.pyplot as plt
import pandas as pd
import scipy 
import seaborn as sns

#%%
df = pd.read_csv("Credit_Scoring.csv")
df
#%%
#Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng có người phụ thuộc không (với mức ý nghĩa 10%)
df_2 = df[['NumberOfDependents','MonthlyIncome']]
df_2 = df_2.dropna()
df_kpt = df_2.loc[df_2['NumberOfDependents'] == 0.0]
df_kpt = df_kpt.reset_index(drop=True)
df_kpt
#%%
df_pt = df_2.loc[df_2['NumberOfDependents'] != 0.0]
df_pt = df_pt.reset_index(drop=True)
df_pt
# %%
df_1 = df[['NumberOfOpenCreditLinesAndLoans','SeriousDlqin2yrs']]
df_1.dropna()
df_kk=df_1.loc[df_1['SeriousDlqin2yrs'] == 1]
df_kk =df_kk.reset_index(drop=True)
df_kk
#%%
scipy.stats.ttest_ind(df_kpt['MonthlyIncome'],df_pt['MonthlyIncome'])

# %%
print("Kết luận: Do p_value << alpha và statistic<0, nên Bác bỏ Ho, chấp nhận H1 là những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng lớn hơn hơn những khách hàng có người phụ thuộc ")
# %%
#Có phải trung bình số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây (SeriousDlqin2yrs =1) thì sẽ cao hơn những khách hàng không gặp khó khăn không với mức ý nghĩa 10%
df_kk1=df_1.loc[df_1['SeriousDlqin2yrs'] == 0]
df_kk1 =df_kk1.reset_index(drop=True)
df_kk1

# %%
scipy.stats.ttest_ind(df_kk['NumberOfOpenCreditLinesAndLoans'],df_kk1['NumberOfOpenCreditLinesAndLoans'])

# %%
print("Kết luận: Do p_value << alpha và statistic<0, nên Bác bỏ Ho, chấp nhận H1 là trung bình số lượng khoản vaynhững khách hàng gặp khó khăn trong vòng 2 năm trở lại đây thì sẽ thấp hơn những khách hàng không gặp khó khăn")