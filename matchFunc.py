from ui import login

class UserMatcher:
    currect_user = login.phone_number_input
    def __init__(self, current_user, database):
        """
        Initialize the UserMatcher class.

        :param current_user: A dictionary containing the current user's data (interests, hobbies, lifestyle, etc.)
        :param database: A list of dictionaries representing the database of all users
        """
        self.current_user = current_user
        self.database = database

    def match_users(self):
        """
        Find matching users based on the current user's interests, hobbies, and lifestyle.

        :return: A list of users from the database who match the current user on at least one aspect in interests, hobbies, or lifestyle,
                 or a message if no matches are found.
        """
        matched_users = []

        current_user_interests = set(self.current_user.get("interests", []))
        current_user_hobbies = set(self.current_user.get("hobbies", []))
        current_user_lifestyle = set(self.current_user.get("lifestyle", []))

        for user in self.database:
            if user == self.current_user:
                continue  # Skip the current user

            user_interests = set(user.get("interests", []))
            user_hobbies = set(user.get("hobbies", []))
            user_lifestyle = set(user.get("lifestyle", []))

            # Check if there's at least one match in interests, hobbies, or lifestyle
            interests_match = current_user_interests.intersection(user_interests)
            hobbies_match = current_user_hobbies.intersection(user_hobbies)
            lifestyle_match = current_user_lifestyle.intersection(user_lifestyle)

            if interests_match or hobbies_match or lifestyle_match:
                matched_users.append(user)

        if matched_users:
            return matched_users
        else:
            return "No current matches found."
