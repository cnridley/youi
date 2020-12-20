# YOU&i

You and i is a website built for a personal trainer (Danielle), which has a 
e-commerce store so that she can sell her merchandise, as well 
as a client login which gives her clients a personalized client portal in which 
Danielle can upload their workouts weekly and they can upload progression pictures, weekly measurements
and any comments that they might have.
You&i also contains a gallery so that Danielle is able to advertise her private studio and a review page so that anyone 
can leave a review. 
The website also contains a contact form, that is linked to Danielles e-mail, this is how potential clients contact Danielle
to discuss workout plan options - only Danielle has the ability to create a new user. 

### When no one is logged in:
* only the 'galley', 'merchandise', 'contact', 'client login' and 'reviews' link will be visible on the web page.

### Danielle is the superuser, when she is logged in she has the ability to:
* Register new clients that have contacted her to set up a workout plan. 
* Delete any reviews that she does not like - this is done with a delete button on each review that is only visible
when a superuser is logged in. 
* Edit and delete any of the merchandise - this is done with a edit button which takes
Danielle to a new page and delete button on each review that is only visible
when a superuser is logged in. 
* Upload new workouts for the clients - this is done by logging into the admin page. 

### When clients are logged in:
* When they log in they will be automatically re-directed to their personalized client portal.
* They will be able to upload progression pictures, measurements and any comments they have for Danielle via a form which is
rendered to a bootstrap modal.

# UX
When designing this website, I wanted to keep the color scheme that matched her logo (pink and white), whilst keeping it 
easy to navigate for new users and visually appealing to make potential new clients stay on the webpage and naviagte around
the webpage. 

# User stories

As a superuser I want to achieve ....<br>
(list items marked with 👍 are complete. List items marked with 👎 still need to be implemented)<br>

👍 Any easy to use visually appealing site to attract new clients.<br>
👍 An admin log-in to be able to update site/upload new photos/new products.<br>
👍 Links to social media accounts an every page which are clear. <br>
👎 Clients to be able to book sessions online. <br>
👎 Free t-shirt with purchase of workout plan. <br>
👍 A personalized client portal for every clients, which I can upload new workouts each week on and track their progress.<br>
👍 An e-commerce store so I am able to sell my merchandise online.<br>
👍 A contact form so that future clients have an easy way to contact. <br>


As a client I want to achieve ....<br>
(list items marked with 👍 are complete. List items marked with 👎 still need to be implemented)<br>

👍 A personalized profile so that I can access workouts from anywhere and track my progress. <br>
👍 The ability to buy merchandise online. <br>
👎 Downloadable PDFs.<br>
👎 The ability to book sessions online.<br> 

As a non-authenticated user I want to achieve ....<br>
(list items marked with 👍 are complete. List items marked with 👎 still need to be implemented)<br>

👍 An easy to navigate website so that I can find what I am looking for easily. <br>
👍 A gallery with up-to-date photos of the studio <br>
👍 Information on Danielle and what services she provides. <br>

# Features
* A nav bar with an integrated 'if' statement so that different list items appear depending whether the user is 
an authenticated user, superuser or either.
* Links with target=_blank to social accounts.
* Login page using django Allauth.
* Contact form using django in-built form model.
* Review form so that individuals can leave feedback.
* A photo gallery with a carousel from bootstrap to show the photos and a 'upload new photos' button which is only 
visible to the superuser.
* merchandise store with the ability for users to select sizes, quantity and add to bag.
* Toasts from bootstrap are used to display messages to the user when they have logged in, logged out and added a new item
to their shopping bag. 
* The built-in UserCreationForm from django has been used to allow the superuser to create a new client. 

# Other features left to implement
* Online booking system so that users can book online. 
* A free you&i t-shirt with the purchase of workout plans. 
* Downloadble PDFs available that potential clients are able to download. 
* A blog page, giving Danielle to upload useful articles etc.

# Technologies used
* Jquery so that I could 'write less, do more' and manipulate the DOM easily. https://jquery.com/
* Bootstrap to help making my website mobile responsive, I also used the toats, carousel and modal off bootstrap. https://getbootstrap.com/docs/4.0/getting-started/introduction/
* Font awesome helped make my site more visually appealing by using their icons https://fontawesome.com/
* Google fonts for the font used on my page, I used 'coda' to try and match the logo https://fonts.google.com/
* Django this is the framework I used to make my website https://www.djangoproject.com/
* Django Allauth An django app that is used to make the log in process easier on my site. https://django-allauth.readthedocs.io/en/latest/
* Stripe to take payments on the e-commerce store.

# Testing
* Used the inspect tool on google to make sure my website looks good on all viewport sizes. 
* Tested the links to the navbar go to the correct pages.
* Used the strip test card numbers to make sure that the payment system was correctly working. 
* Set the contact form to send email to the terminal to test that email were sending correctly. 
* Tested the various 'add new ...' buttons on all of the relevant pages to make sure the forms are working. 
* Tested the 'edit' buttons to ensure it was editing the correct product and making the correct changes. 
* Tested the 'delete' buttons to make sure that it was getting deleted from the web page and the admin. 
* Tested allauth functionality to make sure it was linked up correctly and logging the user in correctly. 
* Used a python code checker to check all the code and made changes accoringly. https://extendsclass.com/python-tester.html
* Tested the links to social accounts and made sure they went to the correct social media platform and opened a 
new webpage. 

# Deployment
To deploy this website, I used multiple different programmes. In this section I will go through each programme and outline how 
I used them to deploy the site. 

## Github
GitHub contains my repository and is where my site was deployed until it was 95% complete. 
As I am using GitPod, I was able to use the green gitpod button on my repo so that is was automatically connected to the 
correct repo. 
Every time I updated the site I would then run the following in the command line:<br>
git add .<br>
git commit -m "repository message"<br>
git push <br>

## Heroku 
To deploy to Heroku I did the following:<br>
* Created a new app in my heroku dashboard. 
* In the resources tab I add the 'Heroku Postrgres' add-on. 
* In the CLI in gitpod I installed gunicorn, dj_database_url and , psycopg2-binary these packages are required to push to Heroku successfully.
* Import dj_database_url in settings.py (at the top)
* Within the settings.py file at the database section, comment out the default configuration and replace the default 
to 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')), the DATABASE_URL is from the config vars in the
settings tab of the new heroku app.
* Becuse we are not connected to Postgres I then had to run all the migrations again, using the command,
python3 manage.py migrate - which applied all the migrations to get the database up and running.
* Load the products data by running 'python3 manage.py loaddata products'.
* I then created a new superuser, as we are now using a new database.
* I then uncommented the database settings are wrapped an if statement to outline if the app is running on Heroku we use
Postgres, otherwise we connect to SequelLite. 
* Created a Procfile to tell Heroku to create a web dyno which will run gunicorn and serve the django app.
* In the CLI login to Heroku using the command 'heroku login -i'
* To make sure Heroku does not collect static files when I deployed (because I am using s3 for that), in the 
CLI I ran 'heroku congig:set DISABLE_COLLECTSTATIC=1 --app you-and-i-cr'
* Added the heroku app name ('you-and-i-cr.herokuapp.com') in the 'allowed hosts' within settings.py, as well as loacalhost.
* Deployed my app by running the following commands:<br>
git add .<br>
git commit -m 'repo message'<br>
git push<br>
heroku git -a you-and-i-cr<br>
git push heroku master<br>
* Once the app is deployed correctly, I set up automatic deployment so that any time I pushed to GitHub it 
would also deploy to heroku.
* Created a SECRET_KEY config variable in heroku using the django secret key generator on google, I updated the secret key 
settings in settings.py to os.environ.get('SECRET_KEY', ''), so that the secret keys stays secret.
* Changed DEBUG variable to DEBUG = 'DEVELOPMENT' in os.environ


## AWS (S3 and IAM)

* AWS is a much larger much more feature-ful Heroku - it offer cloud based services, the two I used for this project 
are S3 (simple storage service), that is where I stored my static and media files, the other service I used 
is IAM (Identity and access management) which creates a user to access the bucket. 

### S3:
* Created a new bucket (you-and-i-cr), unchecked block all public access as they need to be public in 
order to allow public access to our static files. 
* In properties tab with in the new bucket, enable static website hosting, using the default values for the error and index
document as it is not needed for my project.
* Within the permissions tab the following three changes were made: <br>
These settings were added to the CORS values.<br>
[<br>
  {<br>
      "AllowedHeaders": [<br>
          "Authorization"<br>
      ],<br>
      "AllowedMethods": [<br>
          "GET"<br>
      ],<br>
      "AllowedOrigins": [<br>
          "*"<br>
      ],<br>
      "ExposeHeaders": []<br>
  }<br>
]<br><br>

Within the bucket policy, I generated a bucket policy, with a policy type of 's3 bucket policy', allowed all
principles by using an asterix, and actions would be 'get objects', and copy and pasted the ARN into the required 
field.<br>
I then copy and pasted the generated bucket policy into the bucket policy editor, adding a /* at the end of the
resource key as we want to allow access to all resources in this bucket.<br><br>

Under the ACL (access control list), I changed the list object permission to everyone.<br><br>

After altering those settings the S3 bucket is ready to go!!

### IAM 
* In the groups tab, I created a new group (yuo-and-i-cr), skipping the attached policy as I did not 
have one yet. 
* Under the policies tab, I created a policy for the new group. Under the JSON tab (after create new policy has been clicked)
I selected import managed policy which let me import one (s3 full access policy) that AWS has pre-built for full access to s3.
* However, I did not want access to all of s3, therefore I retrievd the ARN from the bucket policy page on S3 and 
copy and pasted it into the resources key on the bucket policy. <br>
"arn:aws:s3:::you-and-i-cr",
"arn:aws:s3:::you-and-i-cr/*"<br>
I had to copy it twice, the first line is the bucket itself and the /* adds another rule for all files and folders in 
the bucket.
* I then reviewed the policy, gave it a name and decription and finally created the policy. 
* I then attached the newly made policy to my group that I made. To do this I clicked on the group, 
clicked attach policy, searched the name of the new policy, and click attach policy. 
* Lastly, I created a user to put into the group. On the users tab I clicked add user, gave it a name of
'you-and-i-staticfile-user, gave the programatic access, by clicking next I was able to add the user to the group, 
making sure I downloaded the CSV file at the end as it contains the user access key and secret access key which are needed
later on. 

## Connecting S3 to Django
Once I had finished setting up my S3 bucket and creating the appropriate policy, group and user, I had to connect it 
to Django and store my static files in it. To do this I:
* Installed two new packages in the CLI (pip3 install boto3 and pip3 install django-storages).
* Add 'storages' to my installed apps in settings.py
* Added the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to config variables (these are from the CSV file I downloaded
and are very important to be kept secret!!).
* I also removed the DISABLE_COLLECTSTATIC variable so that static files can now be accessed by s3.
* Added variable 'USE_AWS' and set it to True.
* I then added the AWS settings that can be found in settings.py 
* Created a new file called 'custom_storages.py', to tell django that in production
we want to use s3 to store our static files whenever someone runs collectstatic.
And that we want any uploaded product images to go there also.
* When I then run a git push command, Heroku has collected static files and s3 had a new folder called 'static'
with in the bucket I created. 
* To manage the media files, I did that from the s3 bucket by creating a new folder called 'media', and adding 
all the neccesary pictures for my project, making sure I had granted public read access to this folder. 

### Connecting stripe to heroku
* Within the Heroku app in the config variables, I added the STRIPE_PUBLIC KEY STRIPE_SECRET_KEY and 
STRIPE_WH_SECRET, which were all on my stripe dashboard under the developers/API keys tab.
* I then set up a new webhook handler as the current one is set to github.
To do this I selected create new webhook and had the endpoint URL as the deployed heroku url with /checkout/wh added to the end
and selecting receive all events. 

# Credits
The content and media for the project was provided by Danielle who kindly allowed my to use her Personal 
Training business as a template for my project. 
### Acknowledgements 
Many thanks goes out to Danielle and all of the Code Institute Tutors that helped massively to get this
project to where it it!! 



<div class="card ProductsCard" style="width: 18rem;">
        <div class="card-body">
            <h2 class="card-text">Week: {{ W.weeks }}</h2>
            <hr>
            <h4 class="card-text">Workout: {{ W.body_part }}</h4>
            <hr>
            <h5 class="card-text">Gym or Home: {{ W.gym_or_home }}</h5>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise1 }}</p>
            <p class="card-text">Sets: {{ W.sets1 }}</p>
            <p class="card-text">Reps: {{ W.reps1 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise2 }}</p>
            <p class="card-text">Sets: {{ W.sets2 }}</p>
            <p class="card-text">Reps: {{ W.reps2 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise3 }}</p>
            <p class="card-text">Sets: {{ W.sets3 }}</p>
            <p class="card-text">Reps: {{ W.reps3 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise4 }}</p>
            <p class="card-text">Sets: {{ W.sets4 }}</p>
            <p class="card-text">Reps: {{ W.reps4 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise5 }}</p>
            <p class="card-text">Sets: {{ W.sets5 }}</p>
            <p class="card-text">Reps: {{ W.reps5 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise6 }}</p>
            <p class="card-text">Sets: {{ W.sets6 }}</p>
            <p class="card-text">Reps: {{ W.reps6 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise7 }}</p>
            <p class="card-text">Sets: {{ W.sets7 }}</p>
            <p class="card-text">Reps: {{ W.reps7 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise8 }}</p>
            <p class="card-text">Sets: {{ W.sets8 }}</p>
            <p class="card-text">Reps: {{ W.reps8 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise9 }}</p>
            <p class="card-text">Sets: {{ W.sets9 }}</p>
            <p class="card-text">Reps: {{ W.reps9 }}</p>
            <hr>
            <p class="card-text">Exercise: {{ W.exercise10 }}</p>
            <p class="card-text">Sets: {{ W.sets10 }}</p>
            <p class="card-text">Reps: {{ W.reps10 }}</p>
            <hr>
            {% if request.user.is_authenticated %}
                <small class="ml-3">
                <a href="{% url 'edit_workout' W.id %}">Edit</a> |
                <a class="text-danger" href="{% url 'delete_workout' W.id %}">Delete</a>
            </small>
            {% endif %}
            

        </div>



