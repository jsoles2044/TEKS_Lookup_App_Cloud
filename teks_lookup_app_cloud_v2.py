import json
import os
import streamlit as st

# Load the index file
index_path = os.path.join(os.path.dirname(__file__), "teks_index.json")

try:
    with open(index_path, "r", encoding="utf-8") as f:
        teks_index = json.load(f)
except FileNotFoundError:
    st.error("❌ teks_index.json not found. Please make sure it is in the same folder as this app.")
    st.stop()

# Let user select from a readable list of grade + subject
selection = st.selectbox("📚 Choose Grade and Subject", list(teks_index.keys()))
selected_filename = teks_index[selection]

# Load the corresponding JSON file
data_folder = os.path.join(os.path.dirname(__file__), "data")
file_path = os.path.join(data_folder, selected_filename)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        teks_data = json.load(f)
except FileNotFoundError:
    st.error(f"❌ Could not find the file: {selected_filename} in the 'data' folder.")
    st.stop()

# Extract grade and subject from the file
grade = list(teks_data.keys())[0]
subject = list(teks_data[grade].keys())[0]
standards = teks_data[grade][subject]

st.subheader(f"📘 {grade} - {subject} TEKS")

# Editable filters
grade_filter = st.text_input("Filter by Grade (e.g., Grade 8)", value=grade)
subject_filter = st.text_input("Filter by Subject (e.g., English Language Arts)", value=subject)

# Search bar
query = st.text_input("🔎 Search by TEKS code or keyword", placeholder="e.g., 8.1A or Constitution")

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
