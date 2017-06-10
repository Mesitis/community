## Canopy Developer Community Page
*Sample code and all things community*

[Canopy](https:/canopy.cloud) is a data aggregation and analytics platform targeting the high networth clients. This page is meant for people who are looking to develop applications on our platform and contains sample code and descriptions of APIs.

Please email us for further information (including if you want a demo login)

### Canopy Universal Language (CanopyUL):
[CanopyUL](https://mesitis.atlassian.net/wiki/display/HOW/Canopy+Universal+Language) is a open source format designed for non-coders (who are more familiar with Excel than with JSONs) to freely transfer information about an accounts transactions and holdings across banks and custodians


### Canopy Open APIs
All (well almost all !!) data inside Canopy can be accessed via APIs ... a small sample of these APIs is [here](https://documenter.getpostman.com/view/884147/canopy-api-calls/6YtywA3)

### Canopy midAPI server
An analytics server that pulls a particular users data from Canopy (via APIs - requires regular authentication to access the data being downloaded) and does a large number of analytics on it. Accessible via Open APIs .. sample [here](https://documenter.getpostman.com/view/884147/canopy-midapi-calls/6YwzFUx) 

### Microsoft Excel Front End
For users who want to access the data directly via Microsoft Excel. This spreadsheet uses the same authentication for the Open APIs (i.e. you need to enter your username / password and OTP (if activated). It works on both Windows and Mac and does not require any particular add-ins to be installed (although it works a little faster on Windows)
Always look for the latest version (as earlier versions may not work).  

### MIT License
While Canopy itself is not open source, we encourage developers to build applications on top of Canopy. Therefore all code in this repository is provided under MIT license
