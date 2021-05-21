# Testing

## Table of Contents

1. [User Stories](#user-stories)

1. [Functionality](#functionality)

1. [Validators](#validators)
    - [HTML5](#html5)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)

1. [Compatibility](#compatibility)

1. [Performance](#performance)

1. [Bugs](#bugs)
    - [Identified Bugs](#identified-bugs)
    - [Existing Bugs](#existing-bugs)

1. [Future Testing](#future-testing)


### **Testing User Stories from the UX Section**

<!-- **First Time Visitor Goals** -->

* *As a First Time Visitor*, I want to know immediately, the purpose of the website.
    *   The name of the website already give a good idea to what the purpose of the website is but the callout section of the home screen has images of multiple socks and a banner just below the navbar advertises free delivery which also suggests that the site is selling goods

* *As a First Time Visitor*, I want to be able to navigate the website simply and easily.
    *   On opening the website the visitor is met with the callout section which has a button connecting to the sign up page and a sticky nav directing the user to relevant pages

* *As a First Time Visitor*, I want to access the site across all devices.
    *	The website is responsive across all devices

* *As a First Time Visitor*, I want to be able to learn more about each product.
    *	The products page leads into individual product detail pages which give a description and large image of each product.

* *As a First Time Visitor*, I want to be able to sign up as a user.
    *   There is a registration link in the navbar and also a button on the callout guiding the user to the registration page.

* *As a First Time Visitor*, I want to be able to checkout without having to first register an account.
    *   Any visitor can make purchases as a guest without having to sign up or sign in.

* *As a First Time Visitor*, I want to receive an email confirmation of my order and be able to register for an account.
    *   Email confirmation is activated whenever a user completes an order
    *   All visitors can sign up for an account needing only to supply their name/username and a valid email address

**Returning Visitor Goals**

* *As a Returning Visitor*, I want to be able to save my delivery info for quicker future checkouts.
    *   If a signed in user makes a purchase their delivery details are automatically saved to the database

* *As a Returning Visitor*, I want to be able to update my delivery and billing information if necessary.
    *	All users can change their delivery and billing information in their profile section as long as they are signed in.

* *As a Returning Visitor*, I want to be able to view my order history
    *	User order history is automatically saved to their profile page and can be accessed at any time as long as they are signed in

* *As a Returning Visitor*, I want a way to save products that I am interested in so I can purchase them at a later date.
    *   Signed in users have access to a wishist section that they can view and update whenever they wish.

**Store Owner Goals**

* *As a Store Owner*, I want to be able to add new products to the website.
    *   Admin users can add products to the website using the admin page

* *As a Store Owner*, I want to be able to update products on the website.
    *   All products can be updated via the admin section.

* *As a Store Owner*, I want to be able to remove products from the website.
    *   *   All products can be deleted from the database via the admin section.

* *As a Store Owner*, Be confident that other users cannot add, remove, or update the products on my website.
    *   The ability to add or remove data within the database is only accessable by admin users

### **Code Validation**

#### *W3 Validators*

*    The HTML was Validated at [W3C Markup Validation Service](https://validator.w3.org/). 

*    The CSS was Validated at [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).

*   The Python was Validated at [pep8online](http://pep8online.com/)

### **Manual Testing**

#### *Google Developer Tools*

   *    The websites design responsiveness has been tested on all device sizes using Google Developer Tools.

#### *Testing On Mobile Devices*
   *    Apple iOS
   *    Google Android 7
   *    Microsoft Windows Phone
   *    Samsung Tizen OS
   *    Nokia Symbian
   *    Mozilla Firefox OS
 
#### *Testing On Browsers*
   *    Google Chrome
   *    Opera
   *    Firefox
   *    Apple Safari
   *    Microsoft Explorer
   *    Microsoft Edge
    
#### *Testing On Operating Systems*
   *    Microsoft Windows
   *    Linux
   *    Apple Mac OS
   *    Google Chrome OS
   *    IBM Warp

### **Functionality Testing**

#### Index page

*   Test all links and buttons on Index page:
    *   All Navbar buttons link to the page expected
    *   All footer links to social media function as expected
    *   Buttons on the "latest products cards direct to expected products pages
    *   The "Register Here" button appears when not signed in and directs user to Sign Up page if user is signed in the button becomes "Get Socking" and directs to the products page as expected

#### Sign Up page

*   Test Sign Up form:
    *   Email Address must have an @ symbol
    *   Email Address confirmation must be the same as the original email input
    *   User cannot create an account without entering a username with less than 4 characters
    *   Password must pass allauth tests for security
        *   If any of these points fail a message appears informing the user what is needed
    *   The link switching the user from login to sign up above the form functions correctly
    *   The home button returns the user to the index page

#### Login page

*   Test Login functionality:
    *   User must enter a correct username already on the system
    *   User must enter the correlating password already on the system
        *   If either of these points are not achieved a "incorrect/username or password" message flashes
    *   The link switching the user from login to sign up above the form functions correctly
    *   The home button returns the user to the index page

#### Profile page

*   Test buttons and links:
    *   Once signed in the success toast tells the user that they are now signed in
    *   The update info updates the users info as expected
    *   The order history links take the user to the order confirmation screen listing the order as expected
    *   The back to profile button on the order confirmtion page returns the user to their profile as expected

#### Wishlist Page

*   Test Wishlist Functionality:
    *   The wishlist tells the user it is empty and directs them back to the product page if there is not any product in the wishlist
    *   The wishlist shows any product that have been placed in the wish list as expected
    *   The view sock button takes the user to the product detail page as expected
    *   The REMOVE button removes the product from the wishlist as expected
    *   The keep socking button returns the user to the products page as expected

<!-- #### Products page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Product Detail page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Shopping Cart page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Checkout page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Checkout Success page -->

<!-- *   Test Edit Sandwich Form:
    *   All original content is placed on the form
    *   Changes can be made to any input as long as the edit complies with the same rule-sets as before
    *   Save changes button saves the new information and directs the customer to the sandwiches page
    *   Cancel edit makes no changes and directs the user to the sandwiches page -->

<!-- #### Logout Buttons -->

<!-- *   Test Logout Button:
    *   Pressing the logout button logs out the user and returns them to the login page -->

<!-- ### Admin Testing -->

<!-- #### Admin Functions -->

<!-- *   Test Admin Functions:
    *   When signed in as admin, the profile page show an Edit Categories button
    *   The Edit Categories button takes the admin to the Edit Categories page

    
<!-- #### *Issues Found* -->

<!-- *   An issue was found with the carousel and callout text being on the same line on different device sizes, the resizing would make the text too large and the carousel too small.
    *   The issue was resolved with some changes to the css in the media queries and by using the bootstrap grid system.

*   Originally the minimum number of letters for the sandwich names was set at 5. It became apparent early on that this was an error as one of the worlds most famous sandwiches is a 3 letter Acronym "BLT"
    *   The minimum letter count on the sandwich name input was changed to 3. -->

---
