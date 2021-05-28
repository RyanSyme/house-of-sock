# **Testing**

## Table of Contents

1. [Testing User Stories](#testing-user-stories)

1. [Code Validation](#Code-Validation)

1. [Validators](#validators)

1. [Manual Testing](#Manual-Testing)

1. [Functionality Testing](#Functionality-Testing)

1. [Issues Found](#Issues-Found)

---
### **Testing User Stories**
---
**First Time Visitor Goals**

* *As a First Time Visitor*, I want to know immediately, the purpose of the website.
    *   The name of the website already gives a good idea to what the purpose of the website is but the callout section of the home screen has images of multiple socks and a banner just below the navbar advertises free delivery which also suggests that the site is selling goods

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
    *   All products can be deleted from the database via the admin section.

* *As a Store Owner*, Be confident that other users cannot add, remove, or update the products on my website.
    *   The ability to add or remove data within the database is only accessable by admin users
---
### **Code Validation**
---
#### *W3 Validators*

*    The HTML was Validated at [W3C Markup Validation Service](https://validator.w3.org/). 

*    The CSS was Validated at [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).

*    The JavaScript was Validated at [JSHint](https://jshint.com/).

*   The Python was Validated at [pep8online](http://pep8online.com/)
---
### **Manual Testing**
---
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
---
### **Functionality Testing**
---
#### *Index Page*

*   Test all links and buttons on Index page:
    *   All Navbar buttons link to the page expected
    *   All footer links to social media function as expected
    *   Buttons on the "latest products cards direct to expected products pages
    *   The "Register Here" button appears when not signed in and directs user to Sign Up page if user is signed in the button becomes "Get Socking" and directs to the products page as expected

#### *Sign Up Page*

*   Test Sign Up form:
    *   Email Address must have an @ symbol
    *   Email Address confirmation must be the same as the original email input
    *   User cannot create an account without entering a username with less than 4 characters
    *   Password must pass Allauth tests for security
        *   If any of these points fail a message appears informing the user what is needed
    *   The link switching the user from login to sign up above the form functions correctly
    *   The home button returns the user to the index page

#### *Login Page*

*   Test Login functionality:
    *   User must enter a correct username already on the system
    *   User must enter the correlating password already on the system
        *   If either of these points are not achieved a "incorrect/username or password" message flashes
    *   The link switching the user from login to sign up above the form functions correctly
    *   The home button returns the user to the index page

#### *Profile Page*

*   Test buttons and links:
    *   Once signed in the success toast tells the user that they are now signed in
    *   The update info updates the user's info as expected
    *   The order history links take the user to the order confirmation screen listing the order as expected
    *   The back to profile button on the order confirmtion page returns the user to their profile as expected

#### *Wishlist Page*

*   Test Wishlist Functionality:
    *   The wishlist tells the user it is empty and directs them back to the product page if there is not any product in the wishlist
    *   The wishlist shows any product that have been placed in the wish list as expected
    *   The view sock button takes the user to the product detail page as expected
    *   The REMOVE button removes the product from the wishlist as expected
    *   The keep socking button returns the user to the products page as expected

#### *Products Page*

*   Test Search bar:
    *   Using the searchbar returns any products that have the chosen word in the title or description of the product
*   Test buttons and links:
    *   Clicking either the anchor in the product image or the view button send the user to the product details page as expected
*   Test Rating:
    *   The average rating of any product that has been given a rating by users is displayed on the product card
    *   Products without a rating display a muted message 'No Rating'
*   Test Pagination:
    *   Paging through the products works as expected
    *   Pagination on categories works as expected - A note on this is in the [Issues Found](#issues-Found) section
    *   The Next and Previous buttons appear or disapear depending on where the user is along the pagination as expect i.e- on page 1 only the next button is showing and at the end only the previous button is showing

#### *Product Detail Page*

*   Test Size and Quantity:
    *   Both Size and Qty dropdowns work as expected adding products to the cart, of different size and/or quantities when the add button is clicked
    *   A success toast appears with each addition to the cart displaying the products in the cart
*   Test buttons and Links:
    *   The Keep Socking button returns the user to the products page as expected
    *   The Category name has a link that sends the user to the products page of that particular category as expected
    *   Add to Cart button adds products to the cart as expected
*   Test Review Area:
    *   If a user is signed in they see a text box where they can add a review
    *   Added reviews appear on the reviews section as expected
    *   Star Ratings are added with each review as expected
    *   An average of the star ratings appears on the detail card when there are 1 or more reviews
    *   If there are no reviews or ratings, A message informing the user of this shows instead of a rating on both the reviews section and the detail card

#### *Shopping Cart Page*

*   Test Quantity Buttons:
    *   Quantities of products in the cart are updated when the update button is clicked as expected
*   Test Buttons and Links:
    *   Items are completely removed from the cart when the remove button is clicked
    *   The Keep Socking button returns the user to the products page as expected
    *   The Checkout button sends the user to the checkout as expected
*   Test FREE_DELIVERY_THRESHOLD:
    *   When a user has products worth €30 or more, the Delivery cost is removed from their total as expected
    *   If the cart contains less than €30 of good, A message informing the user of how much more they need to spend to recieve free delivery shows below the Grand Total

#### *Checkout Page*

*   Test Checkout Form:
    *   If the user has details saved to the database, these are shown on the checkout form as expected
*   Test Buttons and Links:
    *   The adjust cart button returns the user to the shopping cart as expected
    *   The checkout button activates a purchase if a genuine card number is used
    *   Stripe and Allauth protections stop transactions if anything is incorrect as expected

#### *Checkout Success Page*

*   Test Transaction:
    *   When a transaction is activated the user is taken to the Checkout Success Page
    *   A success toast informs the user that the order is a success and that they have been sent an email 
    *   The user receives the email as expected
    *   The page displays the information from the transaction as expected
*   Test Buttons and Links:
    *   The Ready for more socks button sends the user to the products page as expected

#### *Logout Buttons*

*   Test Logout Button:
    *   Pressing the logout button logs out the user and returns them to the Index page
---
### **Admin Testing**
---
#### *Admin Functions*

*   Test Admin Functions:
    *   When signed in as admin, the product_details page shows an Edit button and a delete button
    *   The Edit button takes the admin to the Edit Product page where they can edit:
        *   The category
        *   The SKU
        *   The Name
        *   The Description
        *   Whether the product has different sizes
        *   The Price
        *   The Product Image
    *   The delete button removes the product from the database as expected
*   Test Buttons and Links:
    *   The Select Image Button opens a window allowing the admin to select an image from their hard drive
    *   The Cancel button returns the admin to the products page as expected
    *   The Edit Product button makes any changes that the admin has entered as expected

    
#### **Issues Found**

*   An issue was found with Django Paginator - which was causing the paginator to function incorrectly when viewing the product by *category*. When moving from page 1 to page 2, the paginator would 'lose' the category from the search and show all of the product in the database instead of the expected products from that category.
    *   This problem was finally fix by editing the python code in products.html using code found at [Stackoverflow](https://stackoverflow.com/a/30552369/12782401) by Code Institute mentor **Igor Basuga**

---
