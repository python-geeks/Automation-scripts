from datetime import datetime
from pathlib import Path
import zipfile

source_folder = './auto_backup/source/'  # Source directory to be backed up
backup_folder = './auto_backup/backup'   # Directory to save backups
backup_amount = 5

source_folder_path = Path(source_folder)
backup_folder_path = Path(backup_folder)

# assert source_folder_path.exists()

backup_folder_path.mkdir(parents=True, exist_ok=True)

existing_backups = [x for x in backup_folder_path.iterdir(
) if x.is_file() and x.suffix == '.zip' and x.name.startswith('backup-')]

sorted_backup = list(
    sorted(existing_backups, key=lambda f: f.name))

while len(sorted_backup) >= backup_amount:
    backup_to_delete = sorted_backup.pop(0)
    backup_to_delete.unlink()

backup_file_name = f'backup_{datetime.now().strftime("%Y%m%d%H%M%S")}_{source_folder_path.name}.zip'

zip_file = zipfile.ZipFile(
    str(backup_folder_path / backup_file_name), mode='w')

if source_folder_path.is_file():
    zip_file.write(
        source_folder_path.absolute(),
        arcname=source_folder_path.name,
        compress_type=zipfile.ZIP_DEFLATED
    )

elif source_folder_path.is_dir():
    for file in source_folder_path.glob('**/*'):
        if file.is_file():
            zip_file.write(
                file.absolute(),
                arcname=str(file.relative_to(source_folder_path)),
                compress_type=zipfile.ZIP_DEFLATED
            )

zip_file.close()
