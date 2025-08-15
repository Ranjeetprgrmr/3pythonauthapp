# To create virtual environment
# first open the command prompt from the folder location of the project
# then type the following command:
# 1st install the package called pipenv
# pip install pipenv
# 2nd type the following command
# pipenv shell
# this create the virtual environment by the name of the folder's name
# so it is 
# 1st pip install pipenv
# 2nd pipenv shell


#  createsuper user credentials
# Username (leave blank to use 'lenovo'):
# Email address:
# Password:
# Password (again):
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.


# TO use postgres in render 
# intall the package psycopg2-binary = pip install psycopg2-binary




# CASE = whenever it was deployed in render it was missing table ,,,,tried postgres but didn't work
# then shifted back to sqlite3 ,,,it worked in local host,,,but it didn't work in render with the same
# issue of django table missing,,,,so GEMINI suggested to add the python manage.py migrate in the build
# command of render app's settings(3pythonauthapp) so i followed that suggestion amd added the command at
# the end of the build command and  it worked.

#Build Command : pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate


# CASE2 = so the app worked in render and when i tried to login with google auth ,it warned of being insecure ,,it suggested to 
# add the url in the google console of the app(3pythonauthapp) to add the redirect url to https://3pythonauthapp.onrender.com/google/login/oauth2/callback ,,,went to google console,,,api & services,,,under OAuth 2.0 Client IDs,,in the project's name ,,
# clicked on it,,and added the url
# # here is the instruction i got from google
# To update or add Authorized Redirect URIs for an OAuth 2.0 client in the Google Cloud Console, follow these steps:

# Navigate to the Google Cloud Console: Access the Google Cloud Console and sign in with your Google account.

# Select your Project: Ensure you have selected the correct project associated with the OAuth 2.0 client you wish to modify.

# Go to APIs & Services: In the left-hand navigation menu, click on "APIs & Services." 

# Access Credentials: From the "APIs & Services" menu, select "Credentials."

# Edit OAuth 2.0 Client ID: Under the "OAuth 2.0 Client IDs" section, locate and click on the name of the specific OAuth 2.0     client ID you want to update. This will open a panel or popup with the client's details.

# Update Authorized Redirect URIs: Within the client's details, find the section labeled "Authorized redirect URIs."

    #To add a new URI, click the "+ Add URI" button and enter the new redirect URL.
    #To modify an existing URI, edit the text field containing the URI.

# Save Changes: After making the necessary additions or modifications, click the "Save" button to apply the changes.
