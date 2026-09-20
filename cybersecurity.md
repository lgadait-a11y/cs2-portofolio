#PartA
##Case 1
##1. Phishing Attack
##2. Unsolicited request for credentials
##3. Student Account Credentials
##4. Do not click the link or submit credentials
##5. Multi-Factor Authentication (MFA)
#PartB
##Student Name - Collect because necessary for identification
##Section - Collect because necessary for class identification 
##Club Choice - Collect because necessary for club attendance and forms
##School Email - Collect because necessary for giving out announcements or information
##Attendance Status - Collect because necessary for attendance
##Password - Do Not Collect because passwords can risk hackers getting into your account
##OTP - Do Not Collect because someone could really do something bad on your account
##Home Address - Do Not Collect because any shady person could go to your house and steal something
##Parent Bank Account - Do Not collect because it could get your parents money stolen
#PartC
##Data Capture - Expected Input - Possible Risk - Invalid Input - Validation Rule - Error Message
##Student Name - Letters and spaces - Code injection / Empty input - 12345 - Letters only, non-empty - "Enter a valid name using letters only."
##Section - Letters and spaces - Invalid or missing section - @#$% - Must match valid class list - "Select a valid section."
##Club Choice - Pre-defined club name - Unauthorized entry - Hacking Club - Must select from provided list - "Select a club from the options provided."
##School Email - name@school.edu format - Non-school email / Bad format - name@gmail.com - Must end in @school.edu - "Enter a valid school email address."
##Attendance Status - "Present", "Absent", or "Late" - Invalid status value - Maybe - Must pick a valid status - "Select a valid attendance status."
#PartE
Required tests:
Test Input Situation Expected Result
1 All fields valid Registration accepted
2 Blank name Rejected
3 Invalid section Rejected
4 Invalid club Rejected
5 Email missing @ Rejected
6 Email missing . Rejected
7 Invalid attendance status Rejected
8 Valid alternative values Accepted
