my_fav_items = {1,2,5,9}
my_fav_items.update((6,8))
my_fav_items.remove(9)
friend_fav_numbers = {3,7}
our_fav_numbers = set.union(my_fav_items,friend_fav_numbers)
print(our_fav_numbers)