import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')

image = Image.open('imagen.jpeg')
st.image(image, caption='Photo by Miesha Maiden from Pexels')

st.markdown('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.'+
'In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')


# texto_csv = pd.read_csv("text_csv.csv", sep =';')


def imprime_texto(header_text, mar_text, code_text, code_text_output):
    st.header(header_text)
    st.markdown(mar_text)
    st.subheader('Example')
    code = code_text
    st.code(code, language='python')
    st.subheader('Output')
    code = code_text_output
    st.code(code, language='python')




# 1 walrus operator
header_text = '1. Walrus operator'
mar_text = 'The **Walrus or :=** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.'
code_text = '''Mylist = [1,2,3] \nif(l := len(mylist) > 2) \nprint(l)''' 
code_text_output = '''3'''
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 2. Splitting a string
header_text = '2. Splitting a string'
mar_text = 'If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!'
code_text = '''string = “hello world” \nstring.split()''' 
code_text_output = '''[‘hello’, ‘world’]'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 3. Reversing a string
header_text = '3. Reversing a string'
mar_text = 'If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.'
code_text = '''str=”hello world!” \na=str[::-1] \nprint(a)''' 
code_text_output = '''!dlrow olleh'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 4. Merging two dictionaries
header_text = '4. Merging two dictionaries'
mar_text = 'This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:'
code_text = '''d1 = {“a”: 10, “b”:20} \nd2 = {“c”: 30, “d”:40} \nd3 = {**d1, **d2} \nprint(d3)''' 
code_text_output = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 5. The zip() function
header_text = '5. The zip() function'
mar_text = 'The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.'
code_text = '''colour = [“red”, “yellow”, “green”] \nfruits = [‘apple’, ‘banana’, ‘mango’] \nfor colour, fruits in zip(colour, fruits): \nprint(colour, fruits)''' 
code_text_output = '''red apple \nyellow banana \ngreen mango'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 6. Assigning multiple list values to a variable
header_text = '6. Assigning multiple list values to a variable'
mar_text = 'If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:'
code_text = '''mylist = [1,2,3,4,5] \na,*b = mylist \nprint(f”a =”,a) \nprint(f”b =”,b)''' 
code_text_output = '''a = 1 \nb = [2, 3, 4, 5]'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 7. Remove duplicate list items
header_text = '7. Remove duplicate list items'
mar_text = 'Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.'
code_text = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9] \nnewlist = set(mylist) \nprint(newlist)''' 
code_text_output = '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

# 8. Lambda function
header_text = '8. Lambda function'
mar_text = 'If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.'
code_text = '''mul = lambda a,b: a*b \nmul(5,6)''' 
code_text_output = '''30'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)


# 9. Swapping variable value
header_text = '9. Swapping variable value'
mar_text = 'One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:'
code_text = '''a = 100 \nb = 200 \na,b = b,a \nprint(f’a = ‘,a) \nprint(f’b = ‘,b)''' 
code_text_output = '''a = 200 \nb = 100'''  
imprime_texto(header_text, mar_text, code_text, code_text_output)


# 10. Use a password in your code
header_text = '10. Use a password in your code'
mar_text = 'This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!'
code_text = '''from getpass import getpass \npassword = getpass(“password: “) \nif password == “abcd”: \n    print(“welcome strnger!”) \nelse: \n    print(“wrong password”)''' 
code_text_output = '''password: **** [abcd] \nWelcome stranger! \nPassword: **** [abdc] \nWrong password '''  
imprime_texto(header_text, mar_text, code_text, code_text_output)

st.markdown('Here is < https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922?dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1602697607&sr=8-2&linkCode=sl1&tag=pranjal20-20&linkId=71b2efa5db080e8f74068aebec7d7fb0&language=en_US&ref_=as_li_ss_tl > `a book` on Python programming that I would definitely recommend for all beginners.')
 
st.header('Conclusion')

st.markdown('These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.')

st.markdown('**Note:** This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.')

st.markdown('However, the recommended resource is experienced by me and helped me in my data science career journey.')

st.markdown('Before you go…')

st.markdown('If you liked this article and want to **stay tuned** with more **exciting** articles on **Python & Data Science** — do consider becoming a medium member by clicking here https://pranjalai.medium.com/membership.')

st.markdown('Please do consider signing up using my referral link. In this way, the portion of the membership fee goes to me, which motivates me to write more exciting stuff on Python and Data Science.')

st.markdown('Also, feel free to subscribe to my free newsletter: Pranjal’s Newsletter.')

