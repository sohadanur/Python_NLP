import win32com.client as client

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)

message.Display()  # Optional: Displays the email in Outlook before sending

message.To = "bacbonsohada@outlook.com"  # Recipient email address
message.CC = "20-43386-1@student.aiub.edu"  # CC (Carbon Copy) email address
#message.BCC = "sohadanur01@gmail.com"  # BCC (Blind Carbon Copy) email address
message.Subject = "Happy Birthday"  # Email subject
message.Body = "Wish you a happy birthday!"  # Email body (plain text)

message.Save()  # Optional: Saves the email
message.Send()  # Sends the email
