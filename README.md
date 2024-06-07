# Drug Interaction Checker

## Overview
This script checks for drug interactions based on an input list of drugs. The interactions data is provided in a JSON file (`interactions.json`), and the input is read from a file (`input.txt`) containing space-separated lists of drugs on each line. The script processes each line of input, identifies interactions, and outputs the most severe interaction for each list of drugs.

## Requirements
- Python 3.x

## Files
- `drug_interactions.py`: The main script to check drug interactions.
- `interactions.json`: JSON file containing drug interaction data.
- `input.txt`: Input file with space-separated lists of drugs.

## Usage

1. **Ensure all files are in the same directory:**
   - `drug_interactions.py`
   - `interactions.json`
   - `input.txt`

2. **Create or update `input.txt` with the list of drugs you want to check.** Each line should contain a space-separated list of drugs. For example:
    ```txt
    sildenafil tamsulosin valaciclovir
    sildenafil ibuprofen
    valaciclovir doxepin ticlopidine ibuprofen
    ```

3. **Open a terminal in the directory containing these files.**

4. **Run the script using Python:**
    ```sh
    python3 drug_interactions.py < input.txt
    ```

## Script Explanation

### Design Choices
1. **Data Structure:**
    - The script uses a nested dictionary to store interactions, enabling quick lookups.
    - The outer dictionary keys are drugs, and the inner dictionary keys are the interacting drugs. This design allows for O(1) average-time complexity for lookups.

2. **Input Processing:**
    - The script reads all input lines and splits each line into individual drugs.
    - It uses nested loops to generate all unique pairs of drugs and checks for interactions in the dictionary.

3. **Efficiency:**
    - By precomputing a nested dictionary of interactions, the script avoids redundant lookups and ensures efficient interaction checking.
    - Although generating all pairs of drugs results in O(d^2) complexity per input line, this is necessary to ensure all potential interactions are checked.

### Complexity Analysis
1. **Time Complexity:**
    - **Loading Interactions:** O(n), where n is the number of interactions in the JSON file.
    - **Processing Input:**
        - For each line of input with d drugs, generating pairs and checking interactions results in O(d^2).
    - **Overall Time Complexity:** O(n) + O(m * d^2), where m is the number of input lines.

2. **Space Complexity:**
    - **Storage for Interactions:** O(n), where n is the number of interactions.
    - **Processing Input:** O(m * d), where m is the number of input lines and d is the number of drugs per line.
    - **Overall Space Complexity:** O(n) + O(m * d).

## Example

Given the following `input.txt`:
```txt
sildenafil tamsulosin valaciclovir
sildenafil ibuprofen
valaciclovir doxepin ticlopidine ibuprofen
```

Running the script will produce:

```txt
MODERATE: Sildenafil may potentiate the hypotensive effect of alpha blockers, resulting in symptomatic hypotension in some patients.
No interaction
MAJOR: Valaciclovir may decrease the excretion rate of Doxepin which could result in a higher serum level.
```
