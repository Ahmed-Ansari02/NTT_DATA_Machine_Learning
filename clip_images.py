from PIL import Image
import os
import pandas as pd



def clip_image(image_path, xmin, ymin, xmax, ymax, categories):  # Open the image
    image = Image.open(image_path)
    cropped_image = image.crop((xmin, ymin, xmax, ymax))
    file_hash = hash(f"{xmin} {ymin}  {xmax} {ymax}  {categories}")
    file_path = f"./datasets/v1/validate/{categories}/{file_hash}.jpg"
    save_path = f"./datasets/v1/validate/{categories}"
    if os.path.exists(save_path):
        cropped_image.save(file_path)
    else:
        os.makedirs(save_path)
        cropped_image.save(file_path)


if __name__ == "__main__":
    # CSV file containing coordinates (assuming format: left,upper,right,lower)
    csv_file = "./roboflow_dataset/valid/_annotations.csv"
    path = os.getcwd()
    print(path)
    df = pd.read_csv(os.path.join(path, csv_file))
    distinct_categories = df['class'].unique()
    print(distinct_categories)
    for index, row in df.iterrows():
        file_name = os.path.join(path, f"./roboflow_dataset/valid/{row['filename']}")
        clip_image(
            file_name,
            row["xmin"],
            row["ymin"],
            row["xmax"],
            row["ymax"],
            row["class"],
        )


