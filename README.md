Project Name: 
Blog Website

Description:
The Simple Django Blog is a basic web application designed to facilitate blogging and content creation. It leverages the Django framework, a powerful Python web framework, to provide an intuitive and user-friendly interface for managing and publishing blog posts. This project aims to empower users to share their thoughts, ideas, and expertise with others through the creation of engaging blog content.
 
Database Structure:
The project's database includes the following four tables:
1. User Table:
- ID: Unique identifier for each user.
- Username: User's chosen username.
- Email: User's email address.
- Password: Securely hashed password.

2. Post Table:
- ID: Unique identifier for each blog post.
- Title: Title of the blog post.
- Content: The main textual content of the blog post.
- Category: Category or topic to which the blog post belongs.
- Date Published: Date and time when the blog post was published.

3. Comment Table:
- ID: Unique identifier for each comment.
- Post ID: Foreign key referencing the blog post to which the comment belongs.
- User ID: Foreign key referencing the user who posted the comment.
- Content: The textual content of the comment.
- Date Posted: Date and time when the comment was posted.

4. Category Table:
- ID: Unique identifier for each category.
- Name: Name or title of the category.
 
Sample Data:
Here are ten sample entries for each table to illustrate the data structure:
User Table:
1. Username: johnsmith, Email: johnsmith@example.com
2. Username: emilyjones, Email: emilyjones@example.com
3. Username: davidwilson, Email: davidwilson@example.com
4. Username: sarahbrown, Email: sarahbrown@example.com
5. Username: michaelscott, Email: michaelscott@example.com
6. Username: lisajohnson, Email: lisajohnson@example.com
7. Username: alexturner, Email: alexturner@example.com
8. Username: jessicabaker, Email: jessicabaker@example.com
9. Username: matthewwright, Email: matthewwright@example.com
10. Username: oliviawalker, Email: oliviawalker@example.com
Post Table:
1. Title: Introduction to Django, Content: Lorem ipsum dolor sit amet, Category: Programming, Date Published: 2023-01-01
2. Title: Tips for Effective Time Management, Content: Lorem ipsum dolor sit amet, Category: Productivity, Date Published: 2023-01-05
3. Title: Exploring the Wonders of Nature, Content: Lorem ipsum dolor sit amet, Category: Travel, Date Published: 2023-01-10
4. Title: The Art of Photography, Content: Lorem ipsum dolor sit amet, Category: Art, Date Published: 2023-01-15
5. Title: Understanding Machine Learning Algorithms, Content: Lorem ipsum dolor sit amet, Category: Technology, Date Published: 2023-01-20
6. Title: Healthy Eating Habits for a Balanced Lifestyle, Content: Lorem ipsum dolor sit amet, Category: Health, Date Published: 2023-01-25
7. Title: Exploring the World of Literature, Content: Lorem ipsum dolor sit amet, Category: Books, Date Published: 2023-02-01
8. Title: Mastering the Basics of Graphic Design, Content: Lorem ipsum dolor sit amet, Category: Design, Date Published: 2023-02-05
9. Title: The Benefits of Yoga and Meditation, Content: Lorem ipsum dolor sit amet, Category: Wellness, Date Published: 2023-02-10
10. Title: The Power of Positive Thinking, Content: Lorem ipsum dolor sitamet, Category: Self-Improvement, Date Published: 2023-02-15
Comment Table:
1. Post ID: 1, User ID: 2, Content: Great introduction to Django!
2. Post ID: 1, User ID: 5, Content: Very informative article.
3. Post ID: 2, User ID: 3, Content: These tips are really helpful.
4. Post ID: 3, User ID: 7, Content: I love traveling and exploring nature!
5. Post ID: 4, User ID: 4, Content: Beautifully written article about photography.
6. Post ID: 6, User ID: 8, Content: Healthy eating is so important for overall well-being.
7. Post ID: 7, User ID: 9, Content: I enjoy reading different genres of books.
8. Post ID: 8, User ID: 10, Content: Graphic design is such a creative field.
9. Post ID: 9, User ID: 6, Content: Yoga and meditation have changed my life.
10. Post ID: 10, User ID: 1, Content: Positive thinking can make a huge difference in one's life.

Category Table:
1. Name: Programming
2. Name: Productivity
3. Name: Travel
4. Name: Art
5. Name: Technology
6. Name: Health
7. Name: Books
8. Name: Design
9. Name: Wellness
10. Name: Self-Improvement 
Task To Do:
1.	Create a new project named "BlogWebsite" in Django.
2.	Install Django and configure all necessary settings for the project.
3.	Create a new Django app named "blog" to handle blog-related functionality.
4.	Update the project's settings.py file to include the "blog" app in the INSTALLED_APPS list.
5.	Update the project's urls.py file to include the necessary URL patterns for the "blog" app.
6.	Create the required tables in the database based on the defined models for the blog app.
7.	Set up and configure the admin panel for easy management of the blog application.
8.	Insert sample data into the tables, including entries for users, blog posts, comments, and categories.
9.	Create 7 HTML files with the following names and functionalities:
○	main.html: Represents the main webpage and includes links to all other web pages.
○	master.html: Includes the common elements shared by all web pages, such as the header and footer.
○	users.html: Displays a list of all users, including their usernames and emails.
○	blogs.html: Displays a list of all blog titles.
○	comments.html: Displays all comments and the corresponding blog ID.
○	categories.html: Displays all category names.
○	blogdetails.html: Displays detailed information about a specific blog post when the user clicks on the blog title in the blogs.html page.
10.	Upload the completed project to your GitHub account for version control and easy sharing.

