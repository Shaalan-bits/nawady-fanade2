# import streamlit as st
# from PIL import Image, ImageEnhance
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     # Convert to grayscale
#     image = image.convert("L")
#     # Enhance contrast
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     # Resize for better accuracy
#     image = image.resize((image.width * 2, image.height * 2))
#     return image


# def extract_information(text):
#     """Extract balance, reference number, and note from the OCR text output."""
#     # Initialize results
#     balance = None
#     reference_number = None
#     note = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)  # Match Arabic balance before "م6"
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)  # Match English balance
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")  # Remove commas for consistency
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")  # Remove commas for consistency

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)  # Match Arabic reference
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)  # Match English reference
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)  # Match Arabic note
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)  # Match English note
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     return balance, reference_number, note


# # Streamlit App
# st.title("Image Information Extractor")
# st.write("Upload an image to extract information.")

# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     st.text_area("Raw OCR Output", ocr_text)  # Display raw OCR output for debugging

#     # Extract information from OCR text
#     balance, reference_number, note = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")
###############################################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# from insert_data import insert_data
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     # Convert to grayscale
#     image = image.convert("L")
#     # Enhance contrast
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     # Resize for better accuracy
#     image = image.resize((image.width * 2, image.height * 2))
#     return image


# def extract_information(text):
#     """Extract balance, reference number, note, date, and time from the OCR text output."""
#     # Initialize results
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)  # Match Arabic balance before "م6"
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)  # Match English balance
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")  # Remove commas for consistency
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")  # Remove commas for consistency

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)  # Match Arabic reference
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)  # Match English reference
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)  # Match Arabic note
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)  # Match English note
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     # Extract date and time
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Streamlit App
# st.title("Image Information Extractor")
# st.write("Upload an image to extract information.")

# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     st.text_area("Raw OCR Output", ocr_text)  # Display raw OCR output for debugging

#     # Extract information from OCR text
#     balance, reference_number, note, date_time = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")

#     if date_time:
#         st.write(f"Date and Time: {date_time}")
#     else:
#         st.write("Date and Time not found.")

#     # Insert data into the database
#     if reference_number and balance and note and date_time:
#         try:
#             insert_data(reference_number, balance, note, date_time)
#             st.success("Data inserted successfully into the database.")
#         except Exception as e:
#             st.error(f"Error inserting data: {e}")
#################################################################################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# from insert_data import insert_data
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     # Convert to grayscale
#     image = image.convert("L")
#     # Enhance contrast
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     # Resize for better accuracy
#     image = image.resize((image.width * 2, image.height * 2))
#     return image


# def extract_information(text):
#     """Extract balance, reference number, note, date, and time from the OCR text output."""
#     # Initialize results
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)  # Match Arabic balance before "م6"
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)  # Match English balance
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")  # Remove commas for consistency
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")  # Remove commas for consistency

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)  # Match Arabic reference
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)  # Match English reference
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)  # Match Arabic note
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)  # Match English note
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     # Extract date and time
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Streamlit App
# st.title("Image Information Extractor")
# st.write("Upload an image to extract information.")

# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     st.text_area("Raw OCR Output", ocr_text)  # Display raw OCR output for debugging

#     # Extract information from OCR text
#     balance, reference_number, note, date_time = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")

#     if date_time:
#         st.write(f"Date and Time: {date_time}")
#     else:
#         st.write("Date and Time not found.")

#     # Insert data into the database
#     if reference_number and balance and note and date_time:
#         try:
#             # Log extracted values for debugging
#             st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#             insert_data(reference_number, balance, note, date_time)
#             st.success("Data inserted successfully into the database.")
#         except Exception as e:
#             st.error(f"Error inserting data: {e}")
##############################################################################################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# # Database Initialization
# def create_table():
#     """Create the database and transactions table if they don't exist."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Note TEXT,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()


# def insert_data(reference, amount, note, date_time):
#     """Insert data into the transactions table, handling duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Note, Date)
#         VALUES (?, ?, ?, ?)
#         """, (reference, amount, note, date_time))
#         conn.commit()
#         st.success(f"Data inserted successfully: Reference={reference}, Amount={amount}, Note={note}, Date={date_time}")
#     except sqlite3.IntegrityError:
#         st.error(f"Duplicate entry: Reference={reference} is already in the table.")
#     finally:
#         conn.close()


# # Preprocessing Function
# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     image = image.convert("L")  # Convert to grayscale
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)  # Enhance contrast
#     image = image.resize((image.width * 2, image.height * 2))  # Resize for better accuracy
#     return image


# # Information Extraction Function
# def extract_information(text):
#     """Extract balance, reference number, note, and date/time from OCR text."""
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     # Extract date and time
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Streamlit App
# st.title("نظام التحقق من انستا باي")
# st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

