#!/bin/bash

echo Hello, what would you like to do today? Choose 1 to enter a new model type, 2 to enter a new model, 3 to enter batch information, or 4 to update the test sets of a model. 
read todo

if [ "$todo" == "4" ]; then
	echo enter the model id
	read modelid 
	echo enter the test set to enter
	read newtestset
	rm logLast.sql
	myQuery="SELECT testsets from modelrecords WHERE uniqueid='"
	myQuery+=$modelid
	myQuery+="';"
	echo $myQuery
	echo $myQuery >> logLast.sql
	rm oldSets.txt
	psql -d model-db < logLast.sql >> oldSets.txt
	sed -i '1,2d' ./oldSets.txt
	sed -i '2d' ./oldSets.txt
	sets=$(<oldSets.txt)
	sets+=", "
	sets+=$newtestset
	myQuery="UPDATE ModelRecords SET TestSets = '"
	myQuery+=$sets
	myQuery+="' WHERE uniqueID='"
	myQuery+=$modelid
	myQuery+="';"
	echo $myQuery
	rm logLast.sql
	echo $myQuery >> logLast.sql
	psql -d model-db < logLast.sql

fi
if [ "$todo" == "1" ]; then
	echo enter your model type name
	read modeltypename
	myQuery="INSERT INTO ModelInfo(ModelTypeName) VALUES ('"
	myQuery+=$modeltypename
	myQuery+="');"
	echo $myQuery
	rm logLast.sql
	echo $myQuery >> logLast.sql
	psql -d model-db < logLast.sql 
fi

if [ "$todo" == "2" ]; then
	echo enter unique ID
	read uniqueid
        echo enter model name
        read modelname
	echo enter date run IN YYYY-MM-DD format 
	read daterun
	echo enter replicate Y/N
	read replicate
	echo enter input data
	read inputdata
	echo enter test sets
	read testsets
	echo enter model runner
	read modelrunner
	echo enter model type name
	read modeltypename
	sep="', '"
        myQuery="INSERT INTO ModelRecords(UniqueID, ModelName, DateRun, Replicate, InputData, TestSets, ModelRunner, ModelTypeName) VALUES('"
        myQuery+=$uniqueid$sep$modelname$sep$daterun$sep$replicate$sep$inputdata$sep$testsets$sep$modelrunner$sep$modeltypename
        myQuery+="');"
        echo $myQuery
        rm logLast.sql
	echo $myQuery >> logLast.sql
        psql -d model-db < logLast.sql
fi

if [ "$todo" == "3" ]; then
        echo enter unique ID
        read uniqueid
        echo enter cell lines
        read celllines
        echo enter plating date IN YYYY-MM-DD format
        read pdate
        echo enter fixation date IN YYYY-MM-DD format
        read fdate
        echo enter common name
        read commonname
        echo enter batch
        read batch
        echo enter cell source
        read cellsource
        echo enter cell type
        read celltype
        echo enter density
        read density
        echo enter plate
        read plate
        echo enter microscope
        read microscope
	echo enter CH1
	read ch1
	echo enter CH2
	read ch2
	echo enter CH3
	read ch3
	echo enter wells
	read wells
	echo enter plate setup
	read platesetup
	echo enter experiment
	read experiment
        sep="', '"
        myQuery="INSERT INTO BatchInfo(UniqueBatchID, CellLines, PlatingDate, FixationDate, CommonName, Batch, CellSource, CellType, Density, Plate, Microscope, CH1, CH2, CH3, Wells, PlateSetup, Experiment) VALUES('"
        myQuery+=$uniqueid$sep$celllines$sep$pdate$sep$fdate$sep$commonname$sep$batch$sep$cellsource$sep$celltype$sep$density$sep$plate$sep$microscope$sep$ch1$sep$ch2$sep$ch3$sep$wells$sep$platesetup$sep$experiment
        myQuery+="');"
        echo $myQuery
        rm logLast.sql
        echo $myQuery >> logLast.sql
        psql -d model-db < logLast.sql
fi

