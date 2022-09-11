command = input()

sold_tickets_movie = 0
total_sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
utilization = 0
student_tickets_perc = 0
standard_tickets_perc = 0
kid_tickets_perc = 0
while command != "Finish":
    free_seats = int(input())
    ticket = input()
    sold_tickets_movie = 0
    while ticket != "End":
        sold_tickets_movie += 1
        total_sold_tickets += 1
        if ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        elif ticket == "kid":
            kid_tickets += 1
        if sold_tickets_movie == free_seats:
            break
        ticket = input()
    utilization = (sold_tickets_movie / free_seats) * 100
    print(f"{command} - {utilization:.2f}% full.")
    command = input()

student_tickets_perc = (student_tickets / total_sold_tickets) * 100
standard_tickets_perc = (standard_tickets / total_sold_tickets) * 100
kid_tickets_perc = (kid_tickets / total_sold_tickets) * 100

print(f"Total tickets: {total_sold_tickets}")
print(f"{student_tickets_perc:.2f}% student tickets.")
print(f"{standard_tickets_perc:.2f}% standard tickets.")
print(f"{kid_tickets_perc:.2f}% kids tickets.")
