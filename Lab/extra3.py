# import time
#
# user_start = int(input())
# counter = user_start
#
# tic = time.perf_counter()
#
# while 1:
#     toc = time.perf_counter()
#     if toc - tic > 1:
#         counter -= 1
#         print(counter)
#         if counter <= 0:
#             print("End")
#             break
#         tic = toc