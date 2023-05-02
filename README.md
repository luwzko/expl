# expl
  expl is a simple Python program written to find binaries with SUID/SGID bit set and finding if the binaries entries exist on GTFObins, if yes it prints them out.
  This tool was written in mind with simplicity, to automate boring task of finding GTFObins entries. 
  This tool is not a foolproof and easy way to hack, it just provides some information that is easily accessible to you but automates it...
# How does it work?
  1. The command `find / -type f -perm -04000 -ls 2>/dev/null` is executed and the output is retrieved.
  2. Then `(\/[0-9A-Za-z_.\-]+)+` regex is compared to the output and all instances of binary paths are found.
  3. Then iterating thru all binary paths and using `requests` library to find if a entry exists.
  4. If yes binaries are saved to a list and then the list is printed out
# Execution
  1. Classic - Creating a Python file and running it with the `python` command.
  2. Using python command and `requests` - `python -c "import requests; r=requests.get('https://raw.githubusercontent.com/luwzko/expl/main/expl.py'); exec(r.text)"`
     - This way using `requests` you make a GET request to raw GitHub URL and execute the expl code at the GitHub URL.
