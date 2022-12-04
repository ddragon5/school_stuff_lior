num_books = int(input("number of books: "))

def get_shlefs():
    # calc num of shlefs
    num_of_shelfs = int(num_books) / 15
    return num_of_shelfs

def is_cart_needed(num_of_shelfs):
    # if num_of_shelfs not a whole number
    if type(num_of_shelfs) == float:
        num_of_shelfs = int(num_books) // 15
        num_of_shelf_books = num_of_shelfs * 15
        num_of_cart_books = num_books - num_of_shelf_books
    # if not
    else:
        num_of_cart_books = 0
    return num_of_cart_books, num_of_shelfs

def main():
    num_of_shelfs = get_shlefs()
    num_of_cart_boots, num_of_shelfs = is_cart_needed(num_of_shelfs)
    print("The number of shlefs needed is ", end='')
    print(num_of_shelfs)
    print("The number of books that will be in the cart is ", end='')
    print(num_of_cart_boots)

if __name__ =="__main__":
    main()