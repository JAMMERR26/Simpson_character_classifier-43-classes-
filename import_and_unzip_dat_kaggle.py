!pip install -q kaggle
from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d alexattia/the-simpsons-characters-dataset #firstdownload

!unzip the-simpsons-characters-dataset #then_unzip
