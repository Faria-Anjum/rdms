# Automated tests on generating reports for the Robi Distribution Management System (RDMS) website using pytest-playwright
## Navigates to https://stage-dms.robi.com.bd and validates report generation for the following in the Reports tab:

+ SO Payment Report
+ SO MIS Report
+ SIM Stock
+ SC SIM Stock
+ Individual SIM history
+ Activation Report
+ Delivery Report
+ Real-time Activation Report
+ Retailer Stock
+ Delivery vs Activation Summary
+ Activation Summmary
+ Delivery Summary
+ Pending OD (SIM)
+ SIM Activation Report
+ Pending OD (SC)
+ No Activated MSISDN
+ Lifting vs Activation
+ Sales Call (DSR)
+ Sales Call (Transaction)
+ Market Visit Plan
+ Market Visit (Routewise)
+ BP Performance

# Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

# To run tests:
### Move to rdms folder and run the command:

```
pytest
```

Config files:
+ /conftest: creates single page instance for all test functions
+ /pytest.ini: runs tests in msedge with added cli commands

Reports:
+ /html-test-report: step by step execution of test functions across all tests
