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











