# Simple File Filter
## 🚀 Features
- **Real-time Monitoring:** Uses the `watchdog` library to instantly detect new files.
- **Customizable Rules:** Easily map any file extension to a specific folder in `config.py`.
- **Cross-Platform:** Works on Windows, macOS, and Linux by dynamically resolving user paths.
- **Safe File Handling:** Includes logic to wait for downloads to finish before moving files safely.

## 🛠️ Prerequisites
- Python 3.x
- `watchdog` library

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/FilesFilter.git
   cd FilesFilter
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   .\venv\Scripts\activate
   
   # Activate on Mac/Linux:
   source venv/bin/activate
   
   pip install watchdog
   ```

3. **Configuration:**
   Open `config.py` and modify the `EXTENSIONS` dictionary to fit your needs (e.g., `".pdf": "Documents"`).

## 💻 Usage
Run the main script:
```bash
python main.py
```
Change Path to YOUR donwload and sort directories
The script will start listening to your Downloads folder. Try downloading a file, and watch it magically move to the correct folder! Press `Ctrl+C` to safely stop the script.

## 📂 Project Structure
├── main.py              # Main script (event handler and observer logic)
├── config.py            # Dictionary mapping extensions to folders
└── README.md            # Project documentation
