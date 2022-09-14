# def repeat_string_func(string, counter):
#     print(string * counter)

func = lambda string, counter: string * counter

string_input = input()
counter_input = int(input())

# repeat_string_func(string_input, counter_input)
print(func(string_input, counter_input))
