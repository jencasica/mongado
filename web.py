import streamlit as st
from PIL import Image

def crop_image(image, width, height):
    """
    Crop the uploaded image to fit the desired width and height.
    """
    # Crop the image to the center
    img_width, img_height = image.size
    left = (img_width - width) / 2
    top = (img_height - height) / 2
    right = (img_width + width) / 2
    bottom = (img_height + height) / 2

    # Perform the crop
    return image.crop((left, top, right, bottom))

def main():
    # Page Configuration
    st.set_page_config(
        page_title="My Cute Biography",
        page_icon="🌟",
        layout="wide",
    )

    # Custom CSS for Styling
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            font-size: 3rem;
            color: #3D3B8E;
            text-align: center;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .sub-title {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
            margin-bottom: 2rem;
        }
        .profile-container {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            padding: 2rem;
            border-radius: 50%;
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.2);
            margin: 2rem auto;
            max-width: 450px;
            text-align: center;
        }
        .family-container, .extras-container {
            background: linear-gradient(to bottom, #ffffff, #f7f9fc);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            margin: 2rem 0;
        }
        .footer {
            text-align: center;
            color: gray;
            font-size: small;
            margin-top: 3rem;
        }
        .quote {
            font-style: italic;
            font-size: 1.2rem;
            color: #333;
            margin-top: 1.5rem;
            text-align: center;
        }
        .theme-switch {
            margin-top: 1rem;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header Section
    st.markdown('<h1 class="main-title">🌟 My Biography </h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Customize, preview, and generate a biography that truly represents you and your family!</p>', unsafe_allow_html=True)

    # Sidebar Inputs
    st.sidebar.title("📝 Your Profile Details")
    name = st.sidebar.text_input("👤 Name", placeholder="JENNYLYN M. CASICA")
    gender = st.sidebar.radio("⚥ Gender", options=["Male", "Female", "Non-Binary", "Prefer Not to Say"], index=0)
    age = st.sidebar.number_input("🎂 Age", min_value=1, max_value=120, step=18)
    profession = st.sidebar.text_input("💼 Profession", placeholder="STUDENT")
    hobbies = st.sidebar.text_area("🎨 Hobbies or Interests", placeholder="MUSIC, PLAYING INSTRUMENTS,TABBLE TENNIS")
    about_me = st.sidebar.text_area("✍️ About Me", placeholder="I LOVE MATH AND MUSIC")
    profile_pic = st.sidebar.file_uploader("📷 Upload Your Profile Picture", type=["jpg", "png", "jpeg"])
    favorite_quote = st.sidebar.text_area("💬 Favorite Quote", placeholder="All our dreams can come true, if we have the courage to pursue them.'")

    # Background Customization
    st.sidebar.title("🎨 Customization")
    theme = st.sidebar.radio("🖌️ Choose Theme", ["Light", "Dark"], index=0)
    background_image = st.sidebar.file_uploader("🌄 Upload Background Image (Optional)", type=["jpg", "png"])

    # Family Details Section
    st.sidebar.title("👪 Family Details")
    father_name = st.sidebar.text_input("👨‍👦 Father's Name", placeholder="N/A")
    father_profession = st.sidebar.text_input("👨‍💼 Father's Profession", placeholder="N/A")
    mother_name = st.sidebar.text_input("👩‍👦 Mother's Name", placeholder="MERLY MONGADO")
    mother_profession = st.sidebar.text_input("👩‍💼 Mother's Profession", placeholder="HOUSE WIFE")
    sibling_name = st.sidebar.text_input("🧑‍🤝‍🧑 Sibling's Name", placeholder="Sibling's Name (Optional)")
    sibling_profession = st.sidebar.text_input("💼 Sibling's Profession", placeholder="Sibling's Profession (Optional)")
    pet_name = st.sidebar.text_input("🐾 Pet's Name", placeholder="BARCKLY")
    pet_type = st.sidebar.text_input("🐶 Pet Type", placeholder="BULLDOG")

    # Social Media Section
    st.sidebar.title("🌐 Social Media")
    instagram = st.sidebar.text_input("📸 Instagram Handle", placeholder="@username")
    twitter = st.sidebar.text_input("🐦 Twitter Handle", placeholder="@username")
    linkedin = st.sidebar.text_input("🔗 LinkedIn Profile", placeholder="https://m.facebook.com/merly.andrade.7798/")

    # Generate Button
    generate = st.sidebar.button("✨ Generate Biography")

    if generate:
        # Validate Inputs
        if not name:
            st.error("❗ Please provide your name to generate a biography.")
            return

        # Dynamic Background
        if background_image:
            # Open and crop the background image to a specific size (e.g., 1200x800)
            bg = Image.open(background_image)
            cropped_bg = crop_image(bg, 1200, 800)  # Crop to desired size
            st.image(cropped_bg, use_column_width=True)
        else:
            st.markdown(f"<div style='background-color:{'#f7f9fc' if theme == 'Light' else '#333'}; height: 20px;'></div>", unsafe_allow_html=True)

        # Profile Section
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        if profile_pic:
            img = Image.open(profile_pic)
            st.image(img, caption=f"{name}", use_column_width=True, output_format="auto", class_="profile-pic")
        st.markdown(f"### 👤 **Name:** {name}")
        st.markdown(f"### ⚥ **Gender:** {gender}")
        st.markdown(f"### 🎂 **Age:** {age}")
        st.markdown(f"### 💼 **Profession:** {profession}")
        st.markdown(f"### 🎨 **Hobbies:** {hobbies}")
        st.markdown(f"### ✍️ **About Me:** {about_me}")
        if favorite_quote:
            st.markdown(f'<p class="quote">"{favorite_quote}"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Family Details
        st.markdown('<div class="family-container">', unsafe_allow_html=True)
        st.markdown(f"**👨‍👦 Father's Name:** {father_name} | **Profession:** {father_profession}")
        st.markdown(f"**👩‍👦 Mother's Name:** {mother_name} | **Profession:** {mother_profession}")
        if sibling_name:
            st.markdown(f"**🧑‍🤝‍🧑 Sibling's Name:** {sibling_name} | **Profession:** {sibling_profession}")
        if pet_name:
            st.markdown(f"**🐾 Pet's Name:** {pet_name} | **Type:** {pet_type}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Social Media Links
        st.markdown('<div class="extras-container">', unsafe_allow_html=True)
        if instagram:
            st.markdown(f"📸 **Instagram:** [@{instagram}](https://instagram.com/{instagram})")
        if twitter:
            st.markdown(f"🐦 **Twitter:** [@{twitter}](https://twitter.com/{twitter})")
        if linkedin:
            st.markdown(f"🔗 **LinkedIn:** [{linkedin}](https://{linkedin})")
        st.markdown('</div>', unsafe_allow_html=True)

        st.success("🎉 Your biography has been successfully generated!")

    # Footer
    st.markdown('<div class="footer">Crafted with ❤️ using Streamlit | Ultimate Biography Generator 🌟</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()