---
name: threat-risk-assessment
description: Do a threat risk assessment for a scenario, a system, or a set up. Use when user say "Do a threat risk assessment", "assess the risk of the scenario", or "what is the risk of the following scenario".
metadata:
    - version: 0.1.0
---

# Threat Risk Assessment

## Analysis of Scenario, System or Set Up

- Analyse the scenario, system or set up

## Risk and Mitigation

- Enumerate the risk associate with the screnario, system or set up.
- Recommend mitigations for each of the risk.

## Scoring of risk

- For each of the risk, score the following after the recommended mitigations has been applied
    - Likelihood, from 1 to 5 where 1 means very small probablity, and 5 is very high probability
    - Impact, from 1 to 5 where 1 means very little impact, and 5 means very large impact.

## Usage Example

```
I want to connect a web server to the Internet. Do a threat risk assessment for this scenario.
```

## Output

- Output the threat risk assessment in a table with the columns
    - Risk
    - Mitigation
    - Likelihood
    - Impact

- Example of threat risk assessment output.

    ```
    | Risk | Mitigation | Likelihood | Impact |
    | ---- | ---------- | ---------- | ------ |
    | Risk #1 | Mitigation for Risk #1 | Likelihood Score for Risk #1 | Impact Score for Risk #1 |
    | Risk #2 | Mitigation for Risk #2 | Likelihood Score for Risk #2 | Impact Score for Risk #2 |
    ...
    ```
