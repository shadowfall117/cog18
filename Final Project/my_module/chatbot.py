import string
import my_module.chatbot_functions as cf
from my_module.Computer import MyComputer

#Initialize components as dictionaries and store them inside a list

#CPU
cpu_list=[]
cf.add_component(cpu_list,'Intel','i5-3330','182','3GHz')
cf.add_component(cpu_list,'Intel','i5-4570','192','3.2GHz')
cf.add_component(cpu_list,'Intel','i5-6500','192','3.25GHz')
cf.add_component(cpu_list,'Intel','i5-7500','213','3.4GHz')
cf.add_component(cpu_list,'Intel','i5-8600k','257','3.6GHz')
cf.add_component(cpu_list,'Intel','i5-9600kf','263','3.7GHz')
cf.add_component(cpu_list,'Intel','i7-6800k','434','4GHz')
cf.add_component(cpu_list,'Intel','i7-7700k','339','4.2GHz')
cf.add_component(cpu_list,'Intel','i7-8700k','359','3.7GHz')
cf.add_component(cpu_list,'Intel','i7-9700k','409','4.3GHz')
cf.add_component(cpu_list,'Intel','i9-9900','439','5GHz')
cf.add_component(cpu_list,'Intel','i9-9900k','499','5.2GHz')
cf.add_component(cpu_list,'Ryzen','1600','219','3.2GHz')
cf.add_component(cpu_list,'Ryzen','1700X','399','3.4GHz')
cf.add_component(cpu_list,'Ryzen','2600','199','3.4GHz')
cf.add_component(cpu_list,'Ryzen','2600X','229','3.6GHz')
cf.add_component(cpu_list,'Ryzen','3600','199','3.6GHz')

#GPU
gpu_list=[]
cf.add_component(gpu_list,'Nvidia','gtx1050','120','4GB')
cf.add_component(gpu_list,'Nvidia','gtx1050ti','150','4GB')
cf.add_component(gpu_list,'Nvidia','gtx1060','190','6GB')
cf.add_component(gpu_list,'Nvidia','gtx1060ti','229','6GB')
cf.add_component(gpu_list,'Nvidia','gtx1070','279','8GB')
cf.add_component(gpu_list,'Nvidia','gtx1070ti','329','8GB')
cf.add_component(gpu_list,'Nvidia','gtx1080','529','8GB')
cf.add_component(gpu_list,'Nvidia','gtx1080ti','969','11GB')
cf.add_component(gpu_list,'Nvidia','rtx2060','349','6GB')
cf.add_component(gpu_list,'Nvidia','rtx2070','549','8GB')
cf.add_component(gpu_list,'Nvidia','rtx2080','719','8GB')
cf.add_component(gpu_list,'Nvidia','rtx2080ti','1399','11GB')

#Motherborad
motherboard_list=[]
cf.add_component(motherboard_list,'gigabyte','b450','84','15x12.25x4.22in')
cf.add_component(motherboard_list,'gigabyte','b360','119','11.02x3.54x13.78in')
cf.add_component(motherboard_list,'gigabyte','z390','100','12.79x10.23x2.7in')
cf.add_component(motherboard_list,'gigabyte','h370','134','22.7x14.4x14.8in')
cf.add_component(motherboard_list,'gigabyte,','x570','287','13.58x11.57x3.1in')

#Memory
memory_list=[]
cf.add_component(memory_list,'Kingston','ddr4-8gb','49','3200MHz')
cf.add_component(memory_list,'Kingston','ddr4-16gb','94','3200MHz')
cf.add_component(memory_list,'Kingston','ddr3-4gb','33','1600MHz')
cf.add_component(memory_list,'Kingston','ddr3-8gb','43','1600MHz')
cf.add_component(memory_list,'Kingston','ddr3-16gb','82','1600MHz')

#Cooling
cool_list=[]
cf.add_component(cool_list,'noctua','nh-u12s','69','120mm')
cf.add_component(cool_list,'noctua','nh-u14s','59','140mm')
cf.add_component(cool_list,'noctua','nh-d15s','99','140mm')
cf.add_component(cool_list,'cosair','h115i','136','280mm')
cf.add_component(cool_list,'cosair','h60','59','120mm')
cf.add_component(cool_list,'cosiar','h150i','129','360mm')

#power supply
power_list=[]
cf.add_component(power_list,'cosair','rm750x','119','750Watt')
cf.add_component(power_list,'cosair','rm850x','129','850Watt')
cf.add_component(power_list,'cosair','rm1000x','176','1000Watt')
cf.add_component(power_list,'cosair','rm650x','94','650Watt')
cf.add_component(power_list,'EVGA','650g3','104','650Watt')
cf.add_component(power_list,'EVGA','750g3','129','750Watt')
cf.add_component(power_list,'EVGA','850g3','149','850Watt')
cf.add_component(power_list,'EVGA','1000g3','181','1000Watt')

