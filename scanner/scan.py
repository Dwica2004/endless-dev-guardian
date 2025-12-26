from pathlib import Path
from rules import RULES

def scan_file(file_path):
    text = file_path.read_text(encoding="utf-8", errors="ignore").lower()
    findings = []

    for rule, keywords in RULES.items():
        hits = [k for k in keywords if k.lower() in text]
        if hits:
            findings.append((rule, hits))

    return findings

def main():
    print("🔐 Endless Dev Guardian - Move Static Scan\n")
    target = Path(input("Enter .move file path: ").strip())

    if not target.exists():
        print("❌ File not found")
        return

    results = scan_file(target)
    if not results:
        print("✅ No obvious risk patterns detected.")
        return

    print("\n⚠️ Potential Risks Detected:\n")
    for rule, hits in results:
        print(f"- {rule}: {hits}")

if __name__ == "__main__":
    main()
