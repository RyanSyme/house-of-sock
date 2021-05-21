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
[Heroku](https://www.heroku.com/postgres). The use of a relational database allowed me to connect data stored in separate models through the use of foreign keys and onetoone fields.

### Structure
The models created for this website are as follows:

Order Model - Stores information on each order.

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| order_number | CharField | The order number for this order. Uniquely identifies the order. |
| user_profile | ForeignKey | Foreign key used to identify the user that this order belongs to. |
| full_name | CharField | The users name. Used for billing and delivery. |
| email | EmailField | The users email. Used to send the user a copy of their order. |
| country | CountryField | The users country. Used for billing and delivery. |
| postcode | CharField | The users postcode. Used for billing and delivery. |
| town_or_city | CharField | The users town or city. Used for billing and delivery. |
| street_address1 | CharField | The users street address. Used as billing and delivery. |
| street_address2 | CharField | The users street address (secondary line if needed). Used as billing and delivery. |
| date | DateTimeField | The date and time the order was placed. |
| delivery_cost | DecimalField | The of cost delivery for the order. |
| order_total | DecimalField | The sub-total of the order. |
| grand_total | DecimalField | The grand_total of the order including delivery cost. |
| original_cart | TextField | A copy of the users ordered products. |
| stripe_pid | CharField | The users stripe payment intent id. |

OrderLineItem Model:
Stores the products that the user has ordered and is attached to their order in the Order model.

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| order | ForeignKey | Foreign key attached to the Order model. Identifies which order it belongs to. |
| product | ForeignKey | Foreign key attached to the Product model. Identifies product ordered. |
| product_size | CharField | The products size. |
| quantity | IntegerField | The quantity of the product ordered. |
| lineitem_total | DecimalField | The total of quantity * product price |

Category Model:
Stores information on which category the product belongs to.

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| name | CharField | The name of the product |
| friendly_name | CharField | a simplifed name to make it user friendly. |


Product Model:
Stores information on products sold on the website.

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| category | ForeignKey | Identifies a category the product belongs to. |
| sku | CharField | Unique identifier for each product. |
| name | CharField | The products name. Used for queries and display purposes. |
| description | TextField | A description of the product. Used for queries and display purposes. |
| size | BooleanField | The products size. |
| price | DecimalField | The price of the product. Displayed as content. |
| ---- | ----- | --------------- |
| rating | DecimalField | The products customer rating. Displayed as content. |
| ---- | ----- | --------------- |
| image | ImageField | This is an image of the product. Displayed as content. |
| image_url | URLField | The image url for the product. Displayed as content. |

Review Model:
Stores information from user reviews

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| product | ForeignKey | Foreign key attached to the Product model. Identifies product being reviewed. |
| user | ForeignKey | Foreign key attached to the user model. Identifies user creating the review. |
| content | TextField | The content added by the user for the review. Displayed as content. |
| stars | IntegerField | The rating this user is giving the product. Displayed as content. |
| date_added | DateTimeField | The date and time the review was added. Displayed as content. |

UserProfile Model:
A user profile model for maintaining delivery information and order history

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| user | OneToOneField | A OneToOne Field that identifies the User that the default information belongs to. |
| default_street_address1 | CharField | The users street_address1. For auto filling the checkout form on the users next checkout. |
| default_street_address2 | CharField | The users street_address2 (if applicable). For auto filling the checkout form on the users next checkout. |
| default_postcode | CharField | The users postcode. For auto filling the checkout form on the users next checkout. |
| default_town_or_city | CharField | The users town or city. For auto filling the checkout form on the users next checkout. |
| default_country | CountryField | The users country. For auto filling the checkout form on the users next checkout. |

Wishlist Model:
A model to link a user to bookmarked product

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| user | OneToOneField | A OneToOne Field that identifies the User that the wishlist belongs to. |
    
WishlistItem Model:
bookmarks products to the wishlist

| Key | Model Type | Purpose |
| ---- | ----- | --------------- |
| wishlist | ForeignKey | A Foreign Key that retrevieves the User that the wishlist belongs to. |
| product | ForeignKey | Foreign key attached to the Product model. Identifies product being added to the wishlist. |

Allauth User Model:
Stores the users registration information. A default model installed from django.

#### Relationship
- The relationship between the models are displayed here

    <!-- make data-schema and post it here!!!! -->

The following technologies were used to create this website:-

### **Languages**

*	**HTML5**

*   **CSS3** 
*	**JavaScript**
*	[Python](https://www.python.org/)

### **Frameworks and Libraries**

*	[Bootstrap]( https://getbootstrap.com/) was used for layout aesthetics, including grid styling and device responsiveness

*   [Jquery]( https://jquery.com/) Used in stripe javascript logic
*	[Django](https://www.djangoproject.com/) has been used as the main framework to build the project.
*	[Stripe](https://stripe.com) - used to facilitate payments.
*	[Psycopg2](https://pypi.org/project/psycopg2/)  has been used to allow postgresSQL to be used with python
*   [Heroku](https://www.heroku.com/) - Used to deploy the live website.
*	[GitHub]( https://github.com/) was used to host the website
*	[Gitpod]( https://www.gitpod.io/) was used to code the website

### **Software and Resources**

*	[FontAwesome](https://fontawesome.com/) was used to add icons to the exercise class headers

*	[Gimp]( https://www.gimp.org/) was used to size the images
*	[Balsamiq]( https://balsamiq.com/) was used to create the wireframes of the project
*   [FireShot](https://getfireshot.com/) was used to create the screenshots for the README
*   [Techsini](https://techsini.com/multi-mockup/) was used to style the multi screen mockup
*   [Coolors](https://coolors.co/) was used to create the color palette screenshot
*   [User-Agent Switcher](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) was used for testing functionality on different browsers
*   [Gmail](https://mail.google.com/) - Used to send emails.

---

## **Testing**

All testing has been documented in [TESTING.md](TESTING.MD) file

---
## **Deployment**

<!-- ### **Remote Deployment** -->
<!-- 1. Navigate to the GitHub [Repository:](https://github.com/RyanSyme/url-of-sandwich) -->
<!-- 2. Open [repository](https://github.com/RyanSyme/url-of-sandwich) using [GitPod](https://www.gitpod.io/) IDE. -->
<!-- 3. In terminal run "pip3 freeze --local > requirements.txt" command to create a .txt file with all of the dependencies used that [Heroku](https://www.heroku.com) needs to know what dependencies app uses.
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


### **Local Deployment**
### Pre-requisites
- [Python 3](https://www.python.org/downloads/) - used to write the code and to run the project
- [PIP](https://pypi.org/project/pip/) - used to install packages
- [Git](https://git-scm.com/downloads) - used for version control
- [Visual Studio Code](https://code.visualstudio.com/) or any IDE of your choice - used to compile the code.
- [Stripe](https://stripe.com/en-ie) Account


### Steps

1. Navigate to the project [repository](https://github.com/RyanSyme/house-of-sock)

1. Download the files by clicking the 'Code' button located at the top of the repository, select 'Download ZIP' and unzip the files to the directory of your choice.
    
1. In your IDE, navigate to the project directory where you downloaded files in the repo

1. Activate your virtual environment.

1. Install all the necassary requirements from [requirements.txt](requrements.txt) using in the cli:

    *pip3 install -r requirements.txt*

1. Create a`env.py` file for storing the enviromental variables

1. Add environment variable in the format as shown below:

        os.environ.setdefault('SECRET_KEY', '<enviroment-variable-here>')
        os.environ.setdefault('DEVELOPMENT', '1')
        os.environ.setdefault('ALLOWED_HOSTS', '<enviroment-variable-here>')
        os.environ.setdefault('STRIPE_PUBLIC_KEY', '<enviroment-variable-here>')
        os.environ.setdefault('STRIPE_SECRET_KEY', '<enviroment-variable-here>')
        os.environ.setdefault('STRIPE_WH_SECRET_CH', '<enviroment-variable-here>')
        os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<enviroment-variable-here>')
    
    -  To ensure appropriate security measures a `SECRET_KEY` can be randomly generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) or a similar website.

-  `DEVELOPMENT` should be set to `1` and is entered into `settings.py` logic to ensure file is dynamic between local and remote setups
- `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` values are obatined from the [Stripe](https://dashboard.stripe.com/register) website
        <details>
            <summary>How to retreive Stripe API values</summary>
            <ul>
                <li>Once logged in, you will be redirected to the **Overview** page</li>
                <li>Get the API values by clicking on **Get your test API keys**</li>
                <li>Add Publishable key as `STRIPE_PUBLIC_KEY` and Secret key as `STRIPE_SECRET_KEY` environmental variable values</li>
            </ul>
        </details>
- `STRIPE_WH_SECRET` value is obtained from the [Stripe](https://dashboard.stripe.com/register) website in the developers area
        <details>
            <summary>How to retreive Webhooks API value</summary>
            <ul>
                <li>Go to your [stripe dashboard](dashboard.stripe.com) and naviagte to **Developers** > **Webhooks**</li>
                <li>Click **Add endpoint** and enter your site address followed by `/checkout/wh/`</li>
                <li>Click on **recieve all events** and then Add endpoint to finish the setup</li>
                <li>To get the `STRIPE_WH_SECRET` value, click on the added link under Endpoints and copy the Signing secret key in your variable</li>
            </ul>
    </details>

1. Run the application using - *python3 manage.py runserver*

---

## **Credits**

### **Content**

*	My code was influenced by The Data Centric Development Boutique Ado lessons from the [Code Institute](https://courses.codeinstitute.net/login) Full Stack Developer Course.

*   My Wishlist app was influenced by the Code Institute Slack community - Particualrly a conversation between **ckz8780** and **Keis_almuni**

### **Media**

*   All images and large portions of the product descriptions used for the products 'sold' on this site were obtained from [The Sock Drawer](https://sockdrawer.com/)

*   The 'No Image' image was obtained from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:No-image-available.png)

*   The callout image of multiple pairs of socks was obtained from [CodeWoD](http://www.codewod.com/2014/02/real-life-sock-sorting.html)

### **Acknowledgements**

    
*   Thanks to my mentor **Oluwafemi Medale** for styling and formatting advice.

