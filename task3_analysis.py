import pandas as pd
import numpy as np

#Loading csv into pandas DataFrame
df=pd.read_csv("data/trends_clean.csv")
len(df)
print(f"first 5 rows:\n{df.head(5)}\n")
print(f"shape of the Dataframe: {df.shape}")

#converting score column into numpy array 
avg_scores=df['score'].mean()
print(f"Average scores: {avg_scores.round(2)}")
#converting num_comments column into numpy array 
avg_num_comments=df["num_comments"].mean()
print(f"Average num_comments: {avg_num_comments.round(2)}")

print("--- NumPy Stats ---")
scores=df['score'].to_numpy()
print(f"Mean score   : {scores.mean().round(2)}\nMedian score : {np.median(scores)}\nStd deviation: {scores.std().round(2)}\nMax score    : {scores.max()}\nMin score    : {scores.min()}")
categories=df['category'].to_numpy()
num_comments=df['num_comments'].to_numpy()
title=df["title"].to_numpy()
cat_values, cat_counts = np.unique(categories, return_counts=True)
cat_index = np.argmax(cat_counts)

print(f"Most stories in: {cat_values[cat_index]} ({cat_counts[cat_index]})")

idx = np.argmax(num_comments)
print(f"Most commented story: '{title[idx]}' - {num_comments[idx]}")

#Adding engagement and popular columns to the data frame
df["engagement"]=df['num_comments']/(df["score"]+1)
df["popular"]=df['score']>df["score"].mean()

print(df) #check if columns created

#saving the clean data into a CSV file
df.to_csv("data/trends_analysed.csv",index=False)