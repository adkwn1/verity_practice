import random
import streamlit as st


# Variable Instiation
pic_map = {'c': 'circle.png',
           's': 'square.png',
           't': 'triangle.png',
           'cc': 'sphere.png',
           'tt': 'tetra.png',
           'ss': 'cube.png',
           'cs': 'cylinder.png',
           'ct': 'cone.png',
           'st': 'prism.png'}

name_map = {'c': 'Circle',
           's': 'Square',
           't': 'Triangle',
           'cc': 'Sphere',
           'tt': 'Tetrahedron',
           'ss': 'Cube',
           'cs': 'Cylinder',
           'ct': 'Cone',
           'st': 'Prism'}

shape_map = {'Circle': 'c',
             'Triangle': 't',
             'Square': 's'}

solution = {'c': 'st',
            's': 'ct',
            't': 'cs'}

all_shapes = ['c', 'c', 's', 's', 't', 't']
shapes = ['c', 't', 's']
dissection = ['Circle', 'Triangle', 'Square']
podiums = ['Left', 'Middle', 'Right']
path = 'images/' # image directory path
num_moves = 0

# Trainer Initialization
random.shuffle(shapes)

# Check that problem is not already solved via RNG
while True:
    redo = False
    random.shuffle(all_shapes)
    left = ''.join(sorted(all_shapes[0:2]))
    middle = ''.join(sorted(all_shapes[2:4]))
    right = ''.join(sorted(all_shapes[4:6]))

    statues = [left, middle, right]

    for i in range(len(podiums)):
        if solution[shapes[i]] == statues[i]:
            redo = True
    if not redo:
        break


# Streamlit UI Magic
st.markdown("<h1 style='text-align: center;'>Verity Practice Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>By: Charlie#7446</p>", unsafe_allow_html=True)

st.divider()

with st.container():
    st.markdown(f"<h5 style='text-align: center;'>Starting Conditions</h5>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>{'-'.join(shapes).upper()}</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<b><p style="text-align: center;">Left</p></b>', unsafe_allow_html=True)
        st.image(path + pic_map[left], caption=name_map[left])

    with col2:
        st.markdown('<b><p style="text-align: center;">Middle</p></b>', unsafe_allow_html=True)
        st.image(path + pic_map[middle], caption=name_map[middle])

    with col3:
        st.markdown('<b><p style="text-align: center;">Right</p></b>', unsafe_allow_html=True)
        st.image(path + pic_map[right], caption=name_map[right])
    
    if st.button("Reset"):
        st.session_state.clear()
        st.rerun()

st.divider()

if 'curr_state' not in st.session_state:
    st.session_state.curr_state = {'left': left,
                                   'middle': middle,
                                   'right': right}
    st.session_state.callout = shapes
    st.session_state.moves = num_moves


# Function definitions for solve
def dissect(d1:str, p1:str, d2:str, p2:str):
    s1 = list(p1)
    s2 = list(p2)
    d1_idx = s1.index(shape_map[d1])
    d2_idx = s2.index(shape_map[d2])

    temp = s1[d1_idx]
    s1[d1_idx] = s2[d2_idx]
    s2[d2_idx] = temp

    s1 = sorted(s1)
    s2 = sorted(s2)

    return ''.join(s1), ''.join(s2)

def enc_solved():
    result = [st.session_state.curr_state['left'], st.session_state.curr_state['middle'], st.session_state.curr_state['right']]
    for i in range(len(podiums)):
        if solution[st.session_state.callout[i]] != result[i]:
            return False  

    return True

@st.experimental_fragment
def solve():
    with st.form('dissection_form'):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            d1 = st.radio('First Dissection', dissection, index=None, key='first', on_change=None)
        with col2:
            s1 = st.radio('First Statue', podiums, index=None, key='statue_1', on_change=None)
        with col3:
            d2 = st.radio('Second Dissection', dissection, index=None, key='second', on_change=None)
        with col4:
            s2 = st.radio('Second Statue', podiums, index=None, key='statue_2', on_change=None)
        clicked = st.form_submit_button('Dissect')
    
    st.markdown(f"<h5>Result:</h5>", unsafe_allow_html=True)

    if clicked:
        # Check for illegal moves
        if d1 == d2 or s1 == s2:
            st.markdown("**Illegal Move** -- You cannot pick up same shape twice, or dissect the same statue.")
        elif shape_map[d1] not in st.session_state.curr_state[s1.lower()] or shape_map[d2] not in st.session_state.curr_state[s2.lower()]:
            st.markdown("**Illegal Move** -- The statue must contain the shape you want to dissect.")
        else:
            st.session_state.moves += 1
            p1 = st.session_state.curr_state[s1.lower()]
            p2 = st.session_state.curr_state[s2.lower()]

            st.session_state.curr_state[s1.lower()], st.session_state.curr_state[s2.lower()] = dissect(d1, p1, d2, p2)
    
            with st.container():
                l = st.session_state.curr_state['left']
                m = st.session_state.curr_state['middle']
                r = st.session_state.curr_state['right']

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown('<b><p style="text-align: center;">Left</p></b>', unsafe_allow_html=True)
                    st.image(path + pic_map[l], caption=name_map[l])

                with col2:
                    st.markdown('<b><p style="text-align: center;">Middle</p></b>', unsafe_allow_html=True)
                    st.image(path + pic_map[m], caption=name_map[m])

                with col3:
                    st.markdown('<b><p style="text-align: center;">Right</p></b>', unsafe_allow_html=True)
                    st.image(path + pic_map[r], caption=name_map[r])

    if enc_solved():
        st.markdown(f"<h2 style='text-align: center;'>Solved! Number of moves: {st.session_state.moves}</h2>", unsafe_allow_html=True)
                

solve()
st.stop()