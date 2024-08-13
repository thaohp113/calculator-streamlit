import streamlit as st 

st.title("My simple calculator 🧮")

if 'cal' not in st.session_state:
    st.session_state.cal = ""

def update_display(value):
    if value == "\+":
        value = "+"
    elif value == "\-":
        value = "-"
    elif value == "\*":
        value = "*"
    st.session_state.cal += value

def clear_display():
    st.session_state.cal = ""

def evaluate():
    try:
        # Check if there is a division by zero
        if "/0" in st.session_state.cal:
            st.session_state.cal = "INF"
        else:
            st.session_state.cal = str(eval(st.session_state.cal))
    except ZeroDivisionError:
        st.session_state.cal = "INF"
    except:
        st.session_state.cal = "Error"

st.markdown("""
    <style>
    .output-box {
        background-color: #f0f2f6;
        color: #000;
        border: 1px solid #d6d9dc;
        border-radius: 8px;
        height: 40px;
        padding: 5px;
        font-size: 18px;
        text-align: right;
    }
    .button-ac {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        height: 40px;
        padding: 5px;
        text-align: center;
        cursor: pointer;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)


col1, col2 = st.columns([4, 1])  

with col1:
    st.markdown(f'<div class="output-box">{st.session_state.cal}</div>', unsafe_allow_html=True)

with col2:
    if st.button('AC', key='ac_button', help="Clear display", use_container_width=True):
        clear_display()

# All buttons
buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '\*'],
        ['1', '2', '3', '\-'],
        ['0', '.', '=', '\+']
]

for row in buttons:
    cols = st.columns(len(row)) 
    for i, button in enumerate(row):
        if button == '=':
            cols[i].button(button, on_click=evaluate, use_container_width=True)
        else:
            cols[i].button(button, on_click=update_display, args=(button,), use_container_width=True)



