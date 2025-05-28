key_path:dict = {"1":"abc", "2":"def", "3":"ghi"}


def combination(number:int) -> list[int]:
    num_to_string = str(number)
    
    if num_to_string is None:
        return []
    result = []
    
    def depth(start_index:int, path:list) -> None:
        if start_index == len(num_to_string):
            result.append("".join(path))
            return 
        
        for char in key_path[num_to_string[start_index]]:
            path.append(char)
            depth(start_index + 1, path)
            path.pop()
        
    depth(0, [])
    return result 

print(combination(23))