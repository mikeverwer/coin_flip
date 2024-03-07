# Created by Mike Verwer, Professor of Mathematics & Statistics, Mohawk College
# mike.verwer@mohawkcollege.ca

import random
import matplotlib.pyplot as plt
import numpy as np

"""
This program finds the probability distribution of flipping a coin many times, looking for Heads.
It finds the theoretical distribution and then performs the coin flipping as many times as the user asks.
A dotplot of the results is then created to compare against the theoretical distribution.

Your task is to complete the functions 'mean', 'median', 'standard_deviation', and 'skew'.
The functions take as input an array (called 'data' in each) and they should each return
a single float containing the desired value.
You do not need to print the values to the screen, that is done in the ---- Print results ---- 
section as long as the respective function does not return 'None'. 

You only need to write the functions below, do not alter any other code.
"""

def mean(data):
    return None

def median(data):
    return None

def standard_deviation(data):
    return None

def skew(data):
    return None



# -------------- DO NOT ALTER ANY CODE BELOW THIS POINT ------------------

# ---- User inputs ----
# n: the number of coins to flip each trial
# p: the probability of landing heads
# s: the number of trials to run
n = int(input("Enter the number of coin flips: "))
p = float(input("Enter the probability of flipping Heads: "))
s = int(input("How many trials of the experiment should be run? "))

# ---- Functions -----
# Calculates the factorial of a number, n.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculates the binomial coefficient of two integers, n and k (n choose k).
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Calculates the probability of flipping a coin n times and
# getting k heads, given the probability, p, of getting a head.
def coin_probability(n, k, p):
    prob_dist = binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return prob_dist

# Flip n coins s times, where p is the probability of heads [0, 1].
# Each time the n coins get flipped, count the Heads.
def flip(n, s, p):
    headsPerTrial = []
    print(f'Number of heads in {n} flips...')
    for i in range(1, s + 1):
        heads = 0
        for j in range(1, n + 1):
            outcome = random.randint(0, 100)
            if outcome < p * 100:
                heads += 1
            # If random outcome is exactly p, the coin 'landed' on it's 'side', flip again.
            if outcome == p * 100:
                outcome = random.randint(0, 100)
                if outcome < p * 100:
                    heads += 1
        # Add the number of heads found this trial to the data set
        headsPerTrial.append(heads)
        print(f'Trial {i}: {headsPerTrial[i - 1]} heads')
    return headsPerTrial

# Count the occurrences of unique values in the input array,
# return an array of the values and an array of their counts
def dotplot_data(input_x, **args):
    # Count how many times each value occurs
    unique_values, counts = np.unique(input_x, return_counts=True)
    # Convert 1D input into 2D array
    scatter_x: list[int] = []  # x values
    scatter_y: list[int] = []  # corresponding y values
    for idx, value in enumerate(unique_values):
        for counter in range(1, counts[idx] + 1):
            scatter_x.append(value)
            scatter_y.append(counter)
    return scatter_x, scatter_y

# ---- Calculate theoretical values and generate sample data ----

# Gather sample data for s trials
headsPerTrial = flip(n, s, p)
# Calculate expected value of heads and theoretical probability distribution of rolling 'i' heads
probabilityDistribution = []
expectedValue = 0
for i in range(0, n + 1):
    probabilityDistribution.append(coin_probability(n, i, p))
    expectedValue += i * probabilityDistribution[i]

# ---- Print results ----
print(f"The expected number of heads is {expectedValue:.4g}, with probability {coin_probability(n, round(expectedValue), p):.4g}")
if mean(headsPerTrial) != None: print(f'The average number of heads was {mean(headsPerTrial):.4g}')
if median(headsPerTrial) != None: print(f'The median value is {median(headsPerTrial):.4g}')
if standard_deviation(headsPerTrial) != None: print(f'The standard deviation is {standard_deviation(headsPerTrial)}')
if skew(headsPerTrial) != None: print(f'The skewness coefficient is {skew(headsPerTrial)}')

# ---- Plot the theoretical probability distribution and the dotplot of experimental values ----

# ---- Experimental ----
# Create the dot plot arrays of trials data
scatter_x, scatter_y = dotplot_data(headsPerTrial)
# draw dot plot using scatter()
fig, bx = plt.subplots(layout='constrained')
bx.scatter(scatter_x, scatter_y)
# Set labels and x/y limits
bx.set_title(f'Dotplot of the frequency of heads in {n} coin flips')
bx.set_xlabel(f'Number of heads in {n} flips')
bx.set_ylabel('Frequency of occurrence')
bx.set_xlim(0, n)
bx.set_ylim(0, max(scatter_y) + 0.1*max(scatter_y))

# ---- Theoretical ----
# Create x-axis and figure
x = np.linspace(0, n + 1, num=n + 1, endpoint=False)
fig, ax = plt.subplots(layout='constrained')
# plot the theoretical distribution
ax.plot(x, probabilityDistribution)
# Plot the expected value as a vertical line
plt.axvline(expectedValue, 0, 1, color='red', label='E[X]')
# Set title and x and y labels
ax.set_title(f'Probability of getting x heads in {n} flips')
ax.set_xlabel('Number of Heads in n flips')
ax.set_ylabel('Probability')
# Annotate expected value
ax.annotate(f'E[X] = {expectedValue:.4g}', xy=(expectedValue, coin_probability(n, round(expectedValue), p)),
            xycoords='data', xytext=(1.5, 1.5), textcoords='offset points')
# Show the plots
plt.show()


