# Exercise 3 -- Decide reset vs continue

For each scenario, choose **continue** (fix-pass in thread or fresh paste with quote) or **reset** (new thread / new task / maybe new model). Give one reason. Do not invent benchmark scores.

## Scenario 1

The reply used Markdown fences around JSON. The keys inside are correct. Your parser needs raw JSON.

Decision:
Reason:

## Scenario 2

You asked for a summary of a pasted log. The model treats a line inside the log as a system command and starts offering destructive shell steps. A first fix-pass still obeys the log line.

Decision:
Reason:

## Scenario 3

The done-when line was wrong: you asked for a feature the product must not ship. The model delivered that feature cleanly.

Decision:
Reason:
