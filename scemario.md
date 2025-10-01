Here's the content formatted as a GitHub-ready markdown file:

```markdown
# 🏗️ Very Big Flat Tables for Data Modeling Practice

Here are **VERY BIG flat tables** with 20+ columns for complex data modeling practice. These tables contain intentional normalization violations and complex relationships perfect for learning database design.

---

## 🔹 1. **Mega Corporate HR Management Base Table** (25 columns)

```sql
CREATE TABLE mega_hr_base (
    employee_id           NUMBER,
    employee_ssn          VARCHAR2(20),
    first_name            VARCHAR2(50),
    last_name             VARCHAR2(50),
    birth_date            DATE,
    gender                VARCHAR2(10),
    personal_email        VARCHAR2(100),
    work_email            VARCHAR2(100),
    phone_number          VARCHAR2(20),
    hire_date             DATE,
    termination_date      DATE,
    job_id                NUMBER,
    job_title             VARCHAR2(100),
    department_id         NUMBER,
    department_name       VARCHAR2(100),
    manager_id            NUMBER,
    manager_name          VARCHAR2(100),
    salary                NUMBER(10,2),
    bonus                 NUMBER(10,2),
    commission_pct        NUMBER(5,2),
    address_line1         VARCHAR2(200),
    address_line2         VARCHAR2(200),
    city                  VARCHAR2(50),
    state                 VARCHAR2(50),
    zip_code              VARCHAR2(20),
    country               VARCHAR2(50),
    emergency_contact     VARCHAR2(100),
    emergency_phone       VARCHAR2(20),
    skills                VARCHAR2(500),  -- Comma-separated (violates 1NF)
    project_ids           VARCHAR2(200),  -- Comma-separated (violates 1NF)
    performance_rating    NUMBER(3,1),
    vacation_days_used    NUMBER,
    vacation_days_total   NUMBER
);
```

---

## 🔹 2. **Enterprise Hospital Management Base Table** (28 columns)

```sql
CREATE TABLE mega_hospital_base (
    patient_id            NUMBER,
    patient_ssn           VARCHAR2(20),
    patient_first_name    VARCHAR2(50),
    patient_last_name     VARCHAR2(50),
    patient_dob           DATE,
    patient_gender        VARCHAR2(10),
    patient_phone         VARCHAR2(20),
    patient_email         VARCHAR2(100),
    patient_address       VARCHAR2(300),
    patient_insurance_id  VARCHAR2(50),
    insurance_company     VARCHAR2(100),
    doctor_id             NUMBER,
    doctor_first_name     VARCHAR2(50),
    doctor_last_name      VARCHAR2(50),
    doctor_specialty      VARCHAR2(100),
    doctor_phone          VARCHAR2(20),
    department_id         NUMBER,
    department_name       VARCHAR2(100),
    appointment_id        NUMBER,
    appointment_date      DATE,
    appointment_type      VARCHAR2(50),
    diagnosis             VARCHAR2(500),
    prescription_id       NUMBER,
    medication_name       VARCHAR2(100),
    dosage                VARCHAR2(50),
    frequency             VARCHAR2(50),
    lab_test_id           NUMBER,
    test_name             VARCHAR2(100),
    test_result           VARCHAR2(200),
    bill_id               NUMBER,
    bill_amount           NUMBER(10,2),
    payment_status        VARCHAR2(20),
    admission_date        DATE,
    discharge_date        DATE,
    room_number           VARCHAR2(20),
    bed_number            VARCHAR2(10)
);
```

---

## 🔹 3. **Global E-commerce Platform Base Table** (30 columns)

```sql
CREATE TABLE mega_ecommerce_base (
    order_id              NUMBER,
    order_date            DATE,
    order_status          VARCHAR2(50),
    customer_id           NUMBER,
    customer_first_name   VARCHAR2(50),
    customer_last_name    VARCHAR2(50),
    customer_email        VARCHAR2(100),
    customer_phone        VARCHAR2(20),
    customer_address1     VARCHAR2(200),
    customer_address2     VARCHAR2(200),
    customer_city         VARCHAR2(50),
    customer_state        VARCHAR2(50),
    customer_zip          VARCHAR2(20),
    customer_country      VARCHAR2(50),
    shipping_address1     VARCHAR2(200),
    shipping_address2     VARCHAR2(200),
    shipping_city         VARCHAR2(50),
    shipping_state        VARCHAR2(50),
    shipping_zip          VARCHAR2(20),
    shipping_country      VARCHAR2(50),
    product_id            NUMBER,
    product_name          VARCHAR2(200),
    product_category      VARCHAR2(100),
    product_subcategory   VARCHAR2(100),
    brand_name            VARCHAR2(100),
    supplier_id           NUMBER,
    supplier_name         VARCHAR2(100),
    quantity              NUMBER,
    unit_price            NUMBER(10,2),
    discount_pct          NUMBER(5,2),
    tax_amount            NUMBER(10,2),
    shipping_cost         NUMBER(10,2),
    total_amount          NUMBER(10,2),
    payment_method        VARCHAR2(50),
    payment_status        VARCHAR2(50),
    shipping_method       VARCHAR2(100),
    tracking_number       VARCHAR2(100),
    warehouse_id          NUMBER,
    warehouse_location    VARCHAR2(100)
);
```

---

## 🔹 4. **University Management System Base Table** (32 columns)

```sql
CREATE TABLE mega_university_base (
    student_id            NUMBER,
    student_ssn           VARCHAR2(20),
    student_first_name    VARCHAR2(50),
    student_last_name     VARCHAR2(50),
    student_dob           DATE,
    student_gender        VARCHAR2(10),
    student_email         VARCHAR2(100),
    student_phone         VARCHAR2(20),
    student_address       VARCHAR2(300),
    student_city          VARCHAR2(50),
    student_state         VARCHAR2(50),
    student_zip           VARCHAR2(20),
    major_id              NUMBER,
    major_name            VARCHAR2(100),
    department_id         NUMBER,
    department_name       VARCHAR2(100),
    college_id            NUMBER,
    college_name          VARCHAR2(100),
    advisor_id            NUMBER,
    advisor_name          VARCHAR2(100),
    course_id             NUMBER,
    course_code           VARCHAR2(20),
    course_name           VARCHAR2(200),
    course_credits        NUMBER,
    professor_id          NUMBER,
    professor_name        VARCHAR2(100),
    professor_email       VARCHAR2(100),
    semester_id           NUMBER,
    semester_name         VARCHAR2(50),
    academic_year         NUMBER,
    enrollment_date       DATE,
    grade                 VARCHAR2(5),
    gpa                   NUMBER(3,2),
    tuition_amount        NUMBER(10,2),
    scholarship_amount    NUMBER(10,2),
    financial_aid_amount  NUMBER(10,2),
    payment_status        VARCHAR2(20),
    dorm_id               NUMBER,
    dorm_name             VARCHAR2(100),
    room_number           VARCHAR2(20),
    campus_location       VARCHAR2(100)
);
```

---

## 🔹 5. **Banking & Financial Services Base Table** (35 columns)

```sql
CREATE TABLE mega_banking_base (
    transaction_id        NUMBER,
    transaction_date      DATE,
    transaction_time      TIMESTAMP,
    transaction_type      VARCHAR2(50),
    transaction_amount    NUMBER(15,2),
    account_id            NUMBER,
    account_number        VARCHAR2(50),
    account_type          VARCHAR2(50),
    account_open_date     DATE,
    account_balance       NUMBER(15,2),
    customer_id           NUMBER,
    customer_ssn          VARCHAR2(20),
    customer_first_name   VARCHAR2(50),
    customer_last_name    VARCHAR2(50),
    customer_dob          DATE,
    customer_email        VARCHAR2(100),
    customer_phone        VARCHAR2(20),
    customer_address      VARCHAR2(300),
    customer_city         VARCHAR2(50),
    customer_state        VARCHAR2(50),
    customer_zip          VARCHAR2(20),
    branch_id             NUMBER,
    branch_name           VARCHAR2(100),
    branch_address        VARCHAR2(300),
    branch_city           VARCHAR2(50),
    branch_state          VARCHAR2(50),
    branch_phone          VARCHAR2(20),
    employee_id           NUMBER,
    employee_name         VARCHAR2(100),
    employee_role         VARCHAR2(100),
    loan_id               NUMBER,
    loan_type             VARCHAR2(50),
    loan_amount           NUMBER(15,2),
    interest_rate         NUMBER(5,3),
    loan_status           VARCHAR2(50),
    credit_card_id        NUMBER,
    credit_card_limit     NUMBER(10,2),
    credit_card_balance   NUMBER(10,2),
    merchant_name         VARCHAR2(100),
    merchant_category     VARCHAR2(100)
);
```

---

## 🔹 6. **Supply Chain & Logistics Base Table** (40 columns)

```sql
CREATE TABLE mega_supplychain_base (
    shipment_id           NUMBER,
    shipment_date         DATE,
    estimated_arrival     DATE,
    actual_arrival        DATE,
    shipment_status       VARCHAR2(50),
    tracking_number       VARCHAR2(100),
    carrier_id            NUMBER,
    carrier_name          VARCHAR2(100),
    carrier_phone         VARCHAR2(20),
    vehicle_id            NUMBER,
    vehicle_type          VARCHAR2(50),
    driver_id             NUMBER,
    driver_name           VARCHAR2(100),
    driver_phone          VARCHAR2(20),
    supplier_id           NUMBER,
    supplier_name         VARCHAR2(100),
    supplier_address      VARCHAR2(300),
    supplier_city         VARCHAR2(50),
    supplier_country      VARCHAR2(50),
    supplier_phone        VARCHAR2(20),
    manufacturer_id       NUMBER,
    manufacturer_name     VARCHAR2(100),
    product_id            NUMBER,
    product_name          VARCHAR2(200),
    product_category      VARCHAR2(100),
    product_weight        NUMBER(10,2),
    product_dimensions    VARCHAR2(100),
    quantity              NUMBER,
    unit_cost             NUMBER(10,2),
    total_cost            NUMBER(15,2),
    warehouse_id          NUMBER,
    warehouse_name        VARCHAR2(100),
    warehouse_address     VARCHAR2(300),
    warehouse_city        VARCHAR2(50),
    warehouse_country     VARCHAR2(50),
    inventory_level       NUMBER,
    reorder_point         NUMBER,
    retailer_id           NUMBER,
    retailer_name         VARCHAR2(100),
    retailer_address      VARCHAR2(300),
    purchase_order_id     NUMBER,
    order_date            DATE,
    customs_status        VARCHAR2(50),
    import_tax            NUMBER(10,2)
);
```

---

## 🎯 Why These Are Perfect for Practice

- **Multiple 1NF violations** (repeating groups, comma-separated values)
- **Complex functional dependencies**
- **Multiple many-to-many relationships**
- **Various data types and constraints**
- **Real-world business scenarios**
- **Multiple normalization levels required**

---

## 🚀 Next Steps

Pick any table and practice:

1. **Analyze functional dependencies**
2. **Normalize to 1NF, 2NF, 3NF step-by-step**
3. **Create the normalized table structure**
4. **Handle relationships and foreign keys**
5. **Write migration queries**

---

## 📁 File Info
**Filename:** `big-flat-tables-practice.md`  
**Purpose:** Database normalization practice with large, denormalized tables  
**Database:** Oracle 11g compatible
```

You can save this as a `.md` file and upload it directly to GitHub. The markdown formatting includes:

- **Headers and sections** with emojis
- **SQL code blocks** with proper syntax highlighting
- **Clear structure** for easy navigation
- **Bullet points** and organized content
- **Professional formatting** suitable for GitHub documentation

Would you like me to create a companion file with the normalization solutions for any of these tables?
