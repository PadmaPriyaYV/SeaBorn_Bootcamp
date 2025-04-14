import stremlit as st
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style='whitegrid')
tips=sns.load_dataset("tips")
st.title("SeaBorn data visualization App")
st.write("SeaBorn data visualization App")

# Function to create and display plot
def display_plot(title,plot_func):
    st.subheader(title)
    fig, ax = plt.subplots(figsize=(8,6))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)


    #plot

def scatter_plot(ax):
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time',size='size', palette='deep', ax=ax)
    ax.set_title("Scatter plot")

def line_plot(ax):
    sns.lineplot(data=tips,x='size',y='total_bill',hue='sex',marker='o', ax=ax)
    ax.set_title("Line plot")

def bar_plot(ax):
    sns.barplot(data=tips,x='day',y='total_bill',hue='sex',palette='muted',ax=ax)
    ax.set_title("Bar plot")

def box_plot(ax):
    sns.boxplot(data=tips,x='day',y='tip',hue='smoker',palette='pastel',ax=ax)
    ax.set_title("Box Plot")

def violin_plot(ax):
    sns.violinplot(data=tips,x='day',y='total_bill',hue='time',split=True,palette='Set2',ax=ax)
    ax.set_title("Violin Plot")

def count_plot(ax):
    sns.countplot(data=tips, x='day', hue='smoker', palette='dark',ax=ax)
    ax.set_title("Count Plot")

def reg_plot(ax):  
    sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'s':50}, line_kws={'color':'red'},ax=ax)  
    ax.set_tile("Reg Plot")   

def hist_plot(ax):
    sns.histplot(data=tips, x='total_bill', bins=20, kde=True, color='blue',ax=ax) 
    ax.set_title("History Plot")

def pair_plot(ax):
    sns.pairplot(tips, hue='sex', vars=["total_bill", "tip", "size"], palette='husl',ax=ax)
    ax.set_title("Pair Plot")

def stripe_plot(ax):
    sns.stripplot(data=tips, x='day', y='tip', hue='sex', jitter=True, palette='Set1',ax=ax)
    ax.set_title("Stripe plot")

def kde_plot(ax):
    sns.kdeplot(data=tips, x='total_bill',hue='sex', fill=True, palette='tab10',ax=ax)
    ax=set_title("KDE Plot")


display_plot("Scatter Plot", scatter_plot)
display_plot("Line Plot", line_plot)
display_plot("Bar Plot", bar_plot)
display_plot("Box Plot", box_plot)
display_plot("Violin Plot", violin_plot)
display_plot("Count Plot", count_plot)
display_plot("Reg Plot", reg_plot)
display_plot("Hist Plot", hist_plot)
display_plot("Pair Plot", pair_plot)
display_plot("Stripe Plot", stripe_plot)
display_plot("Kde Plot", kde_plot)
