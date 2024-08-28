import os
import glob
import pandas as pd
# import statistics
# import pandas as pd
import numpy as np
# import scipy.stats, math
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.patches import Rectangle
import matplotlib.pyplot
from pylab import rcParams
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
from numpy import tile

# function to merge multiple csv under the given directory 
def merge_multiple_csv(dir, file_name):
    owd = os.getcwd()
    os.chdir(dir)

    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( file_name, index=False, encoding='utf-8-sig')
    os.chdir(owd)

merge_multiple_csv("Dataset/Malay", "malay_combined.csv")
merge_multiple_csv("Dataset/Mandarin", "mandarin_combined.csv")
merge_multiple_csv("Dataset/Tamil", "tamil_combined.csv")

def clean_data(fileBasePath, fileName, language):
    # Data Cleaning
    temp_df = pd.read_csv(fileBasePath + fileName)
    # remove unnecessary columns Q9 onward
    temp_df = temp_df.drop(columns=temp_df.columns[12:])

    # remove rows and columns with Null value
    temp_df = temp_df.dropna()

    # remove duplicates (Subject ID, Examiner ID)
    temp_df = temp_df.drop_duplicates(subset=['Subject ID', 'Examiner ID'], keep='first')

    # convert Subject ID to uppercase
    temp_df['Subject ID'] = temp_df['Subject ID'].str.upper()

    # remove rows with the question values are invalid/out of range
    valid_range = [-2,-1,0,1,2]
    keep = {}
    for i in range(1,9):
        keep[f'Q{i}'] = valid_range

    temp_df = temp_df[temp_df[list(keep)].isin(keep).all(axis=1)]

    # language name must be unique
    temp_df = temp_df[temp_df['Language'] == language]

    # split and remove date values from Subject ID column
    temp_df['Subject ID'] = temp_df['Subject ID'].str.split('_').str[0]

    # remove the row if the examiner ID column is containing "test" string
    temp_df = temp_df[temp_df['Examiner ID'].str.contains("test") == False]
    # print(temp_df)

    # export to csv file into given dir with modified file name
    temp_df.to_csv(f"{fileBasePath}{language}_combined_cleansed.csv", index=False)


# language name (last parameter) has to start with uppercase (eg. Malay)
clean_data('Dataset/Malay/', 'malay_combined.csv', 'Malay')
clean_data('Dataset/Mandarin/', 'mandarin_combined.csv', 'Mandarin')
clean_data('Dataset/Tamil/', 'tamil_combined.csv', 'Tamil')


##***Continue after data cleaning***###

##Data Exploration By Geraldine

##Read Malay csv
Malay_df = pd.read_csv("Dataset/Malay/Malay_combined_cleansed.csv")
Mandarin_df = pd.read_csv("Dataset/Mandarin/Mandarin_combined_cleansed.csv")
Tamil_df = pd.read_csv("Dataset/Tamil/Tamil_combined_cleansed.csv")

##Plot histogram by question and rating in a graph
## In general, rate each question based on highest rating across languages
def generate_hist_graph(df, titles, fig, axs, language):
    title_index = 0
    for i in range(3):
        for j in range(3):
            if title_index < len(titles):
                title = titles[title_index]
                axs[i,j].set_xlim([-2, 2])
                axs[i,j].set_xticks(np.arange(-2, 3, 1))
                #Add title and axis names
                axs[i,j].set_title(f'{language} - {title}')
                axs[i,j].set_xlabel('Rating')
                axs[i,j].set_ylabel('Sum of Students Rating')
                axs[i,j].hist(df[title])
                title_index += 1
    sum = df.sum(axis=0)
    print(f"{language} Sum by Question \n", sum)
    fig.delaxes(axs[2,2])

questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
fig, axs = plt.subplots(3,3, figsize=(30,30))
plt.subplots_adjust(hspace=0.5)
generate_hist_graph(Malay_df, questions, fig, axs, 'Malay')
plt.show()

fig, axs = plt.subplots(3,3, figsize=(30,30))
plt.subplots_adjust(hspace=0.5)
generate_hist_graph(Mandarin_df, questions, fig, axs, 'Mandarin')
plt.show()

fig, axs = plt.subplots(3,3, figsize=(30,30))
plt.subplots_adjust(hspace=0.5)
generate_hist_graph(Tamil_df, questions, fig, axs, 'Tamil')
plt.show()

