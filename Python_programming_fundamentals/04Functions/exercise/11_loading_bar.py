progress = int(input())

def progress_func(number):
    complete_bars = number // 10
    remaining_bars = 10 - complete_bars
    if complete_bars < 10:
        print(f"{number}% [{'%'*complete_bars}{'.'*remaining_bars}]")
        print('Still loading...')
    else:
        print('100% Complete!')
        print(f"[{'%'*complete_bars}]")

progress_func(progress)