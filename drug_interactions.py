import json
import sys
from itertools import combinations

# Load the interactions from the JSON file
with open("interactions.json", "r") as file:
    interactions = json.load(file)

# Create a nested dictionary to store interactions for quick lookup
interaction_dict = {}
for interaction in interactions:
    drug1, drug2 = interaction["drugs"]
    severity = interaction["severity"]
    description = interaction["description"]

    if drug1 not in interaction_dict:
        interaction_dict[drug1] = {}
    if drug2 not in interaction_dict:
        interaction_dict[drug2] = {}

    interaction_dict[drug1][drug2] = {"severity": severity, "description": description}
    interaction_dict[drug2][drug1] = {"severity": severity, "description": description}

# Define severity levels for comparison
severity_levels = {"minor": 1, "moderate": 2, "major": 3}


def find_interaction(drugs):
    most_severe_interaction = None

    # Check interactions for all drug pairs
    for i in range(len(drugs)):
        for j in range(i + 1, len(drugs)):
            drug1 = drugs[i]
            drug2 = drugs[j]
            if drug1 in interaction_dict and drug2 in interaction_dict[drug1]:
                interaction = interaction_dict[drug1][drug2]
                if (
                    most_severe_interaction is None
                    or severity_levels[interaction["severity"]]
                    > severity_levels[most_severe_interaction["severity"]]
                ):
                    most_severe_interaction = interaction

    if most_severe_interaction:
        return f"{most_severe_interaction['severity'].upper()}: {most_severe_interaction['description']}"
    else:
        return "No interaction"


def main():
    # Read input from STDIN
    input_lines = sys.stdin.read().strip().split("\n")

    # Process each line of input
    for line in input_lines:
        if line.strip():
            drugs = line.strip().split()
            result = find_interaction(drugs)
            print(result)


if __name__ == "__main__":
    main()
