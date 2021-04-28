import pandas as pd
import sys
import os
import glob

input_file = pd.read_csv(sys.argv[1])


clean_input_file = input_file[['First Name', 'Last Name', 'CKI District',
 'What CKI Position Do You Have?', 'Email Address','Phone Number', 
 'Year in School', 'Favorite Means of Communication', 
 'What are some of your hobbies?',
 'What are your favorite movies and/or TV shows?',
 'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)',
 'How many holes does a straw have',
 'How often would you like to communicate with your buddy? ']]

df = input_file[['First Name','Last Name',
 'Please answer the following questions: [When you go somewhere for the day, you would prefer to plan what you will do and when.]',
 'Please answer the following questions: [If you were a teacher, you would prefer to teach courses involving opinion/theory over a facts based course.]',
 'Please answer the following questions: [In a group setting you usually are rather quiet and reserved.]',
 'Please answer the following questions: [When making decisions you let your heart rule over your head.]',
 'Please answer the following questions: [You are better at dealing with the unexpected and seeing quickly what should be done compared to following a detailed plan.]',
 'Please answer the following questions: [You consider yourself an out-of-the-box-thinking person.]',
 'Please answer the following questions: [You talk easily to almost anyone for as long as you have to.]',
 'Please answer the following questions: [It’s better to be a person of real feeling compared to being consistently reasonable.]',
 'Please answer the following questions: [Following a set schedule does not appeal to you.]',
 'Please answer the following questions: [You prefer to have friends that are grounded compared to those that are constantly coming up with new ideas.]',
 'Please answer the following questions: [In a large group of people you introduce other people.]',
 'Please answer the following questions: [You usually value emotion more than logic.]',
 'Please answer the following questions: [You plan on attending CKIx 2021.]']]

df.columns = ['First Name', 'Last Name','a','b','c','d','e','f','g','h','i','j','k','l','CKIx']
# + values == J , N, I, F
# - values == P , S, E, T
df.loc[(df.a == 'Strongly Agree'), 'a'] = 3
df.loc[(df.a == 'Moderately Agree'), 'a'] = 2
df.loc[(df.a == 'Slightly Agree'), 'a'] = 1
df.loc[(df.a == 'Strongly Disagree'), 'a'] = -3
df.loc[(df.a == 'Moderately Disagree'), 'a'] = -2
df.loc[(df.a == 'Slightly Disagree'), 'a'] = -1

df.loc[(df.b == 'Strongly Agree'), 'b'] = 3
df.loc[(df.b == 'Moderately Agree'), 'b'] = 2
df.loc[(df.b == 'Slightly Agree'), 'b'] = 1
df.loc[(df.b == 'Strongly Disagree'), 'b'] = -3
df.loc[(df.b == 'Moderately Disagree'), 'b'] = -2
df.loc[(df.b == 'Slightly Disagree'), 'b'] = -1

df.loc[(df.c == 'Strongly Agree'), 'c'] = 3
df.loc[(df.c == 'Moderately Agree'), 'c'] = 2
df.loc[(df.c == 'Slightly Agree'), 'c'] = 1
df.loc[(df.c == 'Strongly Disagree'), 'c'] = -3
df.loc[(df.c == 'Moderately Disagree'), 'c'] = -2
df.loc[(df.c == 'Slightly Disagree'), 'c'] = -1

df.loc[(df.d == 'Strongly Agree'), 'd'] = 3
df.loc[(df.d == 'Moderately Agree'), 'd'] = 2
df.loc[(df.d == 'Slightly Agree'), 'd'] = 1
df.loc[(df.d == 'Strongly Disagree'), 'd'] = -3
df.loc[(df.d == 'Moderately Disagree'), 'd'] = -2
df.loc[(df.d == 'Slightly Disagree'), 'd'] = -1
#invert
df.loc[(df.e == 'Strongly Agree'), 'e'] = -3
df.loc[(df.e == 'Moderately Agree'), 'e'] = -2
df.loc[(df.e == 'Slightly Agree'), 'e'] = -1
df.loc[(df.e == 'Strongly Disagree'), 'e'] = 3
df.loc[(df.e == 'Moderately Disagree'), 'e'] = 2
df.loc[(df.e == 'Slightly Disagree'), 'e'] = 1