#computer case
case_list=[]
cf.add_component(case_list,'Fractal Design','meshify c','89','Mid-Tower')
cf.add_component(case_list,'Fractal Design','meshify c-dark','89','Mid-Tower')
cf.add_component(case_list,'Fractal Design','meshify c-mini','94','Mini-Tower')
cf.add_component(case_list,'Antec','p101','128','Mid-Tower')
cf.add_component(case_list,'Antec','df500','100','Mid-Tower')
cf.add_component(case_list,'Cooler Master','mb530p','124','Mid-Tower')
cf.add_component(case_list,'Cooler Master','sl600m','190','Mid-Tower')
cf.add_component(case_list,'In Win','805cg','150','Mid-Tower')
cf.add_component(case_list,'In Win','309','249','Mid-Tower')
cf.add_component(case_list,'Cooler Master','h500','113','Mid-Tower')
cf.add_component(case_list,'Cooler Master','nr400','69','Mid-Tower')
cf.add_component(case_list,'Thermaltake','v200','79','Mid-Tower')
cf.add_component(case_list,'Thermaltake','20gt','235','Mid-Tower')


#combine lists together
total_list=cpu_list+gpu_list+motherboard_list+cool_list+power_list+memory_list+case_list


def have_chat():
    """ main function """

    #start chat
    print(cf.start_chat())

    #some varaiables
    start_shopping=False
    check_info=False
    chat=True

    #Initialize a empty list that will store user's shopping list
    user_computer_list=[]

    while chat:



        #User input and convert it to lower case
        user_input=cf.string_convert(input('Input:\t'))


        #check for end message
        if 'exit' in user_input:
            print('See you next time')
            chat=False
        #print commands
        if user_input=='instructions':
            print(cf.print_instructions())
        #CPU
        if user_input=='cpu':
            print('There are two company that produces CPU, which one will you choose? Type in "intel" or "ryzen"')

        if user_input=='intel':
            #return the corresponding model
            print(cf.return_model_name(cpu_list,'brand','Intel','model'))
            print('You can start shopping or get detailed info of products that you interested in')
            cf.print_instructions()

        if user_input=='ryzen':
            print(cf.return_model_name(cpu_list,'brand','Ryzen','model'))
            cf.print_instructions()

        #start shopping
        if user_input=='start shopping':
            start_shopping=True
            print('You can type in the product name you want to purchase, and type in "show shopping list" to show the products you purchased. When you finished, please type in "finish shopping".')

        #check info
        if user_input=='info':
            check_info=True
            print('You can type the model name to get detailed info.')


        #finish shopping
        if user_input=='finish shopping':
            start_shopping=False
            print('shopping finished')

        #show shopping list
        if user_input=='show shopping list':
            print(user_computer_list)

        #check if user's input matches one of the model name; if yes, put them in the shopping cart
        if cf.check_input(cpu_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')


        #print detailed info of the product
        if cf.check_input(total_list,user_input) and check_info==True:
            print(cf.find_and_return_dict(total_list,'model',user_input))

        #GPU
        if user_input=="gpu":
           print('There is a lists of all graphic cards we provided')
           print(cf.return_model_name(gpu_list,'brand','Nvidia','model'))
           cf.print_instructions()

        #same with above, different parameter
        if cf.check_input(gpu_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #motherboard
        if user_input=="motherboard":
           print('There is a lists of all motherboards we provided')
           print(cf.return_model_name(motherboard_list,'brand','gigabyte','model'))
           cf.print_instructions()

        if cf.check_input(motherboard_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #memory stick
        if user_input=="memory":
           print('There is a lists of all memory sticks we provided')
           print(cf.return_model_name(memory_list,'brand','Kingston','model'))
           cf.print_instructions()

        if cf.check_input(memory_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #cooling system
        if user_input=="cooling":
           print('There is a lists of all cooling devices we provided. There are two main producers: noctua and cosair, which one would you choose? Please type in "noctua" or "cosair"')

        if user_input=="noctua":
            print(cf.return_model_name(cool_list,'brand','noctua','model'))
            cf.print_instructions()

        if user_input=="cosair":
            print(cf.return_model_name(cool_list,'brand','cosair','model'))
            cf.print_instructions()

        if cf.check_input(cool_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #power
        if user_input=="power":
            print('There is a lists of all power supply we provided. You can choose between EVGA or Cosair. You need to type "evga" or "cosair"')

        if user_input=="evga":
            print(cf.return_model_name(power_list,'brand','EVGA','model'))
            cf.print_instructions()

        if user_input=="cosair":
            print(cf.return_model_name(power_list,'brand','cosair','model'))
            cf.print_instructions()

        if cf.check_input(power_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #computer case
        if user_input=="computer case":
            print('There is a lists of all computer cases we provided. There are four different brand: Fractal Design, Thermaltake, Cooler Master, and Antec. Type in one of them.')

        if user_input=="fractal design":
            print(cf.return_model_name(case_list,'brand','Fractal Design','model'))
            cf.print_instructions()

        if user_input=="antec":
            print(cf.return_model_name(case_list,'brand','Antec','model'))
            cf.print_instructions()

        if user_input=="cooler master":
            print(cf.return_model_name(case_list,'brand','Cooler Master','model'))
            cf.print_instructions()

        if user_input=="thermaltake":
            print(cf.return_model_name(case_list,'brand','Thermaltake','model'))
            cf.print_instructions()

        if cf.check_input(case_list,user_input) and start_shopping==True:
            user_computer_list.append(user_input)
            print('Successfully Stored')

        #show total price of shopping list
        if user_input=='total price':
            user_computer=MyComputer(user_computer_list, total_list)
            print(str(user_computer.return_price())+'$')


