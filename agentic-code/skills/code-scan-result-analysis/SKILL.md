---
name: code-scan-result-analysis
description: Analyse the code scan results and write a report. Use when user say "Analyse the code scan results", or "Analyse the code scan report".
---

# Default Analysis Parameters

- By default, all the code scan results in the project and all its subfolders will be analysed. The user can specify the scope of the analysis, for example, "Analyse the code scan results in the src folder only", or "Analyse the code scan results in the tests folder only".
- By default, only the findings from code scan results with severity of medium and above will be analysed. The user can specify the severity level to analyse, for example, "Analyse the code scan results with severity of low and above", or "Analyse the code scan results with severity of high only".
- By default, do not generate both the markdown format and the CSV format of the **Complete Code Scan Result Listing** in the report. The user can specify to generate the complete listing, for example, "Analyse the code scan results and generate the complete listing in the report", or "Analyse the code scan results and generate the complete listing in a separate file only".

# Code Scan Result Analysis

- Analyse all the findings from the code scan results.
- Provide a summary of the analysis, including
    - the number of findings for each type of issue
    - the overall severity distribution of the findings
    - any patterns or trends observed in the findings (e.g. certain files or modules having more issues than others, certain types of issues being more prevalent than others, etc.)

# Complete Code Scan Result Listing

- List all the findings from the code scan results.
    - For each findings, list the following:
        - The file where the issue is found
        - The line number of the issue
        - The type of the issue (e.g. SQL injection, XSS, etc.)
        - The severity of the issue (e.g. high, medium, low)
        - A brief description of the issue (Use the description from the code scan results, and do not add any additional information to the description)
    - Write the results listing to a markdown table in an appendix in the report.
    - Also write the same results listing to a separate output file in csv format.
