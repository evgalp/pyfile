
x = [num for num in range(50)]

# print(x)

# def chunk_arr(arr, chunk_size):
#     chunks = []
#     chunk_counter = 0
#     for elem in arr:
#         elem_counter = 0
#         while elem_counter <= chunk_size:
#             chunks[chunk_counter].append[elem_counter]
#             elem_counter += 1
#
# print(chunk_arr(x, 10))


# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     chunks = []
#     for i in range(0, len(l), n):
#         chunks.append(l[i:i + n])
#
# list(chunks(x, 2))

def chunk(input, size):
    return map(None, *([iter(input)] * size))

for i in chunk(x, 10):
    print(i)
