import git

print("Test 1 2 3 ")

remoteurl="git@github.com:ekim197711/gitpythondemo.git"
localfolder="/tmp/gitpythondemo"

myrepo = git.Repo.clone_from(remoteurl, localfolder)
myrepo.git.checkout("mikesbranch")