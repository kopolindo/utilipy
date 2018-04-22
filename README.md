# utilipy
Read from corrupted log, use data and report unrecoverable errors

LANG
	Python2.7

GOAL
- Read from corrupted log files
- Take care of SUBSTITUTE CHARACTERS (ctrl-z = \u001a = 0x1A) that could break python execution on Windows systems
- Take care of any empty line (ignore)
- Take care of data stream interrupted by "\n"
- Try to use data (any use you want, I don't care)
- If not suitable to use, insert them in RECOVER fileF
