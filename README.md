
#  Data engineering for "batch" (student group/cohort/class) performance analysis at Flatiron School   


This pipeline culminates into the creation of a **database table** named `batches` that enables data analysts to easily report on the **student batches** with the **most students that have completed at least 3 lessons**.  A simple join query with the `students` table allows for the analysis of the 'best' batches as well as their individual students.  The tables are continually updated in real time as new records become available    


> New batches are continuously added to the REST API, up to 100, but could keep going   
> New students are continueously added to the `students` table in SQLite    
> New test_Runs are continueously added to the test_runs.log file  



We will approach this project both as a Batch Data Processing project as well as a Streaming Data Processing project.  That is, we will simulate an environement where we already have large amounts of data in our 3 sources, and we plan on continuously injecting in more of said data as Flatiron School continues to operates.  

PySpark will be our processing tool of source as it works well with Batch processes, and we can make use of Spark Streaming for future and real time data  







> Student table query remains the same (SELECT * FROM students), 
    - maybe we'd like to add a 'completed' field (int) that keeps track of number lessons the student has completed  
    - SELECT * from students WHERE completed >= 3  
    
> Every test_runs Dstream, we update students records  
    - (do we need Kafka for this?  can't this just be done with Spark Streaming?)  
    - read in only new lines from log file for each batch (research)  



> ? - this whole REST API with the batches doesn't really seam to matter since it maxes out at 100  
> However, we need to simulate an environement where these batches would also have no bound.   
> for batch created after 'yyyy-mm-dd' add record to batches table - continually   
    - (can be done in python for loop of date-ranges)
    - or just one api request with the after param that checks for duplicates in the db table before appending  