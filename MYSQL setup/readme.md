# GCP
First I went to the SQL section of GCP and created a new instance. I called it 'hha504-assignment4a' and made sure to change the following settings:
1. The database engine I chose was MYSQL
2. I created the instance name and password
3. I changed the cloud SQL edition to Enterpise
4. Changing the environment to Sandbox instead of Production
5. The machine configuration was changed to a lower level of 1 vCPU, 0.614 GB and using a shared core as to also reduce cost.
6. I made sure the connection was public and added a network called 'Allow All' and gave it the IP of 0.0.0.0/0
7. The final step was to go to the bottom and click 'Create Instance'

All in all the total came out to $0.01 per hour. 

## Issues/Errors 
I didn't run into any issues with creating the instance in GCP. The only issues I had was that once I believed that I done all the steps the price was still at $0.07 and I knew that it should've been lower. After going over the options again and the zoom video from the lecture I realized I didn't change the dedicated core option to shared cores. Other than this I didn't run into any issues. 

# Azure

With this I had a lot of trouble with being able to create a connection from MySQL Workbench to the database I created in Azure. After a lot of trial of error over a few days, I finally did figure out what I did wrong. Instead of creating a MYSQL database, I created a SQL database. I will explain my first attempt and then my final successful attempt.

## First Attempt:
I went into Azure and went to create a SQL database. I didn't realize this mistake until a few days after finding a video explaining the process. Once I created it I tried to connect it to MYSQL workbench, but kept receiving two different errors. The first error was "Failed to connect to local host." The second error appeared after I tried adding @(name of the database) after my username. The second error stated, "failed to log in." After receiving both errors and trying to troubleshoot I looked at different documentation pages and forums on how to solve them.

Troubleshooting:
First I tried to go to Azure's "Connectivity: Troubleshoot DB Availability and Connection Errors." page. This didn't help as much as I thought since I had already made the suggestions.
Secondly, I looked at Microsoft's "Quickstart: Use MySQL Workbench to connect and query data in Azure Database for MySQL." This helped slightly by letting me get rid of the login error by confirming how the username should be established. However, the connection error was still there.


I finally looked at a video that showed me the setup process for creating a MySQL database and that was when I realized my mistake. I had originally not looked at a tutorial on how to create it since I believed that I could figure it out on my own. But that resulted in me not realizing the difference between a SQL database and a MySQL database.

## Final Attempt:
I created the database using the parameters given by you in regards to it being Flexible and B1ms. I had not seen these options before when creating the SQL database and so I definitely felt more confident in what I was doing. Once the database was done deploying I went to the connection section of it where I found instructions on how to connect specifically to MySQL Workbench at https://portal.azure.com/#@stonybrook365.onmicrosoft.com/resource/subscriptions/3b4e4fbc-eeed-4b6c-a82e-7a53fb40af26/resourceGroups/hha504-wk4a/providers/Microsoft.DBforMySQL/flexibleServers/mysql-azure-wk4a/networking. I had to make sure that I added the Firewall rule of AllowAll using 0.0.0.0. I then went into MySQL workbench and opened a new connection. I put in my hostname of mysql-azure-wk4a.mysql.database.azure.com, my username johncd and my password. Once I tested the connection and confirmed that it worked I finally finished it. 

# Python
Here I will explain how I attempted to connect to my database using python with the appropriate libraries and the issues that I encountered along the way. 

## Attempt
First I used the template given to us in class to try and connect to my database that I created in Azure. I then created a .env file to store various information of my database such as:
DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
DB_PORT=
DB_CHARSET=

Then I created a .gitignroe file to ensure that once I push these updates to Git Hub this file wouldn't be shown as it has my credentials for accessing the database. Once I set up the app.py file I ran it, but ran into a connection issue. The error came from "Unknown database” and so I looked to see if it was a connection issue. I then looked up to see that possibly the ‘require_secure_transport’ server parameter in my Azure database was the issue. I then turned it OFF and restarted the database. After it was done I ran the code again, but it still had the same error. Trying over and over I still had the same error and couldn’t get it to work sadly. 
