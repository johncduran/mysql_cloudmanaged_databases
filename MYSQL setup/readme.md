#GCP
First I went to the SQL section of GCP and created a new instance. I called it 'hha504-assignment4a' and made sure to change the following settings:
1. The database engine I chose was MYSQL
2. I created the instance name and password
3. I changed the cloud SQL edition to Enterpise
4. Changing the environment to Sandbox instead of Production
5. The machine configuration was changed to a lower level of 1 vCPU, 0.614 GB and using a shared core as to also reduce cost.
6. I made sure the connection was public and added a network called 'Allow All' and gave it the IP of 0.0.0.0/0
7. The final step was to go to the bottom and click 'Create Instance'

All in all the total came out to $0.01 per hour. 

##Issues/Errors 
I didn't run into any issues with creating the instance in GCP. The only issues I had was that once I believed that I done all the steps the price was still at $0.07 and I knew that it should've been lower. After going over the options again and the zoom video from the lecture I realized I didn't change the dedicated core option to shared cores. Other than this I didn't run into any issues. 

#Azure