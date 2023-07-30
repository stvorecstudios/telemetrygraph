"""
Credits : StvorecStvorec & Tom
REQUIREMENTS TO RUN THIS CODE : 
pip install matplotlib
pip install py
"""

import matplotlib.pyplot as plt

time_accelerating = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
speed_accelerating = [270, 308, 262, 82, 142, 202, 296, 138, 275, 220]

time_braking = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
speed_braking = [0, 0, 12, 74, 43, 63, 10, 67, 60, 59]

time_crashes = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
speed_crashes = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

axes[0, 0].plot(time_accelerating, speed_accelerating, marker='o', linestyle='-', color='green')
axes[0, 0].set_xlabel('Time (seconds)')
axes[0, 0].set_ylabel('Speed (km/h)')
axes[0, 0].set_title('Accelerating')
axes[0, 0].grid(True)
axes[0, 0].set_ylim(0, max(speed_accelerating) + 20)

axes[0, 1].plot(time_braking, speed_braking, marker='o', linestyle='-', color='red')
axes[0, 1].set_xlabel('Time (seconds)')
axes[0, 1].set_ylabel('Speed (km/h)')
axes[0, 1].set_title('Braking')
axes[0, 1].grid(True)
axes[0, 1].set_ylim(0, max(speed_braking) + 20)

# Remove duplicates from speed_crashes list
time_crashes_unique, speed_crashes_unique = zip(*sorted(set(zip(time_crashes, speed_crashes))))
axes[1, 0].plot(time_crashes_unique, speed_crashes_unique, marker='o', linestyle='-', color='blue')
axes[1, 0].set_xlabel('Time (seconds)')
axes[1, 0].set_ylabel('Speed (km/h)')
axes[1, 0].set_title('Crashes')
axes[1, 0].grid(True)
axes[1, 0].set_ylim(0, max(speed_crashes_unique) + 20)

# Plot the gained positions graph with given values
gained_positions_data = [1, -2, 1, 1, 3, 1, 1, -3, 4, 3]
axes[1, 1].plot(time_accelerating, gained_positions_data, marker='o', linestyle='-', color='purple', label='Gained Positions')
axes[1, 1].set_xlabel('Time (seconds)')
axes[1, 1].set_ylabel('Gained Positions (km/h)')
axes[1, 1].set_title('Gained Positions')
axes[1, 1].grid(True)
axes[1, 1].legend()

plt.tight_layout()
plt.show()
print("Successful.")
