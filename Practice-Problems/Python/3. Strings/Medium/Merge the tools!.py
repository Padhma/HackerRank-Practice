def merge_the_tools(string, k):
    chunk_list = []
    for i in range(0, len(string), k):
        chunk_list.append(string[i:i+k]) 
    for char in chunk_list:
        seen = ''
        for c in char:
            if c not in seen:
                seen += c
        print(seen)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)