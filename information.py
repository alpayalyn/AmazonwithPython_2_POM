"""
next task would be to put the locators and methods related to different pages 
in their respective classes. Here, there are two approaches to maintain the locators. 
First is keeping all the locators specific to a page in its own class and the other is to keep locators of all pages at a common place. 
We will take the latter one. Methods specific to a page would obviously be kept in that page’s class.

‘Drivers’ folder stores all the executables for different browsers that we want to be used (like ChromeDriver.exe etc.)

‘Reports’ folder would have the test execution reports

‘Resources’ folder stores the locators, test data, helper methods (if any)

‘PO’ folder, which contains page object classes.

‘Tests’ would contain the actual tests that we want to execute plus the testsuite file.

"""

