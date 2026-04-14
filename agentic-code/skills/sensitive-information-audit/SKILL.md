---
name: sensitive-information-audit
description: Analyse the project and list out all the sensitive information. Use when user say "Do a sensitive information audit", or "Audit the project for sensitive information".
---

# Sensitive Information Audit

## Requirement
- Audit the code for the following sensitive information
    - accidentally committed secrets and credentials
    - hardcoded paths
    - user-specific references

## Report
- Include the file name and line number where the sensitive information are found
- Mask out any sensitive information in the report
- Generate the report sensitive-information-audit in the output folder

## Exclusion
- Do not include files that will not be commited
