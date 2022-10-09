#  partition1 = set()  # Fido, Rufus
#   partition2 = set()  # James, Alfie, T-Bone

#    if len(dislikes) == 0:
#         return False

#     first_dog = list(dislikes.keys())[0]  # Fido
#     queue = deque([first_dog])  # , Alfie
#     visited = []  # Fido, Rufus, James, Alfie

#     while queue:
#         current_dog = queue.popleft()  # James
#         if current_dog not in visited:
#             partition1.add(current_dog)
#             visited.append(current_dog)
#         else:
#             # cooper does not want to be with spot, but when you check his part mates, spot is there!
#             if current_dog in partition1:
#                 for dog in dislikes[current_dog]:
#                     if dog in partition1:
#                         return False
#             elif current_dog in partition2:
#                 for dog in dislikes[current_dog]:
#                     if dog in partition2:
#                         return False

#         if dislikes[current_dog]:
#             for disliked_dog in dislikes[current_dog]:
#                 # if disliked_dog in partition1:
#                 #     return False
#                 if disliked_dog not in visited:
#                     partition2.add(disliked_dog)
#                     queue.append(disliked_dog)
#                     visited.append(disliked_dog)
#         else:
#             for dog in dislikes:
#                 if dog not in visited:
#                     queue.append(dog)
#                     break

#     return True
