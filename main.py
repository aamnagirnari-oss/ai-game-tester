from game.grid import Grid
from game.agent import Agent
from game.smart_agent import SmartAgent
import json


# -----------------------------
# RANDOM AGENT
# -----------------------------
def run_random_agent(grid):
    agent = Agent(grid.start)

    for _ in range(50):
        agent.move(grid)
        if agent.reached_goal(grid.goal):
            return True, agent.steps

    return False, agent.steps


# -----------------------------
# SMART AGENT
# -----------------------------
def run_smart_agent(grid):
    agent = SmartAgent(grid.start)
    success = agent.bfs(grid)

    return success, len(agent.path)


# -----------------------------
# EXPERIMENT
# -----------------------------
def run_experiment(n=50):
    results = []

    for _ in range(n):
        grid = Grid()  # SAME maze for both

        r_success, r_steps = run_random_agent(grid)
        s_success, s_steps = run_smart_agent(grid)

        results.append({
            "random": {
                "success": r_success,
                "steps": r_steps
            },
            "smart": {
                "success": s_success,
                "steps": s_steps
            }
        })

    return results


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    results = run_experiment(50)

    # Save CORRECT file name
    with open("comparison_results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("✅ comparison_results.json created")

    # -----------------------------
    # ANALYSIS
    # -----------------------------
    total = len(results)

    random_success = sum(1 for r in results if r["random"]["success"])
    smart_success = sum(1 for r in results if r["smart"]["success"])

    random_avg_steps = sum(r["random"]["steps"] for r in results) / total
    smart_avg_steps = sum(r["smart"]["steps"] for r in results) / total

    print("\n--- RESULTS ---")
    print(f"Random Success Rate: {random_success / total:.2f}")
    print(f"Smart Success Rate: {smart_success / total:.2f}")
    print(f"Random Avg Steps: {random_avg_steps:.2f}")
    print(f"Smart Avg Steps: {smart_avg_steps:.2f}")