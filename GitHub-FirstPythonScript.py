#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: RAGHAV JOSHI
    Description:  This is the assignment while using the python script for the first time.
    Date created: 09/16/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
import arcpy.analysis
import arcpy.management
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "C:\\Users\\rgvjoshi\\OneDrive - Kansas State University\\Documents\\GitHub\\firstpythonscript-rgvjoshi\\GIS_project\\ExerciseData.gdb"

# Select Flint Hills using "Select layer by Attribute"
flint = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

#Create a buffer of 10 kilometers around Flint Hilld
buffer = arcpy.analysis.Buffer(flint, 'Buff_Flint_ecoregion', '10 kilometers')

#Clip rivers inside this buffer
clipped = arcpy.analysis.Clip('ks_major_rivers', buffer,'Rivers_in_FH_clip')

# Calculate length of streams inside Flint Hills ecoregion in miles
arcpy.management.CalculateGeometryAttributes(clipped, [['StreamLength_miles', 'LENGTH']], 'MILES_INT')

# Summarize total length of all streams in miles. The file is saved as "StreamLength_Summary" table.
arcpy.analysis.Statistics('Rivers_in_FH_clip', 'StreamLength_Summary', [['StreamLength_miles', 'SUM']])

# Hence, we can calculate stream length of rivers inside the selected ecoregion.