# # Python codes by Sandi / Mean Comparison
mandarin = pd.read_csv('Dataset/Mandarin/mandarin_combined_cleansed.csv')
df_mandarin = pd.DataFrame(mandarin,columns=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8'])
# print(df_mandarin)

malay = pd.read_csv('Dataset/Malay/malay_combined_cleansed.csv')
df_malay = pd.DataFrame(malay,columns=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8'])

tamil = pd.read_csv('Dataset/Tamil/tamil_combined_cleansed.csv')
df_tamil = pd.DataFrame(tamil,columns=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8'])

# Null Hypothesis: Mean of student average score is equal to 0.
# Alternative Hypothesis: Mean of student average score is not equal to 0.

# Mandarin
# average score of each student (sample mean)
mandarin_mean = df_mandarin.mean(axis=1)
# print(mandarin_mean)
fig, axs = plt.subplots(2,2, figsize=(30,30))
plt.subplots_adjust(hspace=0.5)

# 1 sample t-test
print(stats.ttest_1samp(mandarin_mean,0))
# since p-value is <0.05, we conclude that mean of student average score in Mandarin language is not equal to 0.

# distribution of sample mean
sns.distplot(mandarin_mean, hist = True, color = 'darkblue',kde=False, ax=axs[0,0],
            hist_kws={'edgecolor':'black'}).set(xlabel = 'Mandarin Survey Result',
                                                ylabel = 'Density')
# plt.show()
# population mean
print('Mandarin Population Mean',mandarin_mean.mean())

# Malay
# average score of each student (sample mean)
malay_mean = df_malay.mean(axis=1)
# print(malay_mean)
#
# 1 sample t-test
print(stats.ttest_1samp(malay_mean,0))
# since p-value is <0.05, we conclude that mean of student average score in Malay language is not equal to 0.

# distribution of sample mean
sns.distplot(malay_mean, hist = True, color = 'darkblue',kde=False, ax=axs[0,1],
            hist_kws={'edgecolor':'black'}).set(xlabel = 'Malay Survey Result',
                                                ylabel = 'Density')
# plt.show()
# population mean
print('malay Population Mean',malay_mean.mean())

# Tamil
tamil_mean = df_tamil.mean(axis=1)
# print(tamil_mean)
#
# # 1 sample t-test
print(stats.ttest_1samp(tamil_mean,0))
# since p-value is <0.05, we conclude that mean of student average score in Tamil language is not equal to 0.

# distribution of sample mean
sns.distplot(tamil_mean, hist = True, color = 'darkblue',kde=False, ax=axs[1,0],
            hist_kws={'edgecolor':'black'}).set(xlabel = 'Tamil Survey Result',
                                                ylabel = 'Density')
fig.delaxes(axs[1,1])
plt.show()

# population mean
print('tamil Population Mean',tamil_mean.mean())

# Null Hypothesis: Means of two languages are equal.
# Alternative Hypothesis: Means of two languages are not equal.

# Convert dataframe to numpy array and convert to 1d numpy array
np_mandarin = df_mandarin.to_numpy().reshape(-1)
np_malay = df_malay.to_numpy().reshape(-1)
np_tamil = df_tamil.to_numpy().reshape(-1)

# 2 sample t-test
# Mandarin vs Malay
print(stats.ttest_ind(np_mandarin,np_malay))
# since p-value is <0.05, we conclude that there is significant difference between means of Mandarin and Malay languages.

# Malay vs Tamil
print(stats.ttest_ind(np_malay,np_tamil))
# since p-value is >0.05, we conclude that there is no significant difference between means of Malay and Tamil languages.

# Tamil vs Mandarin
print(stats.ttest_ind(np_tamil,np_mandarin))
# since p-value is <0.05, we conclude that there is significant difference between means of Tamil and Mandarin languages.

colors = ['red','blue','green']
plt.hist([np_mandarin, np_malay,np_tamil], bins=np.arange(-2,4)-0.5, color=colors)
plt.xticks(range(-2, 4))

handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["Mandarin","Malay", "Tamil"]
plt.legend(handles, labels)

plt.show()

# # Python Codes by Kayal / Mean Comparison

fig, axs = plt.subplots(2,2, figsize=(30,30))
plt.subplots_adjust(hspace=0.5)

def plot_distribution(inp, axs):
    # plt.figure()
    ax = axs.hist(inp, align = 'mid')
    axs.set_xticks(range(-2, 3))
    axs.axvline(np.mean(inp), color="b", linestyle="dashed", linewidth=3)
    _, max_ = axs.set_ylim()
    axs.text(
        inp.mean() + inp.mean() / 10,
        max_ - max_ / 10,
        "Mean: {:.2f}".format(inp.mean()),
    )
    return axs.set_figure


tamil = pd.read_csv("Dataset/Tamil/Tamil_combined_cleansed.csv")
malay = pd.read_csv("Dataset/Malay/Malay_combined_cleansed.csv")
mandarin = pd.read_csv("Dataset/Mandarin/Mandarin_combined_cleansed.csv")

tamilQ4 = tamil[["Q4"]]
malayQ4 = malay[["Q4"]]
mandarinQ4 = mandarin[["Q4"]]
print(tamilQ4)
tamilQ4 = pd.DataFrame(tamilQ4).to_numpy()
malayQ4 = pd.DataFrame(malayQ4).to_numpy()
mandarinQ4 = pd.DataFrame(mandarinQ4).to_numpy()

use_at_home = np.concatenate([tamilQ4, malayQ4, mandarinQ4])
print(use_at_home)

tamilQ3 = tamil[["Q3"]]
malayQ3 = malay[["Q3"]]
mandarinQ3 = mandarin[["Q3"]]

tamilQ3 = pd.DataFrame(tamilQ3).to_numpy()
malayQ3 = pd.DataFrame(malayQ3).to_numpy()
mandarinQ3 = pd.DataFrame(mandarinQ3).to_numpy()

use_at_school = np.concatenate([tamilQ3, malayQ3, mandarinQ3])
print(use_at_school)

def compare_2_groups(array1, array2, alpha):
    stat, p = ttest_ind(array1, array2)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Accept null hypothesis: Means are NOT significantly different')
    else:
        print('Reject null hypothesis: Means are significantly different')
        
compare_2_groups(use_at_home, use_at_school, 0.05)

plot_distribution(use_at_home, axs[0,0])
axs[0,0].set_title("Language Use at Home")

plot_distribution(use_at_school, axs[0,1])
axs[0,1].set_title("Language Use at School")

# plt.figure()
ax1 = sns.histplot(use_at_home, ax=axs[1,0], kde=True)
ax2 = sns.histplot(use_at_school, ax=axs[1,0], kde=True)
axs[1,0].axvline(np.mean(use_at_home), color='b', linestyle='dashed', linewidth=3)
axs[1,0].axvline(np.mean(use_at_school), color='orange', linestyle='dashed', linewidth=3)
axs[1,0].set_title("Language Use at Home vs School")
fig.delaxes(axs[1,1])
plt.show()