# # Ensure the database and table exist
# create_table()

# # File Upload
# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     st.text_area("Raw OCR Output", ocr_text)  # Debugging step to display raw OCR output

#     # Extract information
#     balance, reference_number, note, date_time = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")

#     if date_time:
#         st.write(f"Date and Time: {date_time}")
#     else:
#         st.write("Date and Time not found.")

#     # Insert data into the database
#     if reference_number and balance and note and date_time:
#         st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#         insert_data(reference_number, balance, note, date_time)
############################################################(Fully Working Functionality with few tweaks in the UI)#################################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# # Database Initialization
# def create_table():
#     """Create the database and transactions table if they don't exist."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Note TEXT NULL,  -- Allow NULL values
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()


# def insert_data(reference, amount, note, date_time):
#     """Insert data into the transactions table, handling duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         # Use a default value for Note if it's None
#         note = note if note is not None else "Not Available"

#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Note, Date)
#         VALUES (?, ?, ?, ?)
#         """, (reference, amount, note, date_time))
#         conn.commit()
#         st.success(f"Data inserted successfully: Reference={reference}, Amount={amount}, Note={note}, Date={date_time}")
#     except sqlite3.IntegrityError:
#         st.error(f"Duplicate entry: Reference={reference} is already in the table.")
#     finally:
#         conn.close()


# # Preprocessing Function
# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     image = image.convert("L")  # Convert to grayscale
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)  # Enhance contrast
#     image = image.resize((image.width * 2, image.height * 2))  # Resize for better accuracy
#     return image


# # Information Extraction Function
# def extract_information(text):
#     """Extract balance, reference number, note, and date/time from OCR text."""
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     # Extract date and time
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Streamlit App
# st.title("نظام التحقق من انستا باي")
# st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

# # Ensure the database and table exist
# create_table()

# # File Upload
# uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     st.text_area("Raw OCR Output", ocr_text)  # Debugging step to display raw OCR output

#     # Extract information
#     balance, reference_number, note, date_time = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")

#     if date_time:
#         st.write(f"Date and Time: {date_time}")
#     else:
#         st.write("Date and Time not found.")

#     # Insert data into the database
#     if reference_number and balance and date_time:
#         st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#         insert_data(reference_number, balance, note, date_time)
##################################################(Fully working with the UI tweaks)################################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# # Database Initialization
# def create_table():
#     """Create the database and transactions table if they don't exist."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Note TEXT NULL,  -- Allow NULL values
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()


# def insert_data(reference, amount, note, date_time):
#     """Insert data into the transactions table, handling duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         # Use a default value for Note if it's None
#         note = note if note is not None else "Not Available"

#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Note, Date)
#         VALUES (?, ?, ?, ?)
#         """, (reference, amount, note, date_time))
#         conn.commit()
#         st.success(f"Data inserted successfully: Reference={reference}, Amount={amount}, Note={note}, Date={date_time}")
#         st.image("Correct-removebg-preview.png", caption="Saved Successfully", use_column_width=True)
#     except sqlite3.IntegrityError:
#         st.error(f"Duplicate entry: Reference={reference} is already in the table.")
#         st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", use_column_width=True)
#     finally:
#         conn.close()


# # Preprocessing Function
# def preprocess_image(image):
#     """Preprocess the image for better OCR accuracy."""
#     image = image.convert("L")  # Convert to grayscale
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)  # Enhance contrast
#     image = image.resize((image.width * 2, image.height * 2))  # Resize for better accuracy
#     return image


# # Information Extraction Function
# def extract_information(text):
#     """Extract balance, reference number, note, and date/time from OCR text."""
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     # Extract balance
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Extract reference number
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Extract note
#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     # Extract date and time
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Streamlit App
# st.title("اهلا بك في نظام التحقق من تحويلات انستا باي التابع لادارة الفنادق والنوادي القوات المسلحة")
# st.write("برجاء تحميل الصورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

# # Ensure the database and table exist
# create_table()

# # File Upload
# uploaded_file = st.file_uploader("اختيار الصورة", type=["jpg", "jpeg", "png"])
# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="تحميل", use_column_width=True)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Extract OCR text
#     ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#     #st.text_area("Raw OCR Output", ocr_text)  # Debugging step to display raw OCR output

#     # Extract information
#     balance, reference_number, note, date_time = extract_information(ocr_text)

#     # Display results
#     if balance:
#         st.write(f"Balance: {balance}")
#     else:
#         st.write("Balance not found.")

#     if reference_number:
#         st.write(f"Reference Number: {reference_number}")
#     else:
#         st.write("Reference number not found.")

