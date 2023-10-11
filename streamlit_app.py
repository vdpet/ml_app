import streamlit as st
import pickle
from PIL import Image

def show_predict_page(model, label_encoder, vectorizer):

    #image = Image.open(r"C:\Users\quebr\Documents\deployment\api\cohete.png")
    #st.image(image, use_column_width=True)

    
    st.title("Automated Product Categorization for E-commerce with AI :robot_face:")

    st.write("""### We need some information to predict the categories of the product""")
    
    with st.form("form"):
        name = st.text_input("Name")
        price_string = st.text_input("Price in String")
        type = st.text_input("Type")
        description = st.text_input("Description")
        manufacturer = st.text_input("Manufacturer")

        submitted = st.form_submit_button('Submit')

    if submitted:
        st.markdown(f'''
            You have submitted:
            - Name product: `{name}`
            - Price of the product: `{price_string}`
            - Type of the product: `{type}`
            - Description of the product: `{description}`
            - Manufacturer of the product: `{manufacturer}`
            ''')
        
        st.success("✅ Done!")


    string_model = name + ' ' + price_string + ' ' + type + ' ' + description + ' ' + manufacturer

    models = {'Logistic Regression', 'BERT Model'}
    
    model_select = st.selectbox("Choose a model to predict", models)

    predict_button = st.button("Predict")

    if model_select == 'Logistic Regression' and predict_button:
        some_text = model.predict(vectorizer.transform([string_model]))
        st.subheader(f"The level 1 category for the product is: {label_encoder.inverse_transform(some_text)[0]}")
    else:
        pass