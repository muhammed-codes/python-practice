# Mini User Profile Manager

In this project, you will build a User Profile Manager that allows users to manage basic user profiles containing usernames and ages. You will implement functions to add, update, delete, and view users.

## Objective

Fulfill all the requirements below and make sure your program works correctly for all specified cases.

## Requirements

1. You should define a function named `add_user` with two parameters representing:
   - A dictionary of users
   - A tuple containing a username and age

2. `add_user` function should:
   - Convert the username to lowercase.
   - If the username already exists, return:
     `User '[username]' already exists!`
   - If the username does not exist, add the username and age to the given dictionary and return:
     `User '[username]' added successfully!`
   - The username in returned messages should be lowercase.

3. You should define a function named `update_user` with two parameters representing:
   - A dictionary of users
   - A tuple containing a username and a new age

4. `update_user` function should:
   - Convert the username to lowercase.
   - If the username exists, update its age in the given dictionary and return:
     `User '[username]' updated to age [age] successfully!`
   - If the username does not exist, return:
     `User '[username]' does not exist!`
   - The username in returned messages should be lowercase.

5. You should define a function named `delete_user` with two parameters representing:
   - A dictionary of users
   - A username

6. `delete_user` function should:
   - Convert the username passed to lowercase.
   - If the username exists, remove the user from the given dictionary and return:
     `User '[username]' deleted successfully!`
   - If the username does not exist, return:
     `User not found!`
   - The username in returned messages should be lowercase.

7. You should define a function named `view_users` with one parameter representing a dictionary of users.

8. `view_users` function should:
   - Return `No users available.` if the given dictionary of users is empty.
   - If the dictionary contains users, return a string displaying all users.
   - The returned string should start with:
     `Current Users:`
   - Each user should appear on a new line.
   - Each username should have its first letter capitalized.
   - The format should be:
   
   ```text
   Current Users:
   Username: age
   Username: age
   Username: age
````

9. For testing the code, you should create a dictionary named `test_users` to store user profiles.

10. You should test all of the following cases:

    * Adding a new user
    * Adding a user that already exists
    * Updating an existing user
    * Updating a user that does not exist
    * Deleting an existing user
    * Deleting a user that does not exist
    * Viewing users when the dictionary is empty
    * Viewing users when the dictionary contains multiple users
