# log-scanner-app
App that can be used to find exceptions in logs
# Log Scanner App

A simple tool to scan log files for exceptions and crashes.  
Built with [Streamlit](https://streamlit.io/) and packaged with PyInstaller.

---

## 🚀 Features
- Detects "Exception" and "Crash" in logs
- Highlights results by severity
- Generates a downloadable report
- Easy drag-and-drop interface

---

## 📥 Download
Grab the latest version from [Releases](../../releases).

---

## 🖥️ How to Use
1. Download the `.exe` file from Releases.
2. Double-click it to start the app.
3. Your browser will open automatically.
4. Drop in a log file → get instant results!

---

## 🛠️ Development
If you want to run it from source:

```bash
git clone https://github.com/YOUR_USERNAME/log-scanner-app.git
cd log-scanner-app
pip install -r requirements.txt
streamlit run log_scanner.py
