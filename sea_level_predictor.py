import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.axline((1880, 1880 * slope + intercept), (2050, 2050 * slope + intercept))

    # Create second line of best fit
    df.set_index('Year', inplace=True)
    df = df.loc[2000:, ['CSIRO Adjusted Sea Level']]
    slope, intercept, _, _, _ = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    ax.axline((2000, 2000 * slope + intercept), (2050, 2050 * slope + intercept))
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()