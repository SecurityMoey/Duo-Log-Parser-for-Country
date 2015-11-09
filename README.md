# Duo-Log-Parser-for-Country

The DUO Security platform (www.duosecurity.com) allows an admin to block users in specific countries from using the Multi-Factor Authentication (MFA).  

<b>The Problem:</b>
Geo-ip informaiton is not available for analysis

In the web base admin console, the authentication logs will display geo-ip information (i.e country and city) for single authenication entries.  In order to implement the country block, I would like to review my all my authenication logs and see what countries my users have been authenicating from.  


<b>Solution:</b>
This python script will take your authenication logs in csv and provide you with timestamps, user, ip and country for offline analysis in another csv file.

<b>What do I need:</b>
- authenication logs from Duo in the CSV format
- pyGeoIp Python Module
- CSV Python Module
- GeoIP.dat file
- Luck ;)

If there are ways I could improve this script let me know!
