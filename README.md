Here’s the simulated dashboard view for sample_test_report.csv:

📄 Raw Test Report (first 5 rows)
TestCase	Module	Result	Date	Description
TC-0001	Payments	Pass	2025-07-28	Test case for Reports
TC-0002	Checkout	Pass	2025-07-29	Test case for Inventory
TC-0003	Payments	Fail	2025-07-23	Test case for Auth
TC-0004	Auth	Pass	2025-07-25	Test case for Reports
TC-0005	Reports	Fail	2025-07-22	Test case for Checkout

📊 Test Result Summary
Counts:

Pass → 36

Fail → 12

Skipped → 2

Bar Chart:

mathematica
Copy
Edit
Pass    ████████████████████████████████
Fail    ███████
Skipped █
✅ Pass Rate: 72.00%

❌ Failed Test Cases (top 5)
TestCase	Module	Result	Date	Description
TC-0003	Payments	Fail	2025-07-23	Test case for Auth
TC-0005	Reports	Fail	2025-07-22	Test case for Checkout
TC-0007	Reports	Fail	2025-07-28	Test case for Inventory
TC-0011	Auth	Fail	2025-07-30	Test case for Payments
TC-0014	Payments	Fail	2025-07-26	Test case for Auth

📅 Test Case Distribution Over Time (Line Chart)
(Simulated view — actual chart in Streamlit would be interactive)

Date	Pass	Fail	Skipped
2025-07-21	1	0	0
2025-07-22	2	1	0
2025-07-23	1	1	0
...	...	...	...

🔍 Module Filter Example (Payments)
TestCase	Module	Result	Date	Description
TC-0001	Payments	Pass	2025-07-28	Test case for Reports
TC-0003	Payments	Fail	2025-07-23	Test case for Auth
...	...	...	...	...

