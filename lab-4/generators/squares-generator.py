def squares_generator(N):
    for i in range(N):
        yield i**2

squares_generator(10)