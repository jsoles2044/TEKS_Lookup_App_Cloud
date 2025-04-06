# # 📘 TEKS Lookup Tool

The **TEKS Lookup Tool** is a web-based application built with Streamlit that allows educators, administrators, and instructional coaches to search and view Texas Essential Knowledge and Skills (TEKS) standards from uploaded JSON files.

---

## 🚀 Features
- **Upload TEKS JSON** files generated from TEKS PDF documents
- **Search** by TEKS code or keyword
- **View full TEKS details**, including strand and student expectations
- **Grade and subject filters** for clarity and organization
- **Expandable sections** to keep the interface clean and user-friendly

---

## 🛠 How to Use

### 1. Clone or Download the Repository
```bash
git clone https://github.com/your-username/teks-lookup-app.git
cd teks-lookup-app
```

### 2. Install Requirements
Make sure you have Python 3.7+ installed.
```bash
pip install streamlit
```

### 3. Run the App
```bash
streamlit run teks_lookup_app.py
```

### 4. Upload a TEKS JSON File
- Use the TEKS PDF Extractor (included in this project) to convert TEKS PDFs to JSON.
- Upload your JSON file in the web interface.

### 5. Search & Filter
- Use the search bar to enter a TEKS code (e.g., `8.1A`) or keyword (e.g., `Revolution`).
- View results in an expandable format.

---

## 📂 JSON Format
Each JSON file should follow this structure:
```json
{
  "Grade 8": {
    "Social Studies": [
      {
        "Code": "8.1",
        "Strand": "History. The student understands...",
        "Expectations": [
          "(A) identify major eras...",
          "(B) explain the significance of..."
        ]
      },
      ...
    ]
  }
}
```

---

## 🌐 Deployment Options
- **Local**: Run from your machine using Streamlit
- **Streamlit Cloud**: Deploy online for public access
- **Intranet**: Host on a school or district server (Flask version optional)

---

## 📌 Ideal For:
- Walkthroughs and observations
- Instructional planning
- Teacher lesson alignment
- Curriculum team analysis

---

## 🙌 Contributing
Pull requests are welcome! If you'd like to add features such as multi-file search, CSV export, or deployment scripts, feel free to fork and contribute.

---

## 📄 License
MIT License

---

## ✉️ Contact
Developed by Alex (TEKS Tools Project)
For questions or suggestions, reach out via GitHub Issues or your school tech support team.