#     if note:
#         st.write(f"Note: {note}")
#     else:
#         st.write("Note not found.")

#     if date_time:
#         st.write(f"Date and Time: {date_time}")
#     else:
#         st.write("Date and Time not found.")

#     # Insert data into the database
#     if reference_number and balance and date_time:
#         st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#         insert_data(reference_number, balance, note, date_time)
######################################################################(Woring code with login page)########################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }


# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()


# # Function to insert data into the database
# def insert_data(reference, amount, note, date_time):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Note, Date)
#         VALUES (?, ?, ?, ?)
#         """, (reference, amount, note, date_time))
#         conn.commit()
#         st.success(f"Data inserted successfully: Reference={reference}, Amount={amount}, Note={note}, Date={date_time}")
#         st.image("Correct-removebg-preview.png", caption="Duplicate Entry", use_column_width=True)
#     except sqlite3.IntegrityError:
#         st.error(f"Duplicate entry: Reference={reference} is already in the table.")
#         st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", use_column_width=True)
#     finally:
#         conn.close()


# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image


# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")


# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_column_width=True)

#         # Preprocess the image
#         preprocessed_image = preprocess_image(image)

#         # Extract OCR text
#         ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#         #st.text_area("Raw OCR Output", ocr_text)

#         # Extract information
#         balance, reference_number, note, date_time = extract_information(ocr_text)

#         # Display results
#         if balance:
#             st.write(f"Balance: {balance}")
#         else:
#             st.write("Balance not found.")

#         if reference_number:
#             st.write(f"Reference Number: {reference_number}")
#         else:
#             st.write("Reference number not found.")

#         if note:
#             st.write(f"Note: {note}")
#         else:
#             st.write("Note not found.")

#         if date_time:
#             st.write(f"Date and Time: {date_time}")
#         else:
#             st.write("Date and Time not found.")

#         # Insert data into the database
#         if reference_number and balance and date_time:
#             st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#             insert_data(reference_number, balance, note, date_time)


# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()
###############################################(Updated UI/UX)###############################################################################
######################################################################(Working code with login page and improved UI)########################################
######################################################################(Working code with login page and improved UI)########################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }


# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()


# # Function to insert data into the database
# def insert_data(reference, amount, note, date_time):
#     """Insert data into the database and handle duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Note, Date)
#         VALUES (?, ?, ?, ?)
#         """, (reference, amount, note, date_time))
#         conn.commit()
#         st.success(f"Data inserted successfully: Reference={reference}, Amount={amount}, Note={note}, Date={date_time}")
#         # Display success image with reduced size
#         st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=200)
#     except sqlite3.IntegrityError:
#         st.error(f"Duplicate entry: Reference={reference} is already in the table.")
#         # Display error image with reduced size
#         st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=200)
#     finally:
#         conn.close()


# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image


# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     note = None
#     date_time = None

#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, note, date_time


# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")


# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         # Divide the page into two columns
#         col1, col2 = st.columns([1, 2])  # Adjust column proportions

#         with col1:
#             # Display the uploaded image in the smaller column
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_column_width=True)

#         with col2:
#             # Preprocess the image
#             preprocessed_image = preprocess_image(image)

#             # Extract OCR text
#             ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")

#             # Extract information
#             balance, reference_number, note, date_time = extract_information(ocr_text)

#             # Display extracted information in a compact layout
#             st.subheader("Extracted Information")
#             st.markdown(f"**Balance:** {balance if balance else 'Not found'}")
#             st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}")
#             st.markdown(f"**Note:** {note if note else 'Not found'}")
#             st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}")

#             # Insert data into the database
#             if reference_number and balance and date_time:
#                 #st.write(f"Attempting to insert: Reference={reference_number}, Amount={balance}, Note={note}, Date={date_time}")
#                 insert_data(reference_number, balance, note, date_time)


# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()
##########################################(UI Modifications based onn Ra2ed Yehia's orders)
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }

# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Phone_Number TEXT,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()

# # Function to insert data into the database
# def insert_data(reference, amount, phone_number, note, date_time):
#     """Insert data into the database and handle duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         phone_number = phone_number if phone_number else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date)
#         VALUES (?, ?, ?, ?, ?)
#         """, (reference, amount, phone_number, note, date_time))
#         conn.commit()
#         st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
#         st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=200)
#         st.markdown('</div>', unsafe_allow_html=True)
#     except sqlite3.IntegrityError:
#         st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
#         st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=200)
#         st.markdown('</div>', unsafe_allow_html=True)
#     finally:
#         conn.close()

# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image

# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     phone_number = None
#     note = None
#     date_time = None

