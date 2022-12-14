from instagrapi import Client

username = LOGIN
password = password

with open('cred.txt','r') as f:
    username, password  = f.read().splitlines()

client  = Client()
client.login(username,password)

hashtag = "uzb"
medias  = client.hashtag_medias_recent(hashtag,20)
for i, media in enumerate(medias):
    # client.media_like(media.id)
    # print(f"Like Bosildi ❤️| Post Nomeri {i+1} # - {hashtag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"FOLLOWED to {media.user.username}")