df.loc[(df.f == 'Strongly Agree'), 'f'] = 3
df.loc[(df.f == 'Moderately Agree'), 'f'] = 2
df.loc[(df.f == 'Slightly Agree'), 'f'] = 1
df.loc[(df.f == 'Strongly Disagree'), 'f'] = -3
df.loc[(df.f == 'Moderately Disagree'), 'f'] = -2
df.loc[(df.f == 'Slightly Disagree'), 'f'] = -1
#invert
df.loc[(df.g == 'Strongly Agree'), 'g'] = -3
df.loc[(df.g == 'Moderately Agree'), 'g'] = -2
df.loc[(df.g == 'Slightly Agree'), 'g'] = -1
df.loc[(df.g == 'Strongly Disagree'), 'g'] = 3
df.loc[(df.g == 'Moderately Disagree'), 'g'] = 2
df.loc[(df.g == 'Slightly Disagree'), 'g'] = 1

df.loc[(df.h == 'Strongly Agree'), 'h'] = 3
df.loc[(df.h == 'Moderately Agree'), 'h'] = 2
df.loc[(df.h == 'Slightly Agree'), 'h'] = 1
df.loc[(df.h == 'Strongly Disagree'), 'h'] = -3
df.loc[(df.h == 'Moderately Disagree'), 'h'] = -2
df.loc[(df.h == 'Slightly Disagree'), 'h'] = -1

#invert
df.loc[(df.i == 'Strongly Agree'), 'i'] = -3
df.loc[(df.i == 'Moderately Agree'), 'i'] = -2
df.loc[(df.i == 'Slightly Agree'), 'i'] = -1
df.loc[(df.i == 'Strongly Disagree'), 'i'] = 3
df.loc[(df.i == 'Moderately Disagree'), 'i'] = 2
df.loc[(df.i == 'Slightly Disagree'), 'i'] = 1

#invert
df.loc[(df.j == 'Strongly Agree'), 'j'] = -3
df.loc[(df.j == 'Moderately Agree'), 'j'] = -2
df.loc[(df.j == 'Slightly Agree'), 'j'] = -1
df.loc[(df.j == 'Strongly Disagree'), 'j'] = 3
df.loc[(df.j == 'Moderately Disagree'), 'j'] = 2
df.loc[(df.j == 'Slightly Disagree'), 'j'] = 1

#invert
df.loc[(df.k == 'Strongly Agree'), 'k'] = -3
df.loc[(df.k == 'Moderately Agree'), 'k'] = -2
df.loc[(df.k == 'Slightly Agree'), 'k'] = -1
df.loc[(df.k == 'Strongly Disagree'), 'k'] = 3
df.loc[(df.k == 'Moderately Disagree'), 'k'] = 2
df.loc[(df.k == 'Slightly Disagree'), 'k'] = 1

df.loc[(df.l == 'Strongly Agree'), 'l'] = 3
df.loc[(df.l == 'Moderately Agree'), 'l'] = 2
df.loc[(df.l == 'Slightly Agree'), 'l'] = 1
df.loc[(df.l == 'Strongly Disagree'), 'l'] = -3
df.loc[(df.l == 'Moderately Disagree'), 'l'] = -2
df.loc[(df.l == 'Slightly Disagree'), 'l'] = -1

df.loc[(df.CKIx == 'Strongly Agree'), 'CKIx'] = 3
df.loc[(df.CKIx == 'Moderately Agree'), 'CKIx'] = 2
df.loc[(df.CKIx == 'Slightly Agree'), 'CKIx'] = 1
df.loc[(df.CKIx == 'Strongly Disagree'), 'CKIx'] = -3
df.loc[(df.CKIx == 'Moderately Disagree'), 'CKIx'] = -2
df.loc[(df.CKIx == 'Slightly Disagree'), 'CKIx'] = -1

# Scores to Letters
df["IE"] = df['c']+df['g']+df['k']
df['IE'] = df['IE'].apply(lambda x: 'I' if x >=0 else 'E')

df["NS"] = df['b']+df['f']+df['j']
df['NS'] = df['NS'].apply(lambda x: 'N' if x >=0 else 'S')

df["FT"] = df['d']+df['h']+df['l']
df['FT'] = df['FT'].apply(lambda x: 'T' if x >=0 else 'F')

df["JP"] = df['a']+df['e']+df['i']
df['JP'] = df['JP'].apply(lambda x: 'J' if x >0 else 'P')

