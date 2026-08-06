import pandas as pd

# 1. Read raw Excel file
df = pd.read_excel("dmart_dataset.xlsx")

# 2. Handle Missing Values (Discount रिकामं असेल तर 0 fill कर)
df['Discount'] = df['Discount'].fillna(0)

# 3. Correct Data Types
# Quantity मध्ये text values → numeric
df['Quantity'] = df['Quantity'].replace({'two': 2})
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Date ला proper datetime format मध्ये convert कर
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 4. Standardization (spaces काढ, case uniform कर)
df['Store_Location'] = df['Store_Location'].str.strip().str.title()
df['Product_Category'] = df['Product_Category'].str.strip().str.title()
df['Product_Name'] = df['Product_Name'].str.strip().str.title()
df['Payment_Method'] = df['Payment_Method'].str.strip().str.title()

# 5. Outlier Handling (Discount > Gross Sales असेल तर cap करायचं नाही, फक्त flag करायचं)
df['Discount_Flag'] = df['Discount'] > (df['Quantity'] * df['Unit_Price'])

# 6. Remove Duplicates
df = df.drop_duplicates(subset=['Invoice_ID'])

# 7. Save cleaned data to new Excel file
df.to_excel("clean_invoice_data.xlsx", index=False)

print("✅ Cleaned Excel file saved as clean_invoice_data.xlsx")
