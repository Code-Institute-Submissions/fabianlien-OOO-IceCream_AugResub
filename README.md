# OOO Ice Cream - [Live link](https://ooo-icecream.herokuapp.com/nybrogatan23/)

For "Triple Oh!" ice cream is more than just a sweet, nostalgic treat - it is an exploration of taste and texture, served up cold!

Previously, OOO's online pressence has only extended to a single Instagram account, but with the opening of their first permanent location, they are ready for a fully fledged webpage from which users can access information about their delicious flavours and make reservations at the brand new Nybrogatan23.  

<br>  

## Design

### UX Aproach
This projet takes a user experience aproach to its design elements. The governing idea was to be playful enough to instantly get new users intrigued by the brand without being overwhelming. The navigation strives to be intuitive whilst remaining minimal, allowing the user to focus on interacting with visual elements rather than exploring the functionality of the website.

### Design Elements:
* **Layout**  
  The page layout utilizes bootstraps grid functionality in combination with custom css. 
* **Color**  
  As the brand already has a somewhat established social media presence, The color theme for the page follows the palate previously used for digital marketing and posters. The theme offers colors that are pastel-like and playful, whilst providing distinct recognition value.
* **Fonts**  
  The entire website utilizes the Recoleta font also found in the text logotype, which adds nicely to the overall playful feel of the brand. 

### Design Features:
* **Animation**  
  The landing page features a continous background animation, which provides the user with a sense joie de vivre shared by the Triple Oh! Philosophy.
* **Collapsable Navbar**
  All pages feature a customised collapseable bootstrap navbar with a "wavy" burger icon for all screen sizes. The elimination of constantly visible navbar links prevents the user from being distracted from the main content and simultaneously adds to the slightly minimalist feel of the website.
* **Carousel**
  - The landing page contains a bootstrap carousel with both manual and time interval rotation. The slides in the carousel provide the user with an immediate overview of key information without cluttering the screen. The carousel works intuitively in its responsiveness.
  - The Nybrogatan 23 Restaurant page also features a carousel but with a much cleaner look and a soft fade animation as opposed to the standard slide rotation. This serves to establish a more "mature" aura than what the home page strives for.
* **Cards**
  - Bootstrap's "Card" elements are featured heavily in several page of the site as they provide an easy and spacious way to display smaller snippets of text to the user.

<br>

## Admin Features
The website makes use of Django's built-in Admin view to provide several features:
* Account management:
  This includes CRUD functionality surrounding both user and admin accounts.
* Content management:
  Utilizing custom models the admin pages give administrators access to a simple CMS where page content can be update and new media content can be uploaded and displayed.
* Reservations:
  Through a custom model in the booking app, site administrators can filter through and confirm bookings with ease.

<br>

## User Features
* User Registration:
  In order to gain access to select backend CRUD functionality, a user can register to the website. Users are prompted to sign in/sign up where needed. This feature takes advantage of AllAuths built in models and templates.
* Sign in/Sign out:
  A user can easily sign in/out from anywhere on the website, with the current status being reflected to the user at the top of each page.
* Reservation form:
  Registered users can utilize a custom reservation model form in order to register a reservation request to the admin pages.
* User profile:
  Users that have logged in gain access to a profile page through the navbar where their personal bookings are display and the user has the option to add/update a message to the restaurant as well as delete bookings from the database.
* External links:
  The site contains an external link to a downloadable PDF menu for Nybrogatan23, and a link to OOO's instagram account. Both open in new tabs.
* Google Maps:
  The Nybrogatan restaurant page also includes an embedded google map through the Maps Javascript API. The map uses has a custom marker for the restaurant so that the user quickly identifies the location of the restaurant, and custom styling in order to blend in with the rest of the page.

<br>

## Future Features to include
### Availability Check
The most logical feature to include next would be the ability for an authenticated user to only be able to send a reservation request for a table if it is available. This would require creating a new database model for availability which relates to both the user and the reservation model, and custom a lot of custom logic to be able to identify availability parameters (time-slot duration, amount of tables, opening hours, group size). This was initially decided to not be a part of the project as it did not fit into the timeframe.

### Detail View for flavours
A neat social feature to include would be to allow the user to click on a ice cream flavour to get more details about the icecream and, if signed in, also post comments about the specified flavour. This was not included in the scope of the project because it is not part of the required business logic at this point.

