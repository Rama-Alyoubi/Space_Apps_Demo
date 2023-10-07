import subprocess
import sys


# Install required packages using pip
required_packages = [
    'streamlit',
    'streamlit_chat',
    'langchain',
    'openai',
    'faiss-cpu',
    'tiktoken'
]
for package in required_packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from openai.error import AuthenticationError
import tempfile
import os

def main():

    with st.sidebar:
        st.image("Miralux_Logo.png", caption="Logo", use_column_width=True)
    st.markdown(
            """
            <h2 style='text-align: center;'> MIRALUX </h2>
            """,
            unsafe_allow_html=True,
        )
    st.markdown(
            """
            <div style='text-align: center;'>
                <h4 style='text-align: center;'>Bringing brilliance to life</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    st.markdown(
            """
            <div style='text-align: center;'>
                <h6>Enter the <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API key</a> to start chatting</h6>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    user_api_key = st.sidebar.text_input(
    label="#### Your OpenAI API key 👇",
    placeholder="sk-",
    type="password")
    
    csv_file_path = "mIRALUX.csv"

    if csv_file_path and user_api_key:

        loader = CSVLoader(file_path=csv_file_path, encoding="utf-8")
        data = loader.load()
        os.environ["OPENAI_API_KEY"] = "sk-"+ user_api_key
        embeddings = OpenAIEmbeddings()
        try:
            vectors = FAISS.from_documents(data, embeddings)
        except AuthenticationError:
            st.error("Incorrect API key provided. Please check your API key at [this link](https://platform.openai.com/account/api-keys).")

        chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
                                                                        retriever=vectors.as_retriever())

        def conversational_chat(query):
            
            result = chain({"question": query, "chat_history": st.session_state['history']})
            st.session_state['history'].append((query, result["answer"]))
            
            return result["answer"]
        
        if 'history' not in st.session_state:
            st.session_state['history'] = []

        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Hello ! Ask me anything about " + csv_file_path + " 🤗"]

        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey ! 👋"]
            
        #container for the chat history
        response_container = st.container()
        #container for the user's text input
        container = st.container()

        with container:
            with st.form(key='my_form', clear_on_submit=True):
                
                user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
                submit_button = st.form_submit_button(label='Send')
                
            if submit_button and user_input:
                output = conversational_chat(user_input)
                
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

        if st.session_state['generated']:
            with response_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
    # Session state management
    def get_session_state():
        return st.session_state

    def new_page_content():
        st.title("Envisioning AI-Generated Worlds Teeming with Life ✨ !!")
        st.title("")
        button_style = """
            <style>
            .big-button button {
                font-size: 20px;
                width: 200px;
                height: 60px;
            }
            </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # Display the buttons in the respective columns
        col1, col2, col3 = st.columns(3)
        st.write("")
        st.write("")
        st.write("")
        with col1:
            button_aetheria = st.button("Aetheria", key="aetheria_button")

        with col2:
            button_veridion = st.button("Veridion", key="veridion_button")

        with col3:
            button_novaris = st.button("Novaris", key="novaris_button")

        st.write("")  # Add empty space between rows

        _, col4, col5, _ = st.columns([1, 2, 1, 2])

        with col4:
            button_serenova = st.button("Serenova", key="Serenova_button")

        with col5:
            button_elysium = st.button("Elysium", key="Elysium_Prime_button")

        # Button 1
        if button_aetheria:
            st.header("Planet Name: Aetheria")
            st.subheader("Characteristics:")
            
            st.write("Aetheria is a potentially habitable exoplanet located in the habitable zone of its host star. It exhibits several key characteristics that make it a promising candidate for supporting life.")
            
            st.write("1. **Host Star:** Aetheria orbits a G-type main-sequence star similar to our Sun, providing it with a stable and suitable energy source for life to thrive.")
            
            st.write("2. **Orbital Parameters:** Aetheria has an orbital period of approximately 365 days, similar to Earth's year, allowing for relatively stable seasons and climate patterns.")
            
            st.write("3. **Size and Composition:** With a radius of approximately 1.2 times that of Earth, Aetheria falls within the range of rocky exoplanets. Its composition suggests the presence of a solid surface, which is crucial for the development of complex life forms.")
            
            st.write("4. **Atmosphere:** Observations indicate the existence of an atmosphere on Aetheria, primarily composed of nitrogen, oxygen, and trace amounts of other gases. This atmosphere provides protection against harmful radiation and helps regulate surface temperatures.")
            
            st.write("5. **Surface Water:** Aetheria boasts a significant amount of liquid water on its surface, with vast oceans, lakes, and rivers. The presence of water is a fundamental requirement for the emergence and sustenance of life as we know it.")
            
            st.write("6. **Climate:** Aetheria experiences a moderate and stable climate, with temperate regions conducive to supporting a diverse range of ecosystems. The planet exhibits a balanced distribution of heat and moisture, fostering the potential for a rich biosphere.")
            
            st.write("7. **Magnetic Field:** A robust magnetic field envelops Aetheria, shielding the planet's surface from harmful solar winds and cosmic rays. This protection is vital for maintaining a hospitable environment and safeguarding potential life from harmful radiation.")
            
            st.write("8. **Biosignatures:** Preliminary spectroscopic analysis has detected the presence of atmospheric biosignatures, such as the existence of oxygen and methane, indicating the likelihood of biological activity on the planet.")
            
            st.write("The classification of Aetheria as a potentially habitable exoplanet is based on a comprehensive analysis of data gathered from space-based telescopes, ground-based observations, and advanced modeling techniques. Further exploration and detailed study of Aetheria's surface and atmosphere will be required to assess its potential for hosting life.")

        # Button 2
        if button_veridion:
            st.header("Planet Name: Veridion")
            st.subheader("Characteristics:")
            
            st.write("Veridion is an intriguing exoplanet that exhibits unique characteristics that suggest the possibility of supporting life.")
            
            st.write("1. **Host Star:** Veridion orbits a K-type dwarf star, slightly smaller and cooler than our Sun. Despite its lower luminosity, the star provides sufficient warmth and energy for potential life forms on Veridion.")
            
            st.write("2. **Orbital Parameters:** Veridion follows a slightly eccentric orbit around its host star, resulting in seasonal variations that could contribute to dynamic and diverse ecosystems.")
            
            st.write("3. **Size and Composition:** Veridion is a rocky planet with a radius approximately 1.5 times that of Earth. Its composition suggests a solid surface, which could provide stable environments for the emergence and development of life.")
            
            st.write("4. **Atmosphere:** Veridion possesses a dense atmosphere primarily composed of nitrogen, carbon dioxide, and traces of other gases. This atmosphere helps regulate surface temperatures and protects the planet from harmful radiation.")
            
            st.write("5. **Surface Conditions:** Veridion features a diverse range of landscapes, including vast plains, towering mountains, and deep valleys. It exhibits a variety of geological formations and potentially harbors mineral-rich regions that could support complex life.")
            
            st.write("6. **Tidal Locking:** Veridion is tidally locked, meaning one side of the planet always faces its host star, while the other remains in perpetual darkness. This creates stark temperature differences between the illuminated and dark sides, potentially leading to distinct habitats and climate zones.")
            
            st.write("7. **Liquid Water:** Veridion possesses a network of lakes, rivers, and smaller oceans, primarily located in the transitional regions between the illuminated and dark sides. These water bodies could serve as potential habitats for aquatic life forms.")
            
            st.write("8. **Biosignatures:** Observations of Veridion's atmosphere have revealed intriguing biosignatures, including the presence of carbon-based compounds and the potential for atmospheric oxygen. These signs hint at the possibility of biological activity and ecosystems on the planet.")
            
            st.write("Exploration missions and further analysis will be necessary to study Veridion in more detail and determine the extent of its habitability. The unique characteristics of Veridion make it a compelling target for future space missions aimed at searching for life beyond our solar system.")

        # Button 3
        if button_novaris:
            st.header("Planet Name: Novaris")
            st.subheader("Characteristics:")
            
            st.write("Novaris is an exoplanet with intriguing attributes that make it a potential candidate for hosting life in a distant star system.")
            
            st.write("1. **Host Star:** Novaris orbits a red dwarf star, known for its longevity and stability. Although smaller and cooler than our Sun, the red dwarf provides a steady energy source for potential life on Novaris.")
            
            st.write("2. **Orbital Parameters:** Novaris follows a near-circular orbit around its host star, resulting in relatively stable seasons and a consistent climate. This orbital configuration provides a favorable environment for the development of complex ecosystems.")
            
            st.write("3. **Size and Composition:** Novaris is a rocky planet with a radius similar to that of Earth, indicating the presence of a solid surface. Its composition suggests the possibility of continents, mountains, and diverse geological features that could support life.")
            
            st.write("4. **Atmosphere:** Novaris possesses a thin but breathable atmosphere, primarily composed of nitrogen, oxygen, and trace amounts of other gases. This atmosphere provides protection against harmful radiation and helps regulate surface temperatures.")
            
            st.write("5. **Surface Water:** Novaris harbors a significant amount of liquid water in the form of vast oceans and smaller bodies such as lakes and rivers. The presence of water is a crucial factor for the emergence and sustenance of life as we know it.")
            
            st.write("6. **Climate:** Novaris experiences a moderate and stable climate, with a balanced distribution of heat and moisture across its surface. The planet's climate zones support a wide range of habitats, allowing for the potential development of diverse ecosystems.")
            
            st.write("7. **Magnetic Field:** Novaris possesses a magnetic field generated by its molten core, which helps shield the planet's surface from harmful solar winds and cosmic radiation. This protective magnetic field is vital for the preservation of a habitable environment.")
            
            st.write("8. **Biosignatures:** Observations of Novaris reveal the presence of atmospheric biosignatures, such as the detection of oxygen and methane. These indicators suggest the possibility of biological activity and the existence of potential life forms on the planet.")
            
            st.write("Further exploration and detailed investigations, including direct observations and analysis of Novaris, will be required to validate its potential for hosting life. Novaris represents an exciting target for future space missions and offers valuable insights into the potential habitability of exoplanets in the universe.")
            

        # Button 4
        if button_serenova:
            st.header("Planet Name: Serenova")
            st.subheader("Characteristics:")
            
            st.write("Serenova is a captivating exoplanet that possesses a unique set of characteristics, making it a promising candidate for hosting life in a distant star system.")
            
            st.write("1. **Host Star:** Serenova orbits a binary star system consisting of two closely orbiting stars, similar to a binary version of our Sun. This dual-star configuration provides abundant energy and a distinctive day-night cycle, creating diverse light conditions across the planet's surface.")
            
            st.write("2. **Orbital Parameters:** Serenova follows a moderately elliptical orbit around its binary star system, resulting in varying levels of solar radiation throughout its year. This orbital eccentricity influences seasonal changes and potentially fosters the development of adaptable life forms.")
            
            st.write("3. **Size and Composition:** Serenova is a terrestrial planet with a radius slightly larger than Earth's. Its rocky composition suggests the presence of a solid surface, offering the potential for diverse geographical features and stable environments for life to emerge.")
            
            st.write("4. **Atmosphere:** Serenova possesses a substantial atmosphere comprised primarily of nitrogen, oxygen, and trace gases. This atmosphere shields the planet from harmful radiation, moderates temperature fluctuations, and enables the cycling of essential gases necessary for life.")
            
            st.write("5. **Surface Water:** Serenova exhibits a rich hydrological system with vast oceans, lakes, and an intricate network of rivers. The presence of liquid water provides habitats that support the development and sustenance of diverse aquatic ecosystems.")
            
            st.write("6. **Climate:** Serenova experiences a dynamic climate characterized by a complex interplay between the gravitational forces of its binary stars. This interaction can lead to localized climate variations, creating a tapestry of microclimates across the planet.")
            
            st.write("7. **Magnetic Field:** Serenova generates a robust magnetic field, protecting its atmosphere and surface from harmful solar winds and cosmic radiation. This shielding mechanism plays a crucial role in maintaining a stable environment suitable for the evolution of complex life forms.")
            
            st.write("8. **Biosignatures:** Preliminary spectroscopic analysis of Serenova's atmosphere has revealed the presence of potential biosignatures, such as the coexistence of oxygen and methane. These signs hint at the possibility of biological activity and the potential for a thriving biosphere on the planet.")
            
            st.write("Further exploration and detailed studies are necessary to assess the full extent of Serenova's habitability and the presence of life. Serenova represents an intriguing target for future space missions, offering a unique opportunity to understand the complexities of planetary systems and the potential for life beyond our solar system.")

        # Button 5
        if button_elysium:
            st.header("Planet Name: Elysium Prime")
            st.subheader("Characteristics:")
            
            st.write("Elysium Prime is a captivating exoplanet that exhibits a remarkable combination of features that make it a compelling candidate for supporting life.")
            
            st.write("**Host Star:** Elysium Prime orbits a yellow dwarf star, similar in size and characteristics to our Sun. This star provides a stable and nurturing energy source, allowing for the potential development of life-sustaining conditions on the planet.")
            
            st.write("**Orbital Parameters:** Elysium Prime follows a nearly circular orbit around its host star, resulting in stable seasons and a relatively consistent climate. This orbital stability provides favorable conditions for the emergence and evolution of complex ecosystems.")
            
            st.write("**Size and Composition:** Elysium Prime is a terrestrial planet with a radius comparable to that of Earth. Its rocky composition suggests the presence of a solid surface, conducive to the formation of diverse geological features and potential habitats for life.")
            
            st.write("**Atmosphere:** Elysium Prime possesses a dense atmosphere primarily composed of nitrogen, oxygen, and trace amounts of other gases. This atmospheric composition creates a protective shield, shielding the planet's surface from harmful radiation and facilitating the regulation of surface temperatures.")
            
            st.write("**Surface Water:** Elysium Prime boasts an abundance of liquid water, with vast oceans, lakes, and rivers covering a significant portion of its surface. These water bodies provide essential habitats for aquatic life forms and contribute to the planet's overall habitability.")
            
            st.write("**Climate:** Elysium Prime experiences a moderate and stable climate, characterized by relatively mild temperature variations and balanced precipitation patterns. These climatic conditions foster the potential development of diverse ecosystems, supporting a wide range of flora and fauna.")
            
            st.write("**Magnetic Field:** Elysium Prime possesses a robust magnetic field generated by its molten core, offering protection against solar winds and cosmic radiation. This magnetic shielding preserves the planet's atmosphere and supports the long-term sustainability of potential life forms.")
            
            st.write("**Biosignatures:** Preliminary observations of Elysium Prime's atmosphere have revealed intriguing biosignatures, including the presence of oxygen and methane. These indicators hint at the possibility of biological activity on the planet, further raising its potential for hosting life.")
            
            st.write("Understanding the full extent of Elysium Prime's habitability and the existence of life on the planet requires in-depth exploration and comprehensive scientific investigations. Elysium Prime represents an exciting target for future space missions, offering valuable insights into the potential for life beyond our solar system.")
        
        

    if st.sidebar.button("✨ AI-Generated Worlds"):
        session_state = get_session_state()
        session_state.page = "new_page"

    if 'page' not in st.session_state:
        st.session_state.page = ""

    # Display content based on current page
    if get_session_state().page == "new_page":
        new_page_content()

    #Contact
    with st.sidebar.expander("📬 Contact"):

        st.write("**LinkedIn:**")
        st.write("[Rama-Alyoubi](https://www.linkedin.com/in/rama-alyoubi/)")
        st.write("[Rimas-Alshehri](https://www.linkedin.com/in/rimas-alshehri/)")
        st.write("[Yara-Alshehri](https://www.linkedin.com/in/yara-alshehri-663096265/)")
        st.write("[Taif-Alharbi](https://www.linkedin.com/in/taif-alharbi-4b0895270/)")
        st.write("**Twitter \"X\":**")
        st.write("[Rama-Alyoubi](https://twitter.com/Rama_Alyoubi)")
        st.write("[Rimas-Alshehri](https://twitter.com/rimasns)")
        st.write("[Yara-Alshehri](https://twitter.com/iYH_55)") 
        st.write("[Taif-Alharbi](https://twitter.com/ghostchii?s=11)")
        st.write("**Mail** :")
        st.write("*Rama Alyoubi* : Rama.mohammed.alyoubi@gmail.com")
        st.write("*Rimas Alshehri* : rimvasn@hotmail.com")
        st.write("*Yara Alshehri* : Yara55hassan@gmail.com")
        st.write("*Taif Alharbi* : Taif.impo@gmail.com")

if __name__ == "__main__":
    main()