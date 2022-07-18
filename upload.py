import ftplib                                          # We import the FTP module
session = ftplib.FTP('myserver.com','login','passord') # Connect to the FTP server
myfile = open('toto.txt','rb')                         # Open the file to send
session.storbinary('STOR toto.txt', myfile)            # Send the file
myfile.close()                                         # Close the file
session.quit()                                         # Close FTP session