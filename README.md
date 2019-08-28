
#  Data engineering for "batch" (student group/cohort/class) performance analysis at Flatiron School  


This pipeline culminates in the creation of a **database table** named `batches` that enables data analysts to easily report on the **batches** with the **most students that have completed at least 3 lessons**   


> New batches are continuously added to the REST API, up to 100, but could keep going  
> New students are continueously added to the `students` table in SQLite  
> New test_Runs are continueously added to the test_runs.log file  



We will approach this project both as a Batch Data Processing project as well as a Streaming Data Processing project.  That is, we will simulate an environement where we already have large amounts of data in our 3 sources, and we plan to plan to continuously inject in more of said data as Flatiron School continues to operates.

PySpark will be our processing tool of source as it works well with Batch processes, and we can make use of Spark Streaming for future and real time data







> Student table query remains the same (SELECT * FROM students), 
    - maybe we'd like to add a 'completed' field (int) that keeps track of number lessons the student has completed
> Every test_runs Dstream, we update students records