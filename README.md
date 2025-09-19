---

# Ubuntu Image Fetcher

A mindful Python tool for safely fetching and saving images from the web.

This program allows you to download multiple images from URLs, while applying important safety precautions such as verifying content type, limiting file size, and preventing duplicate downloads.

---

## ✨ Features

* ✅ **Download multiple URLs at once** (space or newline separated).
* ✅ **Precautions for unknown sources**:

  * Verifies that the file is an image (`Content-Type`).
  * Skips very large files (default > 10 MB).
* ✅ **Prevents duplicates** by checking SHA256 hashes.
* ✅ **Checks HTTP headers** (`Content-Type`, `Content-Length`) before saving.
* ✅ **Organized storage**: all images are saved inside the `Fetched_Images/` folder.

---

## ⚙️ Requirements

* Python 3.7+
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## 🚀 Usage

1. Clone or copy the script to your local machine.
2. Run the program:

```bash
python image_fetcher.py
```

3. Enter one or more image URLs (separated by spaces or newlines). Example:

```
Please enter image URLs (separate with spaces or newlines):
https://images.unsplash.com/photo-1584395630827-860eee694d7b
https://www.pexels.com/photo/cat-lying-on-floor-617278/
```

4. The images will be saved into the `Fetched_Images/` directory.

---

## 📂 Example Output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Fetching: https://images.unsplash.com/photo-1584395630827-860eee694d7b
✓ Successfully fetched: photo-1584395630827-860eee694d7b
✓ Image saved to Fetched_Images/photo-1584395630827-860eee694d7b

Fetching: https://www.pexels.com/photo/cat-lying-on-floor-617278/
✗ Skipped: Not an image (Content-Type: text/html)

All downloads complete. Connection strengthened. Community enriched.
```

---

## 🔐 Safety Precautions

* **Content-Type validation**: Only downloads files with `image/*` MIME type.
* **File size check**: Skips files larger than **10MB** by default.
* **Duplicate prevention**: Uses SHA256 hashing to detect already-downloaded files.

---

## 📌 Notes

* Filenames are extracted from the URL. If none exists, the program generates one (e.g., `downloaded_1.jpg`).
* You can adjust the **max file size limit** in the code (`10 * 1024 * 1024`).
* Works best with direct image URLs (ending in `.jpg`, `.png`, etc.).

---

## 📝 License

This project is released under the MIT License.
Feel free to use and modify it responsibly.

---
