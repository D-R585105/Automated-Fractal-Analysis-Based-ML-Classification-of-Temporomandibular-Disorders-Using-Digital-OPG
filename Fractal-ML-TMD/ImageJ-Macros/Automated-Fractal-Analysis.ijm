// Automated Fractal Analysis with ImageJ Macro Code
// Author: Sumeet Narayan Raut

// Usage Instructions
// 
// The following ImageJ-Macro was testing on Windows system with username "Sudu"
// While testing this macro on other system please make necessary changes to macro
// according to your system settings

// Procedure used on test system
//
// 1. Copy the image into C:/Users/Sudu/Desktop/Sample-Image/
// 2. Change the image name in first "selectImage()" function
// 3. Select the ROI co-ordinates in "makeRectangle()" function
// 4. Run this macro in ImageJ
// 5. copy the Results from C:/Users/Sudu/Desktop/ImageJ-Macros/Results/ to patients folder
// 6. Remove files from C:/Users/Sudu/Desktop/ImageJ-Macros/Results/ folder

open("C:/Users/Sudu/Desktop/ImageJ-Macros/Sample-Image/PX20240105_114801_6366_45184188.tif");
selectImage("PX20240105_114801_6366_45184188.tif");
makeRectangle(294, 564, 100, 100);
run("Duplicate...", "title=Dup.tif");
selectImage("PX20240105_114801_6366_45184188.tif");
run("Duplicate...", "title=Dup2.tif");
selectImage("Dup.tif");
selectImage("Dup2.tif");
selectImage("Dup.tif");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup.tif");
selectImage("Dup2.tif");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup2.tif");
selectImage("Dup2.tif");
run("Gaussian Blur...", "sigma=35");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup2-GB.tif");
imageCalculator("Subtract create", "Dup.tif","Dup2-GB.tif");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB.tif");
run("Add...", "value=128");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD.tif");
setOption("BlackBackground", true);
run("Convert to Mask");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD-BIN.tif");
run("Erode");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD-BIN-ER.tif");
run("Dilate");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD-BIN-ER-DI.tif");
run("Invert LUT");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD-BIN-ER-DI-IN.tif");
run("Skeletonize");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Dup-GB-SUB-ADD-BIN-ER-DI-IN-SK.tif");
run("Fractal Box Count...", "box=2,3,4,6,8,12,16,32,64 black");
close();
saveAs("Resultss", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Resultss.csv");
run("Fractal Box Count...", "box=2,3,4,6,8,12,16,32,64 black");
saveAs("Tiff", "C:/Users/Sudu/Desktop/ImageJ-Macros/Results/Plot.tif");
close();