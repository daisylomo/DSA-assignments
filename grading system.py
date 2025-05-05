from typing import Final

#type annotation
names: list = ["John","Doe"]
name: str = 'John Doe'

def greet(name: str): #name is the argument
    # print(name)
    return f"Welcome, {name.title()}"

print(f"Welcome, {name}")
    #
    # if age < 20:
    #     print("adult")
    # elif age > 50:
    #     print("adult")
    # else:
    #     print("underage")
    #
    # return None

for i in 'John Doe':
    print(i)

#arguments are pointers to the actual parameters while parameters are the actual values that are passed

greet("John") #john is the parameter

def add(x: int, y: int) -> int:
    return  x + y

def area_circle(radius: float) -> float: # -> is used to specify the return type
    PI: Final = 3.14
    return PI * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))

    scores: list[int] = [] #initializing an empty list

    for i in range(3):
        while True: #while len(scores) < 3
            try:
                score = int(input(f"Enter score for subject {i+1}: ")) #{len(scores) + 1}
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("The score must be between 0 and 100")

            except ValueError:
                print("Please enter a valid number")

        average_score: float = compute_average(scores)
        is_pass: bool = has_passed(average_score)

        print("\n ----Report Card----")
        print(f"Name     : {name}")
        print(f"Scores   : {scores}")
        print(f"Average  : {average_score:.2f}")
        print(f"Status   : {'Pass' if has_passed else 'Fail'}")

        assignments_done: int = 5
        pts: float = 2.5
        total_score: float = average_score + pts

        print(f"Bonus Points: + {pts} for {assignments_done} assignments")
        print(f"Final Score: {total_score:.2f}")

if __name__ == "__main__":
    students_performance()