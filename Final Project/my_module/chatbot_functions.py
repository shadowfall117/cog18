import string


#define function

#convert string into lower case
def string_convert(input_string):
    """
       Parameter
       ---------
       input_string:string

       Returns
       -------
       answer:string
       The same sentence in lower case
    """
    string=input_string.lower()

    return string

#Use a join method to concatenate two strings together
def string_concatenator(string1,string2,separator):
    """
       Parameter
       ---------
       string1:string
       string2:string
       seperator:symbol

       Returns
       -------
       answer:string
       concatenate two strings together and insert separator in middle
    """
    string_list=[string1,string2]
    output=separator.join(string_list)

    return output

# start chat
def start_chat():
    """
       Parameter
       ---------
       None

       Returns
       -------
       answer:string
       print chat words
    """
    return 'Hello, I am your artifical assitance, and I can help you to assemble a computer through this chat. There are 7 main components:CPU, GPU, Motherborad, Memory, Cooling, Power, or computer case. Type in any components to begin.'


#create dictionaries and put them inside a list
def add_component(input_list,brand,model,price,data):
    """
    Parameter
    ---------
    input_list:list
    brand:string
    model:string
    price:string
    data:string

    Returns
    -------
    answer: store dict inside a list
    This function will take four keys like brand, model, price, and data to create a dictionary. And store these dictionary inside a list.
    """
    dictionary={'brand':brand,'model':model,'price':price,'data':data}
    input_list.append(dictionary)

#By using for loop and if statement, this function will find the dictionary according to a value provided
def find_and_return_dict(input_list,target,target_value):
    """
       Parameter:
       input_list: list
       target:string
       target_value:string

       Returns
       -------
       answer:dictionary
       For the dictionary inside the input list, this function will find dictionary according to target value.
    """
    for dict in input_list:
        if dict[target]==target_value:
            return dict

#Return the model name based on the value I want to find
def return_model_name(input_list,target,target_value,return_key):
    """
    Parameter:
    input_list:list
    target:string
    target_value:string
    return_key:string
    return_key:string1

    Returns
    -------
    answer:string
    I input a value, and this function will find this dictionary, and return another within this dictionary
    """
    output=[]
    for dict in input_list:
        if dict[target]==target_value:
            output.append(dict[return_key])

    return output

#check whether user's input is in the dictionary
def check_input(input_list,user_input):
    """
    Parameter
    input_list:list
    user_input:string

    Returns
    -------
    answer:boolean
    check if users' input inside the input list
    """
    for dict in input_list:
        if dict.get('model')==user_input:
            return True

    return False

#print all commands
def print_instructions():
    return 'Here is a list of commands that you can use:\n "instructions":print all commands that you can use \n "cpu","gpu","motherboard","cooling","memory","power","computer case":enter in a section\n "start shopping":begin to shop\n "show shopping list":show the item you purchased\n "finish shopping":type this when you finish shopping(***important***)\n "info":get detailed info of item such as price or frequencies\n "total price":return the total price in the list\n "exit":exit the chat'
