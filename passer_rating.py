def passer_rating(completions, attempts, yards, touchdowns, interceptions):
    if completions < 0 or completions > attempts:
        return 'Error: Completions must be between 0 and attempts'
    if touchdowns < 0 or touchdowns > attempts:
        return 'Error: Touchdowns must be between 0 and attempts'
    if interceptions < 0 or interceptions > attempts:
        return 'Error: Interceptions must be between 0 and attempts'
    if completions == 0 and yards !=0:
        return 'Error: Yards must be zero if there are no completions'
    if attempts == 0:
        return 'N/A'

    a = ((completions/attempts)-0.3)*5
    b = ((yards/attempts)-3)*0.25
    c = (touchdowns/attempts)*20
    d = 2.375 - ((interceptions/attempts)*25)
    
    a = max(0, min(a, 2.375))
    b = max(0, min(b, 2.375))
    c = max(0, min(c, 2.375))
    d = max(0, min(d, 2.375))

    rating = ((a+b+c+d)/6)*100
    return round(rating, 1)

if __name__ == "__main__":
    print("NFL Passer Rating Calculator\n")

    try:
        completions = int(input("Enter completions: "))
        attempts = int(input("Enter pass attempts: "))
        yards = int(input("Enter passing yards: "))
        touchdowns = int(input("Enter touchdowns: "))
        interceptions = int(input("Enter interceptions: "))

        rating = passer_rating(completions, attempts, yards, touchdowns, interceptions)
        print(f"\nPasser rating: {rating}")

    except ValueError:
        print("Please enter only whole numbers for all inputs.")