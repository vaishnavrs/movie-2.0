options=(
        ('Action and Adventure', 'Action & Adventure'),
        ('Horror','Horror'),
        ('Comedy','Comedy'),
        ('Romance','Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Kids','kids'),
        ('Mystery and Thriller','Mystery and thriller')
    )


def get_movie_type():
    type=[]
    for i,j in options:
        if i not in type:
            type.append(i)
    return type
def print_movie_type():
    types=get_movie_type()
    for i in types:
        print(i)

print_movie_type()