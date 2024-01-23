def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name':'Antony Jude John',
        'student_id': 10326739,
        'pizza_toppings':['BBQ Chicken','pineapple and ham','peperoni'],
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
    add_pizza_toppings(about_me, toppings)
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f'My name is {about_me['full_name']},but you can call me Lord {about_me['full_name'].split()[0]}.')
    print(f'My student ID is {about_me['student_id']}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
toppings ={ 
        ('Deluze','supreme')
        }
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].append(toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()