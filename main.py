# import streamlit as st
# from few_shot import FewShotPosts
# from post_generator import generate_post


# length_options = ["Short", "Medium", "Long"]
# language_options = ["English", "Hinglish"]


# def main():
#     st.header("LinkedIn AutoContent")

#     col1, col2, col3 = st.columns(3)

#     fs = FewShotPosts()
#     tags = fs.get_tags()
#     with col1:
#         selected_tag = st.selectbox("Topic", options=tags)

#     with col2:
#         selected_length = st.selectbox("Length", options=length_options)

#     with col3:
#         selected_language = st.selectbox("Language", options=language_options)



#     if st.button("Generate"):
#         post = generate_post(selected_length, selected_language, selected_tag)
#         st.write(post)


# if __name__ == "__main__":
#     main()


import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Specify the absolute path to the style.css file
css_file_path = r'C:\Users\jsrin\OneDrive\Desktop\GenAi\Linkedin_Post_Generator\style.css'

# Read and apply the CSS file with the correct encoding to handle special characters
with open(css_file_path, 'r', encoding='utf-8-sig') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.header("LinkedIn AutoContent")

    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)

if __name__ == "__main__":
    main()
