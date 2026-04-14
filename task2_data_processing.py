import pandas as pd
df=pd.read_json("data/trends_20260414.json")

# Shows all rows that have a duplicated ID
duplicates = df[df.duplicated(subset=['post_id'], keep=False)]
print(duplicates.sort_values(by='post_id'))

# shows if the scores and num_comments are of int datatype
df.info()

#to delete the duplicates leaving the first one as original
df=df.drop_duplicates(subset= "post_id", keep="first")
print(f"After removing duplicates: {len(df)}")

#droping the null values from post_id, title, or score if any present
df=df.dropna(subset=['post_id', 'title', 'score'])
print(f"After removing nulls: {len(df)}")

#droping the rows with the 'scores' less tthan 5
df=df.drop(df[df["score"]<5].index)
print(f"After removing low scores: {len(df)}")

#removing the white spaces from the "title" column
df["title"]=df["title"].str.strip()

#reseting the index after the cleaning
df = df.reset_index(drop=True)
#to show remaining no of stories per category after cleaning the data
count=df.groupby("category").size()
print(f"Stories per category:\n{count.sort_values(ascending=False)}")

#saving the clean data into a CSV file
df.to_csv("data/trends_clean.csv",index=False)