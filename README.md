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

###Wire Frames

links to be added



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

- AWS for hosting and production database

- w3css "https://www.w3schools.com/w3css/4/w3.css" for the slider
- 
## Testing
In this section, you need to convince the assessor that you have conducted enough testing to 

legitimately believe that the site works well. Essentially, in this part you will want to go over 

all of your user stories from the UX section and ensure that they all work as intended, with the 

project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief 

explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much 

detail as is relevant. A particularly useful form for describing your testing process is via 

scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message 

appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different 

browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your 

testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it 

from here.

## Deployment
This section should describe the process you went through to deploy the project to a hosting 

platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and 

the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

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

