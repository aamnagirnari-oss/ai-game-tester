import json
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
with open("results.json", "r") as f:
    data = json.load(f)

# -----------------------------
# HEATMAP DATA
# -----------------------------
grid_size = 5
heatmap = np.zeros((grid_size, grid_size))

for run in data:
    for (x, y) in run["path"]:
        heatmap[x][y] += 1

# -----------------------------
# BOTTLENECK (compute BEFORE plot)
# -----------------------------
max_visits = np.max(heatmap)
bottleneck = np.argwhere(heatmap == max_visits)

# -----------------------------
# HEATMAP PLOT
# -----------------------------
plt.figure()
plt.imshow(heatmap, cmap='hot')
plt.colorbar()
plt.title("Agent Movement Heatmap")

# Goal
plt.scatter(4, 4, color='red', s=100, label='Goal')

# Bottleneck
for (x, y) in bottleneck:
    plt.scatter(y, x, color='blue', s=120, label='Bottleneck')

# Fix duplicate legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.show()

# -----------------------------
# SUCCESS VS FAILURE
# -----------------------------
success = sum(1 for d in data if d["success"])
failure = len(data) - success

plt.figure()
plt.bar(["Success", "Failure"], [success, failure])
plt.title("Success vs Failure")
plt.show()

# -----------------------------
# STEPS DISTRIBUTION
# -----------------------------
steps = [d["steps"] for d in data]

plt.figure()
plt.hist(steps, bins=10)
plt.title("Steps Distribution")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# INTELLIGENCE (ANALYSIS)
# -----------------------------
total_runs = len(data)
success_rate = success / total_runs
avg_steps = sum(steps) / total_runs

print("\n--- GAME ANALYSIS ---")
print(f"Success Rate: {success_rate:.2f}")
print(f"Average Steps: {avg_steps:.2f}")

# -----------------------------
# DIFFICULTY CATEGORY
# -----------------------------
if success_rate < 0.3:
    print("⚠️ Maze Difficulty: VERY HARD")
elif success_rate < 0.6:
    print("⚠️ Maze Difficulty: MEDIUM")
else:
    print("✅ Maze Difficulty: EASY")

# -----------------------------
# INEFFICIENCY CHECK
# -----------------------------
if avg_steps > 30:
    print("⚠️ Agent is inefficient (too many steps)")
else:
    print("✅ Agent efficiency is good")

# -----------------------------
# DIFFICULTY SCORE
# -----------------------------
difficulty_score = (1 - success_rate) * avg_steps

print(f"\n🎯 Difficulty Score: {difficulty_score:.2f}")

if difficulty_score > 25:
    print("🔥 Level: HARD")
elif difficulty_score > 10:
    print("⚠️ Level: MEDIUM")
else:
    print("✅ Level: EASY")

# -----------------------------
# DEAD ZONES
# -----------------------------
dead_zones = np.argwhere(heatmap == 0)
print(f"❌ Dead zones: {dead_zones}")

# -----------------------------
# TOP CELLS
# -----------------------------
flat_indices = np.argsort(heatmap, axis=None)[-3:]
top_cells = [np.unravel_index(i, heatmap.shape) for i in flat_indices]

print(f"🔥 Top 3 most visited cells: {top_cells}")

# -----------------------------
# FINAL INSIGHTS
# -----------------------------
print("\n--- FINAL INSIGHTS ---")

if success_rate < 0.5:
    print("⚠️ Low success rate → maze may be too difficult")

if avg_steps > 25:
    print("⚠️ High steps → agent is inefficient")

if len(dead_zones) > 0:
    print("⚠️ Dead zones detected → parts of maze unused")

if len(bottleneck) > 0:
    print("🔥 Bottleneck detected → movement congestion area")