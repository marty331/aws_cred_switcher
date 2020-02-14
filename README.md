# AWS Cred Switcher
This is a command line application to allow the user to manage AWS credentials for multiple projects.


## Cred Structure
AWS Creds are stored in the user's Home directory under a folder named ".aws".  Having credentials for multiple software projects using AWS can become a burden to manage when signing in to different projects.  Therefore this app has been built to help manage your multiple AWS project credentials.

## Credential Structure
For AWE Cred Switcher to work correctly you will need to setup your sub-folders in the .aws directory as such for each of your projects as such.
```
.aws
├── billion_dollar_product
│   ├── config
│   └── credentials
├── unicorn_dream
│   ├── config
│   └── credentials
├── config  (will be created)
└── credentials (will be created)
```

## Installation
All steps to be ran from the command line.
Clone this repository (git clone) and cd into the directory.
```
virtualenv venv
. venv/bin/activate
pip install --editable .
deactivate
cp venv/bin/cred_switch /usr/local/bin/
```

Now you can run:
cred_switch
