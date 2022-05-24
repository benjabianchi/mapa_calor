FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt
ARG video_path data/input.mp4
ENV video_path=$video_path

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ENTRYPOINT ["tail", "-f", "/dev/null"]

#CMD ["python3", "motion-heatmap.py", "--video", "$video_path"]
