import streamlit as st
import json
import os

st.set_page_config(page_title="TEKS Lookup Tool", layout="wide")
st.title("📘 TEKS Lookup Tool")
st.markdown("Quickly search and view TEKS by code or keyword.")

# Load the index file
index_path = os.path.join(os.path.dirname(__file__), "teks_index.json")

try:
    with open(index_path, "r") as f:
        teks_index = json.load(f)
except FileNotFoundError:
    st.error("❌ Missing teks_index.json file. Please upload it alongside this app.")
    st.stop()

# Dropdown to select grade and subject
selection = st.selectbox("Choose Grade and Subject", list(teks_index.keys()))

# Load the corresponding JSON file
data_folder = os.path.join(os.path.dirname(__file__), "data")
selected_filename = teks_index[selection]
file_path = os.path.join(data_folder, selected_filename)

try:
    with open(file_path, "r") as f:
        teks_data = json.load(f)
except FileNotFoundError:
    st.error(f"❌ Could not find the file: {selected_filename} in the 'data' folder.")
    st.stop()

# Extract grade and subject from the file
grade = list(teks_data.keys())[0]
subject = list(teks_data[grade].keys())[0]
standards = teks_data[grade][subject]

st.subheader(f"Loaded: {grade} - {subject}")

# Grade and subject filters (editable)
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
