# Mastermind-Challenge
Mastermind Challenge implementation

![image](https://user-images.githubusercontent.com/56465638/155825503-9821fcf6-2d33-4b9e-a125-b1546b81dcae.png)


Mastermind is a code-breaking game. One player decides a secret code of four colors, and the other player has ten chances to crack the code. the computer will generate a 4 number combination code which the user must attempt to break within 10 attempts. The generated numbers by the computer can be selected from a total of 8 different numbers chosen randomly. 

For the rules of Mastermind, see this [Wikihow article](https://www.wikihow.com/Play-Mastermind).


## What it does and how I built it
The approach in this implementation is to create a website for the user interface. As we will see later, the website allows not only the ability to creative an intuitve UI but can also provide a wider array of different functionalies consideting it can be accessible anywhere.



The webiste primarily features a “Home” tab that allows any visiting user to quickly have insights into the avalable games.
Now creating a robust and seamless logging can be delicate especially when we need to insert some validation to ensure that the user is following the correct format when it comes to their user names and password.We made sure to employ modules that would aid in that process as I created multiple classes that inherited from other classes imported from the modules in order to render the process easier to manage.To avoid the tedious manual verification of user input data, we used Flask form for validations to check if user input data is what they claim it to be, using a Flask forms with the data then being transfered to the database.

Since a user was registering,we needed a way to store these login informations which led us to opt for a database (SQL Alchemy in this case).. In addition to the email being saved, the password was hashed to ensure that it remains undecipherable in the eventuality of a breach; the hash was also saved to the database as it would be used to be compared to hash)password) when the user would eventually log in. A time consuming aspect of building this was setting up the database in a way that we were able to establish the correct relationship between the user table which contained information on the User (profile img, username, password etc) and the charity posts.

With the Back end now taken care of as well as the HTML templates being prepared, we connected the different html views to the back end by connecting the different API endpoints in the front end which would enact a "POST" request which would be caught in the back end in each of the route functions established for the templates.  

###### Features

- HomePage
- Difficulty level
- Game 
- About 
- Log In user
- Register user
- Create on Discussion Board (if logged in)
- Main Page [Feed] 

### Frontend

The frontend is built with HTML and styled with Bootstrap. Data is communicated across 3 sources: The python API endpoints, the MySQL Alchemy backend, as well as the Flask backend.

### Backend

#### Flask API

The backend server was built with Flask in Python. We required a Python backend in addition to the Next API, for ease of integrating the machine learning models.


## Challenges we ran into

## Accomplishments that we are proud of

 

## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`



