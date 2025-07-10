#name:HK sineth
#uow id: w2051894
#date:2023/12/14
from graphics import GraphWin, Rectangle, Point, Text
def get_credits(prompt):
    while True:
        try:
            credits = int(input(prompt))
            return credits
        except ValueError:
            print("Integer required")
                        
#find the validation of credits
def validate_credits(credit):
    if credit not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range.")
        return False
    else:
        return True
    
#find the total
def validate_credits_sum(pass_credits, defer_credits, fail_credits):
    if pass_credits + defer_credits + fail_credits != 120:
        print("Total incorrect.")
        return False
    else:
        return True
    
#conditions of select the category
def get_progress_outcome(pass_credits, defer_credits, fail_credits):

    total_credits = pass_credits + defer_credits + fail_credits
    
    if total_credits != 120:
        return "Total incorrect."

    elif pass_credits == 120:
        return "Progress"
    
    elif pass_credits == 100:
        return "Progress (module trailer)"

    elif fail_credits >= 80:
        return "Exclude"
    
    else:
        return "Do not progress - module retriever"

#select the vertion 
while True:
    vertion=input("are you student?(enter 'sd'),are you staff?(enter 'st'):")
    if vertion in ("sd","st"):
        break
    else:
        print("enter sd or st")

#create the histogram
def display_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    win = GraphWin("Progression Histogram", 430,415)
    win.setBackground("white")

    bar_width = 80
    bar_heights = [progress_count, trailer_count, retriever_count, exclude_count]
    colors = ["green", "yellow", "red", "gray"]
    categories = ["Progress", "Trailer", "Retriever", "Excluded"]

    max_height = max(bar_heights)

    title_label = Text(Point(200, 15), "Histogram Results")
    title_label.setStyle("bold")
    title_label.setSize(16)
    title_label.draw(win)

    display_y = 40

    for i, height in enumerate(bar_heights):
        scaled_height = int((height / max_height) * 280)
        bar = Rectangle(Point(i * bar_width, 280 - scaled_height + display_y), Point((i + 1) * bar_width, 280 + display_y))
        bar.setFill(colors[i])
        bar.draw(win)

        label = Text(Point((i + 0.5) * bar_width, 280 - scaled_height - 10 + display_y), f"{height}")
        label.setSize(10)
        label.draw(win)

    label_y = 330

    for i, category in enumerate(categories):
        category_label = Text(Point((i + 0.5) * bar_width, label_y), f"{category}")
        category_label.setSize(12)
        category_label.draw(win)

    total_label = Text(Point(200, label_y+30), f"{sum(bar_heights)} outcomes in total.")
    total_label.setSize(12)
    total_label.setStyle("bold")
    total_label.draw(win)

    win.getMouse()
    win.close()
#get the credits
def main():
    data_list = []

    while True:
        pass_credits = get_credits("Please enter your credits at pass: ")
        if not validate_credits(pass_credits):
            continue
        defer_credits = get_credits("Please enter your credit at defer: ")
        if not validate_credits(defer_credits):
            continue
        fail_credits = get_credits("Please enter your credits at fail: ")
        if not validate_credits(fail_credits):
            continue

        if not validate_credits_sum(pass_credits, defer_credits, fail_credits):
            print("Invalid credit sum. Please make sure the total is 120.")
            continue

        outcome = get_progress_outcome(pass_credits, defer_credits, fail_credits)
        print(outcome)

        data_list.append((outcome, pass_credits, defer_credits, fail_credits))

        continue_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if continue_input.lower() == 'q':
            break
        while continue_input not in ['y','q']:
            continue_input = input("would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")

    if not vertion == "sd":
        # Display histogram after collecting all data
        progress_count = sum(1 for outcome, _, _, _ in data_list if outcome == "Progress")
        trailer_count = sum(1 for outcome, _, _, _ in data_list if outcome == "Progress (module trailer)")
        retriever_count = sum(1 for outcome, _, _, _ in data_list if outcome == "Do not progress - module retriever")
        exclude_count = sum(1 for outcome, _, _, _ in data_list if outcome == "Exclude")

        print(progress_count,trailer_count, retriever_count,exclude_count)

        display_histogram(progress_count, trailer_count, retriever_count, exclude_count)

        # Part 2 - Display stored data
        print("\nPart 2:")
        for entry in data_list:
            print(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}")

        # Part 3 - Save to a text file
        with open("progression_data.txt", "w") as file:
            for entry in data_list:
                file.write(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}\n")
               
        with open("progression_data.txt", "r") as file:
            print()
            
if __name__ == "__main__":
    main()

