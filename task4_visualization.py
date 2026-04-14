import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Loading the processed trends data
csv_file = 'data/trends_analysed.csv'
df = pd.read_csv(csv_file)

# Chart 1: Top 10 Stories by Score
plt.figure(figsize=(10, 6))

top_stories = df.nlargest(10, 'score').copy()

# Trim titles to ensure they fit cleanly on the chart
top_stories['display_title'] = top_stories['title'].apply(
    lambda val: f"{val[:47]}..." if len(val) > 50 else val
)

plt.barh(top_stories['display_title'], top_stories['score'], color='skyblue', edgecolor='navy')
plt.xlabel('Upvote Score')
plt.ylabel('Post Title')
plt.title('Hacker News: Top 10 Most Popular Stories')
plt.gca().invert_yaxis() 

plt.tight_layout()
plt.savefig('outputs/chart1_top_stories.png')
plt.show()

# Chart 2: Stories per Category
plt.figure(figsize=(8, 6))

counts = df['category'].value_counts()
branding_colors = ['#FFD700', '#90EE90', '#FF7F50', '#87CEFA', '#DA70D6']

counts.plot(kind='bar', color=branding_colors)
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.title('Story Distribution by Category')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('outputs/chart2_categories.png')
plt.show()

# Chart 3: Score vs Comments Comparison
plt.figure(figsize=(8, 6))

is_popular = df['is_popular'] == True
is_regular = df['is_popular'] == False

plt.scatter(df.loc[is_regular, 'score'], df.loc[is_regular, 'num_comments'], 
            color='royalblue', label='Regular Post', alpha=0.4, s=40)

plt.scatter(df.loc[is_popular, 'score'], df.loc[is_popular, 'num_comments'], 
            color='crimson', label='Popular Post (100+ Score)', alpha=0.8, s=60)

plt.xlabel('Upvotes (Score)')
plt.ylabel('Comment Count')
plt.title('Relationship between Score and Comments')
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/chart3_scatter.png')
plt.show()

print(f"Collection complete. 3 charts saved to the 'outputs' directory.")