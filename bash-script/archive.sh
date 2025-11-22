echo "Enter the directory path that you want to archive"
read directory_path
backup=$directory_path
archived_dir=archived_dir_$(date +%Y-%m-%d).tar.gz
tar -czf $archived_dir $backup
echo "The directory: $backup compressed to: $archived_dir"
