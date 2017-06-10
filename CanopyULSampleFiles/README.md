### Canopy Universal Language (CanopyUL)

[CanopyUL](https://mesitis.atlassian.net/wiki/display/HOW/Canopy+Universal+Language) is a open source format designed for non-coders (who are more familiar with Excel than with JSONs) to freely transfer information about an accounts transactions and holdings across banks and custodians

The format is designed to standardize the transfer of account and holding information across entities (whether banks / custodians / wealth managers or end customers)

Typically people using CanopyUL will be very familiar with Excel but not so good with coding / JSON / SQL / NoSQL etc. Therefore this format is designed to work in a very familiar Excel row and column format.

Each row has to have an Action Column (e.g. CreateTransaction or CreateAccount) which tells the interpreter what to do. In case there is no Action Column or that Column is blank then that row is ignored.

Easiest way to get familar is to look at the Sample files ... start with Create Transaction.xlsx