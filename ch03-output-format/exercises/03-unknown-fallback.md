# Exercise 3 -- add an "if unknown, say UNKNOWN" fallback

Take either your schema from Exercise 1 or the chapter's five-key bug object. Add an explicit fallback rule and a way to audit which fields used it.

## Fallback sentence (copy into Constraints)


## Audit mechanism

How will you see which fields were UNKNOWN? (examples: a parallel `unknown_fields` array; a required literal; a post-parse check)


## Tiny test cases

List three inputs. For each, mark which fields should be real values vs UNKNOWN.

| Case | Real fields | UNKNOWN fields |
| --- | --- | --- |
| A | | |
| B | | |
| C | | |

## Pass/fail note

A reply that invents a root cause when Context had none fails, even if JSON parses. Write that as one success-criterion bullet:
