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

<<<<<<< HEAD
### Technologies used
* Jquery so that I could 'write less, do more' and manipulate the DOM easily. https://jquery.com/
* Bootstrap to help making my website mobile responsive, I also used the toats, carousel and modal off bootstrap. https://getbootstrap.com/docs/4.0/getting-started/introduction/
* Font awesome helped make my site more visually appealing by using their icons https://fontawesome.com/
* Google fonts for the font used on my page, I used 'coda' to try and match the logo https://fonts.google.com/
* Django this is the framework I used to make my website https://www.djangoproject.com/
* Django Allauth An django app that is used to make the log in process easier on my site. https://django-allauth.readthedocs.io/en/latest/

### Testing
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
=======
# Technologies used 
* **Jquery** so that I could 'write less, do more' and manipulate the DOM easily. https://jquery.com/
* **Bootstrap** to help making my website mobile responsive, I also used the toats, carousel and modal 
off bootstrap. https://getbootstrap.com/docs/4.0/getting-started/introduction/
* **Font awesome** helped make my site more visually appealing by using their icons https://fontawesome.com/
* **Google fonts** for the font used on my page, I used 'coda' to try and match the logo https://fonts.google.com/
* **Django** this is the framework I used to make my website https://www.djangoproject.com/
* **Django Allauth** An django app that is used to make the log in process easier on my site. https://django-allauth.readthedocs.io/en/latest/



>>>>>>> fa1c576a5426a95402f652ab916a04b58869bbf8
