# **Gereration RapidAPI Key with Selenium**

## Overview
This is a package to create rapid api key in to Google account with Selenium. After signin
Chrome with login_gmail_selenium package. 

Always active extension is installed by default.
>This has been developed for testing purposes only.
> Any action you take using this script is strictly at your own risk. 
> I will not be liable for any losses or damages you face using this script.

## Requirement
Must have Python <= 3.9 and Google Chrome installed.

## Usage
Then on main.py
```pycon
services = ["https://rapidapi.com/ytdlfree/api/youtube-v31/pricing",
                "https://rapidapi.com/ashutosh05/api/aiov-download-youtube-videos/pricing"]
# Set link to service you need register in rapidapi
# Use array list to configure
```
In accounts.py
```cvs
email1:password1:backupemail1
email2:password2:backupemail2
Configure the account and password according to the form above
```
RapidApiKey will be located in rapid_key.txt
## License
Copyright © 2022 [MoliGroup](https://moligroup.co/), [MIT license](./LICENSE). 
For an improvement or a bug please feel free to open a PR

For work information please contact ngminhhoang1412@gmail.com or 
[LinkedIn](https://www.linkedin.com/in/ho%C3%A0ng-nguy%E1%BB%85n-1b13481b7/).