import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col=["date"],parse_dates=['date'])#or.set_index("date")


# Clean data
df = df[(df["value"] <= np.percentile(df["value"],97.5)) & (df["value"] >= np.percentile(df["value"],2.5))]
#df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


#numpy faster then Pandas 
#https://stackoverflow.com/questions/18580461/eliminating-all-data-over-a-given-percentile

def draw_line_plot():
    # Draw line plot
    fig, axes= plt.subplots(figsize=(18,6))
    plt.plot(df,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.copy()
    
    df_bar['months'],df_bar['year'] = df.index.month,df.index.year
    
    #df_bar = df_bar.groupby(['year','months']).mean()
    df_bar = df_bar.groupby(['year','months'],as_index=False).mean()

    df_bar['Months'] = df_bar['months'].apply(lambda x: calendar.month_name[x])

    # Draw bar plot
    fig, ax = plt.subplots()
    g = sns.catplot(x="year", y="value", hue="Months", data=df_bar, height=6, kind="bar", palette="bright", legend=False,)
    g.despine(left=True)
    g.set_ylabels("Average Page Views")
    g.set_xlabels("Years")
    plt.legend(title='Months', loc='upper left', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    fig = g.fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    print(df_box)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(12, 7), ncols=2, sharex=False)
    sns.despine(left=True)

    ax2 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Year-wise Box Plot(Trend)')

    ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot(Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
