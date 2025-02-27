import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

#json data
data = {

}
  

# Parse JSON data
parsed_data = data["tickets"]

# Initialize a dictionary to store tag counts over time
tag_counts = defaultdict(lambda: defaultdict(int))

# Process each entry in the JSON data
for entry in parsed_data:
    open_time = datetime.strptime(entry["open_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    hour_str = open_time.strftime("%Y-%m-%d %H:00")
    
    for tag_list in entry["tags"]:
        for tag in tag_list:
            tag_counts[hour_str][tag] += 1

# Prepare data for plotting
hours = sorted(tag_counts.keys())
all_tags = set(tag for hour in hours for tag in tag_counts[hour].keys())

# Function to plot the graph with selected tags
def plot_selected_tags(selected_tags):
    plt.figure(figsize=(12, 8))
    color_cycle = plt.cm.tab20.colors
    line_styles = ['-', '--', '-.',':']
    
    for i, tag in enumerate(selected_tags):
        counts = [tag_counts[hour].get(tag, 0) for hour in hours]
        plt.plot(hours, counts, label=tag, color=color_cycle[i % len(color_cycle)], linestyle=line_styles[i % len(line_styles)])
        for j, count in enumerate(counts):
            if count > 0:
                plt.text(hours[j], count, str(count), fontsize=8)
    
    # Customize the plot
    plt.xlabel("Hour")
    plt.ylabel("Count")
    plt.title("Incident tickets by Hour")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the plot
    plt.show()

# Example usage: Select tags to include in the graph
selected_tags = ["Service Down", "General Error", "Order Issue","Launch Issues","User Login","Latency","Crash","Password"]
plot_selected_tags(selected_tags)