#x == they are going to CKIx
df['x'] = df['CKIx'].apply(lambda x: 'x' if x >0 else ' ')
df['Type'] = df[df.columns[15:20]].apply(
    lambda x: ''.join(x.dropna().astype(str)),
    axis=1
)

merge_type = df[['First Name', 'Type']]
result = pd.merge(clean_input_file, merge_type, on = "First Name", how = 'outer')
print(result)
dif = result.groupby('Type')

Position_options = (
#'ISTJ',
#'ISTP',
#'ISFJ',
#'ISFP',
#'INFJ',
#'INFP',
#'INTJ',
#'INTP',
#'ESTP',
#'ESTJ',
#'ESFP',
#'ESFJ',
#'ENFP',
#'ENFJ',
#'ENTP',
#'ENTJ'
#'ISTJx',
#'ISTPx',
#'ISFJx',
#'ISFPx',
#'INFJx',
#'INFPx',
'INTJx',
#'INTPx',
#'ESTPx',
#'ESTJx',
#'ESFPx',
#'ESFJx',
#'ENFPx',
#'ENFJx',
#'ENTPx',
#'ENTJx'
)
for x in Position_options:
    hello = dif.get_group( x )
    hello = hello.sample(frac=1).reset_index(drop=True)
    hello.to_csv(x+"_pairing.csv")

all_files = glob.glob( "./*_pairing.csv")


empty = []
empty_2 = []
for x in all_files:
    df = pd.read_csv(x, index_col=None, header=0)
    print(df)
    df = df.rename(columns={'Unnamed: 0':'Partner Number'})
    for x,y in df.iterrows():
        if x == 0:
            df.at[x, 'Unnamed: 0']= 1
            continue
        elif x % 2 == 0:
            y = x+1
            df.at[x, 'Unnamed: 0']= y
            continue
        elif x % 2 != 0:
            df.at[x, 'Unnamed: 0']= x
            continue
    df_2=df.copy()
    df = df.drop_duplicates(subset='Unnamed: 0', keep="first")
    df_2 = df_2.drop_duplicates(subset='Unnamed: 0', keep="last")
    empty.append(df)
    empty_2.append(df_2)


for x in Position_options:
    os.remove(x+"_pairing.csv")

final_2 = pd.concat(empty_2, axis=0, ignore_index=False, sort=False)

final = pd.concat(empty, axis=0, ignore_index=False, sort=False)

final = final.rename(columns={
'First Name':'First Name_1',
'Last Name':'Last Name_1', 
'CKI District': 'CKI District_1',
'What CKI Position Do You Have?': 'What CKI Position Do You Have?_1', 
'Email Address': 'Email Address_1',
'Phone Number': 'Phone Number_1', 
'Year in School': 'Year in School_1',
'Favorite Means of Communication':'Favorite Means of Communication_1', 
'What are some of your hobbies?':'What are some of your hobbies?_1',
'What are your favorite movies and/or TV shows?':'What are your favorite movies and/or TV shows?_1',
'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)':'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)_1',
'How many holes does a straw have':'How many holes does a straw have_1',
'How often would you like to communicate with your buddy? ': 'How often would you like to communicate with your buddy?_1',
'Type':'Type'})

final_2 = final_2.rename(columns={
'First Name':'First Name_2',
'Last Name':'Last Name_2', 
'CKI District': 'CKI District_2',
'What CKI Position Do You Have?': 'What CKI Position Do You Have?_2', 
'Email Address': 'Email Address_2',
'Phone Number': 'Phone Number_2', 
'Year in School': 'Year in School_2',
'Favorite Means of Communication':'Favorite Means of Communication_2', 
'What are some of your hobbies?':'What are some of your hobbies?_2',
'What are your favorite movies and/or TV shows?':'What are your favorite movies and/or TV shows?_2',
'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)':'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)_2',
'How many holes does a straw have':'How many holes does a straw have_2',
'How often would you like to communicate with your buddy? ': 'How often would you like to communicate with your buddy?_2',
'Type':'Type'})

final['Unnamed: 0']=final['Unnamed: 0'].astype(object)
final_2['Unnamed: 0']=final_2['Unnamed: 0'].astype(object)

final_final= pd.merge(left=final, right=final_2, on=['Unnamed: 0','Type'])

final_final.to_csv('Output_pairings_2.csv')


#Copyright 2020, Austin Underwood, All rights reserved.
