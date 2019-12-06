import my_module.chatbot_functions as cf

string="hello,world"
compare_string="helloworld"
capstring="HELLOWORLD"
input_list=[]
input_list_2=[{'brand':'intel','model':'i5-3330','price':'59','data':'3.3'}]


def test_string_convert():
    """test whether it will turn string to lower case"""
    assert isinstance(cf.string_convert(capstring),str)
    assert cf.string_convert(capstring)==compare_string
    assert callable(cf.string_convert)

def test_string_concatenator():
    """ test string concatenter"""
    assert isinstance(cf.string_concatenator('hello','world',','),str)
    assert cf.string_concatenator('hello','world',',')==string
    assert callable(cf.string_concatenator)

def test_start_chat():
    """test start chat functin"""
    assert isinstance(cf.start_chat(),str)
    assert callable(cf.start_chat)

def test_add_component():
    """test add component functions"""
    assert callable(cf.add_component)

def test_find_and_return_dict():
    """test whether it will return right dictionary"""
    assert isinstance(cf.find_and_return_dict(input_list_2,'brand','intel'), dict)
    assert callable(cf.find_and_return_dict)

def test_return_model_name():
    """test whether it will return the right model name"""
    assert isinstance(cf.return_model_name(input_list_2,'brand','intel','model'),list)
    assert cf.return_model_name(input_list_2,'brand','intel','model')==['i5-3330']
    assert callable(cf.return_model_name)

def test_check_input():
    """ test check input function"""
    assert isinstance(cf.check_input(input_list_2,'i5-3330'),bool)
    assert cf.check_input(input_list_2,'i5-3330')==True
    assert callable(cf.check_input)

def test_print_instructions():
    """test print instructions function"""
    assert isinstance(cf.print_instructions(),str)
    assert callable(cf.print_instructions)

def check_all():
    """test all the functions"""
    test_string_convert()
    test_string_concatenator()
    test_start_chat()
    test_add_component()
    test_find_and_return_dict()
    test_return_model_name()
    test_check_input()
    test_print_instructions()
    
    print("test finished")

