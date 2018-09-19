import pandas as pd
from azureTrans import gen_str, azure_trans_25


"""Colums to stract

File to work wit: ORD-331019-K4F1_final_20180813.xlsx
To use this script specify the name file with extension in the 
variable 'file AND define a array string with the name
'colum_list'
Also you mus define a file name for the output and the end of this
script.


Q10_201
Q10_202
Q10_203	
Q10_301	
Q10_302	
Q10_401	
Q10_402	
Q10_403	
Q10_501	
Q10_502	
Q10_601	
Q10_602	
Q10_603

Q15

Q3_98_other
Q4_98_other    
Q5_98_other    
Q6_98_other    
Q7_97_other    
Q7_98_other

"""


file = 'ORD-331019-K4F1_final_20180813.xlsx'  #Load file

df = pd.read_excel(file)  # Convert all file to panda object

column_list = ["Q10_201", "Q10_202", "Q10_203", "Q10_301", "Q10_302", "Q10_401", "Q10_402",
               "Q10_403", "Q10_501", "Q10_502", "Q10_601", "Q10_602", "Q10_603", "Q15",
               "Q3_98_other", "Q4_98_other", "Q5_98_other", "Q6_98_other", "Q7_97_other",
               "Q7_98_other"]



"""Generate list with panda objects with the columns inside"""
col_pan_list = []
for col in column_list:
    col_pan_list.append(df[col])

"""Generate list with str list of the words/phrases to translate"""
col_str_list = []
for i in range(col_pan_list.__len__()):
    col_str_list.append(col_pan_list[i].values)


"""To fill pal_array with the format of the body request.
   gen_str generates a dictionary {'Text':'Подхолит для любых работ'} """

pal_array = []
text_array = []

for i in range(col_str_list.__len__()):
    for j in range(col_str_list[i].__len__()):
        text_array.append(gen_str(col_str_list[i][j]))
    pal_array.append(text_array.copy())
    text_array.clear()


"""Iterate along pal_array to make request for each collumn"""
tras_col_respond = []
for i in range(pal_array.__len__()):
    tras_col_respond.append(azure_trans_25(pal_array[i]))


"""Insert the translated column next to its corresponding source
    the index in dynamically gotten from name"""
for i in range(tras_col_respond.__len__()):
    panda_pp = pd.DataFrame(tras_col_respond[i])  # Convert string list to panda object
    df.insert(loc=df.columns.get_loc(column_list[i])+1,
              column=column_list[i]+'_translated',
              value=panda_pp)  # Insert translation next to source


"""Write panda object to FILE"""
df.to_excel("Excel_translated.xlsx")  # Save to file


print('')
