import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'api_key'

# Function to interact with OpenAI GPT-3.5 Turbo
def generate_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("OpenAI Chatbot Demo")
    
    # User input
    user_input = st.text_input("You:", "")

    if st.button("Generate Response"):
        if user_input:
            st.text("Assistant:")
            with st.spinner("Thinking..."):
                # Generate response from OpenAI
                response = generate_response(user_input)
                st.text(response)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
