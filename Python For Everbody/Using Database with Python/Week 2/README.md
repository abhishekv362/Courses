#   Counting Organizations

### Aim :: Get Count of Organization having largest number, of domain.

-   This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

>   CREATE TABLE Counts (org TEXT, count INTEGER)

-   If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.
-   Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.
-   The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
>###  Output :: 536