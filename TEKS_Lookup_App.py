import streamlit as st
import json

st.set_page_config(page_title="TEKS Lookup Tool", layout="wide")
st.title("📘 TEKS Lookup Tool")
st.markdown("Quickly search and view TEKS by code or keyword.")

# File uploader
uploaded_file = st.file_uploader("Upload a TEKS JSON file", type=["json"])

if uploaded_file:
    teks_data = json.load(uploaded_file)

    # Extract grade and subject
    grade = list(teks_data.keys())[0]
    subject = list(teks_data[grade].keys())[0]
    standards = teks_data[grade][subject]

    st.subheader(f"Loaded: {grade} - {subject}")

    # Grade and subject filters
    grade_filter = st.text_input("Filter by Grade (e.g., Grade 8)", value=grade)
    subject_filter = st.text_input("Filter by Subject (e.g., Social Studies)", value=subject)

    # Search bar
    query = st.text_input("Search by TEKS code or keyword", placeholder="e.g., 8.1A or Constitution")

    if query:
        query = query.lower()
        results = []

        for entry in standards:
            code = entry["Code"]
            strand = entry["Strand"]
            expectations = entry.get("Expectations", [])

            match_text = f"{code} {strand} {' '.join(expectations)}".lower()

            if query in match_text:
                results.append(entry)

        st.markdown(f"### 🔍 {len(results)} result(s) found for {grade_filter} - {subject_filter}:")

        for entry in results:
            st.markdown("---")
            st.markdown(f"**Code:** `{entry['Code']}`")
            st.markdown(f"**Strand:** {entry['Strand']}")
            if entry["Expectations"]:
                with st.expander("Student Expectations"):
                    for exp in entry["Expectations"]:
                        st.markdown(f"- {exp}")
    else:
        st.info("Start typing a TEKS code or keyword above to search.")
else:
    st.warning("Please upload a TEKS JSON file to begin.")
