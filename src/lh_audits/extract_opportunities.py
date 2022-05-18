import pandas as pd 
import matplotlib.pyplot as plt
import os

# read all csv files in current directory
path_to_csv = os.getcwd()
csv_files = [pos_csv for pos_csv in os.listdir(path_to_csv) if pos_csv.endswith('.csv')]
x = sorted(csv_files)



# separate all failed significant performance audits from individual reports and write it to a file "extracted_failed.csv"

for name in x:

    a = pd.read_csv(name)
    x = a["score"].loc[10:34].to_frame() # extract important performance audits
    i = (x[  (x['score'] < 0.90) & (x['score'] >= 0) ]).index # extract failed audits from important performance audits (Audits with a score between 0-0.9 are considered failed. Score ranges from 0-1)

    table = a.loc[i]['requestedUrl'].to_frame()
    table['titles'] = (a.loc[i])['title']

    x = len(i)
    
    empty_line = pd.DataFrame({1: [""], 2:[""]})
    empty_line.to_csv( 'extract_failed.csv', mode='a', index=False, header=False)

    if not table.empty:
        table.to_csv( 'extract_failed.csv', mode='a', index=False)
    else:
        extra = pd.DataFrame({'requestedUrl': [a.loc[1]['requestedUrl']], 'titles':["-"]})
        extra.to_csv( 'extract_failed.csv', mode='a', index=False)



# read extracted failed and count the frequency of every failed audit

a = pd.read_csv('extract_failed.csv')
os.remove('extract_failed.csv')
b = a.groupby('Unnamed: 1').size()
b.drop('titles', axis = 0, inplace= True)
b.drop('-', axis = 0, inplace= True)
c = b.to_frame('counts')
d = c.reset_index()
print(d)


d.sort_values('counts', inplace=True)
d.to_csv('failed_audits_freq.csv')

res = plt.barh(d['Unnamed: 1'], d['counts'])
plt.xticks(fontsize=18)
plt.yticks(fontsize=16)

plt.title("LH Failed audits on Alexa-500", fontsize=20)
plt.xlabel("Frequency", fontsize=18)
plt.xticks(rotation=0)
plt.show()