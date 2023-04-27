import pyfiglet
def create_output_files(input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        numbers = f.read().split()

    # Convert numbers to integers
    numbers = [int(n) for n in numbers]

    # Separate the even and odd numbers
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 == 1]
    
    # Calculate the squares of even numbers and cubes of odd numbers
    even_squares = [n**2 for n in even_numbers]
    odd_cubes = [n**3 for n in odd_numbers]
   
    # Create output files
    with open('double.txt', 'w') as f:
        for square in even_squares:
            f.write(str(square) + '\n')


    with open('triple.txt', 'w') as f:
        for cube in odd_cubes:
            f.write(str(cube) + '\n')

    # Print success message
    ascii_banner = pyfiglet.figlet_format("Files created!")
    print(ascii_banner)
   
    create_output_files('integers.txt')





