import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the data from the CSV file
data = pd.read_csv('artists.csv', index_col='Artist')

# List of selected artists
selected_artists = ['Johnny Cash', 'Nat King Cole', 'Dean Martin', 'Elvis Presley', 'Frank Sinatra']

# List of stream types to compare
stream_types = ['Streams', 'Daily', 'Solo', 'As feature']

# Create a function to format y-axis labels
def format_y_labels(value, pos):
    if value >= 1_000:
        return f'{value / 1_000:.0f}B'
    elif value >= 100:
        return f'{value / 10:.0f}M'
    elif value >= 1:
        return f'{value * 1_000:.0f}'
    else:
        return str(int(value))

# Create a function to add aesthetics to the graphs
def add_razzle_dazzle(ax, chart_type, stream_type):
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if stream_type == 'Streams':
        ax.set_title(f"Total {stream_type} of Greatest 50's Artists", fontsize=18)
        ax.set_ylabel(f"Total {stream_type}", fontsize=15)
    else:
        title_prefix = "Total" if stream_type == 'Streams' else "Comparison of"
        ax.set_title(f"{title_prefix} {stream_type} Streams of Greatest 50's Artists", fontsize=18)
        ax.set_ylabel(f"Total {stream_type} Streams", fontsize=15)
    ax.set_xlabel('Artist', fontsize=15)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(format_y_labels))
    ax.set_xlim(-0.5, len(selected_artists) - 0.5)

    # Add some random color
    colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in selected_artists]

    if chart_type == 'bar':
        ax.bar(filtered_data.index, filtered_data[stream_type], color=colors)
    elif chart_type == 'line':
        ax.plot(filtered_data.index, filtered_data[stream_type], marker='o', color=colors[0])

# Create a separate chart for each stream type
for stream_type in stream_types:
    # Filter the data for the selected artists and stream type
    filtered_data = data.loc[selected_artists, [stream_type]]

    try:
        # Clean the column by removing commas and converting to float
        filtered_data[stream_type] = filtered_data[stream_type].str.replace(',', '', regex=True).astype(float)
    except AttributeError:
        # The column is already in float format, so no conversion is needed
        pass

    # Sort the artists by alphabetical order
    filtered_data = filtered_data.reindex(selected_artists)

    # Create a chart comparing their stream type
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    ax = plt.gca()

    # Define the chart type based on the stream type
    chart_type = 'bar' if stream_type in ['Streams', 'Daily'] else 'line'

    add_razzle_dazzle(ax, chart_type, stream_type)

    # Save the plot as an image
    savefile = f"charts/{stream_type}Streams_{chart_type}.png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()
