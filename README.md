# Overview

Openxp is not just a backend server but a fullstack web application. The frontend service is hosted in its own repository for the purpose of abstracting backend and [frontend](https://github.com/Open-XP/openxp-frontend) services from one another and development can be done independenty of each other. You can check out the frontend repository [here](https://github.com/Open-XP/openxp-frontend).

If you want to contribute to openxp send a PR and I will look at it as soon as I can. In the mean time you can use our web application by visiting [openxp](http://openxp.study/).

## Check out our application how to use video [here](https://youtu.be/PpmL3YtRZVQ)

# Testing Out the App with a Demo Account

You can try out the app using the follow credentials for testing:

### User Email

```
test@gmail.com
```

### User Password

```
testing@testing
```

# Getting Started With Openxp Backend

## Cloning Our Repository into Our Local Machine

To get started with using and testing the project on our local machine, we have to clone the remote repository onto our local repostory, We can get this done by copy and pasting this code to our terminal:

```
git clone https://github.com/Open-XP/Backend.git
```

**Note**: If you don't have git installed on your local machine follow the direction below according to the platform you currently make use of

- For windows, click [here](https://git-scm.com/download/win) to install and get started and start using git. Also for those who are new to using git here is a useful [video](https://www.simplilearn.com/tutorials/git-tutorial/git-installation-on-windows) on how to get started using git for cloning on windows.

- For Linux all you need to do is run the codes below and you are all set:

```
sudo apt update
```

```
sudo apt upgrade
```

```
sudo apt install git
```

## Creating Our Virtual Environment

This is very important as it helps isolate certain project dependencies from another preventing the overwriting of important dependencies necessary for the proper functioning of various other packages and application. Therefore, getting a virtual environment setup is necessary to get this project up and running as it suppose to. This can be done by copy pasting and running the command below:

```
pip install virtualenv
```

```
virualenv venv
```

**Note**: The keyword venv could be any word at all, this just depends on you. Although the use of env is just a naming convention

**Note**: Change directory into the location where the virtual environment was created then run the code below:

### For Windows

```
env\Scripts\activate
```

### For Linux

```
source env/bin/activate
```

## Installing Necessary Dependencies

For the application to function as intended, it is important the required dependencies are installed onto the virtual environment we created earlier. To do this we can simple run the code below:

```
python manage_dependencies.py install
```

## Creating a Superuser

This is import for managing the local database the project depends on. For the sake of simplicity and for the sake of the project we will be making use of sqlite. We can create a superuser account by running the command:

```
python manage.py createsuperuser
```

While doing this, this will prompt us to input our name email address and input suitable passwords. You can skip inputing a user name if you prefer to make use of the default name.

**Note**: This makes use of the computer's default name. Input your password and hit enter and you are all set.

## Making Migration

Our model have already been setup, all we need to do is instanciate it to add structure all we need to do is instanciate it to add structure to our database. We can achieve this by running the following commands.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## Creating .env File

This file stands in as a link between important pass keys that are essential to the proper functioning of the program. For instance, the app has functionalities which enable sending of OTPs to user email address for authetication. As a result of these functionality, there is a need to conceal the user private information, This is where the `.env` file comes in.

Before we create a `.env` file in the root of the project, we have to import this library into the settings.py file in the CertificateVerification directory. We import the library by pasting the code at the top of the settings.py file:

```
from decouple import config
```

After this we open the `.env` file we created and update the file with the necessary information

```
SECRET_KEY=security_key
DEBUG=True
ALLOWED_HOSTS=your_desired_local_host
CSRF_TRUSTED_ORIGINS=trusted_csrf_trusted_origins
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST_USER=your_desired_email_address
EMAIL_HOST_PASSWORD=your_smtp_password
```

**Note**: It is important to setup our email address to get the application up and running like it ought to. To get our smtp password and **EMAIL_HOST_PASSWORD** get the mailing side of things all setup, we can follow the instructions in the [link](https://drive.google.com/file/d/1qpT1-ttUIz_MqCZnrb8opILXQw1-oXW_/view?usp=share_link).

## Running a Local Instance of the Application

If everything has been properly setup this should spawn a web instance of the certificate verification web application. To get this up and running we need to run the command:

```
python manage.py runserver
```

This will authomaticall create a server at

```
http://127.0.0.1:8000/
```

**Note**: If a brower instance is not automatically started, we can easily copy paste the IP address above to view the running instance.
After we have successfully creaated the server, we can proceed to creating our certificate from the backend by pasting the address into our browser:

```
http://127.0.0.1:8000/admin
```
