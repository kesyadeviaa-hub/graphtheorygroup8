import streamlit as st

st.title("Team Profile")

team_members = [
    {
        "name": "Kesya Devia Anandita",
        "major": "Actuarial Science",
        "role": "Project Leader & UI Designer",
        "foto": "https://raw.githubusercontent.com/kesyadeviaa-hub/teamphoto/refs/heads/main/ACS_25102523320.jpg"
    },
    {
        "name": "Arganta Mahadana Wibowo",
        "major": "Actuarial Science",
        "role": "Backend Graph Algorithms",
        "foto": "https://raw.githubusercontent.com/kesyadeviaa-hub/teamphoto/refs/heads/main/ACS_25102553036.jpg"
    },
]

cols = st.columns(3)

for i, member in enumerate(team_members):
    with cols[i % 3]:
        st.image(member["foto"], width=180)
        st.markdown(f"**{member['name']}**")
        st.caption(member["major"])
        st.caption(member["role"])
