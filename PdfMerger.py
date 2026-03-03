import sys
import os
from PyPDF2 import PdfMerger
from PyPDF2.errors import PdfReadError


def main():
    try:
        # 1 & 2. Read output file name from command line
        if len(sys.argv) < 2:
            print("Error: Merge file name not specified.")
            print("Usage: python pdfmerger.py filename")
            sys.exit(1)

        output_name = sys.argv[1] + ".pdf"

        # 3. Initialize merger object
        merger = PdfMerger()

        # 4. Retrieve files in current directory
        try:
            files = os.listdir(".")
        # Error catcher if perms or a issue occurs so it doesnt crash
        except PermissionError:
            print("Error: Permission denied when accessing directory.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error accessing directory: {e}")
            sys.exit(1)

        # 5. Filter only .pdf files
        pdf_files = [f for f in files if f.lower().endswith(".pdf")]

        # 6. Sort alphabetically
        pdf_files.sort()

        # 9. Remove output file from merge list
        pdf_files = [f for f in pdf_files if f != output_name]

        # 7. Report
        print(f"PDF files found: {len(pdf_files)}")
        print("List:")
        for file in pdf_files:
            print(file)

        if len(pdf_files) == 0:
            print("No PDF files to merge.")
            sys.exit(0)

        # 8. Prompt user
        choice = input("Continue (y/n): ").strip().lower()
        if choice != "y":
            print("Merge operation cancelled.")
            sys.exit(0)

        # 9. Append PDFs safely
        for pdf in pdf_files:
            try:
                merger.append(pdf)
                print(f"Added: {pdf}")
            except Exception:
                print(f"Warning: Skipping corrupted PDF file: {pdf}")
            except Exception as e:
                print(f"Warning: Could not add {pdf}: {e}")

        # 10. Export merged PDF
        try:
            merger.write(output_name)
            print(f"\nMerged file created successfully: {output_name}")
        except PermissionError:
            print("Error: Permission denied when writing output file.")
        except Exception as e:
            print(f"Error writing output file: {e}")
        finally:
            merger.close()

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()