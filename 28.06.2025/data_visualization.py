# Filename:  data_visualization.py
import matplotlib.pyplot as plt

def create_bar_chart(data, labels, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()