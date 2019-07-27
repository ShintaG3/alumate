# Final Project
## Porpuse of the web application
This webapp helps students who plan or study abroad, by providing a social net working platform to exchange information.
Users can register profiles and university to go and share information with their mates and alumumis.

# Main features
## Ajax search field for University
In the form to register my university, name of university(only UK university currently) and images apears automaticall when user type some words, taking advantage of jQuery.
The json file which is refered is created by web-scraping of the UK university directory by taking advantages of beautiful soup.
## Number of the students classified by enrolement type is apeard
Based on the year of study that a user register, the user is classified as applicants, current students or alumni.
Those numbers can be seen at the University page.
## Users picture in the carousel
Users pictures are shown in the carousel format; there are 3 carousels which are based on the enrolement type.
##Topics which are created by users in the swipe card format
Topics and user picture who post the topic are shown in nice card format. When a user click "more button" in the card, the page transforms to actual topic board.
## Information exchange board
The feature is imported from other github repository: https://github.com/sibtc/django-beginners-guide.git and amended to suit the pupose.
Users can creat boards, topics and post their opinion about topics. They can also reply to certain posts.
Users picture if registed or fancy identicon generated via gravatar apear with the posts.
## Authentication
User can signup and login. Most of the pages require user login.
