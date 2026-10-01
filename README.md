# Image Resizer & Watermark Tool 🖼️

A simple Python GUI application that allows you to **resize images in pixels and add a text watermark** to them.

The application is built using **Tkinter** for the GUI and **Pillow** for image processing.

## Features

- 🖼️ Upload JPG, JPEG, and PNG images
- 📏 Resize images using custom width and height in pixels
- ✍️ Add a text watermark to an image
- 🎨 Choose watermark color — White or Black
- 💾 Save the edited image as `watermark.jpg`
- 🖥️ Simple and easy-to-use GUI

## Technologies Used

- Python
- Tkinter
- Pillow (PIL)

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd <project-folder>
```

### 3. Install the required package

The project includes a `requirements.txt` file containing the required dependency.

Install it using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```txt
Pillow
```

## How to Run

Run the Python file:

```bash
python main.py
```

## How to Use

### 1. Upload an Image

Click the **Upload Image** button and select a JPG, JPEG, or PNG image from your computer.

### 2. Set Image Size

Enter the required width and height in pixels.

For example:

```text
400,400
```

The first value represents the **width** and the second value represents the **height**.

```text
Width,Height
400,400
```

Then click **Set**.

### 3. Enter Watermark Text

Enter the text you want to add as a watermark.

For example:

```text
My Image
```

### 4. Choose Watermark Color

Select either:

- White
- Black

### 5. Add Watermark

Click **Add Watermark**.

The watermark will be added to the image.

### 6. Save the Image

Click **Save Image**.

The edited image will be saved as:

```text
watermark.jpg
```

## Example

The basic workflow is:

```text
Upload Image
      ↓
Set Image Size
      ↓
Enter Watermark Text
      ↓
Choose Watermark Color
      ↓
Add Watermark
      ↓
Save Image
```

## Important Note

The image size is entered in **pixels**, not centimeters.

For example:

```text
200,200
```

means:

- Width = 200 pixels
- Height = 200 pixels

## Project Structure

```text
Image-Resizer-Watermark/
│
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Pillow
