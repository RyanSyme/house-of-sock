# **House of Sock**

## **Django E-Commerce Website For "Funky" Socks**

---

<!-- ![House of Sock](Multi shot here) -->
The main goal of this project is the development of an e-commerce website using Django. It is a website dedicated to selling fun and unusal socks. It has been built with a fun but simple user expeierence
as one of the central goals. The user can search the website for products they would like to purchase, they can add them to a wishlist to purchase at a later date or add them to the shopping cart. They can then checkout using the Stripe payment system.
When a user signs up a profile with all their past orders is created which they can view at any time. The site is designed to be easy to navigate and lighthearted to provide a fulfilling user experience so happy customers are encouraged to return.

---

<!-- ### **_Table of contents:_**

1. [Description](#sandwich-recipe-database)
2. [UX](#ux)
    1. [The Objective](#the-objective)
    2. [Wireframes](#wireframes)
    3. [Styling](#styling)
    4. [User Stories](#user-stories)
3. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features Left to Implement](#features-left-to-implement)
4. [Technology Used](#technology-used)
5. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](manual-testing)
6. [Deployment](#deployment)
    1. [Remote Deployment](#remote-deployment)
    2. [Local Deployment](#local-deployment)
7. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Acknowledgements](#acknowledgements) -->

---

## **UX**


### **Strategy Plane**

The main target audience for House of Sock are:
- Age 18 - 50 as the products are light hearted but not childish.
- Users who love socks.
- Users who like to show their humor in their clothing choices.
- Users looking for a slightly unusal take on the 'socks for christmas/birthday' gifts for loved ones.

The objective of this website is to provide users that love socks with an application that allows them to sign up, login, purchase or 'wishlist' their favorite socks and store their delivery information for a speed service on their return.

### **Scope Plane**

On this site a user is able to:

- View the full range of socks available
- Search the socks by keyword
- Search the socks by mens or womens categories
- Add any product to their wishlist
- View each individual pair of socks and a description
- Sign up to an account
- Login as an existing user
- Log out of their account
- View their profile page showing previous purchases (if any exist)
- Leave a review (if signed in)
- Leave a rating (if signed in)

### Skeleton Plane

#### **Wireframes**
<!-- ![Sitemap](static/readme-files/sitemap.png)
![Index](static/readme-files/index.png)
![Sandwiches](static/readme-files/sandwiches.png)
![View-Sandwich](static/readme-files/view-sandwich.png)
![Login](static/readme-files/login.png)
![Sign-Up](static/readme-files/signup.png)
![Profile](static/readme-files/profile.png)
![Create-Sandwich](static/readme-files/createsandwich.png) -->

<!-- you can find a full size PDF of the Wireframes [here](https://bea8e478-4bc6-44df-a287-ee1dbc1f65af.ws-eu03.gitpod.io/files/download/?id=6065fa6f-18e7-4c7c-97f5-54ef1e094bae)  -->

<!-- #### **Design Differences** -->

<!-- There are some minor differences from the original conception and the final website.

* Originally I planned to have the Login and Sign up in the same place and have only one link in the Nav. I decided it would be cleaner to have a Login section and a sign up section.
* I made the callout image a rolling carousel to make the home page more interesting and inviting.
* I changed the search option from a "main ingredient" search to an "any ingredient" search for ease of use for the user.
* I moved the sandwich description in the "view sandwich" page, from the side of the image to underneath, purely for aesthetical reasons.
* I removed the "create a new sandwich" button from the profile page, as I felt it was an unnecessary addition.
* I changed the database category from "main ingredient" to "category" for ease of use for the user (if a sandwich has only two ingredients, which is the main one?). -->

### **Surface Plane**

#### *Framework*
As well as HTML and CSS. Bootstrap, Javascript and jQuery have all been used to form the structural layout of this website.

#### *Fonts*
The Google font Noto Serif had been used as the main font thoughout the website
The Google font Rock Salt had been used as the logo font and is used for most of the headers.

<!-- #### *Colors* -->
<!-- * There are four non-image colors used on the website: -->
    
    <!-- ![Colors](static/readme-files/colors.png)
    *   #2b2d42 has been used for the main text and buttons
    *   #9fd9de has been used for the Nav, Footer and containers
    *   #ffffff has been used for the some text and boxes
    *   #e6e6e6 has been used for the main background color
    *   #993300 has been used for the blue hover response color -->


### **User Stories**

* **First Time Visitor Goals**

    * *As a First Time Visitor*, I want to know immediately, the purpose of the website.

    * *As a First Time Visitor*, I want to be able to navigate the website simply and easily.
    * *As a First Time Visitor*, I want to access the site across all devices.
    * *As a First Time Visitor*, I want to be able to learn more about each product.
    * *As a First Time Visitor*, I want to be able to sign up as a user.
    * *As a First Time Visitor*, I want to be able to checkout without having to first register an account.
    * *As a First Time Visitor*, I want to receive an email confirmation of my order and be able to register for an account.


* **Returning Visitor Goals**

    * *As a Returning Visitor*, I want to be able to save my delivery info for quicker future checkouts.

    * *As a Returning Visitor*, I want to be able to update my delivery and billing information if necessary.
    * *As a Returning Visitor*, I want to be able to view my order history
    * *As a Returning Visitor*, I want a way to save products that I am interested in so I can purchase them at a later date.
    

* **Store Owner Goals**
    * *As a Store Owner*, I want to be able to add new products to the website.
    * *As a Store Owner*, I want to be able to update products on the website.
    * *As a Store Owner*, I want to be able to remove products from the website.
    * *As a Store Owner*, Be confident that other users cannot add, remove, or update the products on my website.
---

## **Features**

* The Project is a multi-page website which uses a Django database and Python template management.

    1. The Index page consists of a Nav section and footer section that feature on every page. It also includes a callout image with a sign up button and a latest products section.
    <!-- ![Top](static/readme-files/top.png)    
    ![Carousel](static/readme-files/carousel.png)    
    ![Latest](static/readme-files/latest.png)     -->
    
    2. The Products section displays the full database of socks that can be viewed and purchased. Each pair of socks has its own card showing an image of the socks, their name and price. Each card also has view button which allows the user to enter the product_detail page.
    <!-- ![Sandwich Cards](static/readme-files/sandwichesscreen.png) -->
    
    3. The Product Detail page allows the customer to see the socks with a larger image and has a fun description of the socks. Here the cuctomer can add the socks to their wishlist (if signed in), read any reviews of the sock that other customers have made, add their own review (if signed in) or add the socks to their shopping cart for purchasing.
    <!-- ![Add Sandwich](static/readme-files/addsandwichscr.png) -->
    
    4. The Login and Register sections take the customer to the related page, allowing the customer to either login or sign up. The pages have links to each other in case the customer has click the wrong one.
    <!-- ![Login](static/readme-files/loginscr.png)
    ![Sign Up](static/readme-files/signupscr.png) -->
    
    
    5. The profile section shows the user their delivery information and any historical purchases they have made.
    <!-- ![Profile](static/readme-files/profilescr.png) -->
    
    6. The log out button logs the user out and returns them to the landing page.
    <!-- ![Log Out](static/readme-files/logout.png) -->

    7. The Admin has an additional pages where they can add, edit or remove products from the database.
    <!-- ![Categories](static/readme-files/categories.png) -->

### Features Across All Pages

*	The site has been designed to be responsive across all devices

*	The navbar remains on every page, allowing easy navigation at all times, On larger screen it remain on screen at all times and on smaller screen it can be found at the top of the page. It gives the user the ability to move to any area of the site they wish to see as well as being able to log out.
*	The navbar is styled differently for different screen sizes, changing from a three line “hamburger” dropdown nav on mobile to a traditional full screen navbar on larger screens
*   The main logo moves from it's own coloumn at the top of the page on large screens to the middle of the Navbar on smaller screens
*	The user has the ability to sign up and/or login using the relative areas in the Account section
*	The footer displays the social media links.
*   The user can access the shopping cart at anytime using the link on the navbar

### Features Specific to Pages

#### Index Page

*   A callout image and slogan with a sign up button which changes to a button directing the user to the products page once logged in
*   A Latest products section that shows the for latest products entered into the database

#### Products Page

*	Any user can view all of the products in the database
*   The products page is paginated to 12 products per page
*   The user can search through all of the product by any keyword using the search bar on the products page.
*   The products page can be viewed by category (Mens or Womens)
*   Each product has a link within it's image (that has a border when hovered over) as well as a view button that will send the user to the product detail page

#### Product Detail Page

*   The Product Detail page shows a larger image of the product and a description
*   The category listed on the page links to the product page for that particular category of sock
*   The user can add products to their wishlist (if signed in)
*   Their are both size and quantity buttons to add multiple pairs of socks and different sizes
*   A "Keeping Socking" button to return the user to the products page with a description of "keep socking" if the user isn't sure what it is
*   An add to cart button to add the product to the shopping cart
*   A reviews section with previous customer reviews and ratings
*   The user can add their own review and/or rating if signed in

#### Profile Page

*   The profile page stores and shows the users delivery info which can be updated by the user
*   The profile page show the users order history with a link to each individual order

#### Wishlist

*   

#### Shopping Cart

*   Shows the items in the shopping cart. Shows an image, the product info, the price, quantity and a sub total.
*   The quantity can be updated
*   A product can be completely removed from the cart
*   A user is given free deliver if they spend over €30 euros. A message below the grand total informs them of this
*   If the cart total reaches €30 the delivery cost is automatically removed
*   If empty, informs user of this fact and supplies a button returning them to the product page

#### Checkout Page

*   Displays an order summary with images
*   Displays a deliver details form with any known information already on the form
*   Allows payment for the order via Stripe or the user can return to their shopping cart to make any changes they wish

#### Checkout Success Page

*   Shows the customers order number, date of order, order details, delivery and billing info
*   Confirms that an email has been sent to the user about their purchase
*   Has a button that returns the user either to the products page or their profile page depending on from where they accessed the page

#### Wishlist Page

*   Displays any products that the user has placed on their wishlist
*   From the wishist page the user can either view the product detail page of any product on their wishlist or return to the product page via a Keep Socking button
*   User has the ability to delete products from the wishlist


### **Features Left to Implement**

<!-- * A 'like' or grading feature that allows user to rate other users sandwiches

* Some defensive programing to ask a user if they are sure that they want to delete a sandwich or not once the delete button has been pressed
    * This would also be needed for the admin page on the delete category button -->

---

## **Information Architecture**

A relational database was used to store the data. The developmental database used was [SQLite](https://www.sqlite.org/index.html), and the deployed database used was
[Heroku](https://www.heroku.com/postgres). The use of a relational database allowed me to connect data stored in separate models through the use of foreign keys.

The models created for this website are as follows:

Order Model:
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

<!-- The following technologies were used to create this website:- -->

<!-- ### **Languages** -->

<!-- *	**HTML5**

*   **CSS3** 
*	**JavaScript**

    have been used throughout the project to create the text, style and functionality of the website.

*	[Python](https://www.python.org/) has been used to run the application -->

<!-- ### **Frameworks and Libraries** -->

<!-- *   [Jquery]( https://jquery.com/) were used to implement the carousel function on the image carousel section and to simplify DOM manipulation

*	[MongoDB](https://www.mongodb.com/) has been used to to store the database
*	[Flask](https://flask.palletsprojects.com/en/1.1.x/) has been used to to dynamically generate pages, links, and content within the app
*	[PyMongo](https://pypi.org/project/pymongo/) has been used to connect to and transfer data to MongoDB
*	[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) has been used to template the website
*	[Bootstrap]( https://getbootstrap.com/) was used for layout aesthetics, including grid styling and device responsiveness
*	[GitHub]( https://github.com/) was used to host the website
*	[Gitpod]( https://www.gitpod.io/) was used to code the website -->

<!-- ### **Software and Resources** -->

<!-- *	[FontAwesome](https://fontawesome.com/) was used to add icons to the exercise class headers

*	[Gimp]( https://www.gimp.org/) was used to size the images
*	[Balsamiq]( https://balsamiq.com/) was used to create the wireframes of the project
*   [FireShot](https://getfireshot.com/) was used to create the screenshots for the README
*   [Techsini](https://techsini.com/multi-mockup/) was used to style the multi screen mockup
*   [Coolors](https://coolors.co/) was used to create the color palette screenshot
*   [User-Agent Switcher](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) was used for testing functionality on different browsers -->

---

<!-- ## **Testing** -->

<!-- ### **Testing User Stories from the UX Section** -->


<!-- **First Time Visitor Goals** -->

<!-- * *As a First Time Visitor*, I want to be able to navigate the website simply and easily.
    *   On opening the website the visitor is met with the callout section which has a button connecting to the sign up page and a sticky nav directing the user to relevant pages

* *As a First Time Visitor*, I want to access the site across all devices.
    *	The website is responsive across all devices
    
* *As a First Time Visitor*, I want to see other users creations.
    *	The nav has a sandwiches button that links to a page that show all of the sandwiches in the database.

* *As a First Time Visitor*, I want a way to search other users creations.
    *	The sandwiches page has a prominent search bar that allows the user to search through the the sandwiches by ingredient.

* *As a First Time Visitor*, I want to be able to sign up as a user.
    *   There is a sign up link in the nav and also a button under the callout guiding the user to the sign up page.
    *   The user only need to provide a user name email and password to sign up.

* *As a First Time Visitor*, I want to add my own creations.
    *   Any member can add a sandwich to the database via the 'add sandwich' page.
    *   The user can add any type of sandwich they wish and can add an image if they wish. If they choose not to add an image, one is added for them automatically.

* *As a First Time Visitor*, I want a page where I can see my own creations.
    *   A signed in user can view all of their own sandwich creations on their profile page. -->

<!-- **Returning Visitor Goals** -->

<!-- * *As a Returning Visitor*, I want to be able to inspect and edit my own creations.
    *   On the profile page, the user can edit or remove any of their own creation if they so choose.
    *   The user can also edit or remove their sandwiches from the view sandwich page.

* *As a Returning Visitor*, I want other users to view my creations but not edit them.
    *	Users can view any sandwich in the database via the sandwiches page and see them in more detail on the view sandwich page.
    *   No user can edit or delete another users sandwiches

* *As a Returning Visitor*, I want to easily navigate to the log in page to view my profile
    *	The sticky nav has a link to the login page
    *   Once logged in a user is directed to their profile page

* *As a Returning Visitor*, I want to view all of the sandwiches I have added to the site
    *   The users profile page displays a collection of all of their own sandwiches

* *As a Returning Visitor*, I want to be able to delete any of my own creations I no longer want.
    *   The user can edit or delete any of their own creations at any point as long as they are signed in
    *   Users can only edit or delete sandwiches that they have created.

* *As a Returning Visitor*, I want to be able to log out of the site.
    *   There is a log out button on the sticky nav that can be used on any page of the site. -->

<!-- ### **Code Validation** -->

<!-- #### *W3 Validators* -->

<!-- *    The HTML was Validated at [W3C Markup Validation Service](https://validator.w3.org/). 

*    The CSS was Validated at [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).

*   The Python was Validated at [pep8online](http://pep8online.com/) -->

<!-- ### **Manual Testing** -->

<!-- #### *Google Developer Tools* -->

   <!-- *    The websites design responsiveness has been tested on all device sizes using Google Developer Tools. -->

<!-- #### *Testing On Mobile Devices*
   *    Apple iOS
   *    Google Android 7
   *    Microsoft Windows Phone
   *    Samsung Tizen OS
   *    Nokia Symbian
   *    Mozilla Firefox OS -->
 
<!-- #### *Testing On Browsers*
   *    Google Chrome
   *    Opera
   *    Firefox
   *    Apple Safari
   *    Microsoft Explorer
   *    Microsoft Edge -->
    
<!-- #### *Testing On Operating Systems*
   *    Microsoft Windows
   *    Linux
   *    Apple Mac OS
   *    Google Chrome OS
   *    IBM Warp -->

<!-- ### **Defensive Design Testing** -->

<!-- #### Index page -->

<!-- *   Test all links and buttons on Index page:
    *   All Navbar buttons link to the page expected
    *   All footer links to social media function as expected
    *   Buttons on the "latest sandwiches cards direct to expected sandwich pages
    *   "Get Started" button appears and directs user to Sign Up page if not already signed in -->

<!-- #### Sign Up page -->

<!-- *   Test Sign Up form:
    *   User cannot create an account without entering a username with less than 5 characters
    *   Email Address must have an @ symbol
    *   Password must be letters and/or numbers and must be between 5-15 characters long
        *   If any of these points fail a message appears informing the user what is needed
    *   The link switching the user from login to sign up at the bottom of the form functions correctly -->

<!-- #### Login page -->

<!-- *   Test Login functionality:
    *   User must enter a correct username already on the system
    *   User must enter the correlating password already on the system
        *   If either of these points are not achieved a "incorrect/username or password" message flashes
    *   The link switching the user from login to sign up at the bottom of the form functions correctly -->

<!-- #### Profile page -->

<!-- *   Test buttons and links:
    *   Once signed in the customer recieves a welcome message with their username so they are aware that they have been signed in
    *   The Added Sandwich button takes the user to the Add Sandwich form
    *   The Edit Sandwich button takes the user to the Edit Sandwich form
    *   The Delete Sandwich button removes the sandwich -->

<!-- #### Add Sandwich page -->

<!-- *   Test Add Sandwich form works:
    *   The sandwich name must be between 3-50 characters
    *   The sandwich must have a description
    *   A category and prep time must be selected
    *   The form needs at least one ingredient and one instruction
    *   If no Image url is added or is added incorrectly, a default image is used
    *   Once a sandwich is created the user is directed to the sandwiches page -->

<!-- #### Edit Sandich page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Logout Buttons -->

<!-- *   Test Logout Button:
    *   Pressing the logout button logs out the user and returns them to the login page -->

<!-- ### Admin Testing -->

<!-- #### Admin Profile page -->

<!-- *   Test Admin Profile Page:
    *   When signed in as admin, the profile page show an Edit Categories button
    *   The Edit Categories button takes the admin to the Edit Categories page

*   Test Edit Categories Page:
    *   The Add Category button takes to the Add Category page, where the admin can add a new category using the single input form
    *   The Edit Category button takes to the Edit Category page, where the admin can edit the name of the category using the single input form
    *   The Edit Category form has a CAncel button that stops the edit and returns the admin to the categories page
    *   The Remove Category button removes the category from the database -->
    
<!-- #### *Issues Found* -->

<!-- *   An issue was found with the carousel and callout text being on the same line on different device sizes, the resizing would make the text too large and the carousel too small.
    *   The issue was resolved with some changes to the css in the media queries and by using the bootstrap grid system.

*   Originally the minimum number of letters for the sandwich names was set at 5. It became apparent early on that this was an error as one of the worlds most famous sandwiches is a 3 letter Acronym "BLT"
    *   The minimum letter count on the sandwich name input was changed to 3. -->

---

<!-- ## **Deployment** -->

<!-- ### **Remote Deployment**
1. Navigate to the GitHub [Repository:](https://github.com/RyanSyme/url-of-sandwich)
2. Open [repository](https://github.com/RyanSyme/url-of-sandwich) using [GitPod](https://www.gitpod.io/) IDE.
3. In terminal run "pip3 freeze --local > requirements.txt" command to create a .txt file with all of the dependencies used that [Heroku](https://www.heroku.com) needs to know what dependencies app uses.
4. In the terminal run the "echo web: python app.py > Procfile" command to create Procfile that [Heroku](https://www.heroku.com) needs to know what file runs the app.
5. Go to [Heroku](https://www.heroku.com) and log in.
6. Once logged in, and in your dashboard, click on "Create New App".
7. Under "Create New App" click on the input field called "App Name".
8. Give your app a unique name and select the closest region to your location.
9. Click "Create App"
10. In the "Deployment Method" section, connect the app by clicking on the "Github" icon.
11. Type the Github repo-name in the "Connect to Github" section input.
12. Click "search" to find the repo and once it is found click "connect".
13. Before clicking the "Enable Automatic Deployment" button, click on the settings tab in the top part of the page.
14. Click on "Reveal Config Var".
15. Here you can inform Heroku of which variables will be required.
16. The required variables are: (IP, PORT, MONGO_URI, MONGODB_NAME, SECRET_KEY).
17. Go back to [GitPod](https://www.gitpod.io/) and make sure that you have pushed your requirements.txt and Procfile to the repo.
18. Return to Heroku and click on "Enable Automatic Deployment".
19. Select your branch. Branch selected (master).
20. Click "Deploy Branch"
21. Once deployment is finished click "View" to launch the new app. -->


<!-- ### **Local Deployment**
1. Navigate to the GitHub [Repository:](https://github.com/RyanSyme/url-of-sandwich)
2. Click the **Code** drop down menu.
3. Download the ZIP file and unpack locally
4. Open a code editor of your choice and open the unzipped file using the code editor.
5. Click **Save** and save to your local device
6. In order to have a functional app, you will have to create your own MongoDB collection and inserted your "MONGO_URI" and not the one used in the project. -->

---

<!-- ## **Credits** -->

<!-- ### **Content** -->

<!-- *	My code was influenced by The Data Centric Development Mini Project lesson from the [Code Institute](https://courses.codeinstitute.net/login) Full Stack Developer Course. -->

<!-- ### **Media** -->

<!-- *   All images used for the carousel, logo and default sandwich card were obtained from [Pixabay](https://pixabay.com/)
    *   With special mention to:
        *   [andreas160578](https://pixabay.com/users/andreas160578-2383079/)
        *   [Christine_Sponchia](https://pixabay.com/users/sponchia-443272/)
        *   [Clker](https://pixabay.com/users/clker-free-vector-images-3736/)
        *   [LuckyLife11](https://pixabay.com/users/luckylife11-5245360/)
        *   [tookapic](https://pixabay.com/users/tookapic-1386459/) -->


<!-- ### **Acknowledgements** -->

<!-- *   I received advice for improving my search bar code from my Code Institute mentor **Oluwafemi Medale**

*   Additional help to create a default image on sandwich cards is credited to [StackOverflow](https://stackoverflow.com/questions/7995080/html-if-image-is-not-found)

*	I received styling inspiration from:

    *   [BBCGoodFood](https://www.bbcgoodfood.com/recipes/egg-less-mayo-sandwiches) 
    
*   Additional Thanks to my mentor **Oluwafemi Medale** for styling and formatting advice. -->

