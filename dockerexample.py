import docker
print("Beginning of program")
client = docker.from_env()
client.containers.run("nginx",  detach=True)
client.images.pull('ubuntu')
myimages = client.images.list()
for img in myimages:
    print("This is an image on my machine: {}".format(str(img)))

print("End of program")
