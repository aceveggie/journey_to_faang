import math
new_list = [1, 2, 3, 4, 5, 6, 7, 8]
length_exceeded = False
tracker = 1
last_queue_index = 0

while True:
    for i in range(last_queue_index, tracker):
        if i == len(new_list):
            length_exceeded = True
            break
        else:
            print(new_list[i], end=',')
    if length_exceeded:
        break
    else:
        last_queue_index=tracker
        tracker=tracker*2+1
        print("")

# while True:
#     for i in range(last_queue_index, tracker):
#         print(new_list[i])
#     if last_queue_index == 0:
#         last_queue_index = last_queue_index + 1
#     else:
#         last_queue_index = last_queue_index*2
    

# while i<len(new_list):
#     for j in range(i, tracker):
#         if j < len(new_list):
#             print(new_list[j], end=', ')
#         else:
#             queue_len_exceeded = True
#             break
#     if queue_len_exceeded:
#         break
#     else:
#         print("")
#         tracker = tracker*2+1
#     if i==0:
#         i = i+1
#     else:
#         i=i*2

# i=2

# while i<len(new_list):
#     for j in range(math.floor(i/2), i):
#         print(new_list[j-1], end=', ')
#     print("")

#     i = i*2