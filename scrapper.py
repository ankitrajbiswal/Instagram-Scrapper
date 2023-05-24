import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account (optional)
loader.login("bea_brand_official", "Beabrand@333")

# Load your own profile
profile = instaloader.Profile.from_username(loader.context, "bea_brand_official")

# Iterate through your following
for followee in profile.get_followees():
    username = followee.username
    bio = followee.biography
    print("Username:", username)
    print("Bio:", bio)
    print()

# Logout from the Instagram account (if logged in)
loader.logout()
