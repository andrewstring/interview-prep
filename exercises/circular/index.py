def chunk(arr, size_chunk):
    chunk_counter = 0
    index = 0
    output = []

    while index < len(arr):
        chunk = []
        for chunk_index in range(size_chunk):
            if index < len(arr):
                chunk.append(arr[index])
                index += 1
            else:
                break
        output.append(chunk)

    return output


#print(chunk([1,2,3,4,5], 2))
#print(chunk([1,2,3,4], 2))
#print(chunk([1,2,3,4,5,6,7,8], 3))
#print(chunk([1,2,3,4,5], 4))
#print(chunk([1,2,3,4,5], 10))


def chunk_sublist(arr, size_chunk):
    output = []
    start = 0
    end = start + size_chunk
    while(start < len(arr)):
        if end > len(arr):
            output.append(arr[start:len(arr)])
        else: output.append(arr[start:end])
        start += size_chunk
        end += size_chunk
    return output


print(chunk([1,2,3,4,5], 2))
print(chunk([1,2,3,4], 2))
print(chunk([1,2,3,4,5,6,7,8], 3))
print(chunk([1,2,3,4,5], 4))
print(chunk([1,2,3,4,5], 10))