### Ordering And Logistics System
The biggest potential feature to include would be the functionality required for a customer to order Ice cream for delivery. This would require a large expansion of several existing features as well as implenting new database models to manage the logistics.

<br>

## Custom Models
The website makes use of several custom database models to provide the neccessary functionality:
* The "Reservation" model is utilized by both the Admin CMS as well as well as user generated form input for creating and managing reservations.
* The Admin panel has access to severeal content management object models that utilize either Djangos standard database model, or "Singleton" a library that provides a model allowing only one instance to be created:
  - The "About" model allows administrators to change the content of the "About" slide.
  - The "Flavour" model provides administrators with CRUD functionality for the "Flavours" slide.
  - The "Contact" model allows administrators to store employee contact information and display it on the webpage.
  - The "Nybro23Image" model allows administrators to upload a single image file in *.jpg* or *.png* format to be displayed on the home page.
  - The "Nybro23Text" model provides CRUD funtionality through a WYSIWYG editor that displays it's content on the restaurant page.

### Custom Views
The website contains custom views for all pages except for the default views provided through Django Admin an Allauth.
 
<br>

## Development

### Agile Tools

#### Kanban Board:
The Project utilized Githubs Kanban board via the "projects" tab. The board was used to track the current progress of the project user stories.

#### User Stories:
Outlined below are the user stories for the project. Due to a very limited project timeline the work was not devided into distinct increments, but still followed an iterative stratagy through user story implementation:

* Admin Content Management System:
  - As a site Admin, I can upload a new pdf file, replacing the old one so that the site users can download the latest menu from the webpage.
  - As a site Admin, I can login to an admin page so that I can easily update the content on a selected webpage.
  - As a site Admin, I can use a toggle function so that I choose which ice cream flavors to display to the user.
  - As a site Admin, I can type and style text content into a field so that the text content on a the location page is updated automatically.

* Reservations:
  - As a site user, I can book a table so that I can visit the restaurant with a garuanteed seat.
  - As a site user, I can select how many people i want to book a table for so that i can visit the restaurant with a group.
  - As a site Admin, I can make alterations to specific bookings or remove them so that I can accomodate a customers specific request.
  - As a Site Admin, I can get the personal details of a specific booking so that I can contact the booker if need be.
  - As a site Admin, I can view all my bookings for a specific day so that I can prepare the restaurant.
  - As a registered user, I can view my profile page so that I can see my account details and my reservation history.
  - As a registered user, I can view my reservation status so that I know if my reservation is confirmed or not.

* Front-End Interaction:
  - As a site user, I can view a playful animation when visiting the site so that I get intrigued by the OOO brand.
  - As a site user, I can navigate to a separate page so that I can view information about the restaurant location and interior in an enticing way.
  - As a site user, I can register an account so that information about my reservations is stored and i can recieve emails from the restaurant.
  - As a site user, I can easily change the content on the main page so that I quickly find the information im looking for.
  - As a site user, I can click a link so that I can download a restaurant menu.
  - As a site user, I can interact with a google map so that I know how to find the restaurant.

![Image of the github Kanban board with an overview of the user stories](screenshots/kanban-ss.jpg)

<br>

### UI Layout
A wireframe was made to get an overview of what the landing page would look like (subsequent pages were designed in the GitPod IDE during development):
![Image of the wireframe for the landing page](screenshots/wireframe-index-ss.jpg)

<br>

### Data Model
A Data modelling tool was used to create an overview of the necessary database models to ensure project functionality:
![Image of the data model map](screenshots/db-model-ss.jpg)

<br>

### Utilized Technologies

* **Coding Languages:**
  * Python
  * HTML
  * CSS
  * JavaScript  
*  **Django Framework:**
   * Colorfield - Color selector widget.
   * AllAuth - Authentication package.
   * SoloApp - Custom "singleton" model.
   * Summernote - WYSIWYG widget.
   * Crispy Forms - Form layout overhaul.
*  **Hosting Platforms:**
   * Heroku - Web application host.
   * Cloudinary - Static and media file host.
*  Coding Environment - **GitPod**
*  Version Control System - **GitHub**
*  Database Technology - **PostgreSQL**

<br>

##Testing