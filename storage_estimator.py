
# Storage Estimator

file_size_mb = float(input("Enter file size in MB: "))
number_of_files = int(input("Enter number of files: "))

if file_size_mb <= 0 or number_of_files <= 0:
    print("Error: Enter positive values.")
else:
    total_mb = file_size_mb * number_of_files
    total_gb = total_mb / 1024

    print("Total storage in MB:", total_mb)
    print("Total storage in GB:", round(total_gb, 2))
    print("Calculation completed successfully!")
