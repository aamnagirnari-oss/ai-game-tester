import json
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------
with open("comparison_results.json", "r") as f:
    data = json.load(f)

# -----------------------------
# CALCULATE METRICS
# -----------------------------
total = len(data)

random_success = sum(1 for d in data if d["random"]["success"])
smart_success = sum(1 for d in data if d["smart"]["success"])

random_avg_steps = sum(d["random"]["steps"] for d in data) / total
smart_avg_steps = sum(d["smart"]["steps"] for d in data) / total

random_success_rate = random_success / total
smart_success_rate = smart_success / total

# -----------------------------
# SUCCESS RATE GRAPH
# -----------------------------
plt.figure()
plt.bar(["Random", "Smart"], [random_success_rate, smart_success_rate])
plt.title("Success Rate Comparison")
plt.ylabel("Success Rate")
plt.ylim(0, 1)
plt.show()

# -----------------------------
# STEPS COMPARISON GRAPH
# -----------------------------
plt.figure()
plt.bar(["Random", "Smart"], [random_avg_steps, smart_avg_steps])
plt.title("Average Steps Comparison")
plt.ylabel("Steps")
plt.show()

# -----------------------------
# PRINT SUMMARY
# -----------------------------
print("\n--- PERFORMANCE SUMMARY ---")
print(f"Random Success Rate: {random_success_rate:.2f}")
print(f"Smart Success Rate: {smart_success_rate:.2f}")
print(f"Random Avg Steps: {random_avg_steps:.2f}")
print(f"Smart Avg Steps: {smart_avg_steps:.2f}")