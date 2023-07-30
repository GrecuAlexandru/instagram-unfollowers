import instaloader

L = instaloader.Instaloader()

USER = "alexandrugrecu22"
PROFILE = USER

# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

# Get the set of profiles you follow (followees)
followees = set(profile.get_followees())

# Get the set of profiles that follow you (followers)
followers = set(profile.get_followers())

# Find the profiles that don't follow you back
non_followers = followees - followers

# Print the usernames of profiles that don't follow you back
print("Profiles that don't follow you back:")
for non_follower in non_followers:
    print(non_follower.username)