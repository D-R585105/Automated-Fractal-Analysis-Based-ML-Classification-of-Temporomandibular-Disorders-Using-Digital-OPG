# ImageJ Macros for Automated Fractal Analysis

This directory contains ImageJ macro scripts and resources for automated fractal dimension analysis of mandibular condyles from digital OPG images.

## Contents

```
ImageJ-Macros/
├── Automated-Fractal-Analysis.ijm  # Main macro script
├── Sample-Image/                   # Sample OPG image for testing
│   └── PX20240105_114801_6366_45184188.tif
├── Results/                        # Output directory for processed images
└── Previous Results/               # Example analysis results
    ├── Left Condyle FA/            # Left condyle fractal analysis
    └── Right Condyle FA/           # Right condyle fractal analysis
```

## Requirements

- **ImageJ** version 1.42 or later (tested on Windows)
- Digital OPG images in TIFF format

## Macro Overview

The `Automated-Fractal-Analysis.ijm` macro automates the fractal analysis workflow using the box-counting method. The processing pipeline includes:

| Step | Operation | Output File |
|------|-----------|-------------|
| 1 | ROI extraction | `Dup.tif` |
| 2 | Duplicate for background | `Dup2.tif` |
| 3 | Gaussian Blur (sigma=35) | `Dup2-GB.tif` |
| 4 | Background subtraction | `Dup-GB-SUB.tif` |
| 5 | Add constant (128) | `Dup-GB-SUB-ADD.tif` |
| 6 | Binary conversion (mask) | `Dup-GB-SUB-ADD-BIN.tif` |
| 7 | Erosion | `Dup-GB-SUB-ADD-BIN-ER.tif` |
| 8 | Dilation | `Dup-GB-SUB-ADD-BIN-ER-DI.tif` |
| 9 | Invert LUT | `Dup-GB-SUB-ADD-BIN-ER-DI-IN.tif` |
| 10 | Skeletonization | `Dup-GB-SUB-ADD-BIN-ER-DI-IN-SK.tif` |
| 11 | Fractal Box Count | `Resultss.csv`, `Plot.tif` |

## Usage Instructions

### Step 1: Prepare the Environment

The macro is configured for a Windows system. Modify the file paths in the macro according to your system settings.

**Default paths (Windows):**
```
Input:  C:/Users/Sudu/Desktop/ImageJ-Macros/Sample-Image/
Output: C:/Users/Sudu/Desktop/ImageJ-Macros/Results/
```

### Step 2: Configure the Macro

1. Open `Automated-Fractal-Analysis.ijm` in a text editor
2. Update the image filename in the `open()` and `selectImage()` functions:
   ```javascript
   open("C:/Users/Sudu/Desktop/ImageJ-Macros/Sample-Image/YOUR_IMAGE.tif");
   selectImage("YOUR_IMAGE.tif");
   ```
3. Adjust the ROI coordinates in `makeRectangle()`:
   ```javascript
   makeRectangle(x, y, width, height);  // Default: 294, 564, 100, 100
   ```

### Step 3: Run the Analysis

1. Copy your OPG image to the `Sample-Image/` directory
2. Open ImageJ
3. Go to `Plugins > Macros > Run...`
4. Select `Automated-Fractal-Analysis.ijm`
5. The macro will process the image and save results to the `Results/` directory

### Step 4: Collect Results

1. Copy the contents of `Results/` to a patient-specific folder
2. Clear the `Results/` directory before processing the next image
3. The fractal dimension (D) value is in `Resultss.csv`

## Output Description

### Results CSV Format

| Column | Description |
|--------|-------------|
| Label | Processed image identifier |
| C2-C64 | Box counts at different scales (2, 3, 4, 6, 8, 12, 16, 32, 64 pixels) |
| D | **Fractal Dimension** (the key output metric) |

### Example Results

**Right Condyle (from Previous Results):**
```
D = 1.311
```

**Left Condyle (from Previous Results):**
```
D = 1.207
```

## Fractal Box Count Parameters

The macro uses the following box sizes for fractal dimension calculation:
- Box sizes: 2, 3, 4, 6, 8, 12, 16, 32, 64 pixels
- Black background option enabled

## Processing Pipeline Explanation

1. **Gaussian Blur (sigma=35):** Creates a smoothed version of the image to estimate background illumination
2. **Background Subtraction:** Removes uneven illumination by subtracting the blurred image
3. **Add Constant (128):** Shifts pixel values to mid-gray for proper thresholding
4. **Binary Conversion:** Creates a binary mask of trabecular bone structure
5. **Erosion/Dilation:** Morphological operations to clean up noise and refine bone boundaries
6. **Skeletonization:** Reduces bone structure to single-pixel-wide lines for fractal analysis
7. **Fractal Box Count:** Calculates the fractal dimension using the box-counting algorithm

## Adapting for Different Systems

### macOS/Linux

Replace Windows-style paths with Unix paths:
```javascript
open("/Users/username/Desktop/ImageJ-Macros/Sample-Image/image.tif");
saveAs("Tiff", "/Users/username/Desktop/ImageJ-Macros/Results/output.tif");
```

### Batch Processing

To process multiple images, wrap the macro in a loop and iterate over files in the input directory.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| File not found | Verify paths match your system configuration |
| ROI out of bounds | Adjust `makeRectangle()` coordinates for your image |
| Results not saving | Ensure the `Results/` directory exists and is writable |
| Fractal analysis fails | Verify the image is properly skeletonized (white lines on black background) |

## Author

**Sumeet Narayan Raut**

## Related Documentation

- [Main Project README](../README.md)
- [ImageJ Documentation](https://imagej.net/ij/)
- [Fractal Box Count Plugin](https://imagej.net/ij/docs/menus/analyze.html#box)
