---
name: threat-risk-assessment
description: Do a threat risk assessment for a scenario, a system, or a set up. Use when user say "Do a threat risk assessment", "assess the risk of the scenario", or "what is the risk of the following scenario".
metadata:
    - version: 0.2.0
---

# Threat Risk Assessment

## Analysis of Scenario, System or Set Up

- Analyse the scenario, system or set up

## Risks and Mitigations

- Enumerate the risk associate with the screnario, system or set up.
- Recommend mitigations for each of the risk.

## Scoring of Risks

### Before Application of Mitigations

- For each of the risk, score the following before the recommended mitigations have been applied.
    - Likelihood, from 1 to 5 where 1 means very small probablity, and 5 is very high probability
    - Impact, from 1 to 5 where 1 means very little impact, and 5 means very large impact
    - Risk Rating, by looking up in the Risk Rating Lookup Table
- Determine the Overall Risk Rating by taking the highest Risk Rating from all of the individual risk.
    - The Risk Rating are, from the lowest to highest - Very Low, Low, Medium, Medium Hight, High, Very High

### After Application of Mitigations

- Do an exact same scoring for the scenario after the recommended mitigations have been applied.

### Risk Rating Lookup Table

|   | Impact | 1 | 2 | 3 | 4 | 5 |
| - | ------ | - | - | - | - | - |
| Likelihood | 5 | Medium | Medium High | High | High | Very High |
| | 4 | Medium Log | Medium | Medium High | High | High |
| | 3 | Low | Medium Low | Medium | Medium High | High |
| | 2 | Low | Low | Medium Low | Medium | Medium High |
| | 1 | Very Low | Low | Low | Medium Low | Medium |

## Summary

- Provide a summary of the Threat Risk Assessment

# Usage

## Usage Example

Example 1:
```
I want to connect a web server to the Internet. Do a threat risk assessment for this scenario.
```

Example 2:
```
Do a threat risk assessment for leaving a stack of cash on a bench in a park.
```

# Output

## Output Example

### Output for Risks and Mitigations

- Output all the risks in a table with the following columns:
    - Risk
    - Mitigation

### Output for Each Scoring

- Output the threat risk assessment scores for all the risks in a table with the following columns:
    - Risk
    - Mitigation
    - Likelihood
    - Impact
    - Risk Rating

- Output the Overall Risk Rating for the table

### Example Output for Each Scoring

- Example of threat risk assessment output.

    ```
    | Risk | Mitigation | Likelihood | Impact | Risk Rating |
    | ---- | ---------- | ---------- | ------ | ----------- |
    | Risk #1 | Mitigation for Risk #1 | Likelihood Score for Risk #1 | Impact Score for Risk #1 | Risk Rating for Risk #1 |
    | Risk #2 | Mitigation for Risk #2 | Likelihood Score for Risk #2 | Impact Score for Risk #2 | Risk Rating for Risk #2 |
    ...

    Overall Risk Rating: Overall Risk Rating calculated from all the individual Risk Ratings
    ```
