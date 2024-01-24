def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name':'Antony Jude John',
        'student_id': 10326739,
        'pizza_toppings':['BBQ CHICKEN','PINEAPPLE AND HAM','GARLIC'],
        'movie':[
            {
                'title':'The Hobbit: An unexpected journey',
                'genre':'Fantasy'   
            },
            {
                'title':'The Dark Knight',
                'genre':'action'
            }
        ] 
    }

    # TODO: Step 3 - Add another movie to the data structure
    Addition = {
        'title':'The wolf of wall street',
        'genre':'biographical'
    }
    about_me['movie'].append(Addition)
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, toppings)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movie'])
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f'My name is {about_me['full_name']},but you can call me Lord {about_me['full_name'].split()[0]}.')
    print(f'My student ID is {about_me['student_id']}')
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
toppings = ('Mushrooms','peperoni')
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]
    return
# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
          print(f'-{topping}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    all_genres = [movie['genre']for movie in about_me['movie']]
    print('I like to watch ', end='')
    for i in range(len(all_genres) - 1):
            print(f"{all_genres[i]},", end=" ")
    print(f'and {all_genres[-1]} movies.')
    return 
# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    all_titles = [' '.join(word.capitalize() for word in movie['title'].split()) for movie in movie_list]
    print('Some of my favourite movies are', end=' ')
    for i in range(len(all_titles)-1):
         print(f'{all_titles[i]},', end = ' ')
    print(f'and {all_titles[-1]}!')
    return
if __name__ == '__main__':
    main()