from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('/home/user/Documents/bitbucket-repos/online_git_clones_prep/image-similarity/pixlredited.jpg')) 
hash1 = imagehash.average_hash(Image.open('/home/user/Documents/bitbucket-repos/online_git_clones_prep/image-similarity/Selection_060.png')) 
cutoff = 5

print(hash0)
print(hash1)
print(hash0 - hash1)
if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')
