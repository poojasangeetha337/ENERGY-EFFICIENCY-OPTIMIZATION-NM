def energy_cost(temp):
    """
    Simple energy cost function:
    Lowest cost is at 22°C.
    """
    return (temp - 22) ** 2 + 5  # Minimum cost at 22°C

# Search range and step
min_temp = 18
max_temp = 30
step = 0.1

# Brute-force search
best_temp = min_temp
min_cost = energy_cost(min_temp)

temp = min_temp
while temp <= max_temp:
    cost = energy_cost(temp)
    if cost < min_cost:
        min_cost = cost
        best_temp = temp
    temp += step

# Output results
print(f"✅ Best Temperature Setpoint: {best_temp:.2f} °C")
print(f"🔋 Minimum Energy Cost: {min_cost:.2f} units")
