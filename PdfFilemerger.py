import sys                      # Gives access to command-line arguments and exit control
import os                       # Lets us interact with the operating system (files/folders)
from PyPDF2 import PdfMerger    # Class used to merge multiple PDFs
from PyPDF2.errors import PdfReadError  # Specific error for corrupted/unreadable PDFs


def main():  # Main function where program execution starts
    try:
        # Check if user provided an output filename argument
        # sys.argv[0] = script name
        # sys.argv[1] = first argument after script name
        if len(sys.argv) < 2:
            print("Error: Merge file name not specified.")
            print("Usage: python pdfmerger.py filename")
            sys.exit(1)  # Exit with error status

        # Create output filename by adding .pdf extension
        output_name = sys.argv[1] + ".pdf"

        # Create a PdfMerger object to hold and combine PDFs
        merger = PdfMerger()

        # Try to retrieve all files in the current directory
        try:
            files = os.listdir(".")  # "." means current folder
        except PermissionError:
            print("Error: Permission denied when accessing directory.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error accessing directory: {e}")
            sys.exit(1)

        # Filter the list to include only files ending with .pdf (case insensitive)
        pdf_files = [f for f in files if f.lower().endswith(".pdf")]

        # Sort the PDF files alphabetically
        pdf_files.sort()

        # Remove the output file name from the list if it already exists
        # Prevents merging the output file into itself
        pdf_files = [f for f in pdf_files if f != output_name]

        # Display how many PDFs were found
        print(f"PDF files found: {len(pdf_files)}")
        print("List:")
        for file in pdf_files:
            print(file)

        # If no PDFs are found, exit normally
        if len(pdf_files) == 0:
            print("No PDF files to merge.")
            sys.exit(0)

        # Ask the user for confirmation before merging
        choice = input("Continue (y/n): ").strip().lower()

        # If the user does not type 'y', cancel the operation
        if choice != "y":
            print("Merge operation cancelled.")
            sys.exit(0)

        # Loop through each PDF file and attempt to add it to the merger
        for pdf in pdf_files:
            try:
                merger.append(pdf)  # Add PDF to merger
                print(f"Added: {pdf}")
            except PdfReadError:
                # Handles corrupted or unreadable PDF files
                print(f"Warning: Skipping corrupted PDF file: {pdf}")
            except Exception as e:
                # Handles any other unexpected error while adding a file
                print(f"Warning: Could not add {pdf}: {e}")

        # Attempt to write the merged output file
        try:
            merger.write(output_name)  # Create final merged PDF file
            print(f"\nMerged file created successfully: {output_name}")
        except PermissionError:
            print("Error: Permission denied when writing output file.")
        except Exception as e:
            print(f"Error writing output file: {e}")
        finally:
            merger.close()  # Always close the merger to free resources

    except KeyboardInterrupt:
        # Handles Ctrl+C safely
        print("\nOperation cancelled by user.")
        sys.exit(1)

    except Exception as e:
        # Catch-all for any fatal unexpected errors
        print(f"Unexpected fatal error: {e}")
        sys.exit(1)


# This ensures main() runs only if the script is executed directly
# and not if it is imported into another Python file
if __name__ == "__main__":
    main()