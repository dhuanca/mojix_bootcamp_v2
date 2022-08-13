import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')

image = Image.open('imagen.jpeg')
st.image(image, caption='Photo by Miesha Maiden from Pexels')

st.markdown('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.'+
'In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

st.subheader('1. Walrus operator')

st.markdown('The **Walrus or :=** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')


if st.button('Example'):
    st.markdown('~~~'+
                'Mylist = [1,2,3]' + 
               'if(l := len(mylist) > 2)' +
                'print(l)'+
                '~~~'
                )
else:
     st.write('Goodbye')


st.title('Ejemplo de uso de datos')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


'''
# Este es un titulo usando magic command

Esto es markdown _markdown_   **resltando algo** 

Siguiente parrafo 

a)
b)
'''


st.caption('This is a string that explains something above.')


code = '''
def hello():
    print("Hello, Streamlit!")
hello() '''

st.code(code, language='python')