st=input("enter a string:")
st=st.casefold()
vowel="aeiou"
data={}.fromkeys(vowel,0)
for character in st:
    if character in vowel:
        data[character]+=1
        for vowel in data:
            print(vowel,"=>",data[vowel]) 