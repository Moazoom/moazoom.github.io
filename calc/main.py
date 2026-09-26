# dividend calculator for dad
import streamlit as st

st.write(" ## Divident Calculator")
"by Moazzam Zahid"

left, mid, right = st.columns(3)

numShares = left.number_input("No. of Shares", value=None, step=1, format="%d")
buyPrice = mid.number_input("Purchase Price", value=None)
faceValue = right.number_input("Face Value", value=None, step=1, format="%d")

col1, col2, col3, col4 = st.columns(4)

q1 = col1.number_input("Quater 1 %", value=None, placeholder="Enter a percentage...")
q2 = col2.number_input("Quater 2 %", value=None, placeholder="Enter a percentage...")
q3 = col3.number_input("Quater 3 %", value=None, placeholder="Enter a percentage...")
q4 = col4.number_input("Quater 4 %", value=None, placeholder="Enter a percentage...")


filer = st.segmented_control("Are you a filer?", ["Filer", "Non filer"])

if (st.button("Calculate")):

    totalDiv = q1 + q2 + q3 + q4
    amount  = numShares * buyPrice

    if (filer == "Filer"):
        st.write("Output: " + str(round(0.85 * faceValue * totalDiv * numShares / amount, 2)) + "%")
    elif (filer == "Non filer"):
        st.write("Output: " + str(round(0.7 * faceValue * totalDiv * numShares / amount, 2)) + "%")
    else:
        st.write("Please enter all values")

#filer = 0.85 * faceValue * totalDiv * numShares / amount 
#nonFiler = 0.7 * faceValue * totalDiv * numShares / amount 

#numShares = float(input("how many shares: "))
#buyPrice = float(input("buy price: "))
#faceValue = float(input("face value: "))

#print("dividend accounced % : ")
#q1 = float(input("q1: "))
#q2 = float(input("q2: "))
#q3 = float(input("q3: "))
#q4 = float(input("q4: "))

#print("filer: " + str(filer) + "%, non filer: " + str(nonFiler) + "%")