#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
#     if phone_match:
#         phone_number = phone_match.group(0)

#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, phone_number, note, date_time

# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")

# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         # Divide the page into three columns
#         col1, col2, col3 = st.columns([1, 1, 2])  # Adjust column proportions

#         with col1:
#             st.subheader("Uploaded Image")
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Original Image", use_column_width=True)

#         with col2:
#             st.subheader("Preprocessed Image")
#             preprocessed_image = preprocess_image(image)
#             st.image(preprocessed_image, caption="Preprocessed Image", use_column_width=True)

#         with col3:
#             st.subheader("Extracted Information")
#             ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#             balance, reference_number, phone_number, note, date_time = extract_information(ocr_text)

#             st.markdown(f"**Balance:** {balance if balance else 'Not found'}")
#             st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}")
#             st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}")
#             st.markdown(f"**Note:** {note if note else 'Not found'}")
#             st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}")

#             if reference_number and balance and date_time:
#                 insert_data(reference_number, balance, phone_number, note, date_time)

# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()

# # Custom CSS to adjust layout and margins
# st.markdown(
#     """
#     <style>
#     .stApp {
#         padding-top: 0 !important;
#     }
#     .css-1v0mbdj {
#         margin-top: 0px !important;
#     }
#     .stButton>button {
#         margin-top: 10px !important;
#     }
#     .stFileUploader {
#         margin-top: 0px !important;
#     }
#     .stTextInput, .stTextArea {
#         margin-top: 0px !important;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )
###############################################################(Fully working with the Powered By added to the arabic note)#####################################################################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }

# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Phone_Number TEXT,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()

# # Function to insert data into the database
# def insert_data(reference, amount, phone_number, note, date_time):
#     """Insert data into the database and handle duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         phone_number = phone_number if phone_number else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date)
#         VALUES (?, ?, ?, ?, ?)
#         """, (reference, amount, phone_number, note, date_time))
#         conn.commit()
#         return True  # Return True for successful insertion
#     except sqlite3.IntegrityError:
#         return False  # Return False for duplicate entry
#     finally:
#         conn.close()

# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image

# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     phone_number = None
#     note = None
#     date_time = None

#     # Match for balance (English or Arabic)
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Match for reference number (English or Arabic)
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Match for phone number
#     phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
#     if phone_match:
#         phone_number = phone_match.group(0)

#     # Match for date and time (English or Arabic)
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     # Match for Note (English or Arabic)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if english_note_match:
#         note = english_note_match.group(1).strip()

#     # Capture the text in an array for Arabic "ملاحظة" handling
#     arr = text.split()
#     if "ملاحظة" in arr and not note:
#         note_index = arr.index("ملاحظة") + 1  # Get the next element after "ملاحظة"
#         if note_index < len(arr):
#             note = arr[note_index]
#         # Handle the case where the Note might have multiple words after "ملاحظة"
#         if note_index + 1 < len(arr):
#             note = " ".join(arr[note_index:])  # Join everything after "ملاحظة"

#     return balance, reference_number, phone_number, note, date_time

# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")

# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         # Divide the page into three columns with adjusted widths
#         col1, col2, col3 = st.columns([1, 1, 1])  # All columns equal width

#         with col1:
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_column_width=True)

#         with col2:
#             # Preprocess the image
#             preprocessed_image = preprocess_image(image)
            
#             # Extract OCR text using psm 6 (for English)
#             ocr_text_psm6 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#             st.text_area("OCR Output (psm 6)", ocr_text_psm6)
#             # Extract information using psm 6
#             balance, reference_number, phone_number, note, date_time = extract_information(ocr_text_psm6)

#             # Check if Note value is missing, if so, use psm 12 for Arabic extraction
#             if not note:
#                 # Run psm 12 to extract missing Note (Arabic)
#                 ocr_text_psm12 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 12")
#                 st.text_area("OCR Output (psm 12)", ocr_text_psm12)
#                 # Extract information using psm 12
#                 _, _, _, note, _ = extract_information(ocr_text_psm12)

#             # Insert data into the database and get success/fail result
#             insertion_success = False
#             if reference_number and balance and date_time:
#                 insertion_success = insert_data(reference_number, balance, phone_number, note, date_time)

#             # Display success or failure image
#             if insertion_success:
#                 st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=150)
#             else:
#                 st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=150)

#         with col3:
#             # Display extracted information with smaller text
#             st.subheader("Extracted Information")
#             st.markdown(f"**Balance:** {balance if balance else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Note:** {note if note else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}", unsafe_allow_html=True)

# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()


#########################(Full version without Note in arabic)###########################
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }

# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Phone_Number TEXT,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()

