import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account (optional)
loader.login("username", "password")

# Load your own profile
profile = instaloader.Profile.from_username(loader.context, "username")

# Iterate through your following
for followee in profile.get_followees():
    username = followee.username
    bio = followee.biography
    print("Username:", username)
    print("Bio:", bio)
    print()

# Logout from the Instagram account (if logged in)
loader.logout()
