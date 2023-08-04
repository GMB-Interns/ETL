# **Anonymization: A Comprehensive Guide**
In data management and database administration, one of the key concerns is maintaining the privacy of sensitive data, while allowing for effective analytics and processing. This document provides a comprehensive overview of how we approached the process of data anonymization in our database.

## **1. Cloning the Database Instance**
To ensure data integrity and minimize potential risks, the first step in our process involved creating a clone of our original database instance. This clone, produced within the Google Cloud platform, serves as a sandbox for our data anonymization process, shielding our original data from any unintentional modification.

## **2. Connecting to the Cloned Instance**
After creating the cloned instance, we established a connection to it through Jupyter Notebook, an open-source tool that allows for interactive data science and scientific computing across various programming languages.

## **3. Identifying Sensitive Data Points**
To locate and isolate potentially sensitive data within our database, we executed an SQL query that searches for columns with specific names suggestive of personal data, such as 'first_name', 'last_name', 'phone', 'email', 'zipcode', and 'password'. This search is performed over all tables in the database.

## **4. Anonymizing Sensitive Data**
With the potentially sensitive data identified, the next step involved anonymizing these data points. Anonymization is the process of removing personally identifiable information from the data set, thus protecting individual privacy. Here are some of the techniques we used:

1. Substitution: This involves replacing a sensitive data field with a random but realistic equivalent. For instance, replacing 'John' under the 'first_name' column with 'User123'.

2. Redaction: This refers to the process of removing specific data. For instance, we can remove the last octet in IP addresses.

3. Generalization: This involves replacing specific data with more generic data. An example is replacing specific street addresses with generic ones like '123 Anonymized St'.

4. Pseudonymization: This technique involves replacing sensitive data with artificial identifiers. Although not a form of anonymization, pseudonymization can be used in combination with other techniques to protect sensitive data.

## **5. Creating a New, Anonymized Table**
To keep our original data intact, we copied the target table, anonymized the sensitive data points in this copied table, and then appended an '_anonymized' suffix to its name.

## **6. Adding the Anonymized Table to the Database**
Once the anonymization process was completed, we added the newly anonymized table to our cloned database. This enables us to work with non-sensitive data while maintaining the structure and relationships of the original data set. The anonymized data can be utilized for various purposes such as testing, analytics or machine learning where personal identifiable information is not required.

## **7. Original Table Removal (Future Step)**
Upon thorough verification of the accuracy and integrity of the anonymized data by the data management team (@Greg and others), we will proceed to drop the original tables containing sensitive data. This measure is part of our ongoing commitment to data privacy and security.

# **Key Anonymization Techniques:**
Substitution: Replacing a data field with a randomly generated equivalent.

***1.Suppression:*** Omitting the entire data field.

***2. Generalization:*** Replacing data with higher level, less specific data.

***3. Pseudonymization:*** Replacing sensitive data with artificial identifiers.

***4. Data Swapping / Shuffling / Permutation:*** Interchanging values between records.

***5. Data Masking:*** Replacing character data with characters such as x or *.

***6. Noise Addition:*** Injecting noise into numerical data to make it harder to deduce the original values.

# **Anonymization vs. De-identification vs. Pseudonymization:**
Anonymization: This is a data processing technique that removes or modifies personally identifiable information; anonymized data cannot be reversed or re-identified.

De-identification: Involves stripping data sets of all unique identifiers; though similar to anonymization, de-identified data carries more risk because it can potentially be re-identified through linkage with other data.

Pseudonymization: This is a data management strategy where personally identifiable information fields are replaced with artificial identifiers or pseudonyms, allowing the data to be linked back to the original data set under specific conditions.

