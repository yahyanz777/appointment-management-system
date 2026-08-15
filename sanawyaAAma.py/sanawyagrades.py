# import pandas as pd
# import re

# def normalize_arabic(text: str) -> str:
#     """Normalizes Arabic letters for flexible searching."""
#     if not isinstance(text, str):
#         return ""
#     text = re.sub(r"[أإآ]", "ا", text)
#     text = text.replace("ى", "ي").replace("ة", "ه")
#     return text

# def search_student_results(file_path: str):
#     try:
#         print("Loading Excel data, please wait...")
#         df = pd.read_excel(file_path)
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return
#     except Exception as e:
#         print(f"Error loading file: {e}")
#         return

#     # Create a normalized column for searching while keeping original names intact
#     df['normalized_name'] = df['arabic_name'].apply(normalize_arabic)

#     while True:
#         search_query = input("\nEnter student name to search (or type 'exit' to quit): ").strip()
        
#         if search_query.lower() in ['exit', 'quit']:
#             print("Exiting search script.")
#             break

#         if not search_query:
#             print("Please enter a valid search term.")
#             continue

#         normalized_query = normalize_arabic(search_query)

#         # Filter matches using substring match on normalized names
#         matches = df[df['normalized_name'].str.contains(normalized_query, na=False)]

#         if matches.empty:
#             print(f"No results found for '{search_query}'.")
#         else:
#             print(f"\nFound {len(matches)} matching student(s) for '{search_query}':\n")
            
#             # Extract and format the columns from your Excel file
#             results = matches[['seating_no', 'arabic_name', 'total_degree', 'student_case_desc']]
#             results = results.rename(columns={
#                 'seating_no': 'رقم الجلوس',
#                 'arabic_name': 'اسم الطالب',
#                 'total_degree': 'المجموع',
#                 'student_case_desc': 'الحالة'
#             })
            
#             print(results.to_string(index=False))

# if __name__ == "__main__":
#     # Make sure this Excel file is in the same folder as sanawyaAAma.py
#     EXCEL_FILE = "نتيجة ثانوية عامة نظام حديث.xlsx"
#     search_student_results(EXCEL_FILE)
import os
import sys
import re
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    """Reshapes Arabic characters and reverses direction for LTR terminals."""
    if not isinstance(text, str):
        return str(text)
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def normalize_arabic(text: str) -> str:
    """Normalizes Arabic letters for flexible search matching."""
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[أإآ]", "ا", text)
    text = text.replace("ى", "ي").replace("ة", "ه")
    return text

def search_student_results(file_path: str):
    if not os.path.exists(file_path):
        print("❌ Error: Excel file not found!")
        print(f"Expected file at: {file_path}")
        return

    try:
        print("Loading Excel data, please wait...")
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return

    # Normalize Arabic names for smooth searching
    df['normalized_name'] = df['arabic_name'].apply(normalize_arabic)
    print("✅ File loaded successfully!\n")

    while True:
        search_query = input("Enter student name to search (or 'exit' to quit): ").strip()
        
        if search_query.lower() in ['exit', 'quit']:
            print("Exiting search script.")
            break

        if not search_query:
            print("Please enter a valid search term.\n")
            continue

        normalized_query = normalize_arabic(search_query)

        # Filter matching students
        matches = df[df['normalized_name'].str.contains(normalized_query, na=False)]

        if matches.empty:
            print(f"❌ No results found for '{fix_arabic(search_query)}'.\n")
        else:
            print(f"\n──────────────────────────────────────────────")
            print(f" Found {len(matches)} matching student(s) for '{fix_arabic(search_query)}':")
            print(f"──────────────────────────────────────────────")
            
            # Print each result with fixed Arabic rendering
            for _, row in matches.iterrows():
                print(f"• {fix_arabic('رقم الجلوس')} : {row['seating_no']}")
                print(f"  {fix_arabic('اسم الطالب')} : {fix_arabic(str(row['arabic_name']))}")
                print(f"  {fix_arabic('المجموع')}    : {row['total_degree']}")
                print(f"  {fix_arabic('الحالة')}      : {fix_arabic(str(row['student_case_desc']))}")
                print("─" * 46)
            print()

if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    EXCEL_FILE = os.path.join(SCRIPT_DIR, "نتيجة ثانوية عامة نظام حديث.xlsx")
    
    search_student_results(EXCEL_FILE)