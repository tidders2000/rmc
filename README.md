# Rate My Crowd

The need for this app comes from the lack of products currently on the market to encourage peer 

recognition in the work place.Typically performance feedback comes from a manager observation 

however the manager is usually poorly placed to notice it. As employees we forget or do not 

appreciate what we achive on a daily basis and when asked about our performance we tend to struggle 

to recount. Our immeadiate colleauges and internal customers are much better placed to recorgnise 

when we do something well. The app creates a platform to share this feedback, recorgnise achivement 

by the way of badges and to bring teams together. The app can then be used as evidence when reviwing 

performance. As a working HR manager having a need for this sort of tool for minimal investement 

this inspired me to use this project to develop something that will fill that gap. The app is aimed 

at smaller businesses with a headcount of 50-300. Companies may wish to have a customised skin so 

design is fairly minimal.




## UX


I was keen for the app to be easy to use and driven by mobile development rather than a desktop app. 

The general design approach was simple and minimal. I aim for this to be a usuable app so there was 

a need to add user autentication from the start. It needs to be easy to find out about colleauges as 

well as add and read feedback. The design challenge is to build a nice looking but practical 

interfacw for users. Although I have tried to do this user feedback would be key for ongoing 

development and this would form a key part of ongoing development.

### User Stories

- Employees to be easily able to add feedback about anyone in the company, even if they did not know 

them personally.

- Employees able to add details about themselves inclusing skills they may be trying to evidence

- A fun factor to try and engage users and build team spirit

- user personal details to be protected

- Able to find out information about my colleauges

- Able to change my details

_ Able to put a name to a face, ie always talk to Joey in accounts in Birmingham on the phone but 

never meet

- Able to easily read feedback written about me

### Wire Frames

https://xd.adobe.com/spec/20ec3011-c4ce-405d-595c-a13f4d6c9e69-56dd



## Features


### Existing Features


-Login pages requires e mail and password or users can create themselves. This could be converted to 

add users on bulk as users would be confined to within a company. Users need to supply team name as 

this is used to identify people with the same name. 

-The home page is dynamic for each user and 

displays key information. Buttons to add badges and feedback and review feedback are prominent. 

Navbar is fairly minimal. Users are able to set their own profile picture and update their profile 

as well as change password. There are currently no minimiumn password criteria. Total feedback and 

pictures of people who have given feedback are also displayed. If you mouse over  badges it shows 

who has awarded it.

- signup. USers get sent an email confirmation when they signup. They also can not register the same 

e mail if it already exsists.


-Add feedback. Names are auto suggested from the current database. For this example version all 

staff have been allocated the team of Audit. In theory you would likely know the team of the person 

you are feeding back on and htis is required for a second identifier as name is not enought( could 

be two steve jones) . However I would like to implement a smoother way of doing this in future.


- Read feedback. feedback headlines and dates are presented. If you do not know a user mouseing over 

the profile pic gives a name. Clicking the heading reveals the actual feedback. Paginatino would 

poteitally need adding to this in the next sprint.

- add badges. A fairly simple screeen. It is deliberate to allow one badge at a time. Badges do not 

currently have a meaning and this could be added

- Colleauges. Again a simple page using cards to show core information about your colleauges to see 

what they are working towards (via there biog). This could also be used to check department




### Features Left to Implement

-Change the feedback screen so it returns department and location for users with the same name in a 

drop down list for the user to select

-Add pagination to the feedback page

-tidy up password change so not showing salted stars

- Add badge names

- At an organisational level it would be useful to analyse feedback trends. A wider dashboard would 

be the next piece of functionality expansion as well as adding the ability to vote and nominate 

employee of the month.

## Technologies Used

-Flask for app development: http://flask.pocoo.org/.I used flask forms and WTF and would use pandas 

for further data anlysis in phase 2.werkzeug for password hashing and flask mail for e mail 

notifications.


-Python for coding https://www.python.org/

-Materialise CSS for page layout and design. https://materializecss.com/

- jQuery for page interaction: https://jquery.com/
Bootstrap 4 for css layout: 

-JQuery
The project uses JQuery to simplify DOM manipulation.

-mysql for the database

-pymysql for using mysql in flask



- w3css "https://www.w3schools.com/w3css/4/w3.css" for the slider
- Amazon RDS to host the production DB
- Clearsql for some testing with the db
- Gunicorn for production web server


## Testing


Unittest was used to test flask routes.

Selenium was used for further automated testing. The following tests were run

-Logon with correct details and get personalised home screen

-Logon with incorrect password/email get flash message

-Registering user with email already in the DB. Email needs converting to lowercase to ensure  consistency in db and for further forms that query using e mail - not fixed yet

-Changing user details under profile- This showed a bug of password/start date being set with blank 
 values. Code was adjusted to compensate


-Adding Feedback to a given user and receiving flash message, showed incorrect formatting corrected

-Checking feedback displays in feedback view and tool tips display users

-Adding and viewing badges and flash message correct and toolstips display users

-Checked that session works and pages cannot be accessed without session token

-Names being listed in dropdown on autotype
-loggin out
-Changing a profile picture and testing the allowed image types

- help displays when clicked


I found during testing very occasionally I would get a 500 error. This had no particular pattern to it.
As i have not done any load testing I have put this down to the flask web server. I have now upgraded to
Gunicorn and performance seems to off improved.



I have not added any backway compatability for old browsers

On checking responsiveness on mobile devices I have noticed profile images on the contacts page do not scale correctly, htis has not yet been fixed

Most testing was done at the end and functionality would be tested manually as I went. However after
completing this project I can now see the need for developing tests as I go to ensure functinoality is not disrupted via development


## Deployment

Deployed to heroku. DB moved across to RDS from cloud dev env. DB is set up on aws rds. A number of values are
stored in env variables and these had to be changed for deployment. There are four test users set up in the database
all users follow the same format email: testuserxxx@email.com (xxx = one,two etc) and all have the password, password. Users
can register as new users but this functionality will be protected after project marking


## Credits


Alot of general advice and tips came from Miguels mega flask tutorial.

Abduls code really helmysql -u USERNAME -p -h RDS-ENDPOINT -D wordpress < backup.sqlped with the name suggesting - http://abdulbaqi.io/2017/11/26/flask-form-

ajax-sqlalchemy/ also this article https://stackoverflow.com/questions/39883425/materialize-

autocomplete-with-dynamic-data-in-jquery-ajax

Badge icons came from https://www.flaticon.com/packs/happiness-13

Kelly Robinsons blog helped with the email notificatoin https://www.twilio.com/blog/2018/03/send-

email-programmatically-with-gmail-python-and-flask.html

This article helped with password hasing https://techmonger.github.io/4/secure-passwords-werkzeug/

Tutorials point for general help on all subjects https://www.tutorialspoint.com/flask/flask_mail.htm

Stack overflow for lots of general posts that put together solved many problems

W3C for code to create a slider

Micheal at code institute for his help in solving the config bug

Micheal Herman discover flask testing (you tube) for test code and videos