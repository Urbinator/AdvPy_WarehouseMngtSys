## WarehouseMngtSys_20220615.py
 
# MIT License
# 
# Copyright (c) 2022 Simon Urban
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import argparse

class Product:
    '''Base class of generic product type'''
    def __init__(self,current_amount: int = 0) -> None:
        '''Initialization function
            current_amount: it's an int
            return: None
        '''
        self.current_amount = current_amount

class Pineapples(Product):
    '''Inheritance class to define Pineapples as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Pineapples: it's an int
            return: None
        '''
        super().__init__()

class Oranges(Product):
    '''Inheritance class to define Oranges as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Oranges: it's an int
            return: None
        '''
        super().__init__()

class Watermelons(Product) :
    '''Inheritance class to define Watermelons as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Watermelons: it's an int
            return: None
        '''
        super().__init__()

class Warehouse:
    '''Main warehouse class with the warehouse functionalities
    Attributes
    ----------
    maximum_capacity: int
        The maximum capacity of the Warehouse
    stock_type: object
        The type of stock to operate on
    quantity: int
        The amount of units to make an operation with
    requested_quantity: int
        The amount of units that is checked for retrival availablitiy
    
    Methods
    -------
    check_spare_capacity()
        returns the difference between max warehouse capacity and used warehouse capacity
    add_stock(stock_type, quantity)
        adds stock quantity to current stock amount
    remove_stock(stock_type, quantity)
        removes stock quantity to current stock amount
    get_stock_amount(stock_type)
        returns current stock amount
    search_stock(stock_type,requested_quantity)
        searches for inputted string in warehouse product list and if found returns product name + current amount.
        If not found it returns an info message + stock product available inside the warehouse
    get_report()
        returns a report with each stock type in store together with their current amount

    '''
    def __init__(self,maximum_capacity: int) -> None:
        '''Initialization function
            maximum_capacity: it's an int
                The maximum capacity of the Warehouse
            pineapples: it's an object
            oranges: it's an object
            watermelons: it's an object
            return: None
        '''
        assert (maximum_capacity > 0), "maximum_capacity has to be greater than 0"
        self.maximum_capacity = maximum_capacity
        self.pineapples = Pineapples()
        self.oranges = Oranges()
        self.watermelons = Watermelons()

    def check_spare_capacity(self):
        return self.maximum_capacity - sum([self.__dict__[i].__dict__['current_amount'] for i in list(self.__dict__.keys())[1:]])

    def add_stock(self,stock_type: object, quantity: int) -> int:  
        '''adds amount to current amount of stock type
            
            returns updated current amount
        '''
        assert (quantity > 0), "Quantity has to be greater than 0"
        assert (self.check_spare_capacity() >= quantity), "Unable to process: Maximum capacity would be exceeded"
        stock_type.current_amount += quantity
        

    def remove_stock(self,stock_type: object, quantity: int) -> int:
        '''removes amount from current amount of stock type
            
            returns updated current amount
        '''
        assert (quantity > 0), "Quantity has to be greater than 0"
        assert (stock_type.current_amount >= quantity), "Unable to process: Requested capacity is not available"
        stock_type.current_amount -= quantity

    def get_stock_amount(self,stock_type: object) -> int:
        '''returns current amount of stock type
        '''
        return stock_type.current_amount

    def search_stock(self, product_searched: str) -> bool:
        '''searches for inputted string in warehouse product list and if found returns product name + current amount.
        If not found it returns an info message + stock product available inside the warehouse
        '''
        product_searched = product_searched.lower()
        input_list = sorted(list(self.__dict__.keys())[1:])
        l_list = len(input_list)-1
        c_index = int(len(input_list)/2.0)
        while c_index != 0 and c_index != l_list:
            if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['current_amount']
            elif product_searched > input_list[c_index]:
                c_index = l_list - int((l_list-c_index)/2)
            else:
                c_index = int((c_index)/2)
        if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['current_amount']
        raise ValueError("Search term not available\nSelect one of the following:\n{}".format(input_list))
        

    def get_report(self) -> list:
        '''returns a report with each stock type in store together with their current amount
        '''
        return [(i, self.__dict__[i].__dict__['current_amount']) for i in list(self.__dict__.keys())[1:]]

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
          description="This program takes 1 argument: Maximum capacity of the warehouse")
    parser.add_argument('-maximum_capacity', '-max_cap',default=100, type=int, required=True, help='Maximum capacity warehouse')
    argument_list = parser.parse_args()
    x = Warehouse(argument_list.maximum_capacity)
    while True:
        try:
            next_step = input("What do you want to do next: add_stock,remove_stock,get_stock_amount,search_stock,get_report,exit ? ")
            match next_step:
                case 'add_stock':
                    which_stock = input('Which stock do you want to add: pineapples,oranges,watermelons ? ')
                    quantity  = int(input('Quantity? '))
                    x.add_stock(getattr(x, which_stock),quantity)
                case 'remove_stock':
                    which_stock = input('Which stock do you want to remove: pineapples,oranges,watermelons ? ')
                    quantity  = int(input('Quantity? '))
                    x.remove_stock(getattr(x, which_stock),quantity)
                case 'get_stock_amount':
                    which_stock = input('For which stock do you want the amount: pineapples,oranges,watermelons ? ')
                    print(x.get_stock_amount(getattr(x, which_stock)))
                case 'search_stock':
                    which_stock = input('Which stock do you want to search: pineapples,oranges,watermelons ? ')
                    print(x.search_stock(which_stock))
                case 'get_report':
                    print(x.get_report())
                case 'exit':
                    break
        except Exception as e:
            print(e)