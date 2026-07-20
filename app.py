from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import shutil
import glob
import subprocess

app = Flask(__name__)

model = YOLO("best.pt")

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return render_template("index.html")

    file = request.files["image"]

    if file.filename == "":
        return render_template("index.html")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    ext = os.path.splitext(file.filename)[1].lower()

    image_ext = [".jpg", ".jpeg", ".png"]
    video_ext = [".mp4", ".avi", ".mov", ".mkv"]

    # ---------------- IMAGE ---------------- #

    if ext in image_ext:

        results = model(input_path)

        annotated = results[0].plot()

        import cv2

        output_name = "result_" + file.filename
        output_path = os.path.join(RESULT_FOLDER, output_name)

        cv2.imwrite(output_path, annotated)

        return render_template(
            "index.html",
            image="results/" + output_name
        )

    # ---------------- VIDEO ---------------- #

    elif ext in video_ext:

        results = model.predict(
            source=input_path,
            conf=0.5,
            save=True,
            verbose=False
        )

        save_dir = str(results[0].save_dir)

        video_files = []

        video_files.extend(glob.glob(os.path.join(save_dir, "*.mp4")))
        video_files.extend(glob.glob(os.path.join(save_dir, "*.avi")))
        video_files.extend(glob.glob(os.path.join(save_dir, "*.mov")))
        video_files.extend(glob.glob(os.path.join(save_dir, "*.mkv")))

        if len(video_files) == 0:
            return "Detection video not found."

        detected_video = video_files[0]

        temp_video = os.path.join(
            RESULT_FOLDER,
            "temp_video.mp4"
        )

        shutil.copy2(
            detected_video,
            temp_video
        )

        final_video = os.path.join(
            RESULT_FOLDER,
            "result_video.mp4"
        )

        subprocess.run([
            "ffmpeg",
            "-y",
            "-i",
            temp_video,
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            final_video
        ])

        os.remove(temp_video)

        return render_template(
            "index.html",
            video="results/result_video.mp4"
        )

    else:

        return "Unsupported File"


if __name__ == "__main__":
    app.run(debug=True)
