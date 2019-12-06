import string
import my_module.chatbot_functions as cf



class MyComputer():
    
    #Initialize components
    def __init__(self,*argv):
        self.user_computer_list=argv[0]
        self.total_list=argv[1]

    def return_price(self):

        #find corresponding dictionary and store them inside a list
        output_list=[]
        for attribute in self.user_computer_list:
            result=cf.find_and_return_dict(self.total_list,'model',attribute)
            output_list.append(result)

        #return and sum all the prices together
        sum_price=0
        for dict in output_list:
            sum_price+=int(dict['price'])

        return sum_price
