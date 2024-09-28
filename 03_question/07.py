# Given a string find the first non-repeated character 

st = "teester"

for char in st:
    if st.count(char) == 1:     #st.count(char). :- will return the count for every character in a string
        print(char)
        break
