import requests
url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Ffree-photos%2Fpic&psig=AOvVaw2JjzCZrp4nilVPo4eV51bl&ust=1740227748825000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMis39rj1IsDFQAAAAAdAAAAABAE'
res=requests.get(url)
content=res.content
print(content)

with open('nature.png', 'wb') as file:
    file.write(content)