# # Function to insert data into the database
# def insert_data(reference, amount, phone_number, note, date_time):
#     """Insert data into the database and handle duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         phone_number = phone_number if phone_number else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date)
#         VALUES (?, ?, ?, ?, ?)
#         """, (reference, amount, phone_number, note, date_time))
#         conn.commit()
#         return True  # Return True for successful insertion
#     except sqlite3.IntegrityError:
#         return False  # Return False for duplicate entry
#     finally:
#         conn.close()

# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image

# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     phone_number = None
#     note = None
#     date_time = None

#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
#     if phone_match:
#         phone_number = phone_match.group(0)

#     arabic_note_match = re.search(r"‏ملاحظة\s*[\n:]*\s*(.+)", text)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if arabic_note_match:
#         note = arabic_note_match.group(1).strip()
#     elif english_note_match:
#         note = english_note_match.group(1).strip()

#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     return balance, reference_number, phone_number, note, date_time

# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")

# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         # Divide the page into three columns with adjusted widths
#         col1, col2, col3 = st.columns([1, 1, 1])  # All columns equal width

#         with col1:
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_column_width=True)

#         with col2:
#             # Preprocess the image
#             preprocessed_image = preprocess_image(image)
#             # Extract OCR text
#             ocr_text = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#             st.text_area("Raw OCR Output", ocr_text)
#             # Extract information
#             balance, reference_number, phone_number, note, date_time = extract_information(ocr_text)

#             # Insert data into the database and get success/fail result
#             insertion_success = False
#             if reference_number and balance and date_time:
#                 insertion_success = insert_data(reference_number, balance, phone_number, note, date_time)

#             # Display success or failure image
#             if insertion_success:
#                 st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=150)
#             else:
#                 st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=150)

#         with col3:
#             # Display extracted information with smaller text
#             st.subheader("Extracted Information")
#             st.markdown(f"**Balance:** {balance if balance else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Note:** {note if note else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}", unsafe_allow_html=True)

# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()
########################################Working Fully with all the languages, without remote sql connection
# import streamlit as st
# from PIL import Image, ImageEnhance
# import sqlite3
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Predefined email-password combinations
# VALID_CREDENTIALS = {
#     "shaalan@gmail.com": "123456",
#     "gen@gmail.com": "123456",
# }

# # Function to create the database and transactions table
# def create_table():
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Phone_Number TEXT,
#         Note TEXT NULL,
#         Date TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()

# # Function to insert data into the database
# def insert_data(reference, amount, phone_number, note, date_time):
#     """Insert data into the database and handle duplicate entries."""
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     try:
#         note = note if note is not None else "Not Available"
#         phone_number = phone_number if phone_number else "Not Available"
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date)
#         VALUES (?, ?, ?, ?, ?)
#         """, (reference, amount, phone_number, note, date_time))
#         conn.commit()
#         return True  # Return True for successful insertion
#     except sqlite3.IntegrityError:
#         return False  # Return False for duplicate entry
#     finally:
#         conn.close()

# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image

# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     phone_number = None
#     note = None
#     date_time = None

#     # Match for balance (English or Arabic)
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Match for reference number (English or Arabic)
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Match for phone number
#     phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
#     if phone_match:
#         phone_number = phone_match.group(0)

#     # Match for date and time (English or Arabic)
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     # Match for Note (English or Arabic)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if english_note_match:
#         note = english_note_match.group(1).strip()

#     # Capture the text in an array for Arabic "ملاحظة" handling
#     arr = text.split()
#     if "ملاحظة" in arr and not note:
#         note_index = arr.index("ملاحظة") + 1  # Get the next element after "ملاحظة"
#         if note_index < len(arr):
#             note = arr[note_index]
#         # Handle the case where the Note might have multiple words after "ملاحظة"
#         if note_index + 1 < len(arr):
#             note = " ".join(arr[note_index:])  # Join everything after "ملاحظة"

#     # Remove unwanted part from the Arabic note
#     if note and "POWERED BY" in note:
#         note = note.replace("POWERED BY", "").strip()

#     return balance, reference_number, phone_number, note, date_time

# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if email in VALID_CREDENTIALS and VALID_CREDENTIALS[email] == password:
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")

# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         # Divide the page into three columns with adjusted widths
#         col1, col2, col3 = st.columns([1, 1, 1])  # All columns equal width

#         with col1:
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Uploaded Image", use_column_width=True)

#         with col2:
#             # Preprocess the image
#             preprocessed_image = preprocess_image(image)
            
#             # Extract OCR text using psm 6 (for English)
#             ocr_text_psm6 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#             #st.text_area("OCR Output (psm 6)", ocr_text_psm6)
#             # Extract information using psm 6
#             balance, reference_number, phone_number, note, date_time = extract_information(ocr_text_psm6)

#             # Check if Note value is missing, if so, use psm 12 for Arabic extraction
#             if not note:
#                 # Run psm 12 to extract missing Note (Arabic)
#                 ocr_text_psm12 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 12")
#                 #st.text_area("OCR Output (psm 12)", ocr_text_psm12)
#                 # Extract information using psm 12
#                 _, _, _, note, _ = extract_information(ocr_text_psm12)

#             # Insert data into the database and get success/fail result
#             insertion_success = False
#             if reference_number and balance and date_time:
#                 insertion_success = insert_data(reference_number, balance, phone_number, note, date_time)

#             # Display success or failure image
#             if insertion_success:
#                 st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=150)
#             else:
#                 st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=150)

#         with col3:
#             # Display extracted information with smaller text
#             st.subheader("Extracted Information")
#             st.markdown(f"**Balance:** {balance if balance else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Note:** {note if note else 'Not found'}", unsafe_allow_html=True)
#             st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}", unsafe_allow_html=True)

# # Run the app
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     login()
# else:
#     app()
#################################(SQL Transfer and online connection and insertion fully working)
# import mysql.connector
# import streamlit as st
# from PIL import Image, ImageEnhance
# import pytesseract
# import re

# # Configure Tesseract executable if needed (Windows setup)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Function to connect to MySQL database
# def connect_db():
#     return mysql.connector.connect(
#         host='mysql-satellite.alwaysdata.net',
#         user='satellite',
#         password='Waw.com1',
#         database='satellite_db'
#     )

# # Function to check user login credentials
# def check_login(email, password):
#     try:
#         conn = connect_db()
#         cursor = conn.cursor()

#         # Check if the user exists with the provided email and password
#         cursor.execute("SELECT * FROM users WHERE Email = %s AND Password = %s", (email, password))
#         user = cursor.fetchone()

#         cursor.close()
#         conn.close()

#         if user:
#             return True  # User is authenticated
#         else:
#             return False  # Authentication failed
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return False

# # Function to create the database and transactions table (online)
# def create_table():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         Reference TEXT PRIMARY KEY,
#         Amount REAL,
#         Phone_Number TEXT,
#         Note TEXT NULL,
#         Date_Time TEXT,
#         User_Comments TEXT
#     )
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Function to insert data into the database
# def insert_data(reference, amount, phone_number, note, date_time, user_comments):
#     try:
#         conn = connect_db()
#         cursor = conn.cursor()
        
#         # Insert data into the transactions table
#         cursor.execute("""
#         INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date_Time, User_Comments)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """, (reference, amount, phone_number, note, date_time, user_comments))
#         conn.commit()

#         cursor.close()
#         conn.close()
#         return True
#     except mysql.connector.Error as err:
#         print(f"Error inserting data: {err}")
#         return False

# # Preprocessing function for images
# def preprocess_image(image):
#     image = image.convert("L")
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)
#     image = image.resize((image.width * 2, image.height * 2))
#     return image

# # Function to extract information from OCR text
# def extract_information(text):
#     balance = None
#     reference_number = None
#     phone_number = None
#     note = None
#     date_time = None

#     # Match for balance (English or Arabic)
#     arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
#     english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
#     if arabic_balance_match:
#         balance = arabic_balance_match.group(1).replace(",", "")
#     elif english_balance_match:
#         balance = english_balance_match.group(1).replace(",", "")

#     # Match for reference number (English or Arabic)
#     arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
#     english_reference_match = re.search(r"Reference\s*(\d+)", text)
#     if arabic_reference_match:
#         reference_number = arabic_reference_match.group(1)
#     elif english_reference_match:
#         reference_number = english_reference_match.group(1)

#     # Match for phone number
#     phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
#     if phone_match:
#         phone_number = phone_match.group(0)

#     # Match for date and time (English or Arabic)
#     arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
#     english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
#     if arabic_date_time_match:
#         date_time = arabic_date_time_match.group(1)
#     elif english_date_time_match:
#         date_time = english_date_time_match.group(1)

#     # Match for Note (English or Arabic)
#     english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
#     if english_note_match:
#         note = english_note_match.group(1).strip()

#     # Capture the text in an array for Arabic "ملاحظة" handling
#     arr = text.split()
#     if "ملاحظة" in arr and not note:
#         note_index = arr.index("ملاحظة") + 1  # Get the next element after "ملاحظة"
#         if note_index < len(arr):
#             note = arr[note_index]
#         # Handle the case where the Note might have multiple words after "ملاحظة"
#         if note_index + 1 < len(arr):
#             note = " ".join(arr[note_index:])  # Join everything after "ملاحظة"

#     # Remove unwanted part from the Arabic note
#     if note and "POWERED BY" in note:
#         note = note.replace("POWERED BY", "").strip()

#     return balance, reference_number, phone_number, note, date_time

# # Login Functionality
# def login():
#     st.title("Login Page")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if check_login(email, password):
#             st.success("Login successful!")
#             st.session_state["logged_in"] = True
#             st.experimental_rerun()  # Trigger a rerun after setting login status
#         else:
#             st.error("Invalid email or password.")

# # Main App Functionality
# def app():
#     st.title("نظام التحقق من انستا باي")
#     st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

#     # Ensure the database and table exist
#     create_table()

#     # File Upload
#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
#     if uploaded_file:
#         # Divide the page into three columns with adjusted widths
#         col1, col2, col3 = st.columns([1, 1, 1])  # All columns equal width

#         with col1:
#             st.write("")  # Placeholder

#         with col2:
#             # Display extracted information
#             st.subheader("Extracted Information")
#             if uploaded_file:
#                 image = Image.open(uploaded_file)
#                 preprocessed_image = preprocess_image(image)

#                 # Extract OCR text using psm 6 (for English)
#                 ocr_text_psm6 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
#                 # Extract information using psm 6
#                 balance, reference_number, phone_number, note, date_time = extract_information(ocr_text_psm6)

#                 # Check if Note value is missing, if so, use psm 12 for Arabic extraction
#                 if not note:
#                     # Run psm 12 to extract missing Note (Arabic)
#                     ocr_text_psm12 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 12")
#                     # Extract information using psm 12
#                     _, _, _, note, _ = extract_information(ocr_text_psm12)

#                 # Display extracted data in col2
#                 st.markdown(f"**Balance:** {balance if balance else 'Not found'}", unsafe_allow_html=True)
#                 st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}", unsafe_allow_html=True)
#                 st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}", unsafe_allow_html=True)
#                 st.markdown(f"**Note:** {note if note else 'Not found'}", unsafe_allow_html=True)
#                 st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}", unsafe_allow_html=True)

#         with col3:
#             # Display image and comment box
#             st.image(image, caption="Uploaded Image", use_column_width=True)
#             user_comments = st.text_area("Your Comments", placeholder="Write your comments here...")

#             # Add a submit button to insert data
#             submit_button = st.button("Submit")

#             if submit_button:
#                 # Insert data only if the submit button is pressed
#                 if reference_number and balance and date_time:
#                     insertion_success = insert_data(reference_number, balance, phone_number, note, date_time, user_comments)
#                     if insertion_success:
#                         st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=150)
#                     else:
#                         st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry", width=150)
#                 else:
#                     st.error("Please make sure all required fields are extracted and filled.")

# if __name__ == "__main__":
#     if "logged_in" not in st.session_state:
#         st.session_state["logged_in"] = False

#     if not st.session_state["logged_in"]:
#         login()
#     else:
#         app()
###############################################(UI Modifications)#################################################################
import mysql.connector
import streamlit as st
from PIL import Image, ImageEnhance
import pytesseract
import re

# Configure Tesseract executable if needed (Windows setup)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host='mysql-satellite.alwaysdata.net',
        user='satellite',
        password='Waw.com1',
        database='satellite_db'
    )

# Function to check user login credentials
def check_login(email, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Check if the user exists with the provided email and password
        cursor.execute("SELECT * FROM users WHERE Email = %s AND Password = %s", (email, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            return True  # User is authenticated
        else:
            return False  # Authentication failed
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Function to create the database and transactions table (online)
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        Reference TEXT PRIMARY KEY,
        Amount REAL,
        Phone_Number TEXT,
        Note TEXT NULL,
        Date_Time TEXT,
        User_Comments TEXT
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Function to insert data into the database
def insert_data(reference, amount, phone_number, note, date_time, user_comments):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Insert data into the transactions table
        cursor.execute("""
        INSERT INTO transactions (Reference, Amount, Phone_Number, Note, Date_Time, User_Comments)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (reference, amount, phone_number, note, date_time, user_comments))
        conn.commit()

        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
        return False

# Preprocessing function for images
def preprocess_image(image):
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    image = image.resize((image.width * 2, image.height * 2))
    return image

# Function to extract information from OCR text
def extract_information(text):
    balance = None
    reference_number = None
    phone_number = None
    note = None
    date_time = None

    # Match for balance (English or Arabic)
    arabic_balance_match = re.search(r"([\d,]+)\s*‏م6‎", text)
    english_balance_match = re.search(r"([\d,]+)\s*Transfer Amount", text)
    if arabic_balance_match:
        balance = arabic_balance_match.group(1).replace(",", "")
    elif english_balance_match:
        balance = english_balance_match.group(1).replace(",", "")

    # Match for reference number (English or Arabic)
    arabic_reference_match = re.search(r"(\d+)\s*‏المرجع‎", text)
    english_reference_match = re.search(r"Reference\s*(\d+)", text)
    if arabic_reference_match:
        reference_number = arabic_reference_match.group(1)
    elif english_reference_match:
        reference_number = english_reference_match.group(1)

    # Match for phone number
    phone_match = re.search(r"(011\d{8}|012\d{8}|010\d{8}|015\d{8})", text)
    if phone_match:
        phone_number = phone_match.group(0)

    # Match for date and time (English or Arabic)
    arabic_date_time_match = re.search(r"(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)\s*‏التاريخ:‎", text)
    english_date_time_match = re.search(r"Date:\s*(\d{1,2}\s+\w+\s+\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)", text)
    if arabic_date_time_match:
        date_time = arabic_date_time_match.group(1)
    elif english_date_time_match:
        date_time = english_date_time_match.group(1)

    # Match for Note (English or Arabic)
    english_note_match = re.search(r"Note\s*[\n:]*\s*(.+)", text)
    if english_note_match:
        note = english_note_match.group(1).strip()

    # Capture the text in an array for Arabic "ملاحظة" handling
    arr = text.split()
    if "ملاحظة" in arr and not note:
        note_index = arr.index("ملاحظة") + 1  # Get the next element after "ملاحظة"
        if note_index < len(arr):
            note = arr[note_index]
        # Handle the case where the Note might have multiple words after "ملاحظة"
        if note_index + 1 < len(arr):
            note = " ".join(arr[note_index:])  # Join everything after "ملاحظة"

    # Remove unwanted part from the Arabic note
    if note and "POWERED BY" in note:
        note = note.replace("POWERED BY", "").strip()

    return balance, reference_number, phone_number, note, date_time

# Login Functionality
def login():
    st.title("Login Page")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(email, password):
            st.success("Login successful!")
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Trigger a rerun after setting login status
        else:
            st.error("Invalid email or password.")

# Main App Functionality
def app():
    st.title("نظام التحقق من انستا باي")
    st.write("قم بتحميل صورة لاستخراج المعلومات وتخزينها في قاعدة البيانات")

    # Ensure the database and table exist
    create_table()

    # File Upload
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        # Divide the page into three columns with adjusted widths
        col1, col2, col3 = st.columns([1, 1, 1])  # All columns equal width

        with col1:
            st.write("")  # Placeholder for the first column
            user_comments = st.text_area("Your Comments", placeholder="Write your comments here...")
            submit_button = st.button("Submit")

            # Display the image under the submit button in col1
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)

        with col2:
            # Display extracted information in col2
            st.subheader("Extracted Information")
            if uploaded_file:
                image = Image.open(uploaded_file)
                preprocessed_image = preprocess_image(image)

                # Extract OCR text using psm 6 (for English)
                ocr_text_psm6 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 6")
                # Extract information using psm 6
                balance, reference_number, phone_number, note, date_time = extract_information(ocr_text_psm6)

                # Check if Note value is missing, if so, use psm 12 for Arabic extraction
                if not note:
                    # Run psm 12 to extract missing Note (Arabic)
                    ocr_text_psm12 = pytesseract.image_to_string(preprocessed_image, lang="ara+eng", config="--psm 12")
                    # Extract information using psm 12
                    _, _, _, note, _ = extract_information(ocr_text_psm12)

                # Display extracted data in col2
                st.markdown(f"**Balance:** {balance if balance else 'Not found'}", unsafe_allow_html=True)
                st.markdown(f"**Reference Number:** {reference_number if reference_number else 'Not found'}", unsafe_allow_html=True)
                st.markdown(f"**Phone Number:** {phone_number if phone_number else 'Not found'}", unsafe_allow_html=True)
                st.markdown(f"**Note:** {note if note else 'Not found'}", unsafe_allow_html=True)
                st.markdown(f"**Date and Time:** {date_time if date_time else 'Not found'}", unsafe_allow_html=True)

        with col3:
            # Image to be shown in col3 after submission
            if submit_button:
                # Insert data only if the submit button is pressed
                if reference_number and balance and date_time:
                    insertion_success = insert_data(reference_number, balance, phone_number, note, date_time, user_comments)
                    if insertion_success:
                        st.image("Correct-removebg-preview.png", caption="Insertion Successful", width=150)
                    else:
                        st.image("Incorrect-removebg-preview.png", caption="Duplicate Entry or Error", width=150)

# Run the app
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    login()
else:
    app()
