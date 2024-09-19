from ui import login

class UserMatcher:
    currect_user = login.phone_number_input
    def __init__(self, current_user, database):

        self.current_user = current_user
        self.database = database

    def match_users(self):

        matched_users = []

        current_user_interests = set(self.current_user.get("interests", []))
        current_user_hobbies = set(self.current_user.get("hobbies", []))
        current_user_lifestyle = set(self.current_user.get("lifestyle", []))

        for user in self.database:
            if user == self.current_user:
                continue

            user_interests = set(user.get("interests", []))
            user_hobbies = set(user.get("hobbies", []))
            user_lifestyle = set(user.get("lifestyle", []))

            interests_match = current_user_interests.intersection(user_interests)
            hobbies_match = current_user_hobbies.intersection(user_hobbies)
            lifestyle_match = current_user_lifestyle.intersection(user_lifestyle)

            if interests_match or hobbies_match or lifestyle_match:
                matched_users.append(user)

        if matched_users:
            return matched_users
        else:
            return "No current matches found."
