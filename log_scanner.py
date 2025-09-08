import streamlit as st

def scan_log(text: str) -> dict:
    lines = text.splitlines()
    results = {
        "exceptions": [],
        "crashes": [],
    }

    for i, line in enumerate(lines, start=1):
        if "exception" in line.lower():
            results["exceptions"].append((i, line.strip()))
        if "crash" in line.lower():
            results["crashes"].append((i, line.strip()))

    return results


def generate_report(results: dict) -> str:
    report_lines = []
    report_lines.append("=== Log Scan Report ===\n")

    if results["exceptions"]:
        report_lines.append("Exceptions found:\n")
        for line_num, line in results["exceptions"]:
            report_lines.append(f"  Line {line_num}: {line}")
    else:
        report_lines.append("No exceptions found.\n")

    report_lines.append("")

    if results["crashes"]:
        report_lines.append("Crashes found:\n")
        for line_num, line in results["crashes"]:
            report_lines.append(f"  Line {line_num}: {line}")
    else:
        report_lines.append("No crashes found.\n")

    return "\n".join(report_lines)


# Streamlit UI
st.title("📜 Log Exception & Crash Scanner")

uploaded_file = st.file_uploader("Upload a log file", type=["txt", "log"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8", errors="ignore")
    results = scan_log(text)

    st.subheader("Scan Results")
    st.write(generate_report(results))

    report_text = generate_report(results)
    st.download_button(
        label="📥 Download Report",
        data=report_text,
        file_name="log_report.txt",
        mime="text/plain",
    )
