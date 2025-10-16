Here’s a **README.md** you can drop into your assignment folder.
It explains the purpose of the script, how to set it up with your Roboflow-trained YOLOv8 weights, and how to run it.

---

```markdown
# License Plate Character Break Detection

This project analyzes pairs of vehicle images (Front and Rear) and determines whether the license plate characters are broken or damaged. It uses a YOLOv8 model to detect license plates and a simple heuristic to flag broken characters.

---

## Features

- Uses a YOLOv8 model (default or custom Roboflow-trained weights) to detect license plates.
- Preprocesses detected plates and segments characters.
- Flags plates whose characters appear broken or damaged.
- Handles batches of images arranged in a folder with `.FR.` and `.RE.` naming convention.
- Saves results to a CSV file.

---

## Folder Structure

Example:

```

project/
├── plate_break_detection.py
├── best.pt                 # your Roboflow-trained YOLOv8 weights
└── dataset/
├── 20250915...FR....jpg
├── 20250915...RE....jpg
├── ...

````

The script expects all front/rear images in a single folder.  
Each front image name contains `.FR.` and each rear image name contains `.RE.`.

---

## Requirements

- Python 3.9+
- [Conda](https://docs.conda.io/) environment
- Packages:
  - `ultralytics` (YOLOv8)
  - `opencv-python`
  - `numpy`
  - `pandas`
  - `pathlib` (built-in)

Install dependencies:

```bash
conda create -n plate-break python=3.9
conda activate plate-break
pip install ultralytics opencv-python pandas numpy
````

---

## How to Use

1. **Extract your dataset** so all `.jpg` files are inside a single folder.

2. **Place your trained YOLOv8 weights** (downloaded from Roboflow, e.g. `best.pt`) somewhere accessible.

3. **Edit `plate_break_detection.py`**:

   ```python
   from pathlib import Path
   # Folder containing .jpg images
   dataset_dir = Path(r"C:\path\to\your\dataset\folder")

   # Load your trained YOLOv8 model
   from ultralytics import YOLO
   model = YOLO(r"C:\path\to\your\best.pt")
   ```

4. **Run the script**:

   ```bash
   python plate_break_detection.py
   ```

5. **Output**:

   * The console prints:

     * How many `.jpg` files were found
     * How many FR/RE groups were detected
     * Any “No plates detected…” messages
   * A file `plate_break_results.csv` is saved in your dataset folder with columns:

     | pair_key | front_file | rear_file | front_broken | rear_broken |

---

## Notes

* Adjust the confidence threshold in `model.predict()` if needed:

  ```python
  results = model.predict(image, conf=0.25, verbose=False)
  ```

* The “broken character” detection uses a simple heuristic (connected components and white pixel ratio). You can tweak it for your dataset.

* Make sure your folder path in `dataset_dir` points directly to the folder containing the `.jpg` images (not just the parent folder).

---

## Example Output

```
Looking in: C:\Users\DELL\OneDrive\문서\assignment\q1\Q1_Broken\Broken
Found 120 jpg files
Found 60 FR/RE groups
Saved results to C:\Users\DELL\OneDrive\문서\assignment\q1\Q1_Broken\Broken\plate_break_results.csv
```

Open the CSV to view which plates are flagged as broken.

