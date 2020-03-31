
class Bucket(object):
  """
  Simple class to operate with GCS buckets for sync of a local folder
  Useful in popular ML notebooks like Kaggle/Paperspace/Colab especially if
  you work across them.
  (C) Ruben 2020-03-28 -> https://www.kaggle.com/mrruben

  Usage:
  b=Bucket(project_path=project_path,
         bucket_name=bucket_name,
         gcloud_projectid=gcloud_projectid,
         gcloud_keys_path=gcloud_keys_path)

  # Check files within bucket
  b.ls()

  # Download project directory FROM bucket
  b.download()

  # Upload project directory TO bucket
  b.upload()

  """

  def __init__(self,project_path,bucket_name="",gcloud_projectid="",gcloud_keys_path=""):
    
    from pathlib import Path
    # Define vars
    self.gcloud_keys=gcloud_keys_path
    self.project_dir=project_path
    self.gcloud_projectid=gcloud_projectid
    self.bucket_name=bucket_name
    self.project_path=project_path

    self.p=Path(self.project_path)
    self.project=self.p.name

    # Convert to path
    if self.gcloud_keys:
      self.pgcloud_keys=Path(self.gcloud_keys)
      

    # Secure Local dir
    self.p=Path(self.project_dir)
    if not self.p.is_dir():
      print("{self.project_dir} not found. Create it.")
      %mkdir --parents --verbose {self.p}


    # Login
    if self.gcloud_keys and self.pgcloud_keys.is_file():
      print("keys found. Login with them.")
      ! gcloud auth activate-service-account --key-file={self.gcloud_keys}
    else:
      print("keys NOT found. Login interactively")
      # Login
      ! gcloud auth login

    # List projects
    print("")
    ! gcloud projects list
    print("")

    # Set project
    if not self.gcloud_projectid:
      # Ask for project
      self.gcloud_projectid=input("\nEnter project in Google Cloud Storage to logon into:  ")
    # Set project
    if self.gcloud_projectid:
      ! gcloud config set  project {self.gcloud_projectid} && echo "ProjectId: {self.gcloud_projectid} set correctly./n"
        #! gcloud config set  project {i}

    if not self.bucket_name:
      # List buckets on project
      print("\nList of buckets on project.")
      ! gsutil ls
      self.bucket_name=input("\nEnter Bucket name to use (the text between /<b_name>/ ): ")
      #print("Initialize the class again setting the bucket this time")

  #--------------------------------------------------------------------

  def ls(self):
    "List files on bucket/project"

    # list files on bucket
    # ! gsutil ls gs://{bucket_name}

    print(f"Content inside bucket/project:  {self.bucket_name}/{self.project}")
    ! gsutil ls gs://{self.bucket_name}/{self.project}/

  #--------------------------------------------------------------------

  def download(self):
    "Transfer FROM GoogleCloud Bucket > Local space"
    
    # Transfer FROM GoogleCloud Bucket > Local space  (-n for dry-run)
    if self.bucket_name and self.project and self.p:
        ! gsutil -m rsync  -J -r -u  gs://{self.bucket_name}/{self.project}/  {self.p}  
  #--------------------------------------------------------------------

  def upload(self):
    "Transfer OUT to GoogleCloud bucket"

    # Transfer OUT to GoogleCloud bucket (-n for dry-run)
    if self.bucket_name and self.project and self.p:
        ! gsutil -m rsync  -J -r -u  {self.p}/  gs://{self.bucket_name}/{self.project}/
  #--------------------------------------------------------------------