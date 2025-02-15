# Malicious URL Processing ELT Pipeline

## Overview

This project focuses on building an **ELT (Extract, Load, Transform) pipeline** to process a CSV file containing malicious URLs. The pipeline consists of three main stages:

- **Extract**: Ingests the raw CSV file into the system.  
- **Load**: Stores the raw data in a structured database while maintaining data integrity. The raw data is then cleaned and validated for use in transformations.
- **Transform**: Applies various transformations, including parsing domains, extracting top-level domains (TLDs), counting character occurrences, filtering malicious records, and ranking domains based on severity.

## Highlights ✨

I used a bash script to act as the orchestration tool for this project. In a larger scale project I would use a tool like Airflow or Databricks Workflows.

I defined schemas in SQL files to enable schema version control, allowing for better tracking of changes over time. This makes it easier to monitor schema evolution and understand how modifications to tables might impact downstream processes. Additionally, explicitly defining schemas enhances data transparency for end users. By including column descriptions, users can better interpret the data model, reducing confusion and ensuring consistency in data usage. This is specifically useful when using a data warehouse that supports schema/column descriptions on the front end for end users.

I chose an ELT approach because it allows us to maintain raw data, which is crucial for ensuring data integrity, preventing data loss, and enhanceing flexibility for future use cases. If a transformation stage fails, we can re-run that stage without losing any data, ensuring a smooth and reliable pipeline. Additionally, having access to raw data enables easy auditing and validation. We can compare final transformed data against the original dataset to guarantee accuracy. Another key benefit is adaptability. End users often identify new analytical needs, and by retaining historical raw data, we can apply new transformations without requiring re-ingestion. This makes the ELT approach scalable, resilient, and future-proof for evolving business requirements.

## Setup & running the pipeline
### Prerequisites
- Python 3.8+
- Git Bash

The bash scirpt will install the python libraries required for the pipeline to run.

**To run the pipeline:**  
- Open Git Bash terminal  
- Navigate to the project directory:        `/BluebeamCodeProject` 
- Start the job by running this command:    `bash run.sh`

## Workflow Diagram
![alt text](diagrams/BluebeamProjectDiagram.jpeg)

## Testing 🧪
To ensure modules work correctly, I tested using:
1. **Direct Testing in the Module (`if __name__ == "__main__"`)**  
   - Each module includes a test block that allows it to be run directly for quick verification.

2. **Automated Testing with `pytest`**  
   - `pytest` was used to test multiple use cases, ensuring robustness across different scenarios.  
   - To run all tests, execute:  
     ```sh
     python -m pytest -v
     ```

## Languages & Libraries used
### **Languages**  
- 🐍 **Python**
- 📄 **SQL**
- 🐧 **Bash**

### **Python Libraries**  
- **pandas** – For handling CSV data and performing transformations.  
- **tldextract** – For extracting domains and top-level domains (TLDs).  
- **urllib3** - For extracting domains
- **python-whois** - For looking up domain owners
- **sqlite3** – For loading and storing data in a database.  

### **Database**  
- **SQLite** – For storing raw and processed data.  

### **Other Tools**  
- **Git** – Version control for managing the project.  