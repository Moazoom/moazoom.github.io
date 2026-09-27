# dividend calculator for dad
import streamlit as st

st.write("## Divident Calculator")
"by Moazzam Zahid"

left, mid, right = st.columns(3)

numShares = left.number_input("No. of Shares", value=0, step=1, format="%d")
buyPrice = mid.number_input("Purchase Price", value=0.00)
faceValue = right.number_input("Face Value", value=0, step=1, format="%d")

investment = numShares * buyPrice
st.write("> #### Your investment is Rs. " + str(round(investment, 2)))

col1, col2, col3, col4 = st.columns(4)

q1 = col1.number_input("Quater 1 %", max_value=100.00, value=0.00, placeholder="Enter a percentage...")
q2 = col2.number_input("Quater 2 %", max_value=100.00, value=0.00, placeholder="Enter a percentage...")
q3 = col3.number_input("Quater 3 %", max_value=100.00, value=0.00, placeholder="Enter a percentage...")
q4 = col4.number_input("Quater 4 %", max_value=100.00, value=0.00, placeholder="Enter a percentage...")


filer = st.segmented_control("Are you a filer?", ["Filer", "Non filer"])

if ((filer != None) and (investment)):

    totalDiv = q1 + q2 + q3 + q4
    amount  = numShares * buyPrice

    if (filer == "Filer"):
        out = 0.85 * faceValue * totalDiv * numShares / amount
        "> #### Your dividend as a percentage is " + str(round(out, 2)) + "%"
        "> #### Your total gain is Rs. " + str(round(out * investment / 100, 2))

    elif (filer == "Non filer"):
        out = 0.7 * faceValue * totalDiv * numShares / amount
        "> #### Your dividend as a percentage is " + str(round(out, 2)) + "%"
        "> #### Your total gain is Rs. " + str(round(out * investment / 100, 2))
    else:
        "> #### Please enter all values"

# legacy maths for reference
#numShares = float(input("how many shares: "))
#buyPrice = float(input("buy price: "))
#faceValue = float(input("face value: "))

#print("dividend accounced % : ")
#q1 = float(input("q1: "))
#q2 = float(input("q2: "))
#q3 = float(input("q3: "))
#q4 = float(input("q4: "))

#filer = 0.85 * faceValue * totalDiv * numShares / amount 
#nonFiler = 0.7 * faceValue * totalDiv * numShares / amount 

#print("filer: " + str(filer) + "%, non filer: " + str(nonFiler) + "%")