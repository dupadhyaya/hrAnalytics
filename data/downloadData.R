#download data into this folder from web

#other sources------
#https://github.com/dphi-official/Datasets


#----------
hrfolder0 = 'E:/analytics/projects/hranalytics/data/'
#https://www.kaggle.com/datasets/rhuebner/human-resources-data-set?resource=download
folder1 = 'set1/'
file1 = 'HRDataset_v14.csv'
data1 = read.csv(paste0(hrfolder0,folder1, file1))
dim(data1)
names(data1)


#dataset2------
#https://www.kaggle.com/datasets/davidepolizzi/hr-data-set-based-on-human-resources-data-set
#It contains 3 data sets:
#Employee data, with information like, name, Date of Birth, Date of hire, Department, etc.
#Action data, indicating actions like, hiring, promotions, demotions, attrition.
#Performance data. For each employee for each period.
#The 3 data set can be related through the Employee ID.

folder2='set2/'
file2a = 'tbl_Action.csv'
data2A = read.csv(paste0(hrfolder0, folder2,file2a))
dim(data2A)
names(data2A)


file2b = 'tbl_Employee.csv'
data2B = read.csv(paste0(hrfolder0, folder2,file2b))
dim(data2B)
names(data2B)

file2c = 'tbl_Perf.csv'
data2C = read.csv(paste0(hrfolder0, folder2,file2c))
dim(data2C)
names(data2C)



#dataset3------
#https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
#Uncover the factors that lead to employee attrition and explore important questions such as ‘show me a breakdown of distance from home by job role and attrition’ or ‘compare average monthly income by education and attrition’. This is a fictional data set created by IBM data scientists.

folder3='set3/'
file3 = 'WA_Fn-UseC_-HR-Employee-Attrition.csv'
data3 = read.csv(paste0(hrfolder0, folder3,file3))
dim(data3)
names(data3)


#dataset4------
#https://www.kaggle.com/datasets/arashnic/hr-ana
#A large MNC have 9 broad verticals across the organisation. One of the problem is identifying the right people for promotion (only for manager position and below) and prepare them in time.
#The final promotions are only announced after the evaluation and this leads to delay in transition to new roles. Hence, company needs help in identifying the eligible candidates at a particular checkpoint so that they can expedite the entire promotion cycle.
#Multiple attributes have been provided around Employee's past and current performance along with demographics.
#Predict whether a potential promotee at checkpoint in the test set will be promoted or not after the evaluation process.
folder4='set4/'
file4a = 'train.csv'
file4b = 'test.csv'

data4A = read.csv(paste0(hrfolder0, folder4,file4a))
dim(data4A)
names(data4A)

data4B = read.csv(paste0(hrfolder0, folder4,file4b))
dim(data4B)
names(data4B)


#dataset5-----
#https://www.kaggle.com/datasets/jacksonchou/hr-data-for-analytics
#https://www.kaggle.com/code/jacksonchou/hr-analytics
#This is dataset is for HR analytics. The dataset contains employee profiles of a large company, where each record is an employee
folder5= 'set5/'
file5='HR_comma_sep.csv'
data5 = read.csv(paste0(hrfolder0, folder5,file5))
dim(data5)
names(data5)


#dataset6------
#https://www.kaggle.com/datasets/rishikeshkonapure/hr-analytics-prediction
folder6='set6/'
file6='HR-Employee-Attrition.csv'
data6 = read.csv(paste0(hrfolder0, folder6,file6))
dim(data6)
names(data6)

#dataset7------
#https://www.kaggle.com/datasets/giripujar/hr-analytics
folder7='set7/'
file7='HR_comma_sep.csv'
data7 = read.csv(paste0(hrfolder0, folder7,file7))
dim(data7)
names(data7)


#dataset8-----
#https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study
#odel the probability of attrition using a logistic regression. The results thus obtained will be used by the management to understand what changes they should make to their workplace, in order to get most of their employees to stay.
folder8='set8/'
file8a='data_dictionary.xlsx'
list.files(paste0(hrfolder0, folder8))
data8a = readxl::read_excel(paste0(hrfolder0, folder8,file8a), sheet=1)
dim(data8a)
names(data8a)
head(data8a)
data8a = read.csv(paste0(hrfolder0, folder8,file8a))

dim(data8)
names(data8)


#dataset9-----
#https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists
#https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists?taskId=3015

folder9='set9/'
list.files(paste0(hrfolder0, folder9))
#Predict the probability of a candidate will work for the company
#Interpret model(s) such a way that illustrate which features affect candidate decision


#datset10------
#https://www.kaggle.com/competitions/codecell2021/data




#dataset11-----
#https://www.kaggle.com/datasets/koluit/human-resource-data-set-the-company


#unsorted
#https://www.kaggle.com/datasets/rhuebner/human-resources-data-set/discussion/116590
#https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction
