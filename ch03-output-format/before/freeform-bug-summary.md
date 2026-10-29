Summarize this bug for the team so people know what's going on:

We ship a CLI named linecount. On Windows PowerShell, when the user passes a path with spaces like C:\Users\Ada Lopez\notes.txt without quotes, the tool prints File not found and exit code 1 even though the file exists. On macOS/Linux with proper quoting it works. Someone said it might be related to how we split argv. Priority feels high because Windows users hit it first day. Ticket stub: LINE-218.
