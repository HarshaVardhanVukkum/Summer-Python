import streamlit as st

# Define the resume content
def main():
    st.title("Vukkum Harsha Vardhan - Resume")

    st.header("Contact Information")
    st.write("**Email:** v.harshavardhan03@gmail.com")
    st.write("**Phone:** +91 9581716919")
    st.write("**LinkedIn:** [Vukkum Harsha Vardhan](https://www.linkedin.com/in/harshavardhanvukkum)")
    st.write("**GitHub:** [HarshaVardhanVukkum](https://github.com/HarshaVardhanVukkum)")

    st.header("Objective")
    st.write("Pursuing B Tech 3rd year in Artificial Intelligence and Data Science with proficiency in C, Python, and Java. Seeking opportunities to solve complex problems and grow in a collaborative, innovative environment.")

    st.header("Education")
    st.write("**Bachelor of Technology in Artificial Intelligence & Data Science**")
    st.write("Sir C. R. Reddy College of Engineering, Eluru")
    st.write("Graduation: 2026 | Current Percentage: 73.9%")
    st.write("**Intermediate (MPC)**")
    st.write("Narayana Junior College, Eluru")
    st.write("Graduation: 2022 | Percentage: 86.9%")
    st.write("**SSC**")
    st.write("Sri Bhavishya High School, Eluru")
    st.write("Graduation: 2020 | Percentage: 94.6%")

    st.header("Technical Skills")
    st.write("- **Programming Languages**: C Language, Python, Basics in Java Programming, HTML")
    st.write("- **Tools**: Visual Studio, Google Colab")

    st.header("Internships")
    internships = [
        "Machine Learning Internship – Apna Guide",
        "Data Science Internship – Skill Dzire",
        "AI-ML Internship – YBI Foundation"
    ]
    for internship in internships:
        st.write(f"- {internship}")

    st.header("Strengths")
    st.write("- Quick learner")
    st.write("- Proactive and initiative-taker")
    st.write("- Strong team collaboration skills")

    st.header("Hobbies")
    st.write("- Reading")
    st.write("- Drawing")
    st.write("- Solving puzzles")

    st.header("Achievements")
    st.write("- **First Prize** in Kho-Kho (2016)")
    st.write("- **Third Runner-up** for Quizzeria Coding (2024)")

    st.header("Personal Details")
    st.write("**Name:** Vukkum Harsha Vardhan")
    st.write("**Father's Name:** V Srinivasa Rao")
    st.write("**Mother's Name:** V Roja")
    st.write("**Date of Birth:** 21-03-2005")
    st.write("**Current Location:** Eluru, West Godavari, Andhra Pradesh")
    st.write("**Nationality:** Indian")
    st.write("**Pin Code:** 534001")

if __name__ == "__main__":
    main()
