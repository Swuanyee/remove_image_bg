# Remove Background from Images

## Installation
1. Clone this repository:
   ```bash
   git clone git@github.com:Swuanyee/remove_image_bg.git
   cd remove_image_bg
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Folder Structure
```
remove_image_bg/
│── preprocessed_images/    # Input images (place images here before running the script)
│── processed_images/       # Output images (processed images will be saved here)
│── remove_bg_batch.py      # Main script
│── requirements.txt        # Required dependencies
│── README.md               # Documentation
```

## Running the Script
1. Place the images you want to process in the `preprocessed_images` folder.
2. Run the script:
   ```bash
   python remove_bg_batch.py
   ```
3. The processed images will be saved in the `processed_images` folder.

## Platform-Specific Notes
To ensure compatibility with all operating systems, `requirements.txt` installs the correct version of `onnxruntime`:

- Windows/Linux: Installs `onnxruntime`
- macOS (M1/M2): Installs `onnxruntime-silicon`

## Troubleshooting
- If you encounter an issue with `onnxruntime` and `numpy`, downgrade `numpy`:
  ```bash
  pip install "numpy<2"
  ```
- If `onnxruntime` is missing, reinstall it:
  ```bash
  pip uninstall onnxruntime
  pip install onnxruntime
  ```
  For macOS M1/M2:
  ```bash
  pip install onnxruntime-silicon
  ```
