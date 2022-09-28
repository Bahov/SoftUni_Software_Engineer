string_input = input().split(' ')

command = input()

temp_list = []
merge_counter = 0
partition_counter = 0
partition_size_counter = 0
temp_string = ''

while True:
    if command == '3:1':
        break

    command_list = command.split(' ')

    if command_list[0] == 'merge':
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(string_input):
            end_index = len(string_input) - 1
        for index in range(len(string_input)):
            if index not in range(start_index + 1, end_index + 1):
                temp_list.append(string_input[index])
            else:
                merge_counter += 1
                temp_list[index - merge_counter] += string_input[index]
    
    elif command_list[0] == 'divide':
        divide_index = int(command_list[1])
        partitions = int(command_list[2])
        partition_size = len(string_input[divide_index]) // partitions
        string_to_split = string_input[divide_index]
        for index in range(len(string_input)):
            if index != divide_index:
                temp_list.append(string_input[index])
            else:
                for symbol_index, symbol in enumerate(string_to_split):
                    partition_size_counter += 1
                    if partition_counter == partitions:
                        temp_list[-1] += string_to_split[symbol_index:]
                        break
                    elif partition_size_counter < partition_size:
                        temp_string += symbol
                    elif partition_size_counter == partition_size:
                        temp_string += symbol
                        temp_list.append(temp_string)
                        partition_size_counter = 0
                        temp_string = ''
                        partition_counter += 1
        
    string_input = [x for x in temp_list]
    
    temp_list.clear()
    merge_counter = 0
    partition_counter = 0
    command = input()

print(' '.join(string_input))
