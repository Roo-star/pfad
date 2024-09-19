import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager

# Read CSV file
data = pd.read_csv("global_temperature_data_1850_present.csv")

# Create Date column
data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))

# Set font for supporting English characters
font_path = 'C:/Windows/Fonts/arial.ttf'  # You can replace with any suitable font
prop = font_manager.FontProperties(fname=font_path)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Initialize plot
line, = ax.plot([], [], lw=2, color='royalblue')
ax.set_xlim(data['Date'].min(), data['Date'].max())
ax.set_ylim(data['Monthly_Anomaly'].min() - 0.5, data['Monthly_Anomaly'].max() + 0.5)
ax.set_xlabel('Year', fontsize=14, weight='bold', fontproperties=prop)
ax.set_ylabel('Temperature Anomaly (℃)', fontsize=14, weight='bold', fontproperties=prop)
ax.set_title('Global Surface Temperature Anomaly from 1850 to Present', fontsize=18, color='darkblue', weight='bold', fontproperties=prop)

# Customize background color and grid lines
ax.set_facecolor('#f0f8ff')  # Background color
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Create gradient background
def create_gradient_background(ax):
    from matplotlib.patches import Rectangle
    gradient = plt.imshow([[0, 1]], cmap='coolwarm', interpolation='bicubic', aspect='auto', 
                          extent=[ax.get_xlim()[0], ax.get_xlim()[1], ax.get_ylim()[0], ax.get_ylim()[1]], 
                          alpha=0.3, vmin=-1, vmax=1)
    plt.colorbar(gradient, ax=ax, orientation='vertical')
    
create_gradient_background(ax)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(num):
    x = data['Date'][:num]
    y = data['Monthly_Anomaly'][:num]
    line.set_data(x, y)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(data), init_func=init, blit=True, interval=100, repeat=False)

# Show animation
plt.show()
