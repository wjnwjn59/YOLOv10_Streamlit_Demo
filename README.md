# YOLOv10 Streamlit Demo

## Description
A simple object detection web demo using YOLOv10 and Streamlit.

## How to use
### Option 1: Using conda environment
1. Create new conda environment and install required dependencies:
```
$ conda create -n <env_name> -y python=3.11
$ conda activate <env_name>
$ pip3 install -r requirements.txt
```
2. Host streamlit app
```
$ streamlit run app.py
```
### Option 2: Using docker
1. Build docker image
```
$ docker build -t <tag_name> -f docker/Dockerfile .
```
2. Run a docker contaier
```
$ docker run -p 8501:8501 -it <tag_name>
```
