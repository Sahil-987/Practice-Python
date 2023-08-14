import zipfile


# open zip file
# zip_path = "file-handling\zipfile\IAM_Words.zip"
# extract_path = "file-handling\zipfile\zipfile_open"

# with zipfile.ZipFile(zip_path,'r') as zip_ref:
#     zip_ref.extractall(extract_path)



# open tgz file
import tarfile

tar_path = "file-handling\zipfile\zipfile_open\IAM_Words\words.tgz"
extract_path = "file-handling/zipfile/tar_open"
with tarfile.open(tar_path, "r:gz") as tar_ref:
    tar_ref.extractall(extract_path)


