# Mastermind Board Game
![image](https://user-images.githubusercontent.com/56465638/155825503-9821fcf6-2d33-4b9e-a125-b1546b81dcae.png)


Mastermind is a code-breaking game. One player decides a secret code of four colors, and the other player has ten chances to crack the code. the computer will generate a 4 number combination code which the user must attempt to break within 10 attempts. The generated numbers by the computer can be selected from a total of 8 different numbers chosen randomly. 

For the rules of Mastermind, see this [Wikihow article](https://www.wikihow.com/Play-Mastermind).
###### Features

- HomePage
- Difficulty level
- Game (Mastermind)
- About us
- Log In user
- Register user
- Create post on Message Board (Players can interact !!)


### Frameworks
- Python3
- HTML
- Flask
- MySQL Alchemy

## Views

Homepage

![Card UI](screenshots/cards_ui-1467754141259.png)

---

Page for choosing difficulty

![Memorizing general knowledge](screenshots/memorize_ui-1467754306971.png)

---

Game Interface. Also provides the ability to view hints/previous guesses

![Code view](screenshots/memorize_code-1467754962142.png)

---

Message board page where people can hold conversations in the form of posted messages

![Code view](screenshots/memorize_code-1467754962142.png)


---

Registration Page

![Code view](screenshots/memorize_code-1467754962142.png)



General folder structure

- game
  - forms template for when user is submitting their guess to the computer
  - support functions for game ex: generatenumbercombination() for user to figure out 
  - session for ability to share data between requests
  - all routing related to game ex: restart game, show hints etc
  - game logic

- templates
  - HTML templates for each webpage
  - Javascript for page animation
  - Bootstrap for styling/components etc

  - error_pages
    - handlers to perform exception handling when user visits invalid page or makes an invalid call

- core
  - routing of core pages such as Homepage/ About us/ Discussion Board posts
  - __init__.py file to mark directories as Python package

- users
  - forms template for userlogin, userregistration and userupdates
  - picture handler for user to update profile picture
  - routing for loggin in user, registrating user, logout, viewing account, showing all posts from user on discussion board 
  - Bootstrap for styling/components etc

- blog_posts
  - forms template for when user is posting to the discussion board
  - routing of when user is creating a post
  - routing of when user is updating their post 
  - routing of when user is deleting their post
  - Retrieves blogpost object from database

- users
  - forms template for userlogin, userregistration and userupdates
  - picture handler for user to update profile picture
  - routing for loggin in user, registrating user, logout, viewing account, showing all posts from user on discussion board 
  - Bootstrap for styling/components etc

- static
  - stores default profile pic for user, audio for webpage

- /mastermindweb [init and models.py]
  - creates flask app
  - assign secret key (for purposes of this project only, this is visible)
  - database set up --> choice: SQLAlchemy for ORM use since small database (abstraction not a factor)
  - sets up database model 




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



