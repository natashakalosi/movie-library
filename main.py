import matplotlib.pyplot as plt
import pandas as pd

print("--- Movie Library ---")

movie_list = []

while True:
    choice = input("\n1. Add movie | 2. Exit and Plot\nSelection: ")
    
    match choice:
        case '1':
            title = input("Input movie title: ").lower().strip()
            genre = input("Input movie genre: ").lower().strip()
            try:
                rating = float(input("Input movie rating (e.g., 8.5): "))
                movie_list.append({'Title': title, 'Genre': genre, 'Rating': rating})
            except ValueError:
                print("Invalid rating. Please enter a number like 7.5")
                
        case '2':
            print("Exiting and generating analysis...")
            break
            
        case _:
            print("Invalid selection. Please try again.")

# Process data if the list is not empty
df = pd.DataFrame(movie_list)

if not df.empty:
    # Filter and display top-rated movies (Rating >= 9)
    # We use .copy() to avoid SettingWithCopyWarning
    fav = df[df['Rating'] >= 9].copy()
    
    if not fav.empty:
        print("\n Your Favorite Movies (Top Rated):")
        fav['Title'] = fav['Title'].str.title()
        print(fav[['Title', 'Rating']].to_string(index=False))

    # Prepare data for the Pie Chart
    # Capitalize genres for a professional look in the chart
    df['Genre'] = df['Genre'].str.title()
    genre_counts = df['Genre'].value_counts()
    
    # Professional color palette
    colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948']

    # Generate Pie Chart
    plt.figure(figsize=(8, 6))
    plt.pie(genre_counts, labels=genre_counts.index, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Movie Genres Distribution")
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

else:
    print("No data entered to display.")
