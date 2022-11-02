
class Return_print_function_class:

    x = 9  # just like attributes in java

    def how_far_from_5 (num: int) -> [int]:  # def means "define function"
        # self is like this in java (parameter)
        # -> type of function

        return num - 5 if num > 5 \
            else 5 - num

# class ends here.

    # In Python, you can continue a line via '\' .
    # you can also write a return statement like this.


print(Return_print_function_class.x)  # print attribute

print(f"\033[94m{Return_print_function_class.how_far_from_5(Return_print_function_class.x)}\033[0m")  # print in color

# another possibility: print("Hello, {}".format(name))  # output = Hello, John